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

The frames are the source of truth, so read them back instead of retyping them: use `use_figma` to dump every layer of every frame (name, type, x, y, width, height, fills, strokes, opacity, radius, effects, text content, size, weight, colour, alignment, tracking, line height, accent ranges) as compact JSON, and generate each `compositions/panel-NN.html` from it.

- A layer's id is its slugified name with the panel prefix (`p04-headline`), so the scene maps back to the Figma layer.
- A state panel (several frames) renders the first state's layers, plus an overlay for every layer that differs in a later state (`p09-headline--s2`); the overlays fade in at the state's time. Mark an overlaying text layer `data-layout-allow-overlap` and fade the base text out as the overlay arrives, or `check` reports overlapping text.
- Wrap parts that move together (phone and screen, a banner and its icon) in a group, with its own transform origin, and animate the group.
- Static opacity is part of the design: keep a map of layers whose opacity is below 1, and tween to that value, not to 1.
- Motion values come from the storyboard's motion spec (expo out for enters, expo in for exits, ease in-out for morphs, 80 ms stagger). A phone entering with a slight perspective tilt (`rotationY` with `transformPerspective`) and a cursor that taps a control are cheap ways to add depth.
- A typewriter headline: split into character spans and reveal them in steps, with a gradient caret as an absolutely positioned pseudo-element so it never shifts the layout.
