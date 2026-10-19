#!/usr/bin/env python3
"""Validate a delivered clip against the piece format.
Usage: validate-clip.py FILE WIDTH HEIGHT FPS DURATION_SECONDS
Exit 0 = ACCEPT, 1 = REJECT, 2 = MISSING."""
import json, os, subprocess, sys

f, W, H, FPS, DUR = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
if not os.path.isfile(f):
    print(f"MISSING {f}"); sys.exit(2)
try:
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate:format=duration", "-of", "json", f],
                         capture_output=True, text=True, check=True).stdout
    j = json.loads(out); s = j["streams"][0]; d = float(j["format"]["duration"])
except Exception as e:
    print(f"REJECT {f} -> not a playable video ({e.__class__.__name__})"); sys.exit(1)
a, b = (s["r_frame_rate"].split("/") + ["1"])[:2]
fps = int(a) / int(b)
tol = 1 / FPS + 0.001
why = []
if (s["width"], s["height"]) != (W, H): why.append(f"size {s['width']}x{s['height']} (expected {W}x{H})")
if abs(fps - FPS) > 0.01: why.append(f"fps {fps:g} (expected {FPS:g})")
if abs(d - DUR) > tol: why.append(f"duration {d:.3f}s (expected {DUR:g}s ±{1/FPS:.3f})")
if why:
    print(f"REJECT {f} -> " + "; ".join(why)); sys.exit(1)
print(f"ACCEPT {f}  {s['width']}x{s['height']} {fps:g}fps {d:.3f}s"); sys.exit(0)
