---
name: motion-audit
description: Audit a motion or video piece against motion-design and accessibility practice, on its plan (storyboard, animation plan, scenes.json) before building, or on a rendered video or scene after. Use when asked to review an animation, check a render's pacing or density, or before handing a motion piece off.
argument-hint: "[storyboard, STORYBOARD.md, scenes.json, or rendered video]"
---

# Motion Audit

1. Resolve the target and say which mode applies: **plan** (a storyboard, `STORYBOARD.md`, an animation plan or `scenes.json`), **render** (an MP4, MOV or WebM file, a scene video or the whole piece), or both when both exist. Also read the motion spec (density target, easing, BPM) and the motion vocabulary from `motion-storyboard`. Ask only if no target is given.
2. Read `references/checklist.md`.
3. For a render, measure it: `python3 -I scripts/measure-motion.py <video> --flash --sheets <scratch folder>`, then read the contact sheets and sample frames at each cut with `ffmpeg`. Never download someone else's video to audit it.
4. Evaluate all 8 categories, using only the checks for the mode in hand. Mark each check **Pass**, **Finding**, **N/A** or **Unverified**; never skip one. A check that needs a human eye or ear (judder, sync, feel) is Unverified with what to look at, never Pass.
5. For each finding give: category, evidence (panel and timecode, or the move and its numbers), severity (Low, Medium, High, from the reference), and a one-line fix named in the vocabulary where possible ("fill the 4 s hold at 0:12 with `glow-drift` and a `phrase-swap`").
6. Output: the measured numbers against the target (density, longest hold, cuts, flashing), the findings table sorted by severity, then the Pass, N/A and Unverified list, then the top 3 fixes. In plan mode, say which findings block approval of the plan.
