"""SentinelFix agent — verify loop with neatlogs tracing."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import neatlogs
from dotenv import load_dotenv
from openai import OpenAI

from agent.tools import TOOL_SCHEMA, dispatch

load_dotenv()
neatlogs.init()

SYSTEM = """You are SentinelFix. Stabilize the demo HTTP service until GET /health returns 200 and body 'healthy'.
Use tools: read files, patch code or set SENTINELFIX_HEALTH_TOKEN=ok in demo .env, run shell, check_health.
After each change, call check_health. If still failing, diagnose and retry (recovery).
Stop only when check_health shows status=200. Summarize what you fixed."""


def run_agent(goal: str, demo_dir: str, max_turns: int = 12) -> None:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL"),
    )
    demo_path = str(Path(demo_dir).resolve())
    messages = [
        {"role": "system", "content": SYSTEM},
        {
            "role": "user",
            "content": f"Goal: {goal}\nDemo directory: {demo_path}\nStart by check_health, then read demo_service/app.py.",
        },
    ]

    for turn in range(max_turns):
        resp = client.chat.completions.create(
            model=os.environ.get("SENTINELFIX_MODEL", "gpt-4o-mini"),
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
