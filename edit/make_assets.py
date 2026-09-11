#!/usr/bin/env python3
"""Generate all graphic overlays for the Cherry Servers / Solana edit."""
import os, sys
from PIL import Image, ImageDraw, ImageFont

S    = "/tmp/claude-0/-home-user-Final/cd63c724-a39b-5037-8d91-6395028ce328/scratchpad"
FONT = "/mnt/skills/examples/canvas-design/canvas-fonts"
BOLD = f"{FONT}/Outfit-Bold.ttf"
REG  = f"{FONT}/Outfit-Regular.ttf"

RED   = (254, 0, 0)
WHITE = (255, 255, 255)
DIM   = (168, 168, 172)

MARK = Image.open(f"{S}/assets/logo_mark.png").convert("RGBA")
WORD = Image.open(f"{S}/assets/wordmark.png").convert("RGBA")


def f(path, size):
    return ImageFont.truetype(path, int(size))


def tw(d, text, font, track=0):
    """Width of text with letter tracking."""
    if not track:
        return d.textbbox((0, 0), text, font=font)[2]
    return sum(d.textbbox((0, 0), c, font=font)[2] + track for c in text) - track


def draw_tracked(d, xy, text, font, fill, track=0, anchor_cx=None):
    x, y = xy
    if anchor_cx is not None:
        x = anchor_cx - tw(d, text, font, track) / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textbbox((0, 0), c, font=font)[2] + track
    return x


def fit(img, h):
    return img.resize((max(1, round(img.width * h / img.height)), int(h)), Image.LANCZOS)


def vgrad(size, rgba_top, rgba_bot):
    """Vertical gradient scrim."""
    w, h = size
    g = Image.new("RGBA", (1, h))
    px = g.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(a + (b - a) * t) for a, b in zip(rgba_top, rgba_bot))
    return g.resize(size, Image.BILINEAR)


def lockup(W, H, s):
    """Persistent small brand lockup, top-left."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    mh = int(52 * s)
    m = fit(MARK, mh)
    w = fit(WORD, mh * 0.40)
    pad = int(56 * s)
    im.alpha_composite(m, (pad, pad))
    im.alpha_composite(w, (pad + m.width + int(18 * s), pad + (m.height - w.height) // 2))
    return im


def headline(W, H, s, vertical=False):
    """Opening claim: 'Bare metal for Solana validators'."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    f_kick = f(BOLD, 34 * s)
    f_big  = f(BOLD, 104 * s)

    kick = "BARE METAL FOR"
    big  = "SOLANA VALIDATORS"
    if vertical:
        f_big = f(BOLD, 88 * s)
        big_lines = ["SOLANA", "VALIDATORS"]
    else:
        big_lines = [big]

    cx = W // 2
    block_h = int(46 * s) + int(20 * s) + len(big_lines) * int(112 * s)
    y = int(H * (0.40 if vertical else 0.46) - block_h / 2)

    # scrim so type survives the busy racing plate
    sc_h = block_h + int(220 * s)
    sc_y = max(0, y - int(110 * s))
    scrim = vgrad((W, sc_h), (0, 0, 0, 0), (0, 0, 0, 150))
    scrim = Image.alpha_composite(
        scrim, vgrad((W, sc_h), (0, 0, 0, 150), (0, 0, 0, 0)).transpose(Image.FLIP_TOP_BOTTOM)
    )
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    base.alpha_composite(vgrad((W, sc_h), (0, 0, 0, 0), (0, 0, 0, 0)), (0, sc_y))
    mid = Image.new("RGBA", (W, sc_h), (0, 0, 0, 0))
    for yy in range(sc_h):
        t = yy / (sc_h - 1)
        a = int(165 * (1 - abs(t - 0.5) * 2) ** 0.7)
        ImageDraw.Draw(mid).line([(0, yy), (W, yy)], fill=(0, 0, 0, a))
    base.alpha_composite(mid, (0, sc_y))
    im = Image.alpha_composite(base, im)
    d = ImageDraw.Draw(im)

    draw_tracked(d, (0, y), kick, f_kick, RED, track=int(7 * s), anchor_cx=cx)
    y += int(46 * s) + int(22 * s)
    for ln in big_lines:
        draw_tracked(d, (0, y), ln, f_big, WHITE, track=int(1 * s), anchor_cx=cx)
        y += int(112 * s)
    return im


def endcard(W, H, s, vertical=False):
    """Final frame: 'Solana servers by Cherry Servers' + CTA."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    cx = W // 2

    mh = int(150 * s)
    m = fit(MARK, mh)
    w = fit(WORD, mh * 0.34)

    f_head = f(BOLD, (52 if not vertical else 56) * s)
    f_cta  = f(BOLD, 40 * s)
    f_url  = f(REG, 30 * s)

    head_lines = ["Solana servers", "by Cherry Servers"] if vertical else ["Solana servers by Cherry Servers"]

    cta_txt = "Explore Solana servers"
    cta_h   = int(88 * s)
    cta_w   = tw(d, cta_txt, f_cta, int(2 * s)) + int(132 * s)

    gap = int(38 * s)
    total = (m.height + int(16 * s) + w.height + int(62 * s)
             + len(head_lines) * int(72 * s) + gap + cta_h + int(34 * s) + int(40 * s))
    y = (H - total) // 2

    im.alpha_composite(m, (cx - m.width // 2, y));  y += m.height + int(16 * s)
    im.alpha_composite(w, (cx - w.width // 2, y));  y += w.height + int(62 * s)

    for ln in head_lines:
        draw_tracked(d, (0, y), ln, f_head, WHITE, track=0, anchor_cx=cx)
        y += int(72 * s)
    y += gap - int(10 * s)

    # CTA pill
    x0 = cx - cta_w // 2
    d.rounded_rectangle([x0, y, x0 + cta_w, y + cta_h], radius=cta_h // 2, fill=RED)
    ty = y + (cta_h - int(52 * s)) // 2
    draw_tracked(d, (0, ty), cta_txt, f_cta, WHITE, track=int(2 * s), anchor_cx=cx)
    y += cta_h + int(34 * s)

    draw_tracked(d, (0, y), "cherryservers.com", f_url, DIM, track=int(3 * s), anchor_cx=cx)
    return im


def portal_slug(W, H, s):
    """Holding slate marking where the real portal capture goes."""
    im = Image.new("RGBA", (W, H), (9, 9, 11, 255))
    d = ImageDraw.Draw(im)
    cx, cy = W // 2, H // 2
    step = int(60 * s)
    for x in range(0, W, step):
        d.line([(x, 0), (x, H)], fill=(255, 255, 255, 12))
    for y in range(0, H, step):
        d.line([(0, y), (W, y)], fill=(255, 255, 255, 12))

    bw, bh = int(W * 0.74), int(H * 0.46)
    x0, y0 = cx - bw // 2, cy - bh // 2
    d.rectangle([x0, y0, x0 + bw, y0 + bh], outline=RED, width=max(2, int(3 * s)))
    L = int(46 * s)
    for (ax, ay, dx, dy) in [(x0, y0, 1, 1), (x0 + bw, y0, -1, 1), (x0, y0 + bh, 1, -1), (x0 + bw, y0 + bh, -1, -1)]:
        d.line([(ax, ay), (ax + dx * L, ay)], fill=RED, width=max(3, int(7 * s)))
        d.line([(ax, ay), (ax, ay + dy * L)], fill=RED, width=max(3, int(7 * s)))

    f1 = f(BOLD, 42 * s); f2 = f(REG, 30 * s); f3 = f(BOLD, 24 * s)
    y = cy - int(74 * s)
    draw_tracked(d, (0, y), "PORTAL CAPTURE", f1, WHITE, track=int(6 * s), anchor_cx=cx); y += int(64 * s)
    draw_tracked(d, (0, y), "Server configuration + deploy  ·  3.5 s", f2, DIM, track=int(1 * s), anchor_cx=cx); y += int(58 * s)
    draw_tracked(d, (0, y), "REPLACE WITH REAL SCREEN RECORDING", f3, RED, track=int(4 * s), anchor_cx=cx)
    return im


def build(tag, W, H, s, vertical):
    out = f"{S}/assets/{tag}"
    os.makedirs(out, exist_ok=True)
    lockup(W, H, s).save(f"{out}/lockup.png")
    headline(W, H, s, vertical).save(f"{out}/headline.png")
    endcard(W, H, s, vertical).save(f"{out}/endcard.png")
    portal_slug(W, H, s).save(f"{out}/portal_slug.png")
    print(f"  {tag}: {W}x{H} scale={s:.3f}")


if __name__ == "__main__":
    print("Generating overlays:")
    build("16x9", 1920, 1080, 1.00, False)
    build("9x16", 1080, 1920, 0.86, True)
    build("1x1",  1080, 1080, 0.80, True)
    print("done")
