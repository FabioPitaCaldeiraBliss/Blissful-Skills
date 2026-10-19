# Blissful Skills

Design skills for Claude Code.

| Skill | What it does |
|---|---|
| [`/blissful-audit`](skills/blissful-audit/SKILL.md) | Full audit: runs the three audits below and merges them into one report (overlaps, findings by severity, top 5 actions). |
| [`/blissful-audit-heuristics`](skills/blissful-audit-heuristics/SKILL.md) | Evaluates a screen or flow against Nielsen's 10 usability heuristics. |
| [`/blissful-audit-laws`](skills/blissful-audit-laws/SKILL.md) | Evaluates against 14 Laws of UX (Hick, Fitts, Miller, Jakob, Gestalt, etc.). |
| [`/blissful-audit-wcag`](skills/blissful-audit-wcag/SKILL.md) | Evaluates against the WCAG POUR principles. |

Pass a screenshot, Figma link, URL, saved HTML file or code: `/blissful-audit <target>`.
When installed as a plugin the namespaced form also works: `/blissful-skills:blissful-audit <target>`.
Static inputs can't verify keyboard, screen-reader, zoom or motion checks; those are reported as unverified.

## Install

This repo is private: you need access and `gh auth login` (or a git credential) first.

**Claude Code (recommended, updates with the plugin version):**

```
/plugin marketplace add FabioPitaCaldeiraBliss/Blissful-Skills
/plugin install blissful-skills@blissful
```

**Other agents (manual updates):**

```
npx skills@latest add FabioPitaCaldeiraBliss/Blissful-Skills -a <agent>
```

Use one route per agent; using both duplicates the skills.

**Manual:** copy folders from `skills/` into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/`.

## Structure

```
.claude-plugin/   plugin.json, marketplace.json
skills/<skill>/   SKILL.md (procedure) + references/ (checklist, loaded on demand)
```

Each `SKILL.md` holds only the steps; the checklist lives once in `references/`. `/blissful-audit` may call the other three but they never call it.

## Contributing

Add a folder under `skills/`, list it in `.claude-plugin/plugin.json`, bump `version`, and add a line to `CHANGELOG.md`. Peers on the plugin route only receive updates when `version` changes.

## License

MIT
