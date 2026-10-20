# Assembly

One HyperFrames project holds the whole piece. Follow HyperFrames' own contract (`/hyperframes-core`) for composition structure; this file adds only what is specific to assembling panels from several routes.

## Render scope

The designer picks what one run renders: the whole piece, one scene, or a run of panels. Each scene is a complete video (it carries its own in and out through its handoff states), so any scope renders on its own.

Write the root `index.html` for the scope with the generator rather than by hand:

```
python3 -I <motion-animate>/scripts/build-scenes.py <project> --scope all        # whole piece
python3 -I <motion-animate>/scripts/build-scenes.py <project> --scope 04         # one scene video
python3 -I <motion-animate>/scripts/build-scenes.py <project> --scope 03-06      # a run of panels
```

It mounts the chosen panels back to back from 0 s, mounts a delivered clip or a stand-in for panels on other routes, mounts the wipe between panels whose `transition_in` is `wipe`, and offsets the music so a scene keeps its own part of the track. `hyperframes render` only renders `index.html` and what it references, so a single scene is rendered through a scope index, never from its composition file alone.

## Start times

Within a scope, panels play in storyboard order, each at the sum of the durations before it. Root `data-duration` is the total. Flag a whole-piece total above the piece format's length limit.

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

None unless the designer supplies a track; never generate or source music. If they do, add it to `scenes.json` (`audio`) so every scope index places it, and follow `/hyperframes-audio` for mixing. With a BPM, move starts were already snapped to the beat map (within ±2 frames) in the storyboard; check the hits land on cuts and key moves in the preview.

- **Sound effects** stay as cues: write `exports/sfx-cues.csv` (`time,cue,panel`) from the storyboard's `SFX` tags, in piece time, for whoever does the sound.
- **Captions** only when there is voice-over: write `exports/captions.srt` from the voice-over timing in the script or storyboard. On-screen text already covers the rest.

## Export formats

| File | Command | When |
|---|---|---|
| Review copy | `npx hyperframes render -f <fps> -q delivery -o renders/<name>.mp4` | Always |
| Editor master | `npx hyperframes render -f <fps> --format mov -o renders/<name>.mov` (ProRes 4444) | When the scene goes to an editor |
| Overlay with alpha | `--format mov` or `--format webm`, with `"background": "transparent"` on the piece and the panel in `scenes.json` | Lower thirds, logo stings, anything laid over other footage |
| Frames for After Effects | `--format png-sequence -o renders/<name>/` | When an animator finishes it |

A **scene video** for an editor gets 0.5 s handles: its first and last frames held, so it can be trimmed or dissolved. Add them after the render, never in the scene:

```
ffmpeg -i renders/04.mov -vf "tpad=start_mode=clone:start_duration=0.5:stop_mode=clone:stop_duration=0.5" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le renders/04-handles.mov
```

(For an MP4, use `-c:v libx264 -crf 16 -pix_fmt yuv420p`; with sound, add `-af "adelay=500:all=1,apad=pad_dur=0.5"`.) A whole-piece render gets no handles. Name scene videos `NN-<panel slug>.<ext>`.

## Render and verify

- Render only after the designer approves the Studio preview.
- Sample the first frame, each cut and the last frame with `ffmpeg`; read them.
- Compare the file's size, fps and duration with the piece format.
- Measure the render's motion density with `<motion-audit>/scripts/measure-motion.py` and report it against the motion spec's target; offer `motion-audit` for the full check.
- Per-panel files: render each scene through its own scope (above) rather than cutting the full render, so each carries its own in and out.

## Editing the root file

`npx hyperframes check` and `preview` stamp `data-hf-id` attributes onto elements of `index.html`. Do not match the file's text with fixed patterns: match by element `id`, or rewrite the file whole.

## Re-runs

Re-running after a delivery changes only that panel's host. Keep every other mount, transition and timing as they are, and re-run `check` and the snapshots for the changed neighbourhood.
