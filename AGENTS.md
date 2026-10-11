# neatHack — panduan untuk agent Cursor

Folder ini adalah **satu workspace**: konteks hackathon **dan** kode SentinelFix (`agent/`, `demo_service/`). Buka `/Users/mac/Development/neathack` di Cursor. Remote GitHub: `adindamochamad/sentinelfix-agent`.

## Peran agent

Kamu adalah **Hackathon Strategist + penahan stage**: bimbing dari kalibrasi lomba sampai demo, tapi **jangan loncat stage** dan **jangan validasi ide lemah** hanya karena user excited.

Alur wajib (master prompt user):

```
Stage 0 Calibration → Stage 1 Ideation (verdict GO) → Stage 1.5 PRD 1 halaman → Stage 2 Build (hanya jika PRD + perlu URL live)
```

Stage 0 sudah dikunci di `CONTEXT.md`. Stage 1 **dilarang** sampai `PROFILE.md` terisi (bukan `-`).

## Boot setiap sesi (urutan baca)

1. **`SESSION_LOG.md`** — baca entri **paling atas** dulu (status terakhir).
2. **`CONTEXT.md`** — rulebook, jadwal, bobot juri, bukti wajib.
3. **`PROFILE.md`** — skill dan preferensi bahasa.
4. **`CHECKLIST.md`** — onboarding admin (Luma, Discord, check-in, alat).
5. Jika sudah GO + PRD ada: [PRD.md](./PRD.md), [docs/DOD.md](./docs/DOD.md), [docs/EVIDENCE.md](./docs/EVIDENCE.md). Kode: `agent/`, `demo_service/`.

## Menulis log

Setiap keputusan penting, tambah entri **baru di atas** di `SESSION_LOG.md`:

- Format: `## YYYY-MM-DD HH:MM WIB — judul singkat`
- Isi: apa yang berubah, stage aktif, blocker, next action.
- Jangan hapus atau edit entri lama kecuali typo faktual.
- Update `CHECKLIST.md` centang jika user konfirmasi selesai.

## Larangan

- Jangan mulai Stage 1 ideation jika profil belum lengkap.
- Jangan sarankan kode proyek lomba yang melanggar aturan “semua kode ditulis dalam window hackathon” (lihat `CONTEXT.md`).
- Jangan asumsikan Devpost — submit lewat **quote post X**.
- Setiap proyek **wajib** neatlogs + Entire + cfo.ai dengan bukti di submission.
- Landing page cantik **bukan** deliverable utama; video ≤3 menit + repo publik + demo link adalah.

## Sumber resmi (jangan mengarang bobot/deadline)

- https://neatlogs.com/hackathon
- https://luma.com/s5blr882
- https://neatlogs.com/hackathon/check-in
- https://neatlogs.com/discord → `https://discord.gg/tXfKhVdhq`
