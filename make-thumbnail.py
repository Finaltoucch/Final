import subprocess, glob, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

SRC = sys.argv[1]          # source clip
OUT = sys.argv[2]          # output png
TIMES = [2.5, 4, 5.5, 7, 8.5, 10, 11]

for i, t in enumerate(TIMES):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", SRC,
                    "-frames:v", "1", f"c{i}.png"], check=False)

# --- pick the frame with the largest detected face -------------------------
best = None   # (area, path, x, y, w, h)
try:
    import cv2
    cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    prof = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
    for p in sorted(glob.glob("c*.png")):
        im = cv2.imread(p)
        if im is None:
            continue
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        g = cv2.equalizeHist(g)
        found = list(cas.detectMultiScale(g, 1.08, 5, minSize=(80, 80)))
        found += list(prof.detectMultiScale(g, 1.08, 5, minSize=(80, 80)))
        # profile cascade only detects one facing direction — flip to catch the other
        gf = cv2.flip(g, 1)
        for (x, y, w, h) in prof.detectMultiScale(gf, 1.08, 5, minSize=(80, 80)):
            found.append((g.shape[1] - x - w, y, w, h))
        for (x, y, w, h) in found:
            a = w * h
            if best is None or a > best[0]:
                best = (a, p, x, y, w, h)
    print("DETECT", "hit" if best else "miss")
except Exception as e:
    print("DETECT unavailable:", e)

OW, OH = 1280, 720

if best:
    _, path, fx, fy, fw, fh = best
    img = Image.open(path).convert("RGB")
    IW, IH = img.size
    # size the crop so the face fills ~42% of the final height
    ch = min(IH, max(int(fh * 2.38), 320))
    cw = int(ch * OW / OH)
    if cw > IW:
        cw = IW
        ch = int(cw * OH / OW)
    fcx, fcy = fx + fw / 2, fy + fh / 2
    left = int(fcx - cw / 2)
    top = int(fcy - ch * 0.42)          # eyes near the upper third
    left = max(0, min(left, IW - cw))
    top = max(0, min(top, IH - ch))
    img = img.crop((left, top, left + cw, top + ch)).resize((OW, OH), Image.LANCZOS)
    face_cx = (fcx - left) * OW / cw
else:
    img = Image.open(sorted(glob.glob("c*.png"))[len(TIMES) // 2]).convert("RGB")
    img = img.resize((OW, OH), Image.LANCZOS)
    face_cx = OW * 0.35

# --- grade: lift the subject, deepen the surround --------------------------
img = ImageEnhance.Color(img).enhance(1.18)
img = ImageEnhance.Contrast(img).enhance(1.16)
img = ImageEnhance.Brightness(img).enhance(1.10)

vig = Image.new("L", (OW, OH), 0)
ImageDraw.Draw(vig).ellipse((-OW * 0.30, -OH * 0.42, OW * 1.30, OH * 1.42), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(150))
img = Image.composite(img, ImageEnhance.Brightness(img).enhance(0.52), vig)

# --- text block on whichever side the face is not ---------------------------
text_right = face_cx < OW / 2
scrim = Image.new("RGBA", (OW, OH), (0, 0, 0, 0))
sd = ImageDraw.Draw(scrim)
for i in range(OW // 2):
    a = int(165 * (i / (OW / 2)) ** 1.5)
    x = OW - 1 - i if text_right else i
    sd.line([(x, 0), (x, OH)], fill=(0, 0, 0, a))
img = Image.alpha_composite(img.convert("RGBA"), scrim)

def font(px):
    for pat in ("*Montserrat*Black*", "*Montserrat*ExtraBold*", "*Montserrat*Bold*",
                "*Metropolis*ExtraBold*", "*Metropolis*Bold*", "*DejaVuSans-Bold*"):
        for root in ("/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts")):
            m = glob.glob(os.path.join(root, "**", pat + ".ttf"), recursive=True)
            if m:
                return ImageFont.truetype(m[0], px)
    return ImageFont.load_default()

d = ImageDraw.Draw(img)
LIME = (204, 255, 0)
f1, f2 = font(190), font(104)

def draw(txt, fnt, cx, cy):
    b = d.textbbox((0, 0), txt, font=fnt)
    x, y = cx - (b[2] - b[0]) / 2 - b[0], cy - (b[3] - b[1]) / 2 - b[1]
    for ox in (-4, 0, 4):
        for oy in (-4, 0, 4):
            d.text((x + ox, y + oy), txt, font=fnt, fill=(0, 0, 0, 210))
    d.text((x, y), txt, font=fnt, fill=LIME)

tx = OW * 0.735 if text_right else OW * 0.265
draw("£850", f1, tx, OH * 0.40)
draw("A MONTH", f2, tx, OH * 0.575)

img.convert("RGB").save(OUT, quality=95)
print("WROTE", OUT, os.path.getsize(OUT))
