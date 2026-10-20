# scenes.json

The input `scripts/build-scenes.py` builds the `hyperframes` scenes from. It lives at the project root, next to `STORYBOARD.md`. Layers come from the Figma frames (`scripts/dump-frames.js`); moves come from each panel's `moves` line in `STORYBOARD.md`. Write it once, then edit it: it is the scene's source until a composition is edited by hand.

## Piece

```json
{
  "format": { "width": 1920, "height": 1080, "fps": 30 },
  "background": "#0e1022",
  "font": "Ubuntu",
  "accent": "#18c8b0",
  "caret": ["#7c5cff", "#18c8b0"],
  "fonts": [{ "family": "Ubuntu", "weight": 700, "src": "assets/fonts/Ubuntu-Bold.woff2" }],
  "audio": { "src": "assets/audio/track.mp3", "volume": 0.8, "media_start": 0 },
  "panels": []
}
```

`accent` colours a `success-burst`; `caret` is the typewriter caret gradient; `audio` is optional (the assembly offsets it to the first panel in the render scope, so a scene video keeps its part of the music).

## Panel

```json
{
  "id": "02", "name": "Device", "duration": 10, "transition_in": "cut",
  "background": "#0e1022",
  "layers": [],
  "groups": { "device": { "members": ["02 Device / phone", "02 Device / screen"], "origin": "960px 620px" } },
  "moves": [{ "move": "device-tilt-in", "target": "device", "at": 0.4 }]
}
```

- `id`, `duration` and `transition_in` match `STORYBOARD.md`.
- `groups` are elements that always move together; a move can target a group by its name. `origin` defaults to the members' centre.
- Panels on other routes are listed with `id`, `duration` and `transition_in` only, so start times stay right; they are never built.

## Layers

Exactly what `dump-frames.js` returns, in frame order (first is at the back). Coordinates are in frame pixels; children of a clipping frame are relative to it.

| Key | For | Meaning |
|---|---|---|
| `name` | all | The Figma layer name (`NN Panel / element`). Unique per state. |
| `state` | all | 1 for the first frame; 2, 3 … for a layer that differs in a later state frame. Moves name it `name@2`. |
| `type` | all | `rect`, `ellipse`, `text`, `image`, `vector`, `video` |
| `x`, `y`, `w`, `h` | all | Position and size. |
| `opacity`, `blur`, `rotation`, `shadow` | all | As in Figma (`blur` is the Figma radius). Moves tween back to `opacity`, never to 1. |
| `fill` | shapes | A hex, or `{type: linear, angle, stops: [[pos, colour]]}` / `{type: radial, stops}` |
| `radius`, `stroke` | shapes | A number or four corners; `{color, width, dashed}` |
| `clip`, `children` | rect | A clipping frame and what is inside it (a screen that scrolls). |
| `text`, `size`, `weight`, `font`, `color`, `align`, `tracking`, `lineHeight`, `accents`, `tabular` | text | `tracking` in em; `lineHeight` a multiplier (or px when over 4); `accents` as `[start, end, colour]` character ranges. |
| `src`, `fit` | image, video | Path from the project root; `fill`, `cover` or `contain`. |
| `paths` | vector | SVG path data from Figma. |
| `allow_overlap`, `allow_overflow` | all | Tell `check` the overlap or overflow is designed. |

## Moves

One object per move: `move` (a name from `motion-vocabulary.md`), `target` (a layer, `layer@state`, a group, or a list of them), `at` (seconds into the panel), and optional `d` (duration) and `ease` (a vocabulary ease name or a GSAP ease). Move-specific keys:

| Move | Keys |
|---|---|
| `enter`, `exit` | `y`, `stagger`; for `enter`, `from` (start values, e.g. `{"scaleX": 0}` or `{"x": -560, "rotationY": 16}`) and `origin` (`"0% 50%"`) |
| `fade` | `dir` (`in`, `out`) |
| `phrase-swap` | `to`: the incoming line |
| `word-swap` | `to`: the line's later state; the words that differ slide, shared words cross-fade |
| `keyword-accent` | `accent`: which accent range (default all) |
| `typewriter` | `per`: seconds per character |
| `shape-morph` | `chain`: layers in order (or `target` + `to`), `hold` between links |
| `push-in` | `fill`: share of the frame the target fills (0.8), `max` scale |
| `satellite-cards` | `from`: the device or group they come out of, `back`: time they tuck in |
| `screen-scroll` | `by`: pixels (negative scrolls up) |
| `tap` | `dx`, `dy`: offset from the target's centre |
| `screen-swap`, `content-swap`, `background-swap`, `state-change` | `to`; or `state: N` alone to swap every layer that changes in state N |
| `card-resize` | `to` (a layer whose box is the end size) or `scaleX`, `scaleY`; `anchor` |
| `card-carousel`, `film-strip` | `by` (pixels), `speed` (px/s for film strip) |
| `notification-drop` | `out`: time it leaves |
| `chat-stack` | `target`: bubbles in order of arrival, at their final positions; `gap` |
| `toggle` | `by`: knob travel; `from` and `to` for the track states |
| `count-up` | `to`, `from`, `decimals`, `prefix`, `suffix`, `separator`; the frame holds the final value |
| `success-burst` | `particles`, `color`, `spread` |
| `mask-reveal`, `masked-video` | `from`: start inset (`50% 50% 50% 50%` is a point), `radius` |
| `dissolve` | `dir`: `out` fades the scene out, `in` fades it in |
| `glow-drift`, `breathe` | `x`, `y` or `amount`, `until` |
| `custom` | `js`: GSAP lines using `tl`; ids follow `p<NN>-<layer slug>` |

Rules the generator keeps for you: one paused timeline per scene, the first tween on each property owns the start state (set before the timeline runs), no layout measuring, every value baked from the frame geometry.
