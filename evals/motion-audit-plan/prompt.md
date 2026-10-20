---
tags: [motion]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Audit this motion plan before we build it. It's a 20 s promo for a fictional app, Lumo, video kind, 1920×1080, 30 fps, no music. The motion spec uses the default density target and easing.

Script: "Money that moves with you. Your wallet, live. Send money in a tap. Lumo."

STORYBOARD.md:

## Frame 1 — Opener
- duration: 6
- transition_in: cut
- moves: 0:00.2 stroke-draw ring · 0:01.0 phrase-in "Money that moves with you" · 0:02.2 phrase-swap → "Your wallet, live." · 0:03.4 shape-morph ring → tile · 0:04.6 breathe tile
- copy: "Money that moves with you" / "Your wallet, live."

## Frame 2 — Device
- duration: 8
- transition_in: custom: full-frame white flash strobe, 6 flashes in 1 s
- moves: 0:06.0 device-rise phone (expo out, 400 ms) · 0:06.4 phrase-in "Trusted by 2 million users" · 0:07.6 exit phrase (expo out, 900 ms) · 0:13.5 tap pay button
- copy: "Trusted by 2 million users"

## Frame 3 — Close
- duration: 6
- transition_in: cut
- moves: 0:14.0 phrase-in "Send money in a tap." · 0:15.2 phrase-swap → "Lumo." · 0:16.4 logo-resolve wordmark · 0:18.0 glow-drift
- copy: "Send money in a tap." / "Lumo."
