# Motion audit checklist

Eight categories. Each check says where it runs: **plan** (storyboard, animation plan, `scenes.json`), **render** (the video), or both. Numbers default to the motion spec of the piece; where the piece has none, use the defaults in `motion-storyboard/references/motion-vocabulary.md`.

Severity: **High** blocks handoff (a seizure risk, unreadable key copy, a missing or wrong claim). **Medium** clearly hurts the piece (dead holds, a muddled focal point, mismatched easing). **Low** is polish.

## 1. Purpose

| Check | Where | Source |
|---|---|---|
| Every move serves the panel's one idea: it reveals, connects, explains or confirms. A move that only decorates sits on a background layer. | plan | Material motion principles; Carbon productive vs expressive |
| One focal point at a time: two hero moves do not start within 0.3 s of each other in different parts of the frame. | both | Disney's staging; Atlassian "one or two properties per transition" |
| The recurring element from the motion spec appears where the storyboard plants and returns it. | both | Motion spec |
| No copy, number or claim on screen that is not in the script or storyboard. | both | Script |

## 2. Timing and density

| Check | Where | Source |
|---|---|---|
| Share of time in motion within the target (default 65–80%). | render (measured); plan (sum of move durations) | Motion spec; reference library |
| No gap between move starts longer than 3 s except the named hero hold. A faster cadence is not a finding unless two hero moves compete (see Purpose). | both | Motion spec |
| Text on screen for at least the time to read it twice: about 0.3 s per word plus 1 s, never under 2 s for a phrase. | both | Rule of thumb; motion spec "phrase on screen" |
| Panel durations add up to the piece length; the total is within the length limit. | plan | Piece format |
| With a BPM, cuts and hits land on the beat map within ±2 frames. | both | Beat map |

## 3. Easing

| Check | Where | Source |
|---|---|---|
| Enters decelerate (expo or ease out), exits accelerate (expo or ease in), morphs ease in-out; no linear movement except constant pans and tickers. | plan | Material 3 easing tokens; Atlassian motion |
| Exits are shorter than enters (by 50–200 ms). | plan | Atlassian; Material 3 |
| One easing family per piece; overshoot (back, spring) only where the motion spec names it. | plan | Motion spec |
| UI interactions inside a scene (tap, toggle, state change) stay within 150–500 ms. | plan | Atlassian 50–150 / 150–400 ms; Carbon duration tokens |

## 4. Choreography

| Check | Where | Source |
|---|---|---|
| Related elements stagger 20–120 ms apart and a group arrives within about 0.5–0.8 s. | plan | Carbon choreography; HyperFrames stagger cap |
| Elements that move together are grouped and share an origin (a phone and its screen). | plan | `scenes.json` groups |
| Joins between `hyperframes` scenes match: the last state of one panel is the first state of the next (handoff state), or the join is a named cut or wipe. | both | Glossary: handoff state |
| No element overlaps another by accident at any sampled moment; `check` reports no unintended overlap or occlusion. | render | HyperFrames `check` layout audit |

## 5. Flashing and auto-play

| Check | Where | Source |
|---|---|---|
| No more than 3 flashes in any second over a large area (about 341×256 px at 1080p); no saturated red flashes. | render (`--flash`, approximate; red rule by eye) | WCAG 2.2 SC 2.3.1 (A), 2.3.2 (AAA) |
| No large-area strobe, rapid oscillation or full-frame sweep used as a transition. | both | Atlassian motion; WCAG 2.3.1 |
| Where the piece plays inside a product or page: auto-playing motion over 5 s can be paused, and sound over 3 s can be stopped. | plan (note for the developer) | WCAG 2.2 SC 2.2.2, 1.4.2 |

## 6. Reduced motion

Only for the `UI` kind; a `video` piece is N/A.

| Check | Where | Source |
|---|---|---|
| Every move in the plan has its reduced-motion fallback (a fade or an instant change) from the vocabulary. | plan | WCAG 2.3.3 (AAA); W3C technique C39 |
| Parallax, large-scale zooms, multi-axis camera moves and spins have a fallback that removes the movement, not just shortens it. | plan | Apple reduced-motion evaluation criteria; MDN prefers-reduced-motion |
| The fallback keeps the meaning: the user still sees the state change. | plan | WCAG 2.3.3 "essential" |

## 7. Performance and build

| Check | Where | Source |
|---|---|---|
| Only transforms, opacity and paint properties are animated; no width, height, top or left. | plan (`scenes.json`, compositions) | HyperFrames contract; Atlassian |
| `npx hyperframes check` passes with 0 errors; warnings are listed. | render | HyperFrames |
| Each scene is seek-safe: snapshots at the same time give the same frame; nothing depends on clocks or randomness. | render | HyperFrames contract |
| Delivered clips match the piece format (size, fps, duration within one frame). | render | `motion-assemble` validator |

## 8. Video quality

| Check | Where | Source |
|---|---|---|
| Size, frame rate and duration match the piece format. | render | Piece format |
| Text and key content inside title-safe (80%), everything visible inside action-safe (90%). | both | Broadcast safe areas; `motion-frames` craft |
| No banding on large gradients (radial or solid with glow preferred), no visible compression blocks in dark areas. | render (by eye on stills) | `motion-frames` craft |
| Type stays at video sizes (headline 60 px or more at 1080p) and meets WCAG AA contrast against what moves behind it. | both | `motion-frames` craft; WCAG 1.4.3 |
| Scene videos for an editor carry 0.5 s handles; the full piece carries none. | render | `motion-assemble` exports |

## Measuring

`scripts/measure-motion.py` reports the share of time in motion, motion segments, holds of 0.75 s or more with where they start, hard cuts and, with `--flash`, an approximate flash check. A frame counts as moving when any cell of an 8×6 grid changes, so a small UI move counts. Live footage, grain and drifting glows also read as motion (a footage-heavy reference can read over 90%), and a continuous move counts as one segment. Compare renders of the same kind, read the numbers with the plan's own count of moves, and treat a surprising reading as a prompt to look at the contact sheet, not a finding on its own.
