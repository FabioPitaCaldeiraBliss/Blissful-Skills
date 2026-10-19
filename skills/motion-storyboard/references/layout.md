# Figma layout

One Figma page per storyboard, read top to bottom.

## Order

1. **Header**: a pill `Motion storyboard v<N> · key frames, not animated`, the piece title, the concept line, and `Format: 1920×1080 · 30 fps · limit 1:30`.
2. **Motion spec**: the six cards in one row (see `motion-spec.md`), each a title and one or two sentences.
3. **Legend**: the tag chips (`EASE`, `CAM`, `TRANS`, `SFX`, `TXT`) and the annotation glyphs (tap, trajectory, next framing), each with its meaning.
4. **Beat map**, only with a BPM: a strip of the piece's length with a tick per beat (taller on each bar), one band per panel, and markers for the hits.
5. **Panel rows**, one per panel, in order.

## Panel row

- A **label chip** row: panel number, name, time range, theme tag. Under it, one compact line with Route, Edit home and Status.
- A row of **key frame cards** with an arrow between neighbours.
- Each card: the 16:9 picture (960 px wide), the timecode `F1 · 0:26.0` in the accent colour, the sentence, and the tag chips. Annotation glyphs sit on the picture.

## Versions

A new version goes below a divider with its own header, so versions can be compared. Never overwrite or restructure an earlier version, and never redraw a panel marked `locked`.

## Build notes

- Frames are fixed-size auto-layout containers: set the sizing modes to fixed after turning on auto-layout, or they collapse to their text.
- A wrapping tag row needs a fixed width and a hugging height (`counterAxisSizingMode = "AUTO"`), or its chips are clipped under the card.
- Draw rings and dots as equal-width, equal-height ellipses; a stretched one reads as an oval.
- Name every card `F<n> · <timecode>` and every picture `Key frame picture`, so rows can be found and edited by name.
- Real screens from another file are exported with `download_assets` (3×) and placed with `upload_assets`; choose each by reading its text, never by frame name.
- Check the render of each row once: no clipped or overlapping text, every chip legible.
