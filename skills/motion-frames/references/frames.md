# Frames

A **frame** is the finished static visual of a panel, built like a layered Illustrator file for After Effects: every part that will move is its own named layer. The same frames serve any route (HyperFrames, Figma motion, After Effects).

## Frame plan

Show it before building, with the design direction (palette, type, treatments):

| Panel | Route | Treatment | Frames (states) | Layers by role | Exports | Needs from you |
|---|---|---|---|---|---|---|
| `01 Hook` | hyperframes | Hero Stat | 1 | bg: ring, glow · mid: counter, label, headline | frame.md | — |

Under the table list: conflicts between storyboard and script (as questions), the size to confirm, and anything missing. Wait for approval.

## How many frames

- The storyboard's key frames are the source. One frame per distinct composition, not per moment.
- Things that only move, scale or fade share one frame; layers sit at their start positions.
- Add a state frame only where layout or content changes: light vs dark, a new screen replacing the old, one logo becoming another.
- A counter or bar needs no start frame: the frame holds the end value, and the storyboard gives the start.
- The designer can override any count in the plan.

## Layers

- Every element that moves on its own is its own layer: phone, screen, headline, counter, background, each decorative.
- Name them `NN Panel / element` (for example `04 Onboarding / phone`). Everything before the `/` is exactly the panel name; put qualifiers after it. `motion-animate` finds layers by this name, so do not rename after approval.
- An element that persists across a panel's state frames keeps the **same name, order and position logic** in every state frame; only what changes differs. Hide a layer with opacity 0, never by deleting it. Change a text layer's content by adding a second text layer, never by editing one between frames.
- Live text and vector shapes. Never flatten text, or something that moves independently, into one image.
- Group only elements that always move together, and name the group the same way.
- One fill, stroke or shadow per object where possible; stacked styles flatten badly.
- Frame size is the size the designer gave.

## Screens and devices

- Screens in the same file: use editable copies or instances.
- Screens in another file cannot be copied: export as PNG, upload onto an image layer, and say in the summary that it is not editable. Export with `download_assets` at 3× (1.5× for tall desktop pages), at most four nodes per batch; `get_screenshot` caps at native size and looks soft at 1920×1080. Pick screens by reading their text, never by frame name.
- A desktop page taller than the window goes in a clipping frame (the window) with the full-height image inside, top-aligned.
- Build a simple 2D phone frame (rounded rectangle) as its own layer, with the screen as a separate layer inside or above it. On a dark ground the device keeps a visible edge. 3D mockups come from the designer.
- When every frame shows one product UI in successive states, mark which layers change state (they will be rebuilt) and which are static chrome (kept as an image).

## Design system and references

- Design system given (library, file variables or brand guide): search it, use its components, bind colour, type and spacing to its tokens instead of hardcoding, and say when variables are not published so values were copied.
- None given: propose a palette and type from the source and the craft rules, get it approved with the plan, and record it in `frame.md`.
- References (images, Figma frames, links): note per reference what was taken (colour, type, composition, pacing) and what was ignored. A reference video cannot be watched; use only the designer's written description.

## Exports by route

Write exports to a folder next to the project (ask where; propose `<piece>/exports/`), one subfolder per panel: `NN-panel/`.

| Route | Export |
|---|---|
| `hyperframes` | Every image layer (screens, photos) at 3×, plus one `frame.md` for the piece (format in `frame-md.md`). HyperFrames rebuilds text and shapes natively, so do not export those as images. |
| `figma motion` | Nothing extra: the layers stay in Figma and `motion-animate` animates them in place. |
| `after effects` | Every layer as PNG at 3× (SVG for vectors), named exactly like its Figma layer, plus `notes.md` with the panel's duration, motion, transition and the piece format. This is the layered file the animator works from. |

## Never create

- Photos, logos or people the designer did not supply: leave a labelled `MISSING:` box and flag it.
- AI-generated images.
- Numbers or copy that are not in the storyboard or script.

## Check before finishing

Run the pre-render self-audit in `craft.md`. Also confirm that every layer follows the naming rule, and that every item missing from the designer is listed.
