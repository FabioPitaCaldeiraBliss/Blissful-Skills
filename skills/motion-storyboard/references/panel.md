# Panels and key frames

A **panel** is one idea of the piece (designers also say "scene"). It carries a label, 3–5 **key frames**, and a few notes. Write `?` for any note the source doesn't answer.

## Key frames

A key frame is a still of one moment inside the panel. Three to five per panel; two for a panel of 4 s or less. The first sits at the panel's start; the last holds until its end, so state what the hold does (see `motion-spec.md`).

| Part | What goes in it |
|---|---|
| **Id and timecode** | `F1 · 0:26.0`: sequenced times, never two events at one timestamp (write "fades out fully by 0:30.2; at 0:30.2 the next line lands"). |
| **Picture** | The real screen, an image, or a **sketch** (below). |
| **Sentence** | What happens at that moment, in one sentence. |
| **Tags** | Chips for what the moment needs (below). |

Key frames become the states `motion-frames` plans from, so a change of layout or content between key frames is a state.

## Tags

| Tag | Content |
|---|---|
| `EASE` | curve and duration, e.g. `expo out · 400 ms` |
| `CAM` | camera move or framing, e.g. `push-in 115%`, `whip pan` |
| `TRANS` | the transition into or out of the moment, e.g. `✓ → padlock` |
| `SFX` | sound at that moment, e.g. `click + ding` |
| `TXT` | exact on-screen copy, in quotes |

Annotation glyphs on the picture: a tap marker, a dashed trajectory arrow, an outline for the next camera framing.

## Panel notes

| Note | What goes in it |
|---|---|
| **Duration** | Start and end, e.g. `0:26–0:40`. |
| **Route** | How the panel gets animated, with a one-line reason (below). |
| **Edit home** | Where the editable source will live (below). |
| **Status** | `outline`, `built` (layout confirmed, no motion) or `animated`. Add `locked` once approved; locked panels are never redrawn. |

UI motion adds a **Trigger** (load, tap, scroll, time). Video adds **Camera**, **Audio** and **On-screen text**; for a count-up, write the final value, not a range.

## Writing the notes

- Copy comes from the source word for word, in quotes. Unquoted copy gets paraphrased downstream.
- Notes are written in the designer's working language; on-screen text stays in the language of the video.
- Keep key content inside the title-safe area (80% of the frame, 10% inset per edge) and everything visible inside the action-safe area (90%).
- Give measurable targets (sizes, opacities, hex values) instead of "a bit bigger".
- A real product screen needs the real footage; hold its slot with a labelled placeholder and never approximate the product's UI.
- A gap stays blank and flagged; raise it with the designer, never fill it silently.
- One idea per panel: split a scene that holds two.
- Order and total length come from the source; flag anything over a stated limit. Key frame times must cover the whole panel, because leftover time becomes a dead hold.

## Route

How one panel gets animated. Propose one per panel with a reason; the designer confirms. Default: `hyperframes`.

| Route | Propose it when | Limits |
|---|---|---|
| `hyperframes` | Kinetic type, true count-ups, data graphics, layered UI or device scenes, camera moves, anything built from the panel's frame layers. | Weak at character rigs, heavy compositing, custom effects. |
| `figma motion` | A simple UI entrance or cross-fade the designer wants to keep editable in Figma's own timeline. | Cannot count a number up; each frame exports on its own. |
| `after effects` | Character or logo animation, 3D, compositing, or anything an asset has to drive or effects the other routes lack. A human does it. | Needs a handoff and a delivered clip (or a Lottie file). |

If a panel mixes needs, route it to the most capable fit and say why; do not split a panel across routes. For `hyperframes` panels, label each key frame element as **rebuild** (it moves or changes state) or **keep** (a logo, icon, illustration or screenshot used as proof), and name the elements that persist across key frames.

## Edit home

One line per panel naming where its editable source lives: the Figma timeline frame (`figma motion`), the HyperFrames composition file (`hyperframes`), or the After Effects project the human names. Write `?` until it exists and keep it current.

## Sketches

A key frame with no supplied screen gets a **sketch**: a simple still drawn from the sentence and the on-screen copy, so no key frame is an empty box.

- Use native Figma shapes and text only; do not generate images.
- Show what the sentence says: big numbers as stat tiles, a counter as large type, a before/after as two boxes, a light/dark switch as a split frame, a team as a grid of avatar circles.
- Take numbers and copy only from the source. Logos and photos become labelled boxes.
- Use brand cues (colours, gradient, white space) only if the source states them; otherwise neutral grey, white and black.
- Add a small `SKETCH` tag in the corner. Keep text on one line inside its box and check the render for wrapped or overlapping text.
