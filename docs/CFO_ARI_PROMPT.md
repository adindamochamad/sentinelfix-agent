# Prompt Ari (cfo.ai) — paste sekali untuk bukti juri

Workspace sudah trial + billing cancel. Juri butuh **plan**, bukan akun kosong.

Paste ke Ari:

```
Build a 12-month finance model for SentinelFix, an autonomous agent that stabilizes a broken demo/staging service: reproduce failure → patch → verify health until green, with recovery if the first patch is wrong.

Assumptions (edit if you have better numbers):
- Solo founder, no payroll in months 1–3; contractor $4k/mo from month 4; second engineer $8k/mo from month 7.
- Price: $15 per completed stabilization job (Base), $12 at volume (Growth).
- Base: 20 teams, 10 jobs/team/month = 200 jobs → $3,000 revenue.
- Growth (month 12): 80 teams, 15 jobs/team/month = 1,200 jobs → $14,400 revenue.
- COGS: LLM inference + hosting. Start at $3 per job, falling to $1.80 at volume (batching, caching, smaller model for verify).
- neatlogs observability ~$50/mo then $150/mo.
- Starting cash $8,000 (personal + hackathon credits). No other funding.

Please produce:
1. Monthly P&L: customers, jobs, revenue, inference, hosting, tools, payroll, gross profit, operating income, ending cash.
2. Two scenarios: Base vs Growth (same costs, different volume).
3. Gross margin and runway (months until cash < $0) in each scenario.
4. Unit economics: contribution per job after inference+hosting.
5. A one-paragraph summary I can put in a hackathon submission.

Keep formulas visible so I can screenshot for the demo video (≤3 min, cfo.ai section).
```

Setelah Ari selesai: screenshot + share/export URL → `docs/EVIDENCE.md` dan `docs/CFO_PLAN.md`.
