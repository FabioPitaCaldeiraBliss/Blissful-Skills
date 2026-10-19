# Figma structure HyperFrames can import

HyperFrames' own Figma import reads a storyboard as a strip of frames: adjacent frames that share an element describe that element's states through time, so it animates the element between states instead of playing stills. Structure the file so that reading works.

## Layout

- Put the frames in a **Section** named `Frames · <piece>`. Scenes are the frame-sized nodes inside the Section (about the composition's size, larger than 1400×900 at 1080p).
- Order is **left to right by x-position** (row-major if the strip wraps). Lay a panel's state frames in one row, in order; panels follow in storyboard order.
- Leave no loose stills in the Section: every frame-sized node is read as a scene.

## Names

- An element that persists across state frames has the same name in each (rule in `frames.md`). HyperFrames matches children across adjacent frames by name first, then by geometry; unmatched children enter or exit at the scene's beat.
- Name brand marks by the brand they show (`Brand / <name> logo`), so they can be found again.

## Director notes

Under each frame, a text layer states the motion intent for that frame in verbs; HyperFrames pairs a text node with the scene whose x-range it overlaps and reads it as direction, never as on-screen copy. Use the verbs it maps to transitions:

| Note says | It becomes |
|---|---|
| EXPLODE, BURST | the incoming element scales from about 1.5 to 1 with a fade |
| SLIDE FROM THE <edge> | a slide in from that edge |
| MORPH, REVEAL | a cross-fade, or a rebuilt element when the motion is inside one frame |
| CYCLE THROUGH | a longer hold, or a rebuilt element |

A frame with no note gets a cross-fade with a slow drift. Take the notes from the storyboard's key-frame sentences and tags.

## Tokens and fills

- Bind fills and text to variables or styles. HyperFrames imports a bound fill as a variable with its literal as fallback, and flags an unbound fill as unresolved; it never matches by hex.
- Variables need an Enterprise plan to read; other plans fall back to published styles. Say which one applied.

## Keep or rebuild

| Keep as an image | Rebuild as live elements |
|---|---|
| Logos, icons, illustrations, screenshots used as proof | Anything that moves or changes state |

Complex vectors and boolean shapes are rasterised on import; keep them simple where they must stay vector.
