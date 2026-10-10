# Demo service

Run: `python app.py` → http://127.0.0.1:8765/health returns **503** until `SENTINELFIX_HEALTH_TOKEN=ok`.

The agent can fix by exporting the env var or patching `app.py` to read the correct default.
