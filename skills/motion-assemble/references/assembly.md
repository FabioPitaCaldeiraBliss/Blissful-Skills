# Assembly

One HyperFrames project holds the whole piece. Follow HyperFrames' own contract (`/hyperframes-core`) for composition structure; this file adds only what is specific to assembling panels from several routes.

## Start times

Panels play in storyboard order, each at the sum of the durations before it. Root `data-duration` is the total. Flag a total above the piece format's length limit.

## Mounting

| Panel source | How it is mounted |
|---|---|
| `hyperframes` scene | A host `<div>` with `data-composition-id`, `data-composition-src="compositions/panel-NN.html"`, `data-start`, `data-duration`, `data-track-index`, `data-width`, `data-height`. The host id equals the composition id. |
| Rendered clip (`figma motion`, or `after effects` clip) | A `<video id="panel-NN" src="clips/NN-panel.mp4" data-start data-duration data-track-index playsinline>` with a unique id. Time the video itself, never a wrapper that also has `data-start`. |
| Lottie (`after effects`) | A sub-composition holding the player, following `/hyperframes-animation` → `adapters/lottie.md`: local file, `autoplay: false`, `loop: false`, registered on `window.__hfLottie`. |
| Missing | A **stand-in** (below). |

## Validate a delivered clip

Run the bundled validator, which uses `ffprobe` and exits 0 (accept), 1 (reject) or 2 (missing):

```
python3 <skill>/scripts/validate-clip.py clips/NN-panel.mp4 <width> <height> <fps> <duration-seconds>
```

It compares the file with the piece format:

- Size equal to the format (e.g. 1920×1080).
- Frame rate equal to the format's fps.
- Duration equal to the panel's, within one frame. A Figma motion export runs exactly one frame long (241 frames for 8 s at 30 fps); that is inside the tolerance, so accept it as is.
- Playable, with a video stream.

Reject a clip that fails any of these: leave it where it is, mount the stand-in instead, and report which check failed and the actual vs expected values. Never stretch, crop or retime a delivered clip to make it fit.

## Stand-ins

A missing panel is a small sub-composition `compositions/standin-NN.html` (id `standin-NN`) of the panel's exact duration: neutral background, the panel number and name, its route, the expected file name, and a `MISSING` label. Style it plainly so it cannot be mistaken for finished work. When the expected file appears and validates, replace the host with the real mount and delete the stand-in file.

## Transitions

A transition is its own sub-composition, mounted on a higher track, centred on the cut between two panels (a 0.8 s wipe starts 0.4 s before the boundary). Build one reusable composition (for example `compositions/wipe.html`) and mount it at each boundary the storyboard asks for. A boundary the storyboard marks as a hard cut gets none. Use the brand curve only if the designer supplied it; otherwise the brand gradient as a stand-in, flagged.

## Audio

None unless the designer supplies a track. If they do, follow `/hyperframes-core` for placement and `/hyperframes-audio` for mixing, and snap nothing to the beat unless a BPM was given.

## Render and verify

- Render only after the designer approves the Studio preview.
- Sample the first frame, each cut and the last frame with `ffmpeg`; read them.
- Compare the file's size, fps and duration with the piece format.
- Per-panel files on request: cut each from the final render by its start time and duration, re-encoded so the cuts are exact.

## Editing the root file

`npx hyperframes check` and `preview` stamp `data-hf-id` attributes onto elements of `index.html`. Do not match the file's text with fixed patterns: match by element `id`, or rewrite the file whole.

## Re-runs

Re-running after a delivery changes only that panel's host. Keep every other mount, transition and timing as they are, and re-run `check` and the snapshots for the changed neighbourhood.
