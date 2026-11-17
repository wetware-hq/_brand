#!/usr/bin/env python3
"""Assemble the WET-104 seed reels from their Higgsfield masters.

For each reel in the manifest: soften any pseudo-text boxes, lay the score under
the diegetic sound, normalise loudness, and encode H.264 for every platform.
Writes <name>.mp4 (with score) and <name>-clean.mp4 (diegetic only).

  assemble_reels.py [--manifest seed/wet-104/manifest.json] [--out seed/wet-104/reels]
                    [--cache /tmp/wet104-assembly]
"""

import argparse
import json
import os
import re
import subprocess
import urllib.request

FPS = 24


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True)


def fetch(url, path):
    if not os.path.exists(path):
        with urllib.request.urlopen(url, timeout=300) as resp, open(path, "wb") as handle:
            handle.write(resp.read())
    return path


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout
    return float(out.strip())


def integrated_lufs(path):
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128", "-f", "null", "-"]).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", err)[-1])


def normalize(src, dst, target, true_peak):
    # loudnorm's dynamic mode barely moves on 8 s clips, so apply a measured gain and
    # hold peaks with a 4x-oversampled limiter, correcting once for what it shaved off.
    limit = 10 ** (true_peak / 20)
    gain = target - integrated_lufs(src)
    for _ in range(3):
        run(["ffmpeg", "-y", "-hide_banner", "-i", src, "-af",
             f"volume={gain:.2f}dB,aresample=192000,alimiter=limit={limit:.4f}:attack=1:release=60:level=0,"
             f"aresample=48000", "-c:a", "pcm_s16le", dst])
        miss = target - integrated_lufs(dst)
        if abs(miss) <= 0.3:
            break
        gain += miss
    return dst


def blur_graph(boxes, length):
    if not boxes:
        return "[0:v]null[v]"
    parts, label = [], "0:v"
    for index, box in enumerate(boxes):
        x, y, w, h = box["x"], box["y"], box["w"], box["h"]
        feather = max(8, min(w, h) // 8)
        parts += [
            f"color=c=black:s={w}x{h}:r={FPS}:d={length + 1}[m{index}]",
            f"[m{index}]drawbox=x={feather}:y={feather}:w={w - 2 * feather}:h={h - 2 * feather}:color=white:t=fill,"
            f"gblur=sigma={feather / 2},format=gray[mask{index}]",
            f"[{label}]split[base{index}][src{index}]",
            f"[src{index}]crop={w}:{h}:{x}:{y},gblur=sigma=9,format=yuva420p[soft{index}]",
            f"[soft{index}][mask{index}]alphamerge[patch{index}]",
            f"[base{index}][patch{index}]overlay={x}:{y}:shortest=1:"
            f"enable='between(n,{box['first_frame']},{box['last_frame']})'[v{index}]",
        ]
        label = f"v{index}"
    parts.append(f"[{label}]null[v]")
    return ";".join(parts)


def encode(video_src, audio_wav, graph, dst, extra):
    run(["ffmpeg", "-y", "-hide_banner", "-i", video_src, "-i", audio_wav, "-filter_complex", graph,
         "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-pix_fmt", "yuv420p",
         "-profile:v", "high", "-r", str(FPS), *extra, "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-shortest", "-movflags", "+faststart", dst])
    return dst


def assemble(reel, score_path, loudness, cache, out_dir):
    name = reel["name"]
    master = fetch(reel["source_url"], os.path.join(cache, f"{reel['source_job']}.mp4"))
    length = duration(master)

    segment = os.path.join(cache, f"{name}-score-segment.wav")
    run(["ffmpeg", "-y", "-hide_banner", "-ss", str(reel["score_start_s"]), "-t", str(length), "-i", score_path,
         "-ar", "48000", "-ac", "2", segment])
    gain = reel["score_lufs"] - integrated_lufs(segment)
    delay_ms = int(round(reel["score_delay_s"] * 1000))
    fade_start = max(0.0, length - 0.4)

    mixed = os.path.join(cache, f"{name}-mix.wav")
    run(["ffmpeg", "-y", "-hide_banner", "-i", master, "-i", segment, "-filter_complex",
         f"[1:a]volume={gain:.2f}dB,adelay={delay_ms}|{delay_ms},afade=t=out:st={fade_start:.3f}:d=0.4[s];"
         f"[0:a]aresample=48000,aformat=channel_layouts=stereo[d];"
         f"[d][s]amix=inputs=2:normalize=0:duration=first[m]",
         "-map", "[m]", "-t", str(length), mixed])
    clean = os.path.join(cache, f"{name}-clean.wav")
    run(["ffmpeg", "-y", "-hide_banner", "-i", master, "-vn", "-ar", "48000", "-ac", "2", clean])

    target, true_peak = loudness["integrated_lufs"], loudness["true_peak_db"]
    mixed = normalize(mixed, os.path.join(cache, f"{name}-mix-norm.wav"), target, true_peak)
    clean = normalize(clean, os.path.join(cache, f"{name}-clean-norm.wav"), target, true_peak)

    graph = blur_graph(reel.get("blur_boxes", []), length)
    return [
        encode(master, mixed, graph, os.path.join(out_dir, f"{name}.mp4"), ["-crf", "16"]),
        encode(master, clean, graph, os.path.join(out_dir, f"{name}-clean.mp4"), ["-crf", "16"]),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manifest", default="seed/wet-104/manifest.json")
    parser.add_argument("--out", default="seed/wet-104/reels")
    parser.add_argument("--cache", default="/tmp/wet104-assembly")
    args = parser.parse_args()

    with open(args.manifest) as handle:
        assembly = json.load(handle)["assembly"]
    os.makedirs(args.out, exist_ok=True)
    os.makedirs(args.cache, exist_ok=True)
    score = fetch(assembly["score"]["url"], os.path.join(args.cache, f"{assembly['score']['job']}.mp3"))
    for reel in assembly["reels"]:
        for path in assemble(reel, score, assembly["loudness"], args.cache, args.out):
            print(f"{path}  {os.path.getsize(path) / 1e6:.1f} MB  {integrated_lufs(path):.1f} LUFS")


if __name__ == "__main__":
    main()
