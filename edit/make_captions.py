#!/usr/bin/env python3
"""Build styled .ass caption tracks (one per ratio) from captions.srt."""
import re, sys, os

S = "/tmp/claude-0/-home-user-Final/cd63c724-a39b-5037-8d91-6395028ce328/scratchpad"
SRT = f"{S}/build/captions.srt"

# per-ratio: (W, H, fontsize, marginV)
RATIOS = {
    "16x9": (1920, 1080, 56, 96),
    "9x16": (1080, 1920, 56, 300),   # lifted clear of platform UI chrome
    "1x1":  (1080, 1080, 52, 110),
}

HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CS,Outfit,{FS},&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0.6,0,1,3.4,2.2,2,{ML},{MR},{MV},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def parse_srt(path):
    if not os.path.exists(path):
        return []
    blocks = re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip())
    out = []
    for b in blocks:
        lines = [l for l in b.strip().splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        tl = next((l for l in lines if "-->" in l), None)
        if not tl:
            continue
        a, bb = [x.strip().replace(",", ".") for x in tl.split("-->")]
        def sec(x):
            hh, mm, ss = x.split(":")
            return int(hh) * 3600 + int(mm) * 60 + float(ss)
        txt = " ".join(lines[lines.index(tl) + 1:]).strip()
        if txt:
            out.append((sec(a), sec(bb), txt))
    return out


def main():
    cues = parse_srt(SRT)
    if not cues:
        print("!! captions.srt is empty - no caption track will be burned in")
    for tag, (W, H, fs, mv) in RATIOS.items():
        body = HEAD.format(W=W, H=H, FS=fs, ML=int(W * 0.08), MR=int(W * 0.08), MV=mv)
        for a, b, t in cues:
            t = t.replace("\\n", "\\N")
            body += f"Dialogue: 0,{ts(a)},{ts(b)},CS,,0,0,0,,{t}\n"
        p = f"{S}/assets/{tag}/captions.ass"
        open(p, "w", encoding="utf-8").write(body)
        print(f"  {tag}: {len(cues)} cues -> {p}")


if __name__ == "__main__":
    main()
