# Contributing

## Structure

```
.claude-plugin/   plugin.json, marketplace.json
skills/<skill>/   SKILL.md (procedure) + references/ (checklist, loaded on demand)
```

Each `SKILL.md` holds only the steps; the checklist lives once in `references/`. `/audit` may call the other three but they never call it.

The Motion skills share a few files instead of copying them: `motion-storyboard/references/motion-vocabulary.md` (the moves), `motion-storyboard/references/library/` (public references), `motion-audit/scripts/measure-motion.py` and `motion-animate/scripts/build-scenes.py`. Change them in one place. Scripts use the Python standard library and `ffmpeg` only.

## Reference library

`skills/motion-storyboard/references/library/` holds public motion references, one Markdown file each in the entry format in `references.md`, listed in `index.md`. Add only public links with notes; never client work, Bliss work or downloaded video. A reference a designer gives while using the skills stays with their project.

## Evals

`evals/` holds `claude plugin eval` cases. The Motion cases use a fictional piece (`evals/fixtures/lumo/`); never put client material there.

## Adding or changing a skill

Add a folder under `skills/`, list it in `.claude-plugin/plugin.json`, bump `version`, and add a line to `CHANGELOG.md`. Peers on the plugin route only receive updates when `version` changes.

## Other agents and manual install

Use one route per agent; using both duplicates the skills.

```
npx skills@latest add FabioPitaCaldeiraBliss/Blissful-Skills -a <agent>
```

Or copy folders from `skills/` into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/`.
