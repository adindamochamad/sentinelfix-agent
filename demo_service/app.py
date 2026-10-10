"""Minimal demo service — intentionally misconfigured until agent fixes it."""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return
        # Bug: wrong default until agent sets SENTINELFIX_HEALTH_TOKEN=ok or patches this line
        token = os.environ.get("SENTINELFIX_HEALTH_TOKEN", "broken")
        if token == "ok":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy\n")
        else:
            self.send_response(503)
            self.end_headers()
            self.wfile.write(b"unhealthy: token mismatch\n")

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    port = int(os.environ.get("PORT", "8765"))
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
