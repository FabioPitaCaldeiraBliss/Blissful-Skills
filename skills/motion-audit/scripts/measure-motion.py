#!/usr/bin/env python3
"""Measure how much a video moves: motion density, holds, hard cuts, contact sheets.

Usage: measure-motion.py VIDEO [--start S] [--end S] [--sheets DIR] [--flash] [--json]

--flash approximates WCAG 2.3.1 on a 64x36 luminance grid at 30 fps: a cell flashes on an opposing
pair of 10%+ luminance changes with the darker state under 0.8; more than 3 flashes in one second
over at least 4.2% of the frame (about 341x256 px at 1080p) is reported as a possible failure.
It does not check the red-flash rule; treat any result as a prompt for a human check.

Needs ffmpeg and ffprobe on PATH. Standard library only.
Exits 0 on success, 2 when the file or ffmpeg is missing.
"""
import argparse, json, os, shutil, subprocess, sys

W, H, FPS = 320, 180, 4      # analysis size and sample rate
ACTIVE = 2.0                 # mean absolute grey difference, in any grid cell, that counts as motion
GRID = (8, 6)                # cells across and down: a small move in one cell still counts
HOLD = 0.75                  # shortest still run reported as a hold, in seconds
CUT = 0.3                    # ffmpeg scene score that counts as a hard cut


def probe_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "json", path], capture_output=True, text=True, check=True)
    return float(json.loads(out.stdout)["format"]["duration"])


def window_args(start, end):
    args = []
    if start:
        args += ["-ss", str(start)]
    if end:
        args += ["-to", str(end)]
    return args


def frames(path, start, end):
    cmd = ["ffmpeg", "-v", "error", *window_args(start, end), "-i", path,
           "-vf", f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", "-"]
    data = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = W * H
    return [data[i:i + n] for i in range(0, len(data) - n + 1, n)]


def cuts(path, start, end):
    cmd = ["ffmpeg", "-v", "info", *window_args(start, end), "-i", path,
           "-vf", f"scale={W}:{H},select='gt(scene,{CUT})',showinfo", "-f", "null", "-"]
    err = subprocess.run(cmd, capture_output=True, text=True).stderr
    times = []
    for line in err.splitlines():
        if "pts_time:" in line:
            t = float(line.split("pts_time:")[1].split()[0])
            times.append(round(t + (start or 0), 2))
    return times


def sheets(path, start, end, out_dir, every=2, cols=6, rows=3):
    os.makedirs(out_dir, exist_ok=True)
    cmd = ["ffmpeg", "-v", "error", "-y", *window_args(start, end), "-i", path,
           "-vf", f"fps=1/{every},scale=320:-2,tile={cols}x{rows}:padding=4:color=white",
           os.path.join(out_dir, "sheet_%02d.png")]
    subprocess.run(cmd, check=True)
    return {"every_s": every, "per_sheet": cols * rows, "dir": out_dir,
            "note": f"tile k (from 0) of sheet n (from 1) is at {start or 0} + ((n-1)*{cols * rows} + k)*{every} s"}


def flashes(path, start, end, fw=64, fh=36, fps=30):
    cmd = ["ffmpeg", "-v", "error", *window_args(start, end), "-i", path,
           "-vf", f"fps={fps},scale={fw}:{fh},format=gray", "-f", "rawvideo", "-"]
    data = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = fw * fh
    lum = [[(b / 255) ** 2.2 for b in data[i:i + n]] for i in range(0, len(data) - n + 1, n)]
    # per cell: times of luminance changes of 10%+ (relative to the brighter side) with the darker under 0.8
    events = [[] for _ in range(n)]
    last = list(lum[0]) if lum else []
    for f in range(1, len(lum)):
        for c in range(n):
            a, b = last[c], lum[f][c]
            if abs(a - b) >= 0.1 and min(a, b) < 0.8:
                d = 1 if b > a else -1
                ev = events[c]
                if not ev or ev[-1][1] != d:
                    ev.append((f / fps, d))
                last[c] = b
    worst, at = 0.0, None
    for t in range(int(len(lum) / fps)):
        hit = 0
        for ev in events:
            flips = sum(1 for (tt, _) in ev if t <= tt < t + 1)
            if flips // 2 > 3:
                hit += 1
        share = hit / n
        if share > worst:
            worst, at = share, t + (start or 0)
    return {"flash_area_pct": round(100 * worst, 1), "flash_at_s": at, "flash_risk": worst >= 0.042}


def measure(path, start=None, end=None):
    fr = frames(path, start, end)
    n = W * H
    cw, ch = W // GRID[0], H // GRID[1]

    def cell_max(a, b):
        worst = 0.0
        for gy in range(GRID[1]):
            for gx in range(GRID[0]):
                tot = 0
                for y in range(gy * ch, (gy + 1) * ch):
                    row = y * W + gx * cw
                    tot += sum(abs(p - q) for p, q in zip(a[row:row + cw], b[row:row + cw]))
                worst = max(worst, tot / (cw * ch))
        return worst

    diff = [cell_max(fr[i], fr[i - 1]) for i in range(1, len(fr))]
    active = [d > ACTIVE for d in diff]
    duration = len(fr) / FPS
    segments, holds, run = 0, [], 0
    for i, a in enumerate(active):
        if a and (i == 0 or not active[i - 1]):
            segments += 1
        if a:
            if run:
                holds.append((round((i - run) / FPS + (start or 0), 2), run / FPS))
            run = 0
        else:
            run += 1
    if run:
        holds.append((round((len(active) - run) / FPS + (start or 0), 2), run / FPS))
    windows = []
    for w in range(0, int(duration), 10):
        part = active[w * FPS:(w + 10) * FPS]
        if part:
            windows.append({"from_s": w + (start or 0), "active_pct": round(100 * sum(part) / len(part))})
    long_holds = sorted((h for h in holds if h[1] >= HOLD), key=lambda h: -h[1])
    return {
        "file": os.path.basename(path),
        "duration_s": round(duration, 2),
        "active_pct": round(100 * sum(active) / max(len(active), 1)),
        "moves": segments,
        "seconds_per_move": round(duration / segments, 2) if segments else None,
        "holds_over_0_75s": len(long_holds),
        "longest_holds_s": [h[1] for h in long_holds[:6]],
        "longest_holds_at_s": [h[0] for h in long_holds[:6]],
        "hard_cuts_s": cuts(path, start, end),
        "per_10s": windows,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("video")
    p.add_argument("--start", type=float)
    p.add_argument("--end", type=float)
    p.add_argument("--sheets", help="write contact sheets (one frame every 2 s) to this folder")
    p.add_argument("--flash", action="store_true", help="also check for flashing (WCAG 2.3.1, approximate)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    if not os.path.isfile(a.video) or not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        print("missing: video file, ffmpeg or ffprobe", file=sys.stderr)
        sys.exit(2)
    r = measure(a.video, a.start, a.end)
    r["source_duration_s"] = round(probe_duration(a.video), 2)
    if a.sheets:
        r["sheets"] = sheets(a.video, a.start, a.end, a.sheets)
    if a.flash:
        r.update(flashes(a.video, a.start, a.end))
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"{r['file']}: {r['duration_s']} s, {r['active_pct']}% in motion, "
          f"{r['moves']} moves (one every {r['seconds_per_move']} s)")
    print(f"holds over {HOLD} s: {r['holds_over_0_75s']}, longest: " +
          ", ".join(f"{d} s at {t} s" for d, t in zip(r["longest_holds_s"], r["longest_holds_at_s"])))
    print(f"hard cuts at: {r['hard_cuts_s'] or 'none'}")
    print("per 10 s: " + ", ".join(f"{w['from_s']:g}s {w['active_pct']}%" for w in r["per_10s"]))
    if a.flash:
        print(f"flashing: {'POSSIBLE FAILURE' if r['flash_risk'] else 'below threshold'} "
              f"(worst second at {r['flash_at_s']} s, {r['flash_area_pct']}% of the frame over 3 flashes)")
    if a.sheets:
        print(f"contact sheets in {a.sheets}; {r['sheets']['note']}")


if __name__ == "__main__":
    main()
