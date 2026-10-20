# Route: hyperframes

Each `hyperframes` panel becomes a native scene in the assembly project: one sub-composition built from the panel's frame layers. Follow HyperFrames' own workflow and rules instead of copying them here: read `/hyperframes`, `/general-video`, `/hyperframes-core` and `/hyperframes-animation` before writing composition HTML.

## Prepare the project

Client material stays out of the plugin repo. Ask where the project lives; propose `~/Documents/Projects/<piece>-motion/` and scaffold with:

```
npx hyperframes init "videos/<piece>" --non-interactive --example=blank --skill=general-video
```

Then write, once:

- `BRIEF.md` with `workflow: general-video`, `flow: automation`, `storyboard: no`, the piece format, the message and the panel list.
- `frame.md` from the `motion-frames` export (tokens and rules; HyperFrames reads it before any `design.md`).
- `assets/screens/` and `assets/fonts/` from the exports. Ship the type locally as `.woff2`.

An already prepared project is extended, not recreated.

Put the plan in the project's `STORYBOARD.md` (written by `motion-storyboard`, format in its `references/storyboard-md.md`) and edit `BRIEF.md` for any decision; HyperFrames works from those files, not from chat. Raise a panel's `status` as it moves from `outline` to `built` to `animated`.

## One scene per panel

- File `compositions/panel-NN.html`, composition id `panel-NN`, timeline registered under that id.
- Duration from the storyboard. Size from the piece format.
- Element ids and names follow the frame's layers (`NN Panel / element`), so the scene maps back to the Figma frames.
- The panel's motion and route notes from the storyboard drive the plan; cite HyperFrames rules and blueprints by name from its indexes rather than inventing motion names.

## Rules that caused first-build failures

- Put `@font-face` inside each sub-composition's own `<template>` `<style>`, or lint rejects the font.
- Asset URLs in a sub-composition resolve from the project root (`assets/...`), not from the composition file.
- Root and sub-composition `#root` use `inset: 0` or 100% sizes; canvas size comes from `data-width` and `data-height`.
- Animate children, never the timed clip; no `Math.random`, clocks or network; register one paused timeline per composition.
- A real count-up uses a proxy value tweened with GSAP and written in `onUpdate`; it stays seek-safe.
- Re-use the same sub-composition for repeated items (a wipe) by mounting it twice.

## Verify

- `npx hyperframes check` must pass with 0 errors (it runs lint, runtime, layout, motion and contrast; a lint error switches the other audits off, so clear errors first).
- Snapshot each panel at its key moments (`npx hyperframes snapshot --at <seconds>`) and read the contact sheets.
- Do not render here; `motion-assemble` renders the whole piece.

## Build from the frames

The frames are the source of truth, so read them back instead of retyping them, and generate the scenes with the bundled scripts rather than writing composition HTML by hand.

1. **Read the frames.** Run `scripts/dump-frames.js` with `use_figma` (load `figma-use`), with `SECTION_ID` set to the `Frames · <piece>` Section. It returns, per panel, every layer (geometry, paint, text, accents, state overlays), the director note under each frame, and the image layers to export with the path each expects.
2. **Export the images** it lists with `download_assets` at 3× into `assets/screens/`, under exactly those paths.
3. **Write `scenes.json`** (format in `scenes-json.md`): the piece format and fonts, each panel's layers from step 1, the groups that move together (a phone and its screen), and the panel's moves taken from its `moves` line in `STORYBOARD.md`. Moves come from `motion-vocabulary.md`; a move with no generator support is `custom` with its own GSAP.
4. **Generate:** `python3 -I <skill>/scripts/build-scenes.py <project> --only <panels>` writes `compositions/panel-NN.html`. It bakes every value from the frame geometry (no layout measuring), gives the first tween on each property the start state, adds `data-layout-allow-overlap` to state overlays, and keeps one paused timeline per scene.
5. **Re-runs** only rewrite what the generator wrote. A composition edited by hand (in Studio or by Claude on request) is reported as `skipped (edited by hand)`: it is now that panel's edit home. Show what changed in Figma and ask whether to apply it with `--force NN` or keep the edited file.

A scene is a complete video: it starts on its **handoff state** (the layers that are already in place at 0 s, matching the previous panel's last state) and ends on the handoff into the next. Layers that should appear later get an entering move; layers that are simply there at 0 s get none.

Pitfalls the generator does not catch:

- A layer whose start opacity is not its Figma opacity: give it a `fade` or an entering move, never edit the HTML.
- `word-swap` needs both lines as states of one layer; if the swapped words differ a lot in width, the shared words visibly shift, so prefer `phrase-swap`.
- A `push-in` target must be inside the frame; the camera scales the whole scene, background included.
