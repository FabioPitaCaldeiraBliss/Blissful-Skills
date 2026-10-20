# Skills for UX Designers at Bliss

The skills we use at Bliss to review and improve designs with Claude. Small, easy to adapt, and based on established UX practice. Audits and a motion pipeline so far, and more UX skills will follow.

> **Beta:** shared with a small test group. Names and behaviour may change.

## Install

You don't need to know the terminal. You only need [Claude Code](https://claude.com/claude-code).

1. Install and open Claude Code.
2. In the Claude Code prompt, paste this line and press Enter:

   ```
   /plugin marketplace add FabioPitaCaldeiraBliss/Blissful-Skills
   ```

3. Then paste this one, and restart Claude Code when it finishes:

   ```
   /plugin install blissful-skills@blissful
   ```

4. Try it: `/audit` followed by a screenshot, a Figma link, a URL, a saved HTML file or code.

Updates arrive with the plugin version. If you have a skill that stopped working after a rename, update the plugin and restart.

## Reference

### Audits

Pass a screenshot, Figma link, URL, saved HTML file or code after the command, for example `/audit <link to your screen>`. If you installed the plugin, the long form also works: `/blissful-skills:audit`.

- **[audit](./skills/audit/SKILL.md)**: The full review. Runs the three audits below and merges them into one report: overlapping issues combined, findings sorted by severity, and the top 5 actions to take first. Use it when you want a complete design review.
- **[audit-heuristics](./skills/audit-heuristics/SKILL.md)**: Checks a screen or flow against [Nielsen's 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/). Use it for a classic usability review.
- **[audit-laws](./skills/audit-laws/SKILL.md)**: Checks against 14 [Laws of UX](https://lawsofux.com/) (Hick, Fitts, Miller, Jakob, Gestalt and more). Use it when a screen feels heavy or confusing and you want to know why.
- **[audit-wcag](./skills/audit-wcag/SKILL.md)**: Checks accessibility against the [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) principles: perceivable, operable, understandable, robust. Use it before handoff or release.

### Motion

A pipeline from a script to a rendered video. Each step is a skill; run them in order, and each one shows a plan for your approval before it builds anything.

1. **[motion-storyboard](./skills/motion-storyboard/SKILL.md)**: Turns a script, plan or screens into a Figma storyboard. Give it reference videos, screen recordings or stills and it writes their **motion language** (pacing, density, signature moves); without references it starts from a public reference library. You get a motion spec, a beat map when there is music, and 3–5 timed key frames per panel, each naming its moves from a shared **motion vocabulary**. Each panel gets a **route**: `hyperframes`, `figma motion` or `after effects` (a human animator).
2. **[motion-frames](./skills/motion-frames/SKILL.md)**: Designs the final, layered frames from the storyboard (design direction first, then frames in a Figma Section, starting from shot templates proven in product launch films) and exports what each route needs.
3. **[motion-animate](./skills/motion-animate/SKILL.md)**: Animates each panel by its route: generates HyperFrames scenes from your Figma frames, builds Figma motion timelines, or writes the handoff pack for After Effects. Scenes you edit by hand are never overwritten.
4. **[motion-assemble](./skills/motion-assemble/SKILL.md)**: Renders the whole piece or just the scenes you pick (each scene is a full video), with stand-ins for clips still missing, validated deliveries, and exports for review, for an editor (ProRes, with handles) or with transparency.
5. **[motion-audit](./skills/motion-audit/SKILL.md)**: Checks a plan before building, or a render after: purpose, timing and density, easing, choreography, flashing, reduced motion, build and video quality.

You need the Figma connector with edit access to your file. For steps 3 and 4, also install the HyperFrames skills once:

```
npx skills add heygen-com/hyperframes -g -a claude-code -s '*' -y
```

For a reference video, share a file or a screen recording you're allowed to use; Claude samples it. It won't download someone else's video from a link, so for those describe the motion or share stills. Logos, photos and people always come from you; missing ones stay as labelled boxes.

### What the audits can't check

Claude reads screenshots and code, but it can't use your prototype. Keyboard, screen-reader, zoom and animation checks are marked **unverified** in the report, so test those yourself.

## For developers

Structure and contributing notes are in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
