# SentinelFix — neatHack 2026

Satu folder: **konteks lomba + kode agent**. Buka **`/Users/mac/Development/neathack`** di Cursor.

Agent **reproduce → diagnose → patch → verify** sampai demo service sehat, dengan recovery jika patch pertama salah.

GitHub (submit): https://github.com/adindamochamad/sentinelfix-agent

## Quick start (dari folder ini)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # isi NEATLOGS_API_KEY + model key
# terminal 1
python demo_service/app.py
# terminal 2
python -m agent.run --goal "Make demo_service healthy" --demo-dir demo_service
```

## Peta folder

| Path | Isi |
| --- | --- |
| `agent/` | Loop agent + neatlogs |
| `demo_service/` | Service rusak (`/health` 503 sampai diperbaiki) |
| `PRD.md` `CONTEXT.md` | Brief + PRD |
| `docs/` | DoD, evidence, submit, Entire, cfo.ai |

Jangan commit `.env`.
