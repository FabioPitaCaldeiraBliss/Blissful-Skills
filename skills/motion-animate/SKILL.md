---
name: motion-animate
description: Animate the panels of a motion or video piece, each by its own route (HyperFrames, Figma motion, or a handoff to a human in After Effects), following the storyboard and final frames. Use after motion-frames, or when asked to turn finished frames and a storyboard into animation.
argument-hint: "[frames page or link] [storyboard] [BPM, optional]"
---

# Motion Animate

Routes each panel by the **route** the storyboard recorded. Builds only the panels in the **render scope** the designer picks (the whole piece, or chosen scenes). Does not render; `motion-assemble` does.

1. Resolve the inputs: the final frames (from `motion-frames`), the storyboard with its piece format and each panel's route, and optional BPM. If there are no frames with `NN Panel / element` layers, stop and point to `motion-frames`, unless the designer says to animate from the storyboard.
2. Check dependencies for the routes in use. `hyperframes` needs the HyperFrames skills (`~/.claude/skills/hyperframes`); if missing, stop and print `npx skills add heygen-com/hyperframes -g -a claude-code -s '*' -y`. `figma motion` needs Figma motion enabled; if a motion call fails with `"not a supported API"`, stop and say so.
3. Read `references/animation.md`, then only the route files the plan uses: `references/hyperframes.md`, `references/figma-motion.md`, `references/handoff.md`.
4. Ask for the render scope if it wasn't given: the whole piece, or which panels. Then read every in-scope panel's duration, moves, motion, transition and audio notes, its route, and the layers of its frame. Note any layer that already has motion.
5. **Stop and show the animation plan** (format in `references/animation.md`), grouped by route. Build nothing until it is approved.
6. Build the approved plan, route by route:
   - `hyperframes`: prepare the HyperFrames project, read the frames back, write `scenes.json` and generate each panel with `scripts/build-scenes.py` (steps in `hyperframes.md`, format in `references/scenes-json.md`).
   - `figma motion`: build timeline frames, keyframe them, export each as a clip.
   - `after effects`: write the handoff pack and note the file name expected back.
7. Verify each route its own way (see the reference files).
8. Output: per panel its route, what was built or written and where, the defaults used, what could not be animated and why, what was verified, and what the designer still has to supply. Update each panel's **edit home** in the storyboard. Point to `motion-assemble` as the next step.
