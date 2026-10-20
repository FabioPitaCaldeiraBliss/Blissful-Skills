# Treatments and shot templates

A treatment fixes a frame's layer roles, focal element and negative space (`craft.md`). Start each one from a **shot template**: HyperFrames' blueprints are time-coded shapes mined from real product launch films (`/hyperframes-animation` → `blueprints-index.md`, then `blueprints/<id>.md`). The storyboard gives each panel a **role** and a **shot**; the frame is laid out so the shot's signature move can happen.

## Role → shot

| Role (storyboard) | Shots to start from |
|---|---|
| Hook | `kinetic-type-beats`, `typewriter-reveal`, `zoom-out-workspace-reveal`, `dataviz-countup` |
| Problem | `kinetic-type-beats`, `dataviz-countup`, `overwhelm-surround` |
| Product intro | `logo-assemble-lockup`, `device-surface-showcase`, `cursor-ui-demo`, `titlecard-reveal` |
| Key feature | `device-surface-showcase`, `cursor-ui-demo`, `grid-card-assemble`, `prompt-type-submit-generate`, `agent-progress-theater`, `comparison-split` |
| Benefits | `kinetic-type-beats`, `grid-card-assemble`, `camera-journey`, `titlecard-reveal` |
| Social proof | `constellation-hub`, `grid-card-assemble`, `titlecard-reveal` |
| CTA, Brand outro | `logo-assemble-lockup`, `cta-morph-press`, `kinetic-type-beats`, `fixed-anchor-cycle` |

Use a shot as it is when its slots fit, adapt it when the content differs (keep the signature move), or compose from the motion vocabulary when none fits. Name the choice in the frame plan.

## Presets

Starting points at 1920×1080; the brand's type and colour always win. Each lists the layers the moves need, so they exist as separate named layers.

| Treatment | Shot | Layout | Type | Layers the moves need |
|---|---|---|---|---|
| **Statement** | `kinetic-type-beats`, `titlecard-reveal` | One line centred, 50–60% negative space, text block 60–80% of the width | Headline 96–120 px, 700+, tracking −0.03 em; one accent word | each phrase as its own text layer (or a state per phrase), bg glow, optional rule |
| **Hero Stat** | `dataviz-countup` | Number anchored to the title-safe left edge, label under it, chart or ring on the right half | Number 240–400 px tabular; label 36–44 px | number (frame holds the final value), label, chart bars or ring as separate layers |
| **Device Hero** | `device-surface-showcase` | Device 70–80% of the frame height, on a third; copy column 800–900 px on the other side | Headline 88–104 px; support 32–40 px | device frame, screen as a clipping frame with the tall screenshot inside (for `screen-scroll`), touch target layers, satellite cards behind the device |
| **UI Demo** | `cursor-ui-demo`, `prompt-type-submit-generate` | Rebuilt UI at 1.5–2× its real size, cropped to the area that acts | UI text at 28–40 px (never web sizes) | the input as live text, each state of the result as its own state frame, the control that gets tapped |
| **Card Grid** | `grid-card-assemble` | 3×2 or 4×2 grid inside title-safe, 32–48 px gutters, equal cards | Card label 28–36 px | each card as its own layer (or group), in reading order |
| **Conversation** | `agent-progress-theater` | A 520–640 px column, bubbles 20 px apart, status line under it | Bubble text 32–36 px | each bubble as a group at its final position, status as two states, the confirmation element |
| **Split** | `comparison-split` | Two equal halves, each with its own title-safe box | Headline per half 64–80 px | both halves as groups, the badge on each |
| **Mosaic** | `grid-card-assemble` | Photo or video tiles at 25–40% opacity framing a centred phrase | Phrase 96–110 px | each tile as its own image layer, the phrase on top |
| **Closing** | `logo-assemble-lockup`, `cta-morph-press` | Mark centred at about 40% of the height, line or CTA below, 60% negative space | Tagline 72–96 px | the mark's parts as separate layers (for `shape-morph` or `stroke-draw`), the wordmark, the CTA |

## Handoff states

A `hyperframes` scene starts on its handoff from the previous panel and ends on its handoff into the next. Design those as the panel's first and last state frames: the first matches the previous panel's last frame (same layer names, positions and sizes for what carries over), and the last matches the next panel's first. Where the storyboard names a `cut` or `wipe`, the frames are free.
