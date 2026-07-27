#!/usr/bin/env python3
"""Resample the sliced panels up to HD (long edge 1080).

Honest limits: this enlarges, it does not reconstruct. Lanczos plus a
mild unsharp pass keeps edges as crisp as resampling allows, but no
detail absent from the ~415px source is recovered.
"""
from PIL import Image, ImageFilter
import os, glob

SRC, OUT, LONG_EDGE = 'slices', 'hd', 1080
os.makedirs(OUT, exist_ok=True)

for path in sorted(glob.glob(os.path.join(SRC, '*.png'))):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    scale = LONG_EDGE / max(w, h)
    tw, th = round(w * scale), round(h * scale)

    big = im.resize((tw, th), Image.LANCZOS)
    # counteract resampling softness without ringing on the flat fills
    big = big.filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=3))

    dest = os.path.join(OUT, os.path.basename(path))
    big.save(dest, optimize=True)
    print(f'{os.path.basename(path):28s} {w}x{h} -> {tw}x{th}  ({scale:.2f}x)')
