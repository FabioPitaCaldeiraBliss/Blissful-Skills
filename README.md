# Skills for UX Designers at Bliss

The skills we use at Bliss to review and improve designs with Claude. Small, easy to adapt, and based on established UX practice. The audits come first, and more UX skills will follow.

> **Beta:** shared with a small test group. Names and behaviour may change.

## Install

You don't need to know the terminal. You only need [Claude Code](https://claude.com/claude-code) and access to this repo.

1. Install and open Claude Code.
2. Ask the person who shared this with you to give your GitHub account access to this repo. It's private, so you'll need a free GitHub account.
3. In the Claude Code prompt, paste this line and press Enter:

   ```
   /plugin marketplace add FabioPitaCaldeiraBliss/Blissful-Skills
   ```

4. Then paste this one, and restart Claude Code when it finishes:

   ```
   /plugin install blissful-skills@blissful
   ```

5. Try it: `/audit` followed by a screenshot, a Figma link, a URL, a saved HTML file or code.

Updates arrive with the plugin version. If you have a skill that stopped working after a rename, update the plugin and restart.

## Reference

### Audits

Pass a screenshot, Figma link, URL, saved HTML file or code after the command, for example `/audit <link to your screen>`. If you installed the plugin, the long form also works: `/blissful-skills:audit`.

- **[audit](./skills/audit/SKILL.md)**: The full review. Runs the three audits below and merges them into one report: overlapping issues combined, findings sorted by severity, and the top 5 actions to take first. Use it when you want a complete design review.
- **[audit-heuristics](./skills/audit-heuristics/SKILL.md)**: Checks a screen or flow against [Nielsen's 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/). Use it for a classic usability review.
- **[audit-laws](./skills/audit-laws/SKILL.md)**: Checks against 14 [Laws of UX](https://lawsofux.com/) (Hick, Fitts, Miller, Jakob, Gestalt and more). Use it when a screen feels heavy or confusing and you want to know why.
- **[audit-wcag](./skills/audit-wcag/SKILL.md)**: Checks accessibility against the [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) principles: perceivable, operable, understandable, robust. Use it before handoff or release.

### What it can't check

Claude reads screenshots and code, but it can't use your prototype. Keyboard, screen-reader, zoom and animation checks are marked **unverified** in the report, so test those yourself.

## For developers

Structure and contributing notes are in [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
