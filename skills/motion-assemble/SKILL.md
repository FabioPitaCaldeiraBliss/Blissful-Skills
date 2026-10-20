---
name: motion-assemble
description: Assemble the animated panels of a motion or video piece in one HyperFrames project, for the whole piece or chosen scenes, with transitions and stand-ins for missing clips, then render and verify each video. Use after motion-animate, and again whenever a human delivers a clip.
argument-hint: "[assembly project] [storyboard]"
---

# Motion Assemble

Needs the HyperFrames skills (`~/.claude/skills/hyperframes`). If missing, stop and print `npx skills add heygen-com/hyperframes -g -a claude-code -s '*' -y`. Safe to re-run: a re-run only changes what changed (a delivered clip, a moved panel, an edited transition).

1. Resolve the inputs: the assembly project (prepared by `motion-animate`), the storyboard (panel order, durations, routes, transitions, piece format), and the **render scope**: the whole piece, one scene video, or a run of panels. Ask for the scope and the export formats (review copy, editor master, alpha, handles) if not given.
2. Read `references/assembly.md`.
3. Take stock of every panel in order: a `hyperframes` panel needs its `compositions/panel-NN.html`; a `figma motion` or `after effects` panel needs its clip `clips/NN-panel.mp4` (or Lottie `NN-panel.json`). **Validate every clip** with `ffprobe` against the piece format and reject mismatches (reasons in the reference).
4. **Stop and show the assembly plan**: the scope, the panels in it in order with start times from their durations, each panel's source (scene, clip, or **stand-in**), the transitions, the total against the length limit, and the missing and rejected items. Build nothing until it is approved.
5. Write the root `index.html` for the scope with `build-scenes.py --scope` (see `assembly.md`): each panel at its start time, a stand-in for anything missing, wipes between panels, the music offset to the scope. Write the SFX cue list, and captions when there is voice-over.
6. Verify: `npx hyperframes check` passes with 0 errors, and snapshots at each panel's midpoint and at each cut are read.
7. Open the Studio preview (`npx hyperframes preview --background`) and ask whether to render or revise. Render only after approval.
8. Render the agreed formats (table in `assembly.md`), add handles to scene videos for an editor, sample frames with `ffmpeg` (first, each cut, last), check duration and size against the piece format, and measure motion density against the motion spec.
9. Output: the preview or rendered file, its real duration against the limit, what is a stand-in or rejected and why, and each panel's edit home.
