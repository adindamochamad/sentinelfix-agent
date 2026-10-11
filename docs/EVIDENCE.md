# Evidence tracker (isi URL sebelum submit)

Ganti `TODO` dengan link nyata. Simpan salinan di repo lomba `docs/SUBMISSION_EVIDENCE.md`.

## The agent (30%)

| Bukti | URL / catatan |
| --- | --- |
| Demo live / recording | TODO |
| Satu flow end-to-end selesai | **11 Okt 17:54 WIB:** curl 503 `legacy_health_code returned 500` → agent baca `app.py` + `.env` → `set_demo_env` → **200 healthy** (~11 dtk). Prompt **tidak** menyebut nilai token. Tidak ada `write_file`: diagnosa langsung env, jadi recovery “patch kode gagal” belum terjadi. |

## neatlogs (bagian dari 25%)

| Bukti | URL |
| --- | --- |
| Trace **sebelum** perbaikan | Belum ada URL. Dashboard `app.neatlogs.com` minta login (sesi browser ini tidak masuk). API list traces 401 tanpa session token. |
| Trace **sesudah** perbaikan | Sama run 17:54 (503 lalu 200 dalam satu trace). URL menyusul setelah login dashboard. |
| Angka yang dibandingkan (latency, tokens, cost, error rate) | TODO |

## Entire (bagian dari 25%)

| Bukti | URL / path |
| --- | --- |
| Checkpoint PR / commit | CLI **0.11.4** terpasang di `~/.local/bin`. `entire enable --agent cursor` di repo ini. Daftar checkpoint diisi setelah commit. |
| entire-graph output | TODO — `entire checkpoint list` masih 0 sebelum commit sesi ini |

## cfo.ai (bagian dari 25%)

| Bukti | URL |
| --- | --- |
| Akun / trial | **Done** — Startup trial + subscription cancelled (11 Okt 2026) |
| Business plan export / link | TODO — paste share/export dari workspace setelah Ari selesai |
| Ringkasan unit economics (1 paragraf) | TODO — copy angka dari cfo.ai ke `docs/CFO_PLAN.md` |

## Recovery (wajib di situs)

| Bukti | URL |
| --- | --- |
| Trace run dengan action gagal + langkah berikutnya | Lokal: 403 lalu retry 200. **Paste URL neatlogs** dari dashboard. |

## Building in public (15%)

| Post | URL |
| --- | --- |
| #neatHack 1 | TODO |
| #neatHack 2 | TODO |
| #neatHack 3+ | TODO |

## Kode dalam window

| Bukti | URL |
| --- | --- |
| Repo publik | https://github.com/adindamochamad/sentinelfix-agent |
| Commit range hackathon | TODO (link compare GitHub) |
