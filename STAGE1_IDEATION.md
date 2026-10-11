# Stage 1 — Ideation (verdict)

**Profil:** flexible full-cycle, Python + TS, solo. **Bahasa:** ID + EN.

## Kandidat (skor cepat: substansial / diferensiasi / 48h / partner fit)

| Ide | Substansial | Original | 48h solo | neatlogs+Entire+cfo | Verdict |
| --- | --- | --- | --- | --- | --- |
| Generic research agent + citations | Medium | Low (median) | Yes | Weak story | **NO** |
| Copy "fix GitHub issue" dari situs | High | Low | Yes | OK | **NO** |
| Invoice PDF → ledger reconcile | High | Medium | Risky | OK | MAYBE |
| **SentinelFix: stabilize broken demo service** | High | Medium-High | Yes | Strong | **GO** |
| Multi-agent coordinator showcase | High | Medium | No (scope) | OK | **NO** |

## Pilihan: **SentinelFix** (GO)

**Satu kalimat:** Agent menerima environment demo yang **sengaja rusak** (test gagal / config salah), lalu **reproduce → diagnose → patch → verify** sampai health check hijau, dengan **recovery** saat patch pertama salah.

**Mengapa menang vs median field:** bukan chat UI; bukti verifiable (test output, health endpoint, traces before/after); failure mode nyata (false fix); Entire natural untuk iterasi patch; cfo.ai menjual "stabilization minutes" ke tim platform.

**Non-goals:** multi-tenant SaaS, landing marketing, banyak integrasi pihak ketiga.

Lanjut: [PRD.md](./PRD.md) → Stage 2 di repo lomba.
