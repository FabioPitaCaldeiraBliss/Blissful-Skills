---
type: llm
weight: 1
---

The response is a plan-mode motion audit. It must:

1. Flag the full-frame white strobe (6 flashes in 1 s) as a High severity flashing finding against WCAG 2.3.1, and not mark flashing as Pass.
2. Flag the gap in Frame 2 between the exit at about 7.6 s and the tap at 13.5 s (well over 3 s with nothing moving) as a timing or density finding, with a fix that adds moves rather than stretching the hold.
3. Flag the exit that is longer than the enter and uses an ease-out (exits should be shorter and ease in).
4. Flag "Trusted by 2 million users" as a claim that is not in the script.
5. Flag at least one phrase that is on screen for less than about 2 s (for example "Money that moves with you", 1.2 s).
6. Mark checks that need a render (measured density, banding, contrast on moving footage) as Unverified or N/A rather than Pass.

Score lower for each missing item, and for findings with no evidence (panel and time).
