#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
printf 'SENTINELFIX_HEALTH_TOKEN=broken\n' > "$ROOT/demo_service/.env"
echo "Reset demo token to broken. Health should be 503 if app.py is running:"
curl -sS -w "\nHTTP %{http_code}\n" http://127.0.0.1:8765/health || true
