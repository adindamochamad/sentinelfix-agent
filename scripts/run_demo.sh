#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
source .venv/bin/activate 2>/dev/null || true

echo "Starting demo_service on :8765 (503 until fixed)..."
python demo_service/app.py &
PID=$!
sleep 1
curl -s -o /dev/null -w "health before: %{http_code}\n" http://127.0.0.1:8765/health || true

echo "Run agent: python -m agent.run --goal 'Make demo_service healthy' --demo-dir demo_service"
echo "Stop server: kill $PID"
