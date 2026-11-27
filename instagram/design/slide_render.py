"""Faceless/carousel slide template matching the approved slides (1080x1350, Inter).
usage: slide_render.py photo out.jpg PAGE NUMBER "Headline line 1|line 2" "Body line 1|line 2"
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D = os.path.join(os.path.dirname(__file__), '..', 'brand', 'fonts')
BOLD = os.path.join(D, 'Inter-Bold.woff'); REG = os.path.join(D, 'Inter-Regular.woff')
W, H = 1080, 1350; X = 88; BG = (30, 30, 30); LIME = (198, 255, 0); GREY = (160, 160, 160)

def main(src, out, page, num, head, body):
    im = Image.open(src).convert('RGB')
    s = max(W / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - W) // 2; im = im.crop((x, 0, x + W, H))
    # blend the photo into the dark text area: smooth fade, no hard edge
    grad = Image.new('L', (1, H))
    for y in range(H):
        t = min(1, max(0, (y - 640) / (980 - 640))); grad.putpixel((0, y), int(255 * (t * t * (3 - 2 * t))))
    im = Image.composite(Image.new('RGB', (W, H), BG), im, grad.resize((W, H)))
    d = ImageDraw.Draw(im)
    small = ImageFont.truetype(REG, 28)
    d.text((X, 60), '@finaltoucch', font=small, fill='white')
    pw = d.textlength(page, font=small); d.text((W - X - pw, 60), page, font=small, fill='white')
    # outlined glowing lime number
    nf = ImageFont.truetype(BOLD, 230)
    lay = Image.new('L', (W, H)); ld = ImageDraw.Draw(lay)
    ld.text((X - 8, 718), num, font=nf, fill=0, stroke_width=7, stroke_fill=255)
    inner = Image.new('L', (W, H)); ImageDraw.Draw(inner).text((X - 8, 718), num, font=nf, fill=255)
    from PIL import ImageChops
    ring = ImageChops.subtract(lay, inner)
    glow = ring.filter(ImageFilter.GaussianBlur(10)).point(lambda v: int(v * 0.8))
    im.paste(Image.new('RGB', (W, H), LIME), (0, 0), glow); im.paste(Image.new('RGB', (W, H), LIME), (0, 0), ring)
    hf = ImageFont.truetype(BOLD, 88); y = 975
    for line in head.split('|'):
        d.text((X, y), line, font=hf, fill='white'); y += 92
    bf = ImageFont.truetype(REG, 36); y += 30
    for line in body.split('|'):
        d.text((X, y), line, font=bf, fill=GREY); y += 46
    im.save(out, quality=93)

if __name__ == '__main__':
    main(*sys.argv[1:7])
