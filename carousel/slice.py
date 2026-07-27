#!/usr/bin/env python3
"""Slice the 3x3 source grid into its individual panels.

Cut lines come from detecting the light gutters between panels rather
than assuming even thirds — the source rows are not equal heights
(445 / 403 / 398 px).
"""
from PIL import Image
import statistics, os

SRC = 'source/grid.webp'
OUT = 'slices'


def gutters(im, vertical=True):
    W, H = im.size
    px = im.load()
    n, m = (W, H) if vertical else (H, W)
    cand = []
    for i in range(n):
        vals = [px[i, j] if vertical else px[j, i] for j in range(0, m, 7)]
        if statistics.pstdev(vals) < 14 and sum(vals) / len(vals) > 225:
            cand.append(i)
    runs = []
    for i in cand:
        if runs and i == runs[-1][-1] + 1:
            runs[-1].append(i)
        else:
            runs.append([i])
    return [(r[0], r[-1]) for r in runs if len(r) >= 2]


def bands(gaps, extent):
    """Panel spans: edge -> first gutter, between gutters, last gutter -> edge."""
    out, start = [], 0
    for a, b in gaps:
        out.append((start, a))
        start = b + 1
    out.append((start, extent))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    im = Image.open(SRC).convert('RGB')
    g = im.convert('L')
    W, H = im.size

    cols = bands(gutters(g, True), W)
    rows = bands(gutters(g, False), H)
    print(f'source {W}x{H}')
    print('columns:', cols)
    print('rows:   ', rows)
    assert len(cols) == 3 and len(rows) == 3, 'expected a 3x3 grid'

    names = ['01-study-targets', '02-study-breaks', '03-sleep',
             '04-meals-hydration', '05-no-quick-fixes', '06-seek-care-early',
             '07-existing-conditions', '08-well-wishes', '09-signoff']

    n = 0
    for ri, (y0, y1) in enumerate(rows):
        for ci, (x0, x1) in enumerate(cols):
            tile = im.crop((x0, y0, x1, y1))
            path = os.path.join(OUT, f'{names[n]}.png')
            tile.save(path)
            print(f'{path}  {tile.width}x{tile.height}  from ({x0},{y0})-({x1},{y1})')
            n += 1


if __name__ == '__main__':
    main()
