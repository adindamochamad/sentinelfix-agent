"""SentinelFix agent — verify loop with neatlogs tracing."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import neatlogs
import openai
from dotenv import dotenv_values
from neatlogs.core import get_tracker
from neatlogs.event_handlers import get_handler_for_provider
from openai import OpenAI

from agent.tools import TOOL_SCHEMA, dispatch

# #region agent log
def _dbg(hypothesis_id: str, message: str, data: dict) -> None:
    try:
        payload = {
            "sessionId": "8b5ffe",
            "runId": "recovery-1",
            "hypothesisId": hypothesis_id,
            "location": "agent/run.py",
            "message": message,
            "data": data,
            "timestamp": int(__import__("time").time() * 1000),
        }
        with open("/Users/mac/Development/neathack/.cursor/debug-8b5ffe.log", "a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload) + "\n")
    except Exception:
        pass
# #endregion

_ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
_file_env = {k: (v or "").strip().strip('"').strip("'") for k, v in dotenv_values(_ENV_PATH).items() if k}
# File wins over a stale OPENAI_API_KEY already in the shell
os.environ.update(_file_env)

_neatlogs_key = os.environ.get("NEATLOGS_API_KEY", "").strip()
_llm_key = os.environ.get("OPENAI_API_KEY", "").strip()
if not _neatlogs_key:
    raise SystemExit(f"NEATLOGS_API_KEY missing in {_ENV_PATH}")
if not _llm_key.startswith("sk-"):
    raise SystemExit(
        f"OPENAI_API_KEY in {_ENV_PATH} must be the LiteLLM key (starts with sk-). "
        f"Got prefix={_llm_key[:4]!r} len={len(_llm_key)}. Do not use the neatlogs key here."
    )

# neatlogs 1.1.8 patches OpenAI + AzureOpenAI in one loop and both classes
# share the last __init__ (Azure). That sends the wrong auth to LiteLLM.
_orig_openai_init = openai.OpenAI.__init__
neatlogs.init(api_key=_neatlogs_key, tags=["neathack", "sentinelfix"])


def _openai_init_with_trace(self, *args, **kwargs):
    _orig_openai_init(self, *args, **kwargs)
    tracker = get_tracker()
    if not tracker or not hasattr(self, "chat"):
        return
    create = self.chat.completions.create
    if getattr(create, "_neatlogs_patched", False):
        return
    handler = get_handler_for_provider("openai", tracker)
    self.chat.completions.create = handler.wrap_method(create, "openai")
    setattr(self.chat.completions.create, "_neatlogs_patched", True)


openai.OpenAI.__init__ = _openai_init_with_trace

SYSTEM = """You are SentinelFix. Stabilize the demo HTTP service until GET /health returns 200 and the body is healthy.
The HTTP server is already running. Never start python app.py or any background server.
Read the code and config. Change one thing at a time, then check_health.
If health is still failing, that change was not the cause: revert it and investigate a different cause.
Do not guess a secret value that you have not read from the code or config.
Stop only when check_health shows status=200. Summarize what failed, what you reverted, and what fixed it."""


def run_agent(goal: str, demo_dir: str, max_turns: int = 12) -> None:
    client = OpenAI(
        api_key=_llm_key,
        base_url=os.environ.get("OPENAI_BASE_URL"),
    )
    demo_path = str(Path(demo_dir).resolve())
    messages = [
        {"role": "system", "content": SYSTEM},
        {
            "role": "user",
            "content": (
                f"Goal: {goal}\nDemo directory: {demo_path}\n"
                "Start with check_health, then read demo_service/app.py. "
                "Change one thing at a time, then check_health. "
                "If status is not 200, revert that change and try a different cause."
            ),
        },
    ]
    # #region agent log
    _dbg(
        "H1",
        "run start",
        {
            "prompt_names_token_ok": "SENTINELFIX_HEALTH_TOKEN=ok" in SYSTEM,
            "max_turns": max_turns,
        },
    )
    # #endregion

    for turn in range(max_turns):
        resp = client.chat.completions.create(
            model=os.environ.get("SENTINELFIX_MODEL", "claude-haiku"),
            messages=messages,
            tools=TOOL_SCHEMA,
            tool_choice="auto",
        )
        msg = resp.choices[0].message
        messages.append(msg.model_dump(exclude_none=True))

        if not msg.tool_calls:
            print(msg.content or "")
            return

        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments or "{}")
            result = dispatch(name, args, demo_path)
            # #region agent log
            _dbg(
                "H2",
                "tool result",
                {
                    "turn": turn,
                    "tool": name,
                    "wrote_app": name == "write_file" and str(args.get("path", "")).endswith("app.py"),
                    "env_key": args.get("key") if name == "set_demo_env" else None,
                    "health_200": "status=200" in result,
                    "health_503": "status=503" in result,
                    "result_prefix": result[:180],
                },
            )
            # #endregion
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                }
            )
            print(f"[tool] {name} -> {result[:200]}...")

    print("Max turns reached without final answer.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", required=True)
    parser.add_argument("--demo-dir", default="demo_service")
    parser.add_argument("--max-turns", type=int, default=12)
    args = parser.parse_args()
    run_agent(args.goal, args.demo_dir, args.max_turns)


if __name__ == "__main__":
    main()
