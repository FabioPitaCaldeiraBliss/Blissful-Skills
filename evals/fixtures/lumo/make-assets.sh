#!/usr/bin/env bash
# Generate the fixture's placeholder screens and photos (gradients, no real product or people).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p assets/screens assets/photos
ffmpeg -v error -y -f lavfi -i "gradients=s=350x1436:c0=0x6b4dff:c1=0x18c8b0:x0=0:y0=0:x1=350:y1=1436" -frames:v 1 assets/screens/home.png
for i in 1 2 3 4 5 6; do
  ffmpeg -v error -y -f lavfi -i "gradients=s=480x280:c0=0x$(printf '%02x' $((i * 40)))4d88:c1=0xf0c060:seed=$i" -frames:v 1 "assets/photos/p$i.png"
done
