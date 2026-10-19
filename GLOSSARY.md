# Glossary

Shared language for the Blissful skills. Terms for the motion skills are listed first.

## Motion

**Source material**
What the designer brings to start work: a script, a plan, Figma screens, images, or any mix. Everything else is derived from it.

**Storyboard**
An ordered sequence of panels that describes a piece of motion or video from start to end. It belongs to one piece of work, for example one animated onboarding or one promo video.

**Panel**
One step of a storyboard: a visual (a screen, an image or a placeholder) plus notes on what happens in it. The unit the designer reads, reorders and approves. Designers often say "scene"; it means the same thing, and "panel" is the canonical word in the skills.

**Frame**
The finished, static, animation-ready visual of a panel. Built from the storyboard, at a size the designer supplies, and made of separate named layers so each moving part can be animated on its own. A frame replaces the panel's sketch once designed.

**Design direction**
The palette, type and treatments for a piece, taken from a design system or proposed from the source, and approved together with the frame plan. Recorded as the piece's `frame.md`.

**Treatment**
A reusable frame type defined once for a piece (for example Hero Stat or Closing) that fixes a frame's layer roles, focal element and negative space without fixing its layout. Each panel is given one.

**Layer role**
Whether a layer is background (persistent decoratives), midground (the message) or a foreground accent. Every role is its own layer so it can be animated alone.

**Element**
One part of a frame that can move on its own (a phone, a headline, a counter, a background). Each element is its own clearly named layer, never merged into a flat image.

**State**
A distinct composition a panel passes through, such as the start and end of a counter or light and dark mode. A panel gets one frame per state only where the layout or content changes; things that merely move or fade share one frame.

**Frame plan**
The proposal shown before any frames are built: per panel, how many frames and states, which elements are separate layers, and what the designer still has to supply. The designer edits and approves it first.

**Animation plan**
The proposal shown before any motion is built: per panel, each layer's motion with start, end and easing, the defaults the skill chose, the meaning gaps it needs answered, and any layers that already have motion. The designer approves it first.

**Timeline frame**
A copy of a panel's frame that carries its animation, with a duration taken from the storyboard. Where a panel has several states, the timeline frame holds all their layers so states can cross-fade or swap inside one timeline. The static frames stay untouched as the final artwork.

**Transition frame**
A frame that holds only a transition between two panels, animated on its own, exported separately and joined to the panels afterwards. Panel timelines carry no in or out of their own.

**Key frame**
A still of one moment inside a panel, with a timecode, a one-sentence description and tags for what the moment needs (ease, camera, transition, sound, text). A panel has three to five. Layout or content changes between key frames are the states that `motion-frames` plans from.

**Motion spec**
The decisions stated once at the top of a storyboard and inherited by every panel: the recurring element, an optional persona, the structure into chapters, easing and timing numbers, camera and depth, and the music. Panels never restate it.

**Beat map**
A strip of the piece's length against the music's beat grid, with each panel as a band and markers for the hits. Only made when a BPM is known.

**Sketch**
A simple drawn picture standing in for a key frame's visual when no screen or image was supplied. Built from the key frame's own sentence and copy, tagged as a sketch, and replaced once real visuals exist.

**Kind**
Whether a storyboard describes UI motion (an interface moving in response to something) or video (a sequence shot or edited over time). The kind only changes which notes a panel carries.

**Gap**
A panel note the source material didn't answer, such as a missing duration. Gaps stay visibly blank in the panel, never filled in silently, and are raised with the designer in one batch.

**Default**
A small choice the animation skill makes where the notes are silent, such as easing or a minor timing. Defaults are listed back to the designer. Anything that changes the meaning (order, trigger, the length of a key moment) is a gap, not a default.

**Route**
How one panel gets animated: `hyperframes` (built as a native scene in the assembly project), `figma motion` (animated in Figma and exported as a clip), or `after effects` (animated by a human and delivered as a clip). Each panel has its own route, proposed in the storyboard with a one-line reason and confirmed by the designer; the default is `hyperframes`. Replaces the older "animation target", which was one choice for the whole piece.

**Piece format**
The frame size, frames per second and length limit recorded once in the storyboard header. Every route inherits it, and anything a human delivers must match it.

**Handoff pack**
What a human animator receives for a panel on the `after effects` route: the layered frames, each layer exported as an image or vector file, the panel's notes (duration, motion, transition), the piece format, and the exact file name expected back. The human delivers either a rendered clip or a Lottie file, and the panel records which was agreed.

**Stand-in**
A labelled placeholder of the right length that the assembly shows while a panel's clip has not arrived yet, so the cut still renders. It is replaced when a file with the expected name appears, and every stand-in is listed as missing.

**Edit home**
The one place where a panel's editable source lives: its Figma timeline frame, its HyperFrames composition file, or the After Effects project the human names. Recorded per panel in the storyboard and kept up to date.

**Assembly**
The single HyperFrames project where the finished piece is put together and rendered. Panels on the `hyperframes` route are native scenes in it; panels on the other routes arrive as video clips mounted in it; transitions sit between them.
