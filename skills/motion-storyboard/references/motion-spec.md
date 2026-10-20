# Motion spec

The decisions stated once at the top of the storyboard and inherited by every panel. A panel never restates them.

## Concept line

One sentence naming the motion language of the piece, then the counts: panels, key frames, length, format.
Example shape: `Continuous morphing, three chapters, one recurring element. 9 panels · 36 key frames · 1:28 · 16:9.`

## The seven cards

Each card is one or two sentences. Fill from the source; propose and mark as `proposed` where it is silent.

| Card | What it fixes |
|---|---|
| **Motion language** | Density, pacing, text behaviour, signature moves, easing feel and transitions, from the references (`references.md`), naming each reference used. |
| **Recurring element** | The motif planted early and returned later, changed (a shape that splits, fuses, becomes the logo). Name both the planting and the change. |
| **Persona** | Optional. A named fictional person whose story runs through the panels. |
| **Structure** | Chapters or acts: names, time ranges, the keyword of each, and the breathing room before each. Exactly one breather panel. |
| **Easing and timing** | Numbers: enter, exit, morph, stagger, minimum time a phrase stays on screen (defaults below), and the density target (defaults in `motion-vocabulary.md`). |
| **Camera and depth** | Push-in limit, parallax layers, blur values, motion blur on fast gestures. |
| **Music** | BPM, beat and bar length in seconds, the times of the hits, or `no audio`. |

## Defaults for easing and timing

Use when the source states none; list them back as `proposed`.

| Move | Default |
|---|---|
| Enter | expo out, 600 ms |
| Exit | expo in, 400 ms (shorter than the enter) |
| Morph | ease in-out, 800 ms |
| Stagger | 80 ms |
| A phrase on screen | at least 2 s |
| Breath before a chapter | 2 s |
| Motion density | 65–80% of the time in motion, a new move at least every 3 s, no still hold over 3 s but one |

Density is the default most often missed: a piece that holds each frame while its phrase is read feels slow on video. Fill holds with the next move or an ambient move, never with nothing.

## Beat map

With a BPM, beat = 60 / BPM seconds and bar = 4 beats. Write the hit times (a split, a reveal, a pause, the final chord) and place each panel boundary on a beat. Without a BPM, skip the beat map and say timing follows the panel durations only.

## Holds

Decide once per piece what a held frame does: stays fully still, or shows a gentle ambient idle (`glow-drift`, `breathe`). A literal "hold" renders as a frozen still, so choose deliberately and state it in the Camera and depth card. Only one hold in the piece may run past 3 s, and it is named as the hero hold.

## Specificity

Carry exact tokens where a default could miss: hex values, type families and weights, textures, and the technique where it matters (3D by a real 3D engine, not flat CSS). Mood words alone leave the design to chance.
