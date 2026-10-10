# Recovery demo (for video + neatlogs evidence)

1. Start demo server: `python demo_service/app.py`
2. Run agent until it proposes a fix
3. **Inject failure:** manually set `SENTINELFIX_HEALTH_TOKEN=wrong` in `demo_service/.env` and restart server, or revert a bad patch in `app.py`
4. Re-run agent (or let it continue) — capture trace showing tool error + retry
5. Save **both** trace URLs in [SUBMISSION_EVIDENCE.md](./SUBMISSION_EVIDENCE.md)

Judges expect: action failed → agent did something next (not a silent stop).
