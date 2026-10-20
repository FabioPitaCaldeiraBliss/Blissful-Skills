---
tags: [motion]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Run a motion audit on this plan. 12 s, fictional app Lumo, video kind, 1920×1080, 30 fps, no music, default motion spec.

Script: "Money that moves with you. Meet Lumo."

STORYBOARD.md:

## Frame 1 — Opener
- duration: 7
- transition_in: cut
- moves: 0:00.0 glow-drift bg glow · 0:00.2 stroke-draw ring · 0:01.0 phrase-in "Money that moves with you" · 0:02.0 keyword-accent "moves" · 0:02.6 shape-morph ring → disc → tile · 0:04.0 phrase-swap → "Meet Lumo." · 0:05.6 breathe tile · 0:06.5 phrase-out "Meet Lumo."
- handoff_out: the tile, centred, 180 px, no copy
- copy: "Money that moves with you" / "Meet Lumo."

## Frame 2 — Close
- duration: 5
- transition_in: morph-through
- handoff_in: the tile, centred, 180 px
- moves: 0:07.0 shape-morph tile → small tile (140 px, left of centre) · 0:07.6 phrase-in wordmark type "lumo" beside it · 0:09.0 ring-pulse from the tile · 0:10.0 logo-resolve lockup (blur 12 → 0 px, scale 0.92 → 1, 1000 ms) · 0:11.0 breathe lockup
- copy: "lumo"
