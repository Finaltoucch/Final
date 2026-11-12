"""Builds two A4 Secsaway flyers as one HTML file (rendered to PDF/JPEG by render_flyers.js)."""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "src")
PH = os.path.join(ROOT, "photos-v2")

NAVY, ORANGE, INK, CONCRETE, STEEL, PAPER, WHITE, MUTE = (
    "#0F2B46", "#E8551C", "#14181C", "#646C75", "#D5D9DD", "#F4F4F1", "#FFFFFF", "#8FA3B6")
KRAFT_INK = "#1A2A3A"

ICON_D = ("M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
          "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z")
with open(os.path.join(SRC, "wordmark.txt")) as f:
    wm_w, wm_cap = map(float, f.readline().split())
    WM_D = f.read().strip()
LOCK_W = 120 + 40 + 60 * wm_w / wm_cap  # lockup width in 120-high units


def icon_svg(size, color, style=""):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 120 120" style="{style}"><path d="{ICON_D}" fill="{color}"/></svg>'


def lockup_svg(width, icon_c, wm_c, style=""):
    h = width * 120 / LOCK_W
    s = 60 / wm_cap
    return (f'<svg width="{width:.1f}" height="{h:.1f}" viewBox="0 0 {LOCK_W:.2f} 120" style="{style}">'
            f'<path d="{ICON_D}" fill="{icon_c}"/>'
            f'<g transform="translate(160,30) scale({s:.6f})"><path d="{WM_D}" fill="{wm_c}"/></g></svg>')


ICONS = {
    "Road haulage": '<path d="M9 33H4V11H30V33H17 M30 17H38L44 24V33H41 M33 33H30"/><circle cx="13" cy="34" r="4"/><circle cx="37" cy="34" r="4"/>',
    "Sea freight": '<path d="M4 30H44L38 41H10Z M12 30V21H22V30 M22 30V14H32V30 M32 30V21H38V30"/>',
    "Air freight": '<path d="M24 4C26 4 27 6 27 9V18L44 28V32L27 26V36L32 40V43L24 41L16 43V40L21 36V26L4 32V28L21 18V9C21 6 22 4 24 4Z"/>',
    "Warehousing": '<path d="M6 19L24 7L42 19V41H6Z M14 41V26H34V41 M14 31.5H34"/>',
    "Customs clearance": '<path d="M10 4H30L38 12V44H10Z M30 4V12H38 M16 19H32 M16 25H32 M16 31H23"/><circle cx="30" cy="35" r="5"/>',
    "Last-mile delivery": '<path d="M8 15L24 7L40 15V33L24 41L8 33Z M8 15L24 23L40 15 M24 23V41 M16 11L32 19"/>',
}


def line_icon(name, size, color):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" stroke="{color}" stroke-width="3" '
            f'stroke-linejoin="round">{ICONS[name]}</svg>')


def b64(fn):
    return "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(PH, fn), "rb").read()).decode()


def font_face():
    out = []
    for fam, w, fn in [("Archivo", 400, "Archivo400"), ("Archivo", 500, "Archivo500"), ("Archivo", 600, "Archivo600"),
                       ("Archivo", 800, "Archivo800"), ("IBM Plex Mono", 400, "IBMPlexMono400"), ("IBM Plex Mono", 500, "IBMPlexMono500")]:
        b = base64.b64encode(open(os.path.join(SRC, fn + ".ttf"), "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/ttf;base64,{b}) format('truetype');}}")
    return "\n".join(out)


# Contact placeholders: replace before printing.
PHONE, EMAIL, WEB, ADDR = "+000 000 000 0000", "hello@secsaway.com", "secsaway.com", "[Head office address]"

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #777; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.fl { width: 1240px; height: 1754px; position: relative; overflow: hidden; font-family: 'Archivo', sans-serif; page-break-after: always; }
.fl:last-child { page-break-after: auto; }
.mono { font-family: 'IBM Plex Mono', monospace; font-weight: 500; text-transform: uppercase; letter-spacing: .12em; }
.abs { position: absolute; }
.ph { position: absolute; overflow: hidden; }
.ph img { position: absolute; display: block; }
"""

# ---------- Flyer 1: Every handover is a promise (light) ----------
# handover photo 2688x1520 shown 1000px high -> scale .65789, width 1768.4, offset -264.2
s1 = 1000 / 1520
w1 = 2688 * s1
ox1 = (1240 - w1) / 2
box_x, box_y = ox1 + 0.50 * w1, 0.46 * 1000
lk_w = 516
lk_h = lk_w * 120 / LOCK_W
services = '<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:28px">' + "".join(
    f'<div style="padding:26px 0 30px;border-top:1.5px solid {STEEL}">'
    f'{line_icon(n, 48, NAVY)}<div style="font-size:22px;font-weight:600;color:{NAVY};letter-spacing:-.01em;margin-top:16px;line-height:1.2">{n}</div></div>'
    for n in ICONS) + '</div>'
flyer1 = f'''
<section class="fl" style="background:{PAPER}">
  <div class="ph" style="left:0;top:0;width:1240px;height:1000px">
    <img src="{b64('22_handover.jpg')}" style="left:{ox1:.1f}px;top:0;width:{w1:.1f}px;height:1000px">
    <div class="abs" style="left:{box_x - lk_w/2:.1f}px;top:{box_y - lk_h/2:.1f}px;mix-blend-mode:multiply;opacity:.88">{lockup_svg(lk_w, KRAFT_INK, KRAFT_INK)}</div>
  </div>
  <div class="abs" style="left:0;top:0;width:1240px;height:92px;background:{NAVY};display:flex;align-items:center;justify-content:space-between;padding:0 72px">
    {lockup_svg(230, ORANGE, WHITE)}
    <span class="mono" style="font-size:14px;color:{MUTE}">Road · Sea · Air · Customs</span>
  </div>
  <div class="abs" style="left:72px;top:1060px;width:600px">
    <div class="mono" style="font-size:15px;color:{ORANGE}">Logistics, handled end to end</div>
    <h1 style="font-size:86px;line-height:.98;font-weight:800;letter-spacing:-.035em;color:{NAVY};margin-top:26px">Every<br>handover<br>is a promise.</h1>
    <p style="font-size:23px;line-height:1.5;color:#3A424A;margin-top:34px;max-width:540px">From collection to signature, one team owns your shipment. Every scan, seal and signature is recorded, so you always know where your goods are and who has them.</p>
  </div>
  <div class="abs" style="left:720px;top:1072px;width:448px">
    <div class="mono" style="font-size:13px;color:{CONCRETE};margin-bottom:12px">Our services</div>
    {services}
  </div>
  <div class="abs" style="left:0;top:1586px;width:1240px;height:168px;background:{NAVY};border-top:8px solid {ORANGE};display:flex;align-items:center;justify-content:space-between;padding:0 72px">
    <div>
      <div style="font-size:30px;font-weight:600;color:{WHITE};letter-spacing:-.015em">Request a quote today</div>
      <div class="mono" style="font-size:15px;color:{MUTE};margin-top:12px;letter-spacing:.06em">{PHONE} &nbsp;·&nbsp; {EMAIL} &nbsp;·&nbsp; {WEB}</div>
    </div>
    {icon_svg(76, ORANGE)}
  </div>
</section>'''

# ---------- Flyer 2: Track every handover (dark) ----------
# driver photo 2688x1520 shown 860px high, right-aligned so the dark left area holds the type
s2 = 860 / 1520
w2 = 2688 * s2
ox2 = 1240 - w2
# phone photo 1792x2240 shown 520 wide
pw = 520
ph_s = pw / 1792
phh = 2240 * ph_s
sx0, sy0, sx1, sy1 = .307 * pw, .147 * phh, .689 * pw, .799 * phh
UIW, UIH = 367, 783
k = (sx1 - sx0) / UIW
steps_ui = "".join(
    f'''<div style="display:flex;gap:16px;position:relative;height:66px">
      <div style="width:14px;height:14px;border-radius:7px;background:{ORANGE if d else STEEL};margin-top:4px;flex:none"></div>
      {f'<div style="position:absolute;left:6px;top:18px;width:2px;height:52px;background:{ORANGE if i == 0 else STEEL}"></div>' if i < 3 else ''}
      <div><div style="font-size:15px;font-weight:600;color:{NAVY if d else CONCRETE}">{t}</div>
      <div style="font:400 10px 'IBM Plex Mono';color:{CONCRETE};margin-top:5px">{sub}</div></div></div>'''
    for i, (t, sub, d) in enumerate([("Picked up", "Apapa depot · 06:40", 1), ("In transit", "Lagos–Ibadan expressway", 1),
                                      ("Out for delivery", "Driver assigned", 0), ("Delivered", "Signature on handover", 0)]))
ui = f'''<div style="position:absolute;left:{sx0:.1f}px;top:{sy0:.1f}px;width:{UIW}px;height:{UIH}px;transform:scale({k:.4f});transform-origin:0 0;border-radius:34px;overflow:hidden;background:{PAPER}">
  <div style="height:313px;background:{NAVY};padding:18px 22px;position:relative">
    <div class="mono" style="font-size:11px;color:{WHITE};letter-spacing:.06em">06:42</div>
    <div style="margin-top:28px">{icon_svg(26, ORANGE)}</div>
    <div class="mono" style="font-size:10px;color:{MUTE};margin-top:12px">Shipment</div>
    <div class="mono" style="font-size:14px;color:{WHITE};margin-top:6px;letter-spacing:.04em">SCW-2026-048213</div>
    <div style="font-size:28px;font-weight:800;color:{WHITE};letter-spacing:-.02em;margin-top:22px">Arriving today</div>
    <div style="font-size:13px;color:#C3CED8;margin-top:6px">Estimated 11:30 – 12:00</div>
  </div>
  <div style="padding:34px 24px 0">{steps_ui}</div>
  <div style="position:absolute;left:22px;right:22px;bottom:22px;height:48px;background:{NAVY};color:{WHITE};font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center">Contact driver</div>
</div>'''
proc = "".join(
    f'''<div style="display:grid;grid-template-columns:64px 1fr;padding:24px 0;border-top:1.5px solid #2A4562">
      <span class="mono" style="font-size:16px;color:{ORANGE};padding-top:4px">0{i+1}</span>
      <div><div style="font-size:27px;font-weight:600;color:{WHITE};letter-spacing:-.015em">{t}</div>
      <div style="font-size:18px;line-height:1.45;color:#C3CED8;margin-top:6px">{d}</div></div></div>'''
    for i, (t, d) in enumerate([("Book", "Request a pickup online or by phone."),
                                ("Collect", "A uniformed driver scans and seals your goods."),
                                ("Track live", "Follow every stage from your phone."),
                                ("Signed handover", "Delivery is confirmed with a signature and photo.")]))
flyer2 = f'''
<section class="fl" style="background:{NAVY}">
  <div class="ph" style="left:0;top:0;width:1240px;height:860px">
    <img src="{b64('26_driver.jpg')}" style="left:{ox2:.1f}px;top:0;width:{w2:.1f}px;height:860px">
  </div>
  <div class="abs" style="left:72px;top:84px">{lockup_svg(300, ORANGE, WHITE)}</div>
  <div class="abs" style="left:72px;top:520px;width:600px">
    <h1 style="font-size:74px;line-height:1.0;font-weight:800;letter-spacing:-.035em;color:{WHITE}">Freight that<br>arrives when<br>we said it would.</h1>
  </div>
  <div class="ph" style="left:72px;top:932px;width:{pw}px;height:{phh:.0f}px;max-height:640px">
    <img src="{b64('24_phone.jpg')}" style="left:0;top:0;width:{pw}px;height:{phh:.1f}px">
    {ui}
  </div>
  <div class="abs" style="left:656px;top:924px;width:512px">
    <div class="mono" style="font-size:14px;color:{ORANGE}">How it works</div>
    <h2 style="font-size:46px;line-height:1.04;font-weight:800;letter-spacing:-.03em;color:{WHITE};margin:18px 0 26px">Track every<br>handover.</h2>
    {proc}
  </div>
  <div class="abs" style="left:0;top:1586px;width:1240px;height:168px;background:{ORANGE};display:flex;align-items:center;justify-content:space-between;padding:0 72px">
    <div>
      <div style="font-size:32px;font-weight:800;color:{INK};letter-spacing:-.02em">Book your first shipment</div>
      <div class="mono" style="font-size:15px;color:{INK};margin-top:12px;letter-spacing:.06em">{PHONE} &nbsp;·&nbsp; {WEB}</div>
    </div>
    {icon_svg(76, NAVY)}
  </div>
</section>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>Secsaway Flyers</title>
<style>{font_face()}{CSS}</style></head><body>{flyer1}{flyer2}</body></html>'''
open(os.path.join(HERE, "flyers.html"), "w").write(html)
print("ok", round(k, 4), round(phh))
