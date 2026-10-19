# Route: figma motion

Figma motion works per top-level frame: each frame has its own timeline, a top-level frame itself cannot be animated, and there is no timeline across frames. Use `figma-use` and `figma-use-motion`.

## Timeline frames

- One per `figma motion` panel, named `NN Panel · timeline`, on the page `Animation · <piece>`.
- Duration is the storyboard duration for that panel. A new timeline frame may be set shorter or longer than the 2 s default; never shorten an existing designer-made timeline.
- A single-frame panel: clone its frame. A panel with several states: clone the first state's frame and add the other states' layers, named `NN Panel / <state> <element>`, then cross-fade or swap them inside the one timeline.
- Leave the static frames untouched.
- Panel timelines carry no in or out of their own; transitions are built in the assembly.

## Keyframes

- `SCALE_XY` takes a vector value `{x, y}`; the other transform fields take a float.
- Easing uses the public enum (`EASE_OUT`, `EASE_IN_AND_OUT`, never `EASE_IN_OUT`).
- Opacity is an absolute field: a layer whose static opacity is below 1 must animate to that value, not to 1.
- Re-applying a track replaces it, so a failed batch can be re-run safely.
- Timeline values are in seconds.

## Export the clip

Export each timeline frame with `export_video` at the piece format: full size (no `constraint`), `fps` equal to the piece fps, medium or high quality, and save it as `clips/NN-panel.mp4` in the assembly project (the file name is the contract with `motion-assemble`). The export runs one frame longer than the timeline, which `motion-assemble` accepts. The render service limits concurrent and per-minute exports (about 5 at once): start 3–5, download them, then start the next batch; if throttled, wait about 90 s.

## Verify

- Render each timeline once small (about 480 px wide, low quality, 5 fps) and sample the first, middle and last frames with `ffmpeg`; read them all, fix everything in one batch, re-render only if needed.
- Check that moving elements never cross text or other layers on the way in or out; prefer a path that stays clear.
- `get_screenshot` shows only the resting state; it cannot verify motion.
- No `ffmpeg`: skip rendering and say motion was not verified.
