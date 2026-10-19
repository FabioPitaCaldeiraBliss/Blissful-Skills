---
name: motion-assemble
description: Assemble every animated panel of a motion or video piece into one HyperFrames project, with transitions and stand-ins for missing clips, then render and verify the final cut. Use after motion-animate, and again whenever a human delivers a clip.
argument-hint: "[assembly project] [storyboard]"
---

# Motion Assemble

Needs the HyperFrames skills (`~/.claude/skills/hyperframes`). If missing, stop and print `npx skills add heygen-com/hyperframes -g -a claude-code -s '*' -y`. Safe to re-run: a re-run only changes what changed (a delivered clip, a moved panel, an edited transition).

1. Resolve the inputs: the assembly project (prepared by `motion-animate`), and the storyboard (panel order, durations, routes, transitions, piece format). Ask only for what is missing.
2. Read `references/assembly.md`.
3. Take stock of every panel in order: a `hyperframes` panel needs its `compositions/panel-NN.html`; a `figma motion` or `after effects` panel needs its clip `clips/NN-panel.mp4` (or Lottie `NN-panel.json`). **Validate every clip** with `ffprobe` against the piece format and reject mismatches (reasons in the reference).
4. **Stop and show the assembly plan**: the panels in order with start times from their durations, each panel's source (scene, clip, or **stand-in**), the transitions, the total against the length limit, and the missing and rejected items. Build nothing until it is approved.
5. Build the root `index.html`: each panel mounted at its start time, a stand-in for anything missing, transitions between panels, nothing else. Edit what exists; do not recreate the project.
6. Verify: `npx hyperframes check` passes with 0 errors, and snapshots at each panel's midpoint and at each cut are read.
7. Open the Studio preview (`npx hyperframes preview --background`) and ask whether to render or revise. Render only after approval.
8. After the render, sample frames with `ffmpeg` (first, each cut, last) and check duration and size against the piece format. Offer each panel as its own file on request.
9. Output: the preview or rendered file, its real duration against the limit, what is a stand-in or rejected and why, and each panel's edit home.
