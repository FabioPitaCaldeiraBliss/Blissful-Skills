# frame.md

`frame.md` is the frame-scale design system HyperFrames reads for a video project. Write it into the project root, lowercase. HyperFrames reads the first that exists of `frame.md`, then `design.md`, then `DESIGN.md`; when a `design.md` already exists, either keep it and add `frame.md` above it or migrate it.

The frontmatter is the normative layer (machine-readable values, quoted verbatim); the prose is context for judgement.

## Frontmatter

```yaml
---
version: 1
name: <piece name>
description: <one sentence>
unit: "the frame, 1920x1080"
principle: <the one-line design principle>
colors:
  background: "#f7fbff"
  ink: "#1a1a1a"
  accent: "#e2231a"
typography:
  display: { family: "<family>", weight: 700, size: 96, tracking: "-0.03em" }
  body: { family: "<family>", weight: 400, size: 36 }
  label: { family: "<family>", weight: 500, size: 22 }
spacing:
  pad-frame: 96
  gap: 32
components:
  chip: { radius: 100, border: 2 }
---
```

Take every value from the design system or the approved design direction. Never round or invent a hex, family or weight. Motion tokens live in the storyboard's motion spec, not here.

## Prose sections

`Overview`, `The Frame` (format, safe areas), `Colors`, `Typography`, `Depth & Surface`, `Shapes`, `Components`, `Frame Treatments` (the named frame types and which panels use them), `Composition Rules` (Do and Don't), `Approved Entities` (logos and product names that may appear), `Numerals & Claims` (the numbers and copy that are allowed, quoted), `Pre-render Self-Audit` (the list in `craft.md`).

Seed from one of HyperFrames' ready-made presets only when the brand has no system of its own; a brand's own tokens always win.
