# Contributing

## Structure

```
.claude-plugin/   plugin.json, marketplace.json
skills/<skill>/   SKILL.md (procedure) + references/ (checklist, loaded on demand)
```

Each `SKILL.md` holds only the steps; the checklist lives once in `references/`. `/audit` may call the other three but they never call it.

## Adding or changing a skill

Add a folder under `skills/`, list it in `.claude-plugin/plugin.json`, bump `version`, and add a line to `CHANGELOG.md`. Peers on the plugin route only receive updates when `version` changes.

## Other agents and manual install

Use one route per agent; using both duplicates the skills.

```
npx skills@latest add FabioPitaCaldeiraBliss/Blissful-Skills -a <agent>
```

Or copy folders from `skills/` into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/`.
