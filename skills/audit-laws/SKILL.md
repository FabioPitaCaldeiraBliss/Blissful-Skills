---
name: audit-laws
description: Audit a screen, component or flow against the Laws of UX (Hick, Fitts, Miller, Jakob, Gestalt laws, Von Restorff, Peak-End, etc.). Use when asked to check a design for UX laws or cognitive-load issues.
argument-hint: "[screenshot, Figma link, URL or file]"
---

# UX Laws Audit

1. Resolve the target: attached image, Figma link (use the Figma MCP screenshot/context tools), URL or code. Ask only if none is given.
2. Read `references/laws.md`.
3. Evaluate all 14 laws independently. Mark each **Pass**, **Finding** or **N/A** — never skip one.
4. For each finding give: law, evidence (where in the target), severity (Low/Medium/High, using the severity examples in the reference), one-line fix.
5. Output: findings table sorted by severity, then Pass/N/A list, then top 3 priorities.
