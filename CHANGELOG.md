# Changelog

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
