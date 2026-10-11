# PRD — SentinelFix (1 halaman)

| | |
| --- | --- |
| **Tim** | adindamochamad (solo) |
| **Event** | neatHack 2026 |
| **Verdict** | GO — [STAGE1_IDEATION.md](./STAGE1_IDEATION.md) |

## Problem

Tim membangun agent yang terlihat pintar tetapi **tidak membuktikan** stabilitas: patch satu kali tanpa verify loop, tanpa recovery saat salah diagnosa. Juri perlu melihat agent **menyelesaikan** tugas dengan bukti.

## User

Developer / judge yang menjalankan demo: memberi target repo sandbox + perintah "make it healthy."

## Job to be done

Dari state **broken** (tests fail atau `/health` tidak OK), agent harus mencapai state **verified healthy** tanpa intervensi manual di tengah loop.

## Killer flow (demo)

1. Operator menjalankan CLI/API: goal + path ke demo service
2. Agent **plans** langkah (reproduce, read logs/tests, hypothesize, patch, re-run verify)
3. **Injected fault path:** patch pertama sengaja salah atau environment misleading → tool error
4. Agent **recovers** (re-plan, rollback context via Entire checkpoint)
5. Verify pass → output ringkasan + link neatlogs trace compare

## Partner roles (bukan logo)

| Partner | Peran konkret |
| --- | --- |
| neatlogs | Instrument setiap LLM + tool call; simpan run before/after fix; tunjukkan retry |
| Entire | Checkpoint setelah setiap patch attempt; entire-graph untuk relasi file yang diubah |
| cfo.ai | Model harga per "stabilization job" / menit autonomous fix; infra + inference cost; runway |

## Failure & recovery (wajib bukti)

- Skenario: salah root cause (mis. mengubah kode padahal env var) → test masih fail
- Bukti: span error + tool retry + trace run berikutnya sukses

## Evidence artifacts (submission)

- Public repo commits 10–12 Okt 2026
- `docs/SUBMISSION_EVIDENCE.md` dengan URL trace, Entire, cfo.ai, #neatHack
- Video ≤ 3 menit mengikuti [docs/VIDEO_SCRIPT.md](./docs/VIDEO_SCRIPT.md)

## Non-goals

- Production multi-region deploy
- Generic chat assistant
- Fitur tambahan di luar satu demo service + satu verify loop

## Stack (48h)

Python agent core (tools: run tests, read/write files, health check); optional thin TS dashboard hanya jika waktu cukup. Prioritas: agent + traces > UI.

## Success metrics (internal)

- [ ] End-to-end demo < 5 menit live
- [ ] ≥1 failed action + recovery di neatlogs
- [ ] ≥2 Entire checkpoints
- [ ] cfo.ai plan konsisten dengan usage tokens di trace
