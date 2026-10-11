"""Minimal demo service — intentionally misconfigured until agent fixes it."""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

_DIR = Path(__file__).resolve().parent


def legacy_health_code() -> int:
    """Old helper. The live handler does not return this code."""
    return 500


def _health_token() -> str:
    """Prefer demo_service/.env so the agent can fix without restarting."""
    env_file = _DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("SENTINELFIX_HEALTH_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"')
    return os.environ.get("SENTINELFIX_HEALTH_TOKEN", "broken")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return
        token = _health_token()
        if token == "ok":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy\n")
        else:
            self.send_response(503)
            self.end_headers()
            self.wfile.write(
                f"unhealthy: legacy_health_code returned {legacy_health_code()}\n".encode()
            )

    def log_message(self, format: str, *args) -> None:
        print(f"[demo] {self.address_string()} {format % args}")


def main() -> None:
    port = int(os.environ.get("PORT", "8765"))
    print(f"SentinelFix demo listening on http://127.0.0.1:{port}/health", flush=True)
    print("Expected until agent fixes: HTTP 503  (leave this terminal running)", flush=True)
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
