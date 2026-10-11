# neatHack — Competition Brief & rulebook (Stage 0)

**Terakhir disinkronkan dari situs resmi:** 10 Okt 2026. Jika bentrok dengan halaman live, percayakan https://neatlogs.com/hackathon.

## Identitas lomba

| | |
| --- | --- |
| Nama | neatHack |
| Penyelenggara | neatlogs |
| Format | Online, 48 jam |
| Tanggal | 10–12 Oktober 2026 |
| Track | **Satu track** — “Build an agent that works (literally)” |
| Hadiah | ~$19k (cash + credits + neatlogs Pro) |
| Peserta (indikasi) | ~1.300+ di Luma |
| Portal submit | **Bukan Devpost** — quote post di **X** |

Tema inti: bangun **AI agent** (atau sistem agent) yang menyelesaikan **tugas substansial** dari awal sampai selesai — planning, tool use, state, context, execution, recovery, verification, iteration.

Contoh ukuran tugas di situs (bukan track terpisah — **hindari copy mentah**):

- Fix GitHub issue end-to-end
- Research question dengan sumber
- Watch running system + remediate
- Multi-agent dengan coordinator
- Long task saat environment berubah

## Zona waktu

Semua jadwal resmi **IST**. Untuk **WIB**: **IST + 1 jam 30 menit**.

| Event (IST) | WIB |
| --- | --- |
| Kickoff call — 10 Okt 09:00 | 10:30 |
| Web check-in buka — 10 Okt 08:00 | 09:30 |
| Hackathon **build window** mulai — 10 Okt 12:30 | **14:00** |
| Submit buka — 12 Okt 19:00 | 20:30 |
| Submit tutup — 12 Okt 23:55 | **13 Okt 01:25** |
| Pemenang — 16 Okt | (sama tanggal, konfirmasi jam di update) |

### Aturan kode

- Boleh **merencanakan** ide sebelum build window.
- **Semua kode** harus ditulis antara start hackathon dan deadline.
- Proyek jadi / setengah jadi **tidak boleh** dibawa masuk.
- Gunakan neatlogs **selama** development untuk trace, debug, perbaikan.

## Onboarding (4 langkah resmi)

1. **Luma** — https://luma.com/s5blr882 ✅ (user sudah)
2. **Discord** — https://neatlogs.com/discord
3. **Web check-in** — https://neatlogs.com/hackathon/check-in (email = Luma; solo = satu orang check-in)
4. **Submit** — Senin malam WIB, tombol “Submit on X” di halaman hackathon

Tim 1–4: setiap anggota daftar Luma dengan **nama tim sama**, check-in sendiri-sendiri. User: **solo**.

## Partner wajib (setiap proyek)

Harus dipakai dengan peran jelas; demo video harus cover **ketiganya**:

| Tool | Peran | Bukti yang juri cek |
| --- | --- | --- |
| **neatlogs** | Trace runs, debug agent | Link/screenshot traces; before/after fix |
| **Entire** | Context repo untuk coding agent | Checkpoints, entire-graph |
| **cfo.ai** | Ekonomi agent: pricing, cost, revenue, runway | Business plan di submission |

cfo.ai signup: kartu diminta → **cancel subscription segera** di Billing; kredit hackathon dari panitia — https://cfo.ai/neathacks

## Submission (apa yang dikirim)

Satu proyek per tim, sebagai **public quote post** dari posting submit resmi neatlogs di X:

- Nama tim, nama proyek, **repo publik**, **link demo**
- Video demo **≤ 3 menit**
- Video harus secara eksplisit menjelaskan neatlogs, Entire, cfo.ai: architecture, implementation, runtime, reasoning, result
- Bukti pendukung di repo
- Juri harus bisa verifikasi **commit dalam window hackathon**
- Buka draft saja **tidak** dihitung submit
- Terlambat **tidak dinilai**

Building in public: tag **#neatHack**, share selama hackathon (bukan hanya hari submit).

## Penilaian (bobot resmi, total 100)

| Kriteria | Bobot |
| --- | --- |
| The agent (tugas substantial end-to-end) | **30%** |
| Use of neatlogs, Entire, cfo.ai | **25%** |
| Demo video | **20%** |
| Building in public | **15%** |
| Usefulness & originality | **10%** |

**Prinsip:** buktikan, jangan hanya “menyentuh” kriteria. Evidence checklist di situs: trace before/after, recovery dari failure, commit dates, dll.

### Community Winner (terpisah, bisa stack)

- $500 cash
- Dinilai dari minat komunitas **genuine** selama hackathon (kualitas produk/demo, launch, engagement asli)
- Follower count **bukan** faktor utama
- Bot / bought likes = disqualify
- Tetap wajib pakai tiga tool; partner usage tidak masuk skor community

### Hadiah utama (ringkas)

| | Cash | Lainnya |
| --- | --- | --- |
| 1st | $2,000 | $5k Dodo credits + 3 bln neatlogs Pro |
| 2nd | $1,000 | $3k Dodo |
| 3rd | $500 | $1k Dodo |

## Arketipe & winning formula (Stage 0)

- **Sprint 48h** + **sponsor challenge** (3 tool wajib) + **async video** (bukan panel pitch utama)
- **Winning formula:** satu agent, satu tugas ber-stakes tinggi, **working demo** + side-by-side before/after di traces + Entire checkpoints + cfo.ai unit economics — **bukan** banyak fitur setengah jadi
- **Median threat (~60% field):** GPT wrapper, generic “research agent”, clone contoh “fix GitHub issue” dari halaman hackathon
- **Diferensiasi:** niche problem + failure mode yang ditakuti (bukan inconvenience), bukti verifiable, posting publik konsisten

### Alokasi effort (48 jam, mengikuti bobot)

- 40% — agent core (satu killer flow)
- 20% — neatlogs + Entire terintegrasi dari awal build
- 10% — cfo.ai plan
- 15% — building in public
- 15% — video + buffer submit

## Juri (engineer / devrel / founder)

- Haimantika Mitra — Entire
- Abhi Singh — Entire
- Prateek Karnal — Orchestrator.inc
- Ajay Yadav — neatlogs
- Akshay Hangloo — neatlogs

## Stage gate (workflow Cursor)

| Stage | Status | Syarat lanjut |
| --- | --- | --- |
| 0 Calibration | **Selesai** | Brief ini |
| 1 Ideation | **Belum** | `PROFILE.md` lengkap → ide → verdict **GO** |
| 1.5 PRD | Belum | PRD 1 halaman disepakati |
| 2 Build | Belum | PRD; URL live hanya jika demo butuh web — video+repo tetap utama |

## Link cepat

- Hackathon hub: https://neatlogs.com/hackathon
- Check-in: https://neatlogs.com/hackathon/check-in
- Docs neatlogs: https://docs.neatlogs.com
- Skill halaman (opsional): https://neatlogs.com/hackathon/skill
