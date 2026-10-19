---
name: blissful-audit
description: Run a full UX audit on a screen or flow — usability heuristics, UX laws and WCAG accessibility — and merge the results into one report. Use when asked for a complete UX/design audit.
argument-hint: "[screenshot, Figma link, URL or file]"
---

# Full UX Audit

1. Resolve the target once; ask only if none is given.
2. Invoke `blissful-audit-heuristics`, `blissful-audit-laws` and `blissful-audit-wcag` with that same target.
3. Merge into one report:
   - **Overlap**: issues flagged by 2+ audits, raised one severity level when accessibility-related.
   - **All findings** by severity, tagged with source audit.
   - **Top 5 actions**.
