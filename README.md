# DubScript Studio

**A dubbing sheet builder for video dubbing creators** — by **Prime Khatab Services**

Turn any subtitle file into a ready-to-record dubbing sheet, check that every
Hindi dub line actually *fits* its scene timing, and export the finished sheet
for your voice artists — all offline, in one HTML file.

## The problem

Thousands of creators dub donghua, anime and short dramas from Chinese/Korean/
English into Hindi and other languages. Their workflow is painful:

- Subtitles live in an `.srt` file, but recording happens from messy
  spreadsheets or screenshots.
- A translated line that is **too long for its time slot** is only discovered
  *during recording* — the voice artist has to rush, the line spills into the
  next scene, and the whole take is wasted.
- There is no simple, free, offline tool made for this one job.

## The solution

DubScript Studio takes an `.srt` file and instantly builds a proper dubbing
sheet:

1. **Load** — upload an `.srt`, drag & drop it, paste SRT text, or try the
   built-in demo lines.
2. **Write** — every cue becomes a row: timing, slot duration, original line,
   and an editable Hindi (Hinglish) dub-line field.
3. **Fit check** — a live characters-per-second indicator per line:
   - 🟢 **Fits** — comfortable speaking pace (≤ 16 chars/sec)
   - 🟡 **Tight** — the artist must speak fast (16–20 chars/sec)
   - 🔴 **Too long** — shorten the line before recording (> 20 chars/sec)
4. **Export** — download the finished dubbing sheet as **CSV** (for Excel /
   Google Sheets / voice artists) or as a clean **SRT** with the new dub
   lines, ready to burn into the video or upload to YouTube.

No accounts, no API keys, no internet needed. Your subtitles never leave your
computer.

## How to run

**Option 1 — just open it (easiest)**

Double-click `index.html`, or open it in any browser. Everything works offline.

**Option 2 — tiny local server**

```bash
python3 server.py
# then open http://localhost:8000
```

## Demo

1. Click **Load demo lines** — a 10-line donghua-style sample loads
   (the same lines are in `sample.srt`).
2. Type a short Hindi line for cue 1 — watch the fit badge turn green.
3. Type a very long Hindi line for cue 2 — the badge turns red:
   **"Too long ✗ shorten it"**.
4. Click **Download dubbing sheet (.csv)** and **Download dubbed subtitles
   (.srt)**.

A full 60–90 second walkthrough script is in [`DEMO.md`](DEMO.md).

## Tech used

- Pure **HTML + CSS + vanilla JavaScript** — a single self-contained
  `index.html`, zero dependencies, zero build step.
- A standards-based **SRT parser** (handles `,`/`.` millisecond separators,
  multi-line cues, files with or without cue numbers).
- Optional **Python 3** standard-library HTTP server (`server.py`) — nothing
  to install.

## Screenshots

<!-- TODO: add screenshots after the demo recording -->
- _Screenshot 1 — dubbing sheet with fit indicators (placeholder)_
- _Screenshot 2 — CSV export in a spreadsheet (placeholder)_

## Files

| File         | Purpose                                   |
|--------------|-------------------------------------------|
| `index.html` | The complete app (open this)              |
| `server.py`  | Optional local server                     |
| `sample.srt` | 10-line sample subtitle file for the demo |
| `DEMO.md`    | 60–90 second demo video script            |
| `README.md`  | This file                                 |

## Built for

Orbix 48-Hour Global Hackathon (21–23 Nov 2026) by **Mohd Khatab (Prime)**,
founder of **Prime Khatab Services**, Rajouri, Jammu & Kashmir, India.

## License

MIT — free to use, copy and modify.
