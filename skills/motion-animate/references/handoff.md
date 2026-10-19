# Route: after effects

A human animates these panels. The skill's job is a complete handoff and a clear contract for what comes back.

## Handoff pack

Per panel, in the exports folder (`NN-panel/`), written by `motion-frames` and completed here:

- The layered artwork: every layer as PNG at 3× (or SVG), named exactly like its Figma layer (`NN Panel / element`).
- `notes.md`: the panel's duration, motion, transition, trigger and on-screen text, in the storyboard's words, plus the piece format (size, fps) and the Figma frame link.
- A short list of what is a `MISSING:` placeholder and still needs an asset.
- The delivery request (below).

Also add one `HANDOFF.md` at the folder root listing every After Effects panel, its expected file name and its status.

## Delivery

The human delivers one of:

- **Rendered clip** `NN-panel.mp4` (H.264, or ProRes if alpha is needed): any effects, not editable downstream.
- **Lottie** `NN-panel.json` (or dotLottie): vector, editable at source in After Effects, crisp at any size, but only a subset of After Effects features.

Record which format was agreed in the panel's notes, and the human's project path as the panel's edit home.

Files go in `clips/` in the assembly project and keep the exact name. The clip must match the piece format: same size, same fps, duration equal to the panel's (a tolerance of one frame). `motion-assemble` validates this on arrival.

## While waiting

The panel stays on the plan as `awaiting delivery`; the assembly shows a stand-in of the right length. Nothing else is animated for it.
