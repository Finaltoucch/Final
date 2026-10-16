"""Final Touch thumbnail template: one fixed layout for every thumbnail.

Never alters the photo. It only adds the title:
- Anton, all caps; the second line is slightly faded; each line is scaled to the same width, so the title forms a justified block.
- The block is centered horizontally. The top margin and the side margins are FIXED for every thumbnail.
- Text is black on a light background and lime #C6FF00 with a soft glow on a dark one (decided automatically).
- His cut-out is pasted back over the text, so his head sits in front of the title.

usage: render_thumb.py photo.png out.png "LINE ONE" "LINE TWO" [--ratio 9:16|4:5]
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageStat

FONT = os.path.join(os.path.dirname(__file__), '..', '..', 'brand', 'fonts', 'Anton-Regular.ttf')
TOP = 0.065      # top margin, fraction of height (same on every thumbnail)
SIDE = 0.08      # side margins, fraction of width
GAP = 0.018      # gap between lines, fraction of width
MAXH = 0.32      # max block height, fraction of height
FAINT = 0.62     # opacity of the second line (slight fade)
LIME, BLACK = (198, 255, 0), (10, 10, 10)

def cover(img, W, H):
    s = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x, y = (img.width - W) // 2, 0  # keep the top of the photo (heads are near the top)
    return img.crop((x, y, x + W, y + H))

def line_img(text, width, color):
    f = ImageFont.truetype(FONT, 400)
    l, t, r, b = f.getbbox(text)
    im = Image.new('L', (r - l, b - t))
    ImageDraw.Draw(im).text((-l, -t), text, font=f, fill=255)
    h = round(im.height * width / im.width)
    return im.resize((width, h), Image.LANCZOS)

def main():
    a = sys.argv[1:]
    ratio = '9:16'
    if '--ratio' in a:
        i = a.index('--ratio'); ratio = a[i + 1]; del a[i:i + 2]
    src, out, lines = a[0], a[1], [s.upper() for s in a[2:]]
    W = 1080; H = 1920 if ratio == '9:16' else 1350
    photo = cover(Image.open(src).convert('RGB'), W, H)
    bw = round(W * (1 - 2 * SIDE))
    masks = [line_img(s, bw, None) for s in lines]
    gap = round(W * GAP)
    total = sum(m.height for m in masks) + gap * (len(masks) - 1)
    if total > H * MAXH:  # shrink the whole block evenly, still centered
        k = H * MAXH / total
        masks = [m.resize((round(m.width * k), round(m.height * k)), Image.LANCZOS) for m in masks]
        gap = round(gap * k); total = round(H * MAXH)
    top = round(H * TOP)
    region = photo.crop((0, top, W, top + total)).convert('L')
    dark = ImageStat.Stat(region).mean[0] < 140
    color = LIME if dark else BLACK
    layer = Image.new('L', (W, H))
    y = top
    for i, m in enumerate(masks):
        if i > 0:
            m = m.point(lambda v: int(v * FAINT))
        layer.paste(m, ((W - m.width) // 2, y)); y += m.height + gap
    canvas = photo.copy()
    if dark:
        glow = layer.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * 0.55))
        canvas.paste(Image.new('RGB', (W, H), LIME), (0, 0), glow)
    canvas.paste(Image.new('RGB', (W, H), color), (0, 0), layer)
    try:
        from rembg import remove, new_session
        cut = remove(photo, session=new_session('u2net_human_seg'))
        canvas.paste(cut, (0, 0), cut.split()[-1])
    except Exception as e:
        print('cutout skipped:', e)
    canvas.save(out, quality=95)
    print(out, 'dark' if dark else 'light', 'block', bw, 'x', total, 'top', top)

if __name__ == '__main__':
    main()
