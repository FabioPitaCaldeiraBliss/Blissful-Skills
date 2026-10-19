---
name: blissful-audit-heuristics
description: Audit a screen, component or flow against Nielsen's 10 usability heuristics. Use when asked to run a heuristic evaluation or usability review of a design, Figma file, URL or code.
argument-hint: "[screenshot, Figma link, URL or file]"
---

# UX Heuristic Audit

1. Resolve the target: attached image, Figma link (use the Figma MCP screenshot/context tools), URL or code. Ask only if none is given.
2. Read `references/heuristics.md`.
3. Evaluate all 10 heuristics independently. Mark each **Pass**, **Finding** or **N/A** — never skip one.
4. For each finding give: heuristic, evidence (where in the target), severity (Low/Medium/High, using the severity examples in the reference), one-line fix.
5. Output: findings table sorted by severity, then Pass/N/A list, then top 3 priorities.
