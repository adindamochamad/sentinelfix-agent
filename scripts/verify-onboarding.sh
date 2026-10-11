#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ok=0
warn=0

check() {
  if [[ -n "${!1:-}" ]]; then
    echo "OK   $1 set"
    ok=$((ok + 1))
  else
    echo "MISS $1 (export or add to repo .env)"
    warn=$((warn + 1))
  fi
}

if [[ -f "$ROOT/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT/.env"
  set +a
fi

echo "=== neatHack onboarding verify ==="
check NEATLOGS_API_KEY

if command -v entire >/dev/null 2>&1; then
  echo "OK   entire CLI in PATH"
  ok=$((ok + 1))
else
  echo "MISS entire CLI (install from https://entire.io)"
  warn=$((warn + 1))
fi

if [[ -d "$ROOT/.git" && -f "$ROOT/.env.example" && -d "$ROOT/agent" ]]; then
  echo "OK   unified repo at $ROOT (git + agent + .env.example)"
  ok=$((ok + 1))
else
  echo "MISS expected files in $ROOT"
  warn=$((warn + 1))
fi

echo ""
echo "Manual (cannot verify here): Discord, Luma check-in, cfo.ai, X account."
echo "Runbook: $ROOT/docs/ELIGIBILITY_RUNBOOK.md"
echo "Result: $ok checks passed, $warn gaps"

[[ $warn -eq 0 ]] || exit 1
