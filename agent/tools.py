"""Tools for SentinelFix verify loop."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import httpx


def read_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_file(path: str, content: str) -> str:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"wrote {len(content)} bytes to {path}"


def run_shell(command: str, cwd: str | None = None) -> str:
    lowered = command.lower()
    if "app.py" in lowered or "serve_forever" in lowered:
        return (
            "refused: demo HTTP server must stay in the user's terminal. "
            "After set_demo_env, call check_health — /health reloads demo_service/.env."
        )
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except subprocess.TimeoutExpired as e:
        return f"timeout after {e.timeout}s: {command[:200]}"
    out = (result.stdout or "") + (result.stderr or "")
    return f"exit={result.returncode}\n{out[-8000:]}"


def check_health(base_url: str = "http://127.0.0.1:8765") -> str:
    url = (base_url or "").strip() or "http://127.0.0.1:8765"
    if "8765" not in url:
        url = "http://127.0.0.1:8765"
    url = url.rstrip("/")
    if not url.endswith("/health"):
        url = f"{url}/health"
    try:
        r = httpx.get(url, timeout=5.0)
        return f"status={r.status_code} body={r.text.strip()} url={url}"
    except Exception as e:
        return f"error={e!r} url={url}"


def set_demo_env(key: str, value: str, demo_dir: str) -> str:
    env_path = Path(demo_dir) / ".env"
    lines = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8").splitlines()
    lines = [ln for ln in lines if not ln.startswith(f"{key}=")]
    lines.append(f"{key}={value}")
    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f"set {key} in {env_path}"


TOOL_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a UTF-8 text file",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write or overwrite a UTF-8 text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_shell",
            "description": "Run a shell command in optional cwd",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string"},
                    "cwd": {"type": "string"},
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_health",
            "description": "GET /health on the demo HTTP server",
            "parameters": {
                "type": "object",
                "properties": {"base_url": {"type": "string"}},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "set_demo_env",
            "description": "Set KEY=value in demo_service/.env. The running server reads this on each /health — do not restart app.py.",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {"type": "string"},
                    "value": {"type": "string"},
                    "demo_dir": {"type": "string"},
                },
                "required": ["key", "value", "demo_dir"],
            },
        },
    },
]


def dispatch(name: str, args: dict, demo_dir: str) -> str:
    try:
        if name == "set_demo_env":
            args = {**args, "demo_dir": demo_dir}
        if name == "read_file":
            return read_file(**args)
        if name == "write_file":
            return write_file(**args)
        if name == "run_shell":
            return run_shell(**args)
        if name == "check_health":
            return check_health(**args)
        if name == "set_demo_env":
            return set_demo_env(**args)
        return f"unknown tool {name}"
    except Exception as e:
        return f"tool_error {type(e).__name__}: {e}"
