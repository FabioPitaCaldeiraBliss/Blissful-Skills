# Changelog

## 0.5.0
- New `motion-audit`: checks a motion plan or a rendered video across purpose, timing and density, easing, choreography, flashing, reduced motion, build and video quality, and measures density, holds, cuts and flashing on a render.
- A closed **motion vocabulary** of about 40 named moves, shared by storyboard, animation and audit, with a density target in every motion spec (by default 65–80% of the time in motion, a new move at least every 3 s).
- `motion-storyboard` analyses the designer's references (recordings, stills, links) into a **motion language**, starts from a public reference library of 11 product films, and gives each panel a role and a shot template.
- `motion-frames` has treatment presets mapped to HyperFrames' shot templates, and designs handoff states between scenes.
- `motion-animate` reads the frames back from Figma (`dump-frames.js`) and generates the HyperFrames scenes from `scenes.json` (`build-scenes.py`) instead of hand-written HTML; scenes the designer edited are never overwritten.
- Each scene is a complete video: render the whole piece or chosen scenes (render scope), with review, editor (ProRes) and alpha exports, handles for editors, an SFX cue list and captions when there is voice-over.

## 0.4.0
- New Motion skills, run in order: `motion-storyboard` (motion spec, beat map, timed key frames, a route per panel), `motion-frames` (layered, animation-ready frames with a design direction and a self-audit), `motion-animate` (routes each panel to HyperFrames, Figma motion or an After Effects handoff) and `motion-assemble` (one HyperFrames project: transitions, stand-ins for missing clips, clip validation, render).
- Added `GLOSSARY.md` with the shared vocabulary of the Motion skills.
- HyperFrames' skills are a dependency of the animation and assembly steps (install command in the README).

## 0.3.0
- Breaking: skills renamed to `audit`, `audit-heuristics`, `audit-laws`, `audit-wcag` (dropped the `blissful-` prefix; plugin name unchanged).

## 0.2.0
- Breaking: skills renamed to `blissful-audit`, `blissful-audit-heuristics`, `blissful-audit-laws`, `blissful-audit-wcag` (old `ux-*` commands removed).
- Removed references to private notes from the skills.

## 0.1.0
- Initial release: `ux-audit`, `ux-heuristic-audit`, `ux-laws-audit`, `wcag-accessibility-audit`.
