# Motion vocabulary

The closed list of moves every motion skill plans, builds and audits with. Key frames, animation plans and audits name moves from this list. A move not on it is written `custom: <one line>` and listed back to the designer, so it is designed on purpose.

Times are defaults for a 1080p piece at 30 fps; the motion spec may override them once for the whole piece. Eases use the motion spec's names (expo out, expo in, ease in-out). "Reduced" is the fallback for the `UI` kind; the `video` kind has none.

## Basics

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `enter` | An element arrives: rise 40 px and fade in (or from the side given) | 600 ms, expo out | fade |
| `exit` | An element leaves: lift 30 px and fade out | 400 ms, expo in | fade |
| `fade` | Opacity only, in or out | 500 ms, ease in-out | same |

## Text

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `phrase-in` | A phrase enters word by word: rise 24 px and fade, 80 ms stagger | 600 ms, expo out | fade |
| `phrase-out` | A phrase leaves word by word: lift 16 px and fade, 40 ms stagger | 400 ms, expo in | fade |
| `phrase-swap` | The phrase on screen leaves and the next takes its place, same position | out 400 ms, in 600 ms, 100 ms overlap | cut |
| `keyword-accent` | One word of a phrase turns the accent colour as it lands, or after a 200 ms beat | 300 ms, ease in-out | instant colour |
| `word-swap` | One word changes while the rest of the line stays still ("Uma nova…" → "A sua…") | 500 ms, ease in-out | cut |
| `title-over-device` | An oversized title sits in front of or behind a device, the device moving under it | 800 ms, expo out | fade |
| `typewriter` | Characters appear in steps with a caret | 40 ms per character | full line fades |

## Shape and brand

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `stroke-draw` | An outline draws along its path (logo bars, arcs, rings) | 1200 ms, ease in-out | fade |
| `shape-morph` | One shape becomes the next in place, keeping its centre (ring → disc → tile → card) | 800 ms per link, ease in-out | cross-fade |
| `ring-pulse` | A ring expands from an element and fades | 900 ms, expo out | none |
| `logo-resolve` | The brand mark completes from the recurring element and holds | 1000 ms, expo out, then hold | fade |

## Device and camera

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `device-rise` | A device enters from below the frame to its rest position | 900 ms, expo out | fade |
| `device-tilt-in` | A device enters with a perspective tilt that settles to flat (rotationY 18° → 0) | 1000 ms, expo out | fade |
| `push-in` | The camera moves into a part of the UI until it fills the frame | 1200 ms, ease in-out | cut |
| `pull-out` | The reverse: from a close-up back to the whole device or layout | 1200 ms, ease in-out | cut |
| `satellite-cards` | Cards slide out from behind a device to the sides, hold, and tuck back in | 700 ms out, 500 ms back, 80 ms stagger | fade |
| `screen-scroll` | The screen content scrolls inside the device frame | 1000 ms, ease in-out | cut to end |
| `tap` | A touch indicator presses a control: scale 0.9 → 1 with a ripple | 400 ms | highlight only |
| `screen-swap` | The device keeps still while its screen changes | 500 ms cross-fade or push | cut |

## UI

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `cards-assemble` | A group of cards builds into a grid, one by one | 600 ms each, 120 ms stagger, expo out | fade |
| `card-resize` | A card changes size to show it adapts (with optional arrows) | 800 ms, ease in-out | cut |
| `card-carousel` | Cards fan or slide sideways, the focused one larger | 800 ms, ease in-out | cut |
| `notification-drop` | A notification drops from the top edge and settles | 500 ms, expo out | fade |
| `chat-stack` | Bubbles arrive one at a time, older ones pushed up | 400 ms each, 600–900 ms apart | fade each |
| `state-change` | A control or card goes from one state to the next (loading → result, off → on) | 500 ms, ease in-out | cut |
| `toggle` | A switch flips and the UI around it updates | 300 ms, ease in-out | cut |
| `count-up` | A number counts to its value, tabular numerals | 1200 ms, expo out | final value |
| `content-swap` | One item replaces another in place (initial → avatar) | 500 ms, ease in-out | cut |
| `success-burst` | A confirmation lands with a small burst (stars, ring, check) | 700 ms, expo out | check only |

## Media

| Move | What happens | Default | Reduced |
|---|---|---|---|
| `masked-video` | Footage plays inside a rounded window that can grow or shrink | 800 ms window change, ease in-out | still |
| `film-strip` | A strip of windows pans sideways, the centre one in focus | constant, 120 px/s | still |
| `photo-mosaic` | A grid of photos fills in tile by tile around a message | 60 ms stagger, 400 ms each | fade |
| `background-swap` | The background changes (inside → outside) while the UI in front keeps still | 600 ms cross-fade | cut |

## Transitions

Between panels and inside one. A `hyperframes` scene joins its neighbours through its **handoff state**; the other transitions need a transition frame.

| Move | What happens | Default |
|---|---|---|
| `morph-through` | The last element of one panel becomes the first of the next (default between UI panels) | 800 ms, ease in-out |
| `zoom-through` | The camera pushes through an element into the next panel | 900 ms, expo in then expo out |
| `cut` | A hard cut, on a beat when there is music (default for footage) | 0 |
| `wipe` | A brand shape crosses the frame and reveals the next panel | 700 ms, expo in-out |
| `dissolve` | Cross-dissolve, for a change of time or place | 600 ms |

## Ambient

Runs under holds so nothing freezes.

| Move | What happens | Default |
|---|---|---|
| `glow-drift` | A background glow drifts slowly | 6–10 s per cycle, sine |
| `breathe` | A held element scales 1 → 1.02 and back | 3 s per cycle, sine |

## Built by, and HyperFrames recipes

`motion-animate` builds every move above from `scenes.json` with `scripts/build-scenes.py`, except `cut` and `wipe`, which the assembly mounts between scenes. When a move needs more than the generator gives, write it as `custom` with its own GSAP and start from the HyperFrames recipe named here (`/hyperframes-animation` → `rules/<name>.md`):

| Moves | HyperFrames recipe |
|---|---|
| `phrase-in`, `cards-assemble`, `photo-mosaic` | `waterfall-entry` |
| `phrase-swap`, `word-swap` | `kinetic-beat-slam`, `discrete-text-sequence`, `vertical-spring-ticker` |
| `keyword-accent` | `asr-keyword-glow`, `gradient-text-sweep` |
| `typewriter` | `gsap-effects` (typewriter) |
| `stroke-draw` | `svg-path-draw` |
| `shape-morph`, `morph-through`, `masked-video` | `card-morph-anchor`, `scale-swap-transition` |
| `ring-pulse`, `tap` | `cursor-click-ripple`, `physics-press-reaction` |
| `logo-resolve`, `notification-drop`, `success-burst` | `spring-pop-entrance`, `particle-burst` |
| `device-tilt-in` | `split-tilt-cards`, `orbit-3d-entry` |
| `push-in`, `pull-out`, `zoom-through` | `coordinate-target-zoom`, `viewport-change`, `multi-phase-camera`, `motion-blur-streak` |
| `satellite-cards` | `center-outward-expansion` |
| `screen-scroll` | `3d-page-scroll` |
| `card-resize`, `chat-stack` | `anchored-layout-expand`, `reactive-displacement` |
| `state-change`, `toggle`, `screen-swap`, `background-swap` | `control-target-sync`, `theme-crossfade-morph` |
| `count-up` | `counting-dynamic-scale`, `stat-bars-and-fills` |
| `card-carousel`, `film-strip` | `nudge-curve` |
| `glow-drift`, `breathe` | `ambient-glow-bloom`, `sine-wave-loop` |

## Density

Set in the motion spec, measured on the render by `motion-audit`.

| Target | Default |
|---|---|
| Share of time in motion | 65–80% |
| Gap between move starts | 3 s at most (busier is fine while one hero move plays at a time) |
| Longest still hold | 3 s, except one deliberate hero hold per piece |

Plan key frames from it: about one move per 2.5 s of panel time, so an 8 s panel carries 3–4 moves. Ambient moves do not count toward density; they only keep holds alive.
