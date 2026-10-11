# Stage 2 build playbook

Repo: folder ini (`/Users/mac/Development/neathack`) — [PRD.md](../PRD.md)

## Hour 0–2 (partner wiring)

1. `NEATLOGS_API_KEY` in `.env`; run agent once → confirm trace in neatlogs dashboard
2. `entire init` + first checkpoint after any file edit
3. Draft economics in cfo.ai → copy summary to `docs/CFO_PLAN.md` + link

## Hour 2–20 (killer flow)

1. Run `demo_service/app.py` in background; prove 503 on `/health`
2. Run `python -m agent.run` until 200 — **save trace URLs**
3. Introduce **wrong fix** once (e.g. patch wrong line) → recovery → second trace
4. Harden: max turns, clearer tool errors, README demo steps

## Hour 20–28 (evidence + public)

1. Fill `docs/SUBMISSION_EVIDENCE.md` and [EVIDENCE.md](./EVIDENCE.md)
2. Three #neatHack posts — [BUILDING_IN_PUBLIC.md](./BUILDING_IN_PUBLIC.md)
3. Record [VIDEO_SCRIPT.md](./VIDEO_SCRIPT.md)

## Hour 28–32 (submit buffer)

Follow [SUBMIT.md](./SUBMIT.md) — quote post early in window.

## Recovery demo script (injected fault)

Optional env `SENTINELFIX_FORCE_WRONG_PATCH=1` in agent (TODO implement) or manually revert `.env` once mid-run to show re-plan.
