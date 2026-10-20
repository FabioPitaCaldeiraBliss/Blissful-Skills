# Animation

The piece is animated panel by panel, each by its own route, then assembled and rendered in one HyperFrames project by `motion-assemble`. Every route inherits the **piece format** (size, fps, length limit) from the storyboard header.

## Animation plan

Show it before building, grouped by route:

| Panel | Route | Duration | What happens |
|---|---|---|---|
| `01 Hook` | hyperframes | 6 s | counter counts up to its final value (0.1–1.4 s), label fades in (1.4 s), headline lands word by word (2.2 s) |
| `04 Onboarding` | figma motion | 8 s | headline slides in (0–0.6 s), phone slides up (0.2–0.9 s) |
| `03 The turn` | after effects | 4 s | handoff pack; clip `03-the-turn.mp4` expected back |

For `hyperframes` panels, list each move by its vocabulary name (`motion-vocabulary.md`) with its start and target; for `figma motion` panels, each layer's motion with start, end and easing. For `after effects` panels, list the handoff pack contents and the delivery format.

Under the table list: the **render scope** (which panels this run builds; the designer chooses), the planned density per panel against the motion spec's target (moves per second, longest gap between moves), the defaults used, meaning gaps as questions, layers that already have motion (ask keep or replace), what cannot be animated and why, and the BPM question if none was given. Wait for approval.

## Defaults

Apply only where the storyboard notes are silent, and list them back:

- Durations and eases come from the move's default in `motion-vocabulary.md`, then the motion spec.
- Where a panel falls short of the density target, propose moves to fill the gap (an ambient move under a hold, a supporting move on a secondary element); never stretch a hold.
- Animate transform and opacity; avoid width, height, top and left.
- Keep functional motion within 150–500 ms; longer only for rare expressive moments.
- Never flash more than 3 times a second, and avoid large-area flashes.

Anything that changes meaning (order, a trigger, the length of a key moment) is a gap: ask, do not default.

## Limits

- Counting a number up works in `hyperframes`, not in `figma motion` (stepped layers only). Prefer `hyperframes` for counters.
- A layer that is a `MISSING:` box can be animated for timing, but its real motion (an old app cracking, a logo disintegrating) waits for the asset.
- Image layers move as whole images; nothing inside a screenshot can be animated separately.
- No audio in Figma. Snap motion starts to the beat only when the designer gives a BPM (beat = 60 / BPM seconds); otherwise say timing follows the storyboard only.
- A `hyperframes` scene carries its own in and out through its handoff states, so it renders alone. Wipes, cuts and the joins with clips from other routes are built in the assembly.

## Verify, by route

- `hyperframes`: `npx hyperframes check` passes, and snapshots at key moments are read.
- `figma motion`: one low-resolution `export_video` per timeline frame, sampled with `ffmpeg` (see `figma-motion.md`).
- `after effects`: nothing to verify until the clip arrives; `motion-assemble` validates it.
