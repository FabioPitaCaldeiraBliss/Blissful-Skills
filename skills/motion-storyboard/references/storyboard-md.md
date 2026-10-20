# STORYBOARD.md mirror

HyperFrames reads a `STORYBOARD.md` at its project root as the plan it builds from. The Figma storyboard stays the visual source; this file is its machine-readable mirror, so the `hyperframes` route does not re-derive anything.

## Frontmatter

```yaml
---
format: 1920x1080
duration: 88            # seconds; advisory, assembly reports drift against it
message: "<the one-sentence thesis of the piece>"
arc: "<the story arc in a phrase>"
audience: "<who it is for>"
mode: automation
---
```

## One block per panel

```markdown
## Frame 5 — Simpler to pay.
- status: outline
- src: compositions/panel-05.html
- duration: 14
- transition_in: morph-through
- scene: One-line caption of what the panel shows.
- route: hyperframes
- edit_home: compositions/panel-05.html
- keyframes: 0:26.0 chapter title lands · 0:28.5 card leaps out of the screen · 0:32.0 payment confirmed · 0:36.0 padlock draws
- role: key feature
- shot: device-surface-showcase
- moves: 0:26.0 phrase-in title · 0:28.5 custom: card leaps out of the screen · 0:30.0 state-change card · 0:32.0 success-burst · 0:36.0 stroke-draw padlock
- handoff_in: payment card centred, 640 px wide (panel 04's last state)
- handoff_out: padlock outline centred, 220 px (panel 06's first state)
- copy: "Simpler / to pay."
- beat: <what the viewer feels or learns>
- focal: <the one element the eye lands on>
```

Rules:

- Emit `status`, `src`, `duration`, `transition_in` and `scene` exactly; HyperFrames parses them. Other keys (`route`, `edit_home`, `keyframes`, `role`, `shot`, `moves`, `handoff_in`, `handoff_out`, `copy`, `beat`, `focal`) are kept verbatim as extras.
- `moves` lists every move with its start time, named from `motion-vocabulary.md`; `motion-animate` builds from it and `motion-audit` checks against it.
- `handoff_in` and `handoff_out` describe the shared state with the neighbouring panels; leave them out next to a `cut` or a clip from another route.
- `transition_in` is a vocabulary transition (`morph-through`, `zoom-through`, `cut`, `wipe`, `dissolve`).
- `status` runs `outline` → `built` (layout confirmed, no motion) → `animated`. Mirror the Figma panel's status.
- `src` is the composition file for a `hyperframes` panel and the expected clip (`clips/NN-panel.mp4`) for the other routes.
- `copy` is quoted exactly; `/` marks a line break.
- A panel marked `locked` in Figma is never overwritten here. New decisions are appended as dated notes under the panel, not edited in place.
- When Figma and this file disagree, the Figma storyboard wins until the designer says otherwise.
