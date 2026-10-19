# WCAG Principles — Audit Checklist (POUR)

Use this checklist to identify accessibility issues in UI screens, components, or flows.
Each principle should be evaluated independently during accessibility and UX audits.

WCAG principles ensure content is **Perceivable, Operable, Understandable, and Robust (POUR)**.

---

## WCAG Principles Audit Table

| # | Principle | Audit Checklist | Examples of Failures | Severity Examples |
|---|----------|-----------------|---------------------|------------------|
| 1 | Perceivable | • Is content available to all senses?<br>• Is text readable and contrast sufficient?<br>• Are alternatives provided? | • Missing alt text<br>• Low color contrast<br>• Text in images only | Low: minor contrast issues<br>Medium: hard-to-read content<br>High: content completely unavailable |
| 2 | Operable | • Can everything be used via keyboard?<br>• Are focus states visible?<br>• Are time limits reasonable? | • Keyboard traps<br>• No focus indicator<br>• Hover-only actions | Low: awkward navigation<br>Medium: difficult interaction<br>High: user cannot operate UI |
| 3 | Understandable | • Is language clear and consistent?<br>• Are errors explained?<br>• Is behavior predictable? | • Vague labels<br>• Confusing errors<br>• Unexpected UI changes | Low: mild confusion<br>Medium: frequent mistakes<br>High: task failure |
| 4 | Robust | • Does it work across browsers and AT?<br>• Is semantic markup used?<br>• Is ARIA used correctly? | • Broken screen reader flow<br>• Non-semantic divs<br>• Incorrect ARIA roles | Low: degraded experience<br>Medium: partial AT failure<br>High: unusable with assistive tech |

---

## WCAG Principles — Explanations (For Auditing)

### 1. Perceivable
Users must be able to perceive the information being presented.
Audit whether content is accessible through sight, sound, or touch equivalents.

Key checks:
- Text alternatives for non-text content
- Sufficient color contrast
- Resizable text without loss of content
- Captions and transcripts for media

If information cannot be perceived, it does not exist for that user.

---

### 2. Operable
Users must be able to operate the interface.
Audit all interactions using only a keyboard and assistive technologies.

Key checks:
- Full keyboard accessibility
- Visible focus indicators
- No keyboard traps
- Sufficient time to complete tasks
- No content that causes seizures or physical reactions

If users cannot interact, they cannot complete tasks.

---

### 3. Understandable
Users must be able to understand both the content and how to use the interface.
Audit clarity, predictability, and error handling.

Key checks:
- Clear, simple language
- Consistent navigation and patterns
- Helpful, human-readable error messages
- No unexpected context changes

If users cannot understand what’s happening, usability and accessibility break down together.

---

### 4. Robust
Content must be robust enough to work across different user agents and assistive technologies.
Audit technical foundations and semantic correctness.

Key checks:
- Proper HTML semantics
- Correct ARIA usage (when needed)
- Compatibility with screen readers
- Graceful degradation across browsers and devices

If assistive technology cannot interpret the UI, access fails entirely.

---

## Severity Reference

- **Low** — Degraded experience but usable with effort  
- **Medium** — Significant friction or partial task failure  
- **High** — Content or functionality is inaccessible  

---

## Notes for UX Audits

- WCAG issues often overlap with **usability heuristics**
- Accessibility failures frequently become **high-severity UX issues**
- Test with:
  - Keyboard only
  - Screen readers
  - Zoomed text (200%+)
  - Reduced motion settings

---

