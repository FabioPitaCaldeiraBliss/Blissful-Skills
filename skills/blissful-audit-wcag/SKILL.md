---
name: blissful-audit-wcag
description: Audit a screen, component or flow for accessibility against the WCAG POUR principles (Perceivable, Operable, Understandable, Robust). Use when asked for an a11y or WCAG review.
argument-hint: "[screenshot, Figma link, URL or file]"
---

# WCAG Accessibility Audit

1. Resolve the target: attached image, Figma link (use the Figma MCP screenshot/context tools), URL or code. Ask only if none is given.
2. Read `references/wcag-pour.md`.
3. Evaluate all 4 principles independently. Mark each **Pass**, **Finding** or **N/A** — never skip one.
4. For each finding give: principle, evidence (where in the target), severity (Low/Medium/High, using the severity examples in the reference), one-line fix.
5. If the target is a static image or design, list the checks that cannot be verified (keyboard, screen reader, 200% zoom, reduced motion — see "Notes for UX Audits" in the reference) instead of marking them Pass.
6. Output: findings table sorted by severity, then Pass/N/A/unverified list, then top 3 priorities.
