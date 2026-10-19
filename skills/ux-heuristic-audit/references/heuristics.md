# UX Heuristic Audit Checklist

Use this checklist to identify usability issues in screens, components, or user flows.
Review each heuristic independently and document findings elsewhere or via backlinks.

---

## Heuristic Audit Table

| #   | Heuristic                     | Audit Checklist                                             | Examples of Failures                          | Severity Examples                                                                    |
| --- | ----------------------------- | ----------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------ |
| 1   | Visibility of system status   | • Is feedback immediate?<br>• Is system state always clear? | • No loading indicator<br>• Silent submission | Low: brief delay<br>Medium: unclear progress<br>High: user thinks system is broken   |
| 2   | Match with real world         | • Is language user-friendly?<br>• Are metaphors familiar?   | • Internal jargon<br>• Abstract icons         | Low: unclear wording<br>Medium: confusing labels<br>High: misunderstood actions      |
| 3   | User control and freedom      | • Can users undo or exit?<br>• Are actions reversible?      | • No undo<br>• Forced flows                   | Low: extra steps<br>Medium: hard to cancel<br>High: irreversible action              |
| 4   | Consistency and standards     | • Are patterns consistent?<br>• Are conventions followed?   | • Inconsistent behavior<br>• Custom patterns  | Low: visual mismatch<br>Medium: interaction changes<br>High: relearning core actions |
| 5   | Error prevention              | • Are errors prevented early?<br>• Are constraints clear?   | • Late validation<br>• No guidance            | Low: late feedback<br>Medium: frequent errors<br>High: costly mistakes               |
| 6   | Recognition over recall       | • Are options visible?<br>• Is memory load minimized?       | • Hidden actions<br>• Recall required         | Low: small memory load<br>Medium: repeated recall<br>High: task failure              |
| 7   | Flexibility and efficiency    | • Are shortcuts available?<br>• Can experts move faster?    | • No bulk actions<br>• Linear flows only      | Low: slow expert flow<br>Medium: repetitive work<br>High: productivity blocker       |
| 8   | Aesthetic & minimalist design | • Is every element needed?<br>• Is hierarchy clear?         | • Visual clutter<br>• Competing CTAs          | Low: visual noise<br>Medium: unclear focus<br>High: missed key actions               |
| 9   | Error recovery                | • Are errors understandable?<br>• Is recovery explained?    | • Generic messages<br>• Technical errors      | Low: vague copy<br>Medium: unclear fix<br>High: user blocked                         |
| 10  | Help & documentation          | • Is help discoverable?<br>• Is guidance contextual?        | • Hidden help<br>• External docs only         | Low: hard to find<br>Medium: context switch<br>High: abandonment                     |

---

## Heuristic Explanations

### 1. Visibility of System Status
The interface should continuously inform users about what is happening.
Check for feedback after actions such as clicks, submissions, or background processes.
Missing or delayed feedback is a common violation.

---

### 2. Match Between System and the Real World
The UI should use concepts and language familiar to users.
Audit for internal terminology, technical phrasing, or unclear metaphors.
Users should not need to interpret or translate meaning.

---

### 3. User Control and Freedom
Users should be able to recover from mistakes.
Audit for undo, cancel, back, and exit options.
Irreversible actions are high-severity issues.

---

### 4. Consistency and Standards
Similar actions should behave consistently across the product.
Audit visual patterns, interactions, and terminology.
Breaking conventions increases cognitive load.

---

### 5. Error Prevention
Preventing errors is more effective than handling them later.
Audit for proactive validation, constraints, and smart defaults.
Frequent errors indicate a failure in prevention.

---

### 6. Recognition Rather Than Recall
Users should not rely on memory to use the interface.
Audit whether information and options are visible when needed.
Hidden steps increase cognitive effort.

---

### 7. Flexibility and Efficiency of Use
The system should support both novice and expert users.
Audit for shortcuts, accelerators, and workflow optimizations.
Expert users should not be slowed by basic paths.

---

### 8. Aesthetic and Minimalist Design
Minimalism focuses on clarity, not emptiness.
Audit for unnecessary elements and weak visual hierarchy.
Clutter distracts from core tasks.

---

### 9. Help Users Recognize, Diagnose, and Recover from Errors
Error messages should be clear and actionable.
Audit tone, clarity, and recovery guidance.
Errors should help users move forward, not block them.

---

### 10. Help and Documentation
Help should be available at the moment of need.
Audit discoverability and contextual relevance.
Users should not need to leave the product to understand it.

---

## Severity Reference

- **Low** — Minor friction or cosmetic issue  
- **Medium** — Causes confusion or repeated mistakes  
- **High** — Blocks task completion or causes abandonment