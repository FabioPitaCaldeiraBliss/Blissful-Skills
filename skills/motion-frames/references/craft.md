# Craft

Frames are video frames, not web pages. The design spec is brand, not layout: the brand is strict, the application is yours.

**Strict from the brand:** exact hex values (including the background), font families, weight relationships, Do's and Don'ts. Quote them verbatim. A light canvas stays light; do not switch to dark.
**Adapted for video:** type size, spacing, decorative opacity, border weight, component treatment.

## Scale (1080p)

Web sizes disappear on video. Scale everything up.

| Element | Video |
|---|---|
| Headline | 64–120 px |
| Body | 28–42 px |
| Label | 18–24 px |
| Border | 2–4 px |
| Margin and padding | 60–140 px |
| Decorative opacity | 12–25% (under 10% is invisible) |

Floors: headline 60 px, body 20 px, label 16 px for full-screen viewing; in-feed 90, 32 and 24 px. Text on screen for 3 s must be readable in 2 s. Justify any text under 24 px.

## Layer roles

Plan every frame's layers by role; each role is its own layer so it can be animated alone.

- **Background:** 2–5 persistent decoratives (radial glow, oversized ghost type, hairline rules, grain, grid). They get ambient motion later, so keep each separate.
- **Midground:** the message (headline, stats, cards, devices, images).
- **Foreground accents:** dividers, labels, data bars, registration marks, metadata.

A produced frame carries roughly 6–10 roles; a lower third or a logo sting needs fewer. Decoration never adds claims, copy or new content. A decorative must never sit under content it competes with (oversized ghost type behind a chart), and no two layers may overlap by accident: check that charts, boxes and text keep their own zones.

## Composition

- Two focal points at least, so the eye travels.
- Hero text fills 60–80% of the frame width.
- Anchor content to edges; split or zone layouts beat centred stacks.
- Add structural elements (rules, dividers, panels); they create paths and animate well.
- A statement frame keeps 50–60% negative space.
- Safe areas: action-safe 90% (5% inset, about 96×54 px), title-safe 80% (10% inset, about 192×108 px) for text and key content. Each half of a 50/50 layout has its own title-safe box.

## Colour and type

- One accent hue, visible: 15–25% opacity for atmosphere, full saturation on the focal element.
- Tint neutrals toward the brand hue; reach for pure `#000` or `#fff` only when the brand specifies them.
- A full-screen linear gradient on a dark ground bands under video compression; use a radial gradient, a solid, or a solid with a local glow.
- A light canvas gets bolder structure and texture (2 px+ rules, grain), not a dark switch.
- Display type: weight 700–900 against body 300–400, tracking −0.03 to −0.05 em, tabular numerals for stacked numbers, one expressive family per frame. The brand's own typeface wins over any generic font list.
- Text boxes use auto height, never shorter than their line height (shorter boxes drift about 6 px on import).

## Treatments

Define the piece's reusable frame types once (for example Hero Stack, Hero Stat, Grid, Pull Quote, Cards, Closing) and give each panel one. A treatment fixes layer roles, focal element and negative space; it does not fix layout details.

## Defaults to question

A default is fine when the content calls for it and a tell when it is automatic: gradient text, left-edge accent stripes, neon on dark, identical card grids, everything centred with equal weight, web-sized type, 1 px borders, two similar sans families.

## Pre-render self-audit

Check, and fix every miss in one pass:

1. Every hex exists in the palette; fonts and weights match the brand.
2. Sizes sit in the scale table; contrast meets WCAG AA.
3. Text and key content sit inside title-safe; everything visible inside action-safe.
4. Each frame has its layer roles, separate decoratives, and at least two focal points.
5. Layer names follow the rule in `frames.md`; persisting elements keep one name across state frames.
6. No default from the list above is present unless the design direction chose it.
7. No copy, number or claim beyond the storyboard and script.
