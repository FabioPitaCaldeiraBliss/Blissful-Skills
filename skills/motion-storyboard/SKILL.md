---
name: motion-storyboard
description: Build a motion or video storyboard in Figma from a script, plan, screens or images: a motion spec, a beat map and timed key frames per panel, each panel with a route. Use when asked to storyboard an animation, a UI motion sequence or a promo video before designing frames.
argument-hint: "[script, plan, Figma link or images]"
---

# Motion Storyboard

Needs the Figma MCP with edit access to the target file. If it is missing, stop and say so.

1. Resolve the source material: script, plan, Figma screens, images, or any mix. Ask only if none is given. Warm sources (a script, real screens, a brief) produce richer storyboards than a one-line idea; ask for them when the request is cold.
2. Decide the **kind** (UI motion or video) and the **piece format**: size, fps, length limit, and BPM when there is music. Take what the source states; propose the rest once and ask.
3. Read `references/motion-spec.md` and write the **concept line** and the **motion spec**: the decisions every panel inherits. Ask only where the source is silent.
4. Read `references/panel.md`. Split the source into **panels**, in order, one idea each. Give every panel 3–5 timed **key frames**: timecode, one sentence, tags. Leave unanswered notes as a visible **gap** (`?`).
5. Propose a **route** and an **edit home** for each panel (rules in `panel.md`). Default route: `hyperframes`.
6. Read `references/layout.md` and build it in Figma (load `figma-use` first): header, motion spec, legend, beat map when there is a BPM, then one row per panel. A new version goes below a divider; earlier versions stay.
7. When any panel's route is `hyperframes`, write the machine-readable mirror: read `references/storyboard-md.md`.
8. Output: the Figma link, a one-line summary per panel with its route, the total against the limit, then **all open gaps and route confirmations in one batch of questions**. Draw first, ask after.
