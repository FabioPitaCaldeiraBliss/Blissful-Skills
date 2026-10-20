---
name: motion-frames
description: Design the final, layered, animation-ready static frames for a motion or video piece from its storyboard, and export what each animation route needs. Use after motion-storyboard and before motion-animate, or when asked to turn a storyboard into finished frames to animate.
argument-hint: "[storyboard link] [frame size] [references / design system]"
---

# Motion Frames

Needs the Figma MCP with edit access to the target file. If it is missing, stop and say so.

1. Resolve the inputs: the storyboard (required) with its motion spec, key frames and each panel's **route**; the frame size from the piece format (ask only if missing; propose from the source, never default silently); the script or plan; optional references and design system.
2. Read `references/craft.md`, `references/frames.md` and `references/treatments.md`. When any panel's route is `hyperframes`, also read `references/figma-structure.md` and `references/frame-md.md`.
3. Read every panel: its key frames, notes and route. Compare with the script and list any conflict; ask, never resolve silently.
4. **Stop and show the frame plan** (format in `frames.md`) together with the **design direction**: palette, type, treatments, from the design system or, if none, a proposal. Build nothing until the designer approves both; the designer may edit either.
5. Build the approved plan (load `figma-use` first) in a Section named `Frames · <piece>`: one frame per state, panels in storyboard order, a director note under each frame.
6. Run the **pre-render self-audit** in `craft.md`; fix every miss in one pass.
7. Export what each route needs (`frames.md`, Exports by route).
8. Output: the Figma link, per panel the frames, treatment and layers by role, the exports and where they went, what is editable and what is an image, what was taken from each reference and what was ignored, every missing asset, and the audit result. Update each panel's **edit home** in the storyboard.
