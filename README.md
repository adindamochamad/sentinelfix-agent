# SentinelFix — neatHack 2026

Agent that **reproduces → diagnoses → patches → verifies** until a demo service is healthy, with **recovery** when the first fix is wrong.

**Context pack (PRD, submit):** [neathack](https://github.com/adindamochamad/neathack) _(private/local — not required for judges; this repo is the submission)._

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # NEATLOGS_API_KEY, model key (LiteLLM/OpenAI-compatible)

# Broken demo (health fails until fixed)
cd demo_service && python app.py

# Agent (from repo root)
python -m agent.run --goal "Make demo_service healthy" --demo-dir demo_service
```

## Partners (submission evidence)

| Tool | Where in this repo |
| --- | --- |
| neatlogs | `agent/run.py` — `neatlogs.init()`; compare traces before/after |
| Entire | [docs/ENTIRE.md](docs/ENTIRE.md) — checkpoint each patch attempt |
| cfo.ai | [docs/CFO_PLAN.md](docs/CFO_PLAN.md) — export link in `docs/SUBMISSION_EVIDENCE.md` |

## Demo URL

TODO: deploy or `ngrok` for submit — add link to `docs/SUBMISSION_EVIDENCE.md`.

## License

MIT
