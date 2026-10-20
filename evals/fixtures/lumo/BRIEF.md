---
workflow: general-video
flow: automation
storyboard: no
---

# Lumo — fixture brief

Fictional three-panel promo (27 s, 1920×1080, 30 fps, no audio) for testing the Motion skills and scripts. Lumo, its UI and its copy are invented; the screens and photos are generated gradients (`make-assets.sh`).

Panels: 01 Opener (8 s), 02 Device (10 s), 03 Chat and close (9 s). Every route is `hyperframes`.

Known on purpose: the render measures about 62% in motion, just under the default 65% target, with its longest hold (2.5 s) at 5.25 s while "Meet Lumo." sits still, so `motion-audit` should flag the density as Low or Medium.
