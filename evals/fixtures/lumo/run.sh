#!/usr/bin/env bash
# Regression run for the Motion scripts: scaffold a HyperFrames project from this fixture,
# generate the scenes, check them, render a draft and measure it.
# Usage: evals/fixtures/lumo/run.sh <empty scratch folder>
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILLS="$HERE/../../../skills"
OUT="${1:?pass an empty scratch folder}"
mkdir -p "$OUT" && cd "$OUT"
npx hyperframes init lumo --non-interactive --example=blank --skill=general-video >/dev/null
cp "$HERE/scenes.json" "$HERE/STORYBOARD.md" "$HERE/BRIEF.md" lumo/
bash "$HERE/make-assets.sh" && cp -R "$HERE/assets" lumo/
cd lumo
python3 -I "$SKILLS/motion-animate/scripts/build-scenes.py" . --scope all
npx hyperframes check
npx hyperframes render -f 30 -q draft -o renders/lumo.mp4
python3 -I "$SKILLS/motion-audit/scripts/measure-motion.py" renders/lumo.mp4 --flash
