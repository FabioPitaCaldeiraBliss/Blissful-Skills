# References and motion language

A piece's **motion language** is written from references before the motion spec, so pacing and moves come from something the designer chose, not from defaults. Two sources, used together:

- **Reference library** (`library/`): public references shared by every piece. Read `library/index.md` and pick 1–3 entries whose tags fit the kind and the source.
- **User references**: what the designer gives for this piece. They come first; the library fills what they leave open.

## Analysing a user reference

| Given | What to do |
|---|---|
| A local video file or screen recording | Measure it with `../../motion-audit/scripts/measure-motion.py <file> --sheets <scratch folder>` (run Python with `-I`), then read the contact sheets. |
| Stills or Figma frames | Read them; motion is inferred only from what changes between them. |
| A link to someone else's video (YouTube, Vimeo, a studio site) | Do not download it. Read the public page, description and thumbnails, and ask the designer to describe the motion or share a recording they are allowed to use. Mark the notes `from description`. |
| A spoken description | Write it down as given. |

Client and Bliss work given as a reference is the designer's material: analyse it, never copy it into the plugin repo or the library.

## What to write

Per reference, and then merged into the piece's motion language:

- **Density**: share of time in motion, a move every N s, longest hold, hard cuts (from the script, or `not measured`).
- **Pacing**: how long a phrase or a screen stays, where it slows down, where it bursts.
- **Text**: how copy arrives and leaves, accent colour on keywords, one line or several.
- **Signature moves**: the 3–6 moves that make it recognisable, named from `motion-vocabulary.md` (`custom` where none fits).
- **Easing feel**: snappy, soft, springy; overshoot or none.
- **Transitions**: how panels join (morph, cut, wipe, zoom), and where cuts are used.

Take the density target in the motion spec from the user reference when one was measured; otherwise keep the defaults in `motion-vocabulary.md`.

## Where it is kept

- The merged motion language goes into the motion spec's **Motion language** card, naming each reference used.
- When the piece has a project folder (or the designer names one), save each user reference as `references/<slug>.md` next to `BRIEF.md`, in the entry format below, with any stills in `references/<slug>/`. Otherwise it lives only in the storyboard and the conversation.
- A user reference is never added to `library/`. To propose a public reference for the library, see `CONTRIBUTING.md`.

## Entry format

Library entries and saved user references use the same file:

```markdown
---
title: <name>
maker: <studio or company>
url: <public link, or "local file">
year: <year>
length: <m:ss>
kind: video | UI
moves: [phrase-swap, shape-morph, push-in]
density: { active_pct: 74, seconds_per_move: 2.6, longest_hold_s: 2.75, hard_cuts: 8 }   # or "not measured"
notes_from: measured | watched | from description
---

## Motion language
- Pacing: …
- Text: …
- Signature moves: …
- Easing feel: …
- Transitions: …

## Use it for
One line: the kind of piece or panel this reference is good for.
```
