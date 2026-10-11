# Eligibility runbook (lakukan sekali, ~30 menit)

Centang di [CHECKLIST.md](../CHECKLIST.md) hanya setelah **kamu** selesai langkahnya.

## 1. Discord

1. Buka https://neatlogs.com/discord → join `discord.gg/tXfKhVdhq`
2. Baca channel pengumuman — **final submit cutoff** hanya di sini

## 2. Web check-in

1. https://neatlogs.com/hackathon/check-in
2. Email **sama** dengan Luma
3. Solo = satu orang check-in

**Hadiah check-in:** AWS $25 (350 tim pertama). Key model: https://neatlogs.com/hackathon/models → paste ke `.env` sebagai `OPENAI_API_KEY` + `OPENAI_BASE_URL=https://litellm.vision.aivar.app/v1`. Bukan wajib key dari platform.openai.com. Jangan tempel secret di markdown.

## 3. Partner wajib (buat akun hari ini)

| Alat | Langkah |
| --- | --- |
| neatlogs | https://app.neatlogs.com → Settings → API Keys → simpan sebagai `NEATLOGS_API_KEY` |
| Entire | https://entire.io → pasang CLI/workflow di repo lomba → checkpoints + `entire-graph` |
| cfo.ai | Lihat **§3.3** di bawah — halaman pricing **bukan** deadlock |

## 4. X + GitHub

- Akun X publik siap quote-tweet
- Repo publik: [sentinelfix-agent](https://github.com/adindamochamad/sentinelfix-agent) — commit dalam window 10–12 Okt 2026

## 5. Verifikasi lokal

```bash
cd /Users/mac/Development/neathack
./scripts/verify-onboarding.sh
```

Env opsional di shell atau `.env` di repo lomba (jangan commit secret).

---

## 3.3 cfo.ai — stuck di “Try cfo.ai free for 14 days”

URL seperti `app.cfo.ai/signup/plan?org=...` **benar**. Tidak ada tombol “skip” atau “hackathon free”. Panitia **sengaja** minta kartu, lalu kamu cancel.

Teks di halaman: **$0 today**. Cancel sebelum trial berakhir → **tidak ditagih**, trial 14 hari tetap jalan.

### Langkah (urutan wajib)

1. Buka [https://cfo.ai/neathacks](https://cfo.ai/neathacks) dulu (landing lomba), login dengan email Luma yang sama.
2. Kalau sudah di chooser plan: toggle **Monthly** (opsional; Annual default — tetap $0 hari ini).
3. Klik **Start free trial** hanya di kartu **Startup** (bukan Growth, bukan Talk to sales).
4. Isi kartu. Tagihan hari ini **$0**.
5. Setelah masuk workspace: **Settings → Billing → Cancel subscription**. Dialog akan sebut tanggal trial; cancel **tidak** memotong sisa 14 hari.
6. Jangan klik **Start paid plan** jika nanti muncul banner “used all AI usage”.
7. Kredit extra neatHack datang dari panitia (Discord), bukan dari tombol di halaman ini.

### Jangan

- Jangan pilih Growth / Enterprise.
- Jangan biarkan trial tanpa cancel (risiko tagihan setelah 14 hari).
- Jangan hapus workspace.

### Tidak mau pakai kartu

Tidak ada jalur resmi tanpa kartu di plan chooser. Tanya Discord neatHack (channel help/credits) dengan screenshot. Sementara itu, model bisnis bisa didraft di [CFO_PLAN.md](./CFO_PLAN.md) — **tapi** juri tetap butuh bukti cfo.ai (link workspace / export), jadi trial Startup tetap target.

**Status 11 Okt:** trial aktif + billing cancel — checklist cfo.ai dicentang. Langkah bukti juri masih: buat model SentinelFix di Ari, paste link ke `docs/EVIDENCE.md`.
