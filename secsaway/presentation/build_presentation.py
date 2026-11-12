"""Rebuilds the Figma 'Secsaway — Brand Presentation' (17 modules, 1920 wide) as HTML for PDF export.
Same photos, vector logo, fonts and coordinates as the Figma build."""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC, P2 = os.path.join(ROOT, "src"), os.path.join(ROOT, "photos-v2")
K = dict(navy='#0F2B46', tone='#1B4166', line='#2A4562', orange='#E8551C', ink='#14181C', concrete='#646C75',
         steel='#D5D9DD', paper='#F4F4F1', white='#FFFFFF', mute='#8FA3B6')
ICON_D = ("M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
          "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z")
with open(os.path.join(SRC, "wordmark.txt")) as f:
    wm_w, wm_cap = map(float, f.readline().split())
    WM_D = f.read().strip()
WMW = 60 * wm_w / wm_cap          # wordmark width at cap 60  (= 540.44)
LH_W, LV_H = 160 + WMW, 220       # lockup widths
WMG = f'<g transform="scale({60 / wm_cap:.6f})"><path d="{WM_D}" fill="__W"/></g>'


def _svg(vw, vh, body, width, extra=""):
    h = width * vh / vw
    return f'<svg width="{width:.2f}" height="{h:.2f}" viewBox="0 0 {vw:.2f} {vh}" style="display:block;overflow:visible" {extra}>{body}</svg>', h


def logo(kind, cx, cy, width, ic, wc, op=1, blend=None):
    if kind == "icon":
        s, h = _svg(120, 120, f'<path d="{ICON_D}" fill="{ic}"/>', width)
    elif kind == "h":
        s, h = _svg(LH_W, 120, f'<path d="{ICON_D}" fill="{ic}"/><g transform="translate(160,30)">{WMG.replace("__W", wc)}</g>', width)
    else:  # stacked
        s, h = _svg(WMW, LV_H, f'<g transform="translate({(WMW - 120) / 2:.2f},0)"><path d="{ICON_D}" fill="{ic}"/></g>'
                                f'<g transform="translate(0,160)">{WMG.replace("__W", wc)}</g>', width)
    bl = f"mix-blend-mode:{blend};" if blend else ""
    return f'<div class="a" style="left:{cx - width / 2:.2f}px;top:{cy - h / 2:.2f}px;opacity:{op};{bl}">{s}</div>'


def b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


PHOTOS = {}


def photo(fn, iw, ih, x, y, w, h, extra=""):
    if fn not in PHOTOS:
        PHOTOS[fn] = b64(os.path.join(P2, fn))
    s = max(w / iw, h / ih); ox, oy = (w - iw * s) / 2, (h - ih * s) / 2
    html = (f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden;{extra}">'
            f'<img src="{PHOTOS[fn]}" style="position:absolute;left:{ox:.2f}px;top:{oy:.2f}px;width:{iw * s:.2f}px;height:{ih * s:.2f}px"></div>')
    return html, (lambda fx, fy: (x + ox + fx * iw * s, y + oy + fy * ih * s))


def T(s, x, y, size=20, color=K['ink'], weight=400, fam="Archivo", ls=None, lh=None, w=None, align=None, upper=False, op=1, italic=False):
    st = f"left:{x}px;top:{y}px;font-family:'{fam}';font-size:{size}px;font-weight:{weight};color:{color};opacity:{op};"
    st += f"letter-spacing:{ls / 100}em;" if ls is not None else ""
    st += f"line-height:{lh}px;" if lh else "line-height:normal;"
    st += f"width:{w}px;" if w else "white-space:pre;"
    st += f"text-align:{align};" if align else ""
    st += "text-transform:uppercase;" if upper else ""
    return f'<div class="a" style="{st}">{s}</div>'


def mono(s, x, y, color, size=14, ls=10, upper=True, **kw):
    return T(s, x, y, size=size, color=color, weight=500, fam="IBM Plex Mono", ls=ls, upper=upper, **kw)


def R(x, y, w, h, fill, op=1, r=0, extra=""):
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{fill};opacity:{op};border-radius:{r}px;{extra}"></div>'


def module(name, h, bg, body):
    return f'<section class="m" data-name="{name}" style="height:{h}px;background:{bg}">{body}</section>'


M = []
# 01 HERO
p, at = photo('11_hero.jpg', 2688, 1520, 0, 0, 1920, 1080)
M.append(module('01_Hero', 1080, K['ink'], p + logo('h', 960, 330, 860, K['orange'], K['white'])
    + mono('Every handover is a promise.', 0, 470, K['white'], size=16, ls=16, w=1920, align='center', op=.9)
    + R(894, 518, 132, 36, 'transparent', r=18, extra=f"border:1.2px solid rgba(255,255,255,.7);box-sizing:border-box")
    + mono('EST. 2026', 894, 528, K['white'], size=13, w=132, align='center', op=.9)
    + mono('Secsaway Logistics Company', 80, 1020, K['white'], size=13, op=.75)
    + mono('Brand identity — 2026', 1640, 1020, K['white'], size=13, op=.75, w=200, align='right')))
# 02 INTRO
M.append(module('02_Intro', 760, K['paper'],
    mono('01 — About the brand', 160, 170, K['orange'])
    + T('Secsaway\nLogistics', 160, 210, 56, K['navy'], 600, ls=-2, lh=60)
    + T('Secsaway moves freight by road, sea and air, and handles the paperwork in between. The identity is built on one idea: the handover. Every time cargo changes hands, someone takes responsibility for it. The mark draws that moment as two identical routes meeting at one precise point.', 760, 170, 32, K['ink'], ls=-1, lh=46, w=1000)
    + R(760, 560, 1000, 1, K['steel'])
    + mono('Freight forwarding   ·   Haulage   ·   Warehousing   ·   Customs clearance   ·   Last mile', 760, 590, K['concrete'], size=13)))
# 03 CONSTRUCTION
LW = 1200; ux = LW / LH_W * 20; L = (1920 - LW) / 2; Tp = 540 - 3 * ux
g = ''.join(f'<line x1="0" y1="{y:.2f}" x2="1920" y2="{y:.2f}"/>' for y in (Tp, Tp + 1.5 * ux, Tp + 4.5 * ux, Tp + 6 * ux))
g += ''.join(f'<line x1="{x:.2f}" y1="0" x2="{x:.2f}" y2="1080"/>' for x in (L, L + 6 * ux, L + 8 * ux, L + LW))
g += f'<circle cx="{L + 1.75 * ux:.2f}" cy="{Tp + 1.75 * ux:.2f}" r="{1.75 * ux:.2f}"/><circle cx="{L + 4.25 * ux:.2f}" cy="{Tp + 4.25 * ux:.2f}" r="{1.75 * ux:.2f}"/>'
M.append(module('03_Logo_Construction', 1080, K['navy'],
    f'<svg class="a" style="left:0;top:0" width="1920" height="1080"><g fill="none" stroke="{K["line"]}" stroke-width="1.2" stroke-dasharray="6 6">{g}</g></svg>'
    + logo('h', 960, 540, LW, K['tone'], K['tone'])
    + mono('Logo construction — 6x grid, 1x stroke, 2x gap, 3x cap height', 80, 1020, K['mute'], size=13)))
# 04 PALETTE
p, at = photo('21_highway.jpg', 2688, 1520, 0, 0, 1920, 1080)
cols = [('Depot Navy', K['navy'], '15 43 70', '100 80 40 45', 'PMS 2965 C'), ('Signal Orange', K['orange'], '232 85 28', '0 75 95 0', 'PMS 1665 C'),
        ('Ink', K['ink'], '20 24 28', '75 65 60 85', 'PMS Black 6 C'), ('Concrete', K['concrete'], '100 108 117', '55 42 35 20', 'PMS Cool Gray 10 C'),
        ('Steel', K['steel'], '213 217 221', '15 10 8 0', 'PMS Cool Gray 1 C'), ('Paper', K['paper'], '244 244 241', '3 2 4 0', 'Uncoated white')]
cards = ''
for i, (n, h, rgb, cmyk, pms) in enumerate(cols):
    x = 240 + i * 244
    cards += R(x, 360, 220, 230, h) + R(x, 590, 220, 130, K['white']) + T(n, x + 16, 606, 16, K['ink'], 600)
    cards += T(f'HEX {h}\nRGB {rgb}\nCMYK {cmyk}\n{pms}', x + 16, 632, 11, K['concrete'], fam='IBM Plex Mono', lh=17)
M.append(module('04_Colour_Palette', 1080, K['ink'], p + R(0, 0, 1920, 1080, K['ink'], .25) + cards + mono('02 — Colour', 240, 300, K['white'], op=.85)))
# 05 TYPOGRAPHY
ws = [('Light', 300), ('Regular', 400), ('Medium', 500), ('SemiBold', 600), ('Bold', 700), ('ExtraBold', 800), ('Black', 900)]
b = ''
for i, (s, n) in enumerate(ws):
    y = 200 + i * 96
    b += mono(s, 160, y + 30, K['concrete'], size=12, ls=2, upper=False) + mono(str(n), 160, y + 50, K['concrete'], size=11, ls=2)
    b += T('Aa', 600, y + 16, 44, K['navy'], n) + R(160, y + 92, 520, 1, K['steel'])
b += R(860, 200, 150, 38, 'transparent', r=19, extra=f"border:1.2px solid {K['navy']};box-sizing:border-box") + mono('Typography', 860, 211, K['navy'], size=13, w=150, align='center')
b += T('Archivo', 852, 262, 150, K['navy'], 800, ls=-3)
b += T('Primary typeface for headlines, body text and interfaces. A grotesque with sturdy, slightly squared forms that reads clearly on vehicles at distance and on a phone in a moving cab. The wordmark is drawn from its ExtraBold weight.', 860, 470, 22, K['ink'], lh=34, w=820)
b += R(860, 650, 880, 1, K['steel']) + T('IBM Plex Mono', 860, 690, 48, K['navy'], 500, fam='IBM Plex Mono', ls=-2)
b += T('Secondary typeface for tracking numbers, weights, times and labels: anything a driver or clerk must read exactly.', 860, 770, 20, K['ink'], lh=30, w=820)
b += mono('SCW-2026-048213   ·   ETA 11:30   ·   1,240 KG   ·   LOS → IBA', 860, 870, K['orange'], size=15, ls=4)
M.append(module('05_Typography', 1080, K['paper'], b))
# 06 MARK & APP ICONS
b = R(0, 0, 960, 1080, K['paper'])
b += (f'<svg class="a" style="left:0;top:0" width="960" height="1080"><g fill="none" stroke="{K["steel"]}" stroke-width="1.2">'
      f'<rect x="240" y="300" width="480" height="480"/><circle cx="480" cy="540" r="240"/><line x1="240" y1="300" x2="720" y2="780"/><line x1="720" y1="300" x2="240" y2="780"/></g></svg>')
b += logo('icon', 480, 540, 290, K['navy'], K['navy']) + mono('Mark — 6x grid', 240, 830, K['concrete'], size=12)
for i, (bg, ic, st, l) in enumerate([(K['paper'], K['orange'], None, 'Light'), (K['navy'], K['orange'], K['mute'], 'Outline'), (K['orange'], K['navy'], None, 'Signal')]):
    x = 1148 + i * 216
    b += R(x, 452, 176, 176, bg, r=40, extra=(f"border:2px solid rgba(143,163,182,.6);box-sizing:border-box" if st else ""))
    b += logo('icon', x + 88, 540, 92, ic, ic) + mono(l, x, 652, K['mute'], size=12, w=176, align='center')
M.append(module('06_Mark_App_Icons', 1080, K['navy'], b))
# 07 WORDMARK
M.append(module('07_Wordmark', 760, K['ink'], logo('h', 960, 380, 1060, K['orange'], K['white'])))
# 08 APP
p, at = photo('24_phone.jpg', 1792, 2240, 960, 0, 960, 1080)
(x0, y0), (x1, y1) = at(0.307, 0.147), at(0.689, 0.799)
SW, SH = x1 - x0, y1 - y0
ui = R(0, 0, SW, SH * .40, K['navy']) + mono('06:42', 22, 18, K['white'], size=11, ls=2)
ui += logo('icon', 34, 72, 26, K['orange'], K['orange']) + mono('Shipment', 22, 110, K['mute'], size=10)
ui += mono('SCW-2026-048213', 22, 128, K['white'], size=14, ls=2) + T('Arriving today', 22, 170, 28, K['white'], 800, ls=-2)
ui += T('Estimated 11:30 – 12:00', 22, 208, 13, '#C3CED8')
for i, (t, d, done) in enumerate([('Picked up', 'Apapa depot · 06:40', 1), ('In transit', 'Lagos–Ibadan expressway', 1), ('Out for delivery', 'Driver assigned', 0), ('Delivered', 'Signature on handover', 0)]):
    y = SH * .40 + 34 + i * 66
    ui += R(24, y, 14, 14, K['orange'] if done else K['steel'], r=7)
    if i < 3:
        ui += R(30, y + 14, 2, 52, K['orange'] if i == 0 else K['steel'])
    ui += T(t, 54, y - 3, 15, K['navy'] if done else K['concrete'], 600) + mono(d, 54, y + 18, K['concrete'], size=10, ls=1, upper=False)
ui += R(22, SH - 70, SW - 44, 48, K['navy']) + T('Contact driver', 22, SH - 55, 14, K['white'], 600, w=SW - 44, align='center')
M.append(module('08_App', 1080, K['navy'], R(370, 430, 220, 220, K['paper'], r=52) + logo('icon', 480, 540, 116, K['orange'], K['orange'])
    + mono('App icon — iOS / Android', 260, 690, K['mute'], size=12, w=440, align='center') + p
    + f'<div class="a" style="left:{x0:.2f}px;top:{y0:.2f}px;width:{SW:.2f}px;height:{SH:.2f}px;border-radius:34px;overflow:hidden;background:{K["paper"]}">{ui}</div>'))
# 09 CAMPAIGN
p, at = photo('26_driver.jpg', 2688, 1520, 0, 0, 1920, 1080)
M.append(module('09_Campaign', 1080, K['ink'], p + logo('h', 390, 420, 460, K['orange'], K['white'])
    + T('Freight that arrives\nwhen we said it would.', 160, 500, 46, K['white'], 600, ls=-2, lh=54)
    + mono('Campaign — Out of home', 160, 1020, K['white'], size=13, op=.7)))
# 10 VALUES & MUG
b = ''
for i, w in enumerate(['Collect', 'Sort', 'Route', 'Handover', 'Track', 'Deliver', 'Confirm']):
    on = w == 'Handover'
    b += T(('+ ' if on else '') + w, 148 if on else 190, 190 + i * 92, 62, K['ink'] if on else '#B9BFC5', 600 if on else 500, ls=-2)
p, at = photo('23_mug_cab.jpg', 1792, 2240, 960, 0, 960, 1080)
mx, my = at(0.525, 0.53)
M.append(module('10_Values_Mug', 1080, K['paper'], b + logo('icon', 830, 960, 40, K['navy'], K['navy']) + p + logo('icon', mx, my, 118, K['orange'], K['orange'], .95)))
# 11 SHIPMENT CARD
p, at = photo('25_port.jpg', 2688, 1520, 0, 0, 1920, 1080)
cx, cy = 700, 220
b = p + R(cx, cy, 520, 640, K['white']) + R(cx + 16, cy + 16, 488, 330, K['navy']) + logo('icon', cx + 52, cy + 52, 30, K['orange'], K['orange'])
b += mono('Live route', cx + 370, cy + 44, K['mute'], size=11)
b += (f'<svg class="a" style="left:{cx + 50}px;top:{cy + 100}px;overflow:visible" width="400" height="220"><path d="M 0 220 L 120 220 C 170 220 170 140 120 140 L 80 140 C 30 140 30 60 80 60 L 260 60 C 310 60 340 20 400 10" fill="none" stroke="{K["orange"]}" stroke-width="4" stroke-linecap="round"/></svg>')
b += R(cx + 42, cy + 312, 16, 16, K['white'], r=8) + R(cx + 442, cy + 102, 16, 16, K['orange'], r=8)
for i, (k, v) in enumerate([('Shipment', 'SCW-048213'), ('Origin', 'Apapa, Lagos'), ('Destination', 'Ibadan'), ('Distance', '128 km'), ('ETA', '11:30'), ('Weight', '1,240 kg')]):
    x, y = cx + 32 + (i % 3) * 160, cy + 384 + (i // 3) * 110
    b += mono(k, x, y, K['concrete'], size=11, ls=4) + T(v, x, y + 24, 19, K['navy'], 600)
b += R(cx + 32, cy + 592, 456, 1, K['steel']) + mono('Status — In transit', cx + 32, cy + 606, K['orange'], size=11)
M.append(module('11_Shipment_Card', 1080, K['ink'], b))
# 12 HANDOVER
p, at = photo('22_handover.jpg', 2688, 1520, 0, 0, 1920, 1080)
bx, by = at(0.50, 0.46)
M.append(module('12_Parcel_Handover', 1080, K['ink'], p + logo('h', bx, by, 560, '#1A2A3A', '#1A2A3A', .88, 'multiply')
    + mono('Packaging — 1-colour flexo on kraft', 80, 1020, K['white'], size=13, op=.8)))
# 13 STORIES
b = mono('Social — Stories 9:16', 160, 120, K['concrete'], size=12)
for i, (fn, t) in enumerate([('25_port.jpg', 'Cleared.\nLoaded.\nOn its way.'), ('11_hero.jpg', ''), ('21_highway.jpg', '128 km\nLagos → Ibadan')]):
    sp, _ = photo(fn, 2688, 1520, 0, 0, 340, 604)
    inner = sp + R(0, 0, 340, 604, K['ink'], .25) + R(16, 14, 308, 3, K['white'], .5, 2) + R(16, 14, 308 * (i + 1) / 3, 3, K['white'], 1, 2)
    inner += logo('icon', 36, 46, 24, K['orange'], K['orange']) + mono('secsaway', 58, 38, K['white'], size=11, ls=2, upper=False)
    if i == 1:
        inner += logo('v', 170, 282, 220, K['orange'], K['white']) + mono('Track every handover', 0, 372, K['white'], size=11, w=340, align='center')
    else:
        inner += T(t, 24, 414, 34, K['white'], 800, ls=-2, lh=38)
    inner += R(20, 542, 300, 42, 'transparent', r=21, extra="border:1px solid rgba(255,255,255,.6);box-sizing:border-box")
    inner += mono('Send message', 36, 555, K['white'], size=10, ls=2, upper=False, op=.8)
    b += f'<div class="a" style="left:{390 + i * 400}px;top:238px;width:340px;height:604px;border-radius:22px;overflow:hidden">{inner}</div>'
M.append(module('13_Social_Stories', 1080, K['paper'], b))
# 14 HOODIE
p1, a1 = photo('12_hoodie_back.jpg', 1792, 2240, 0, 0, 960, 1200)
p2, a2 = photo('13_label.jpg', 1792, 2240, 960, 0, 960, 1200)
M.append(module('14_Merch_Hoodie', 1200, K['ink'], p1 + logo('v', *a1(0.49, 0.395), 200, K['orange'], '#EDEFF0', .9)
    + p2 + logo('icon', *a2(0.49, 0.565), 118, '#122B44', '#122B44', .9, 'multiply')
    + mono('Heavyweight hoodie — screen print, back', 40, 1150, K['white'], size=13, op=.8) + mono('Woven hem label', 1000, 1150, K['white'], size=13, op=.8)))
# 15 TOTE
p, at = photo('14_tote.jpg', 2688, 1520, 0, 0, 1920, 1080)
M.append(module('15_Merch_Tote', 1080, K['ink'], p + logo('v', *at(0.598, 0.60), 300, '#122B44', '#122B44', .9, 'multiply')
    + mono('Canvas tote — 1-colour print', 80, 1020, K['white'], size=13, op=.8)))
# 16 CAP & VEST
p1, a1 = photo('15_cap_hands.jpg', 1792, 2240, 0, 0, 960, 1200)
p2, a2 = photo('16_vest_back.jpg', 1792, 2240, 960, 0, 960, 1200)
M.append(module('16_Merch_Cap_HiVis', 1200, K['ink'], p1 + logo('icon', *a1(0.495, 0.355), 92, K['orange'], K['orange'], .95)
    + p2 + logo('v', *a2(0.50, 0.475), 190, '#122B44', '#122B44', .92, 'multiply')
    + mono('Twill cap — embroidered mark', 40, 1150, K['white'], size=13, op=.8) + mono('Hi-vis vest, Class 2 — printed back', 1000, 1150, K['white'], size=13, op=.8)))
# 17 CLOSING
M.append(module('17_Closing', 820, K['navy'], logo('v', 960, 380, 420, K['orange'], K['white'])
    + mono('Secsaway Logistics Company — Brand identity 2026', 0, 700, K['mute'], size=13, w=1920, align='center')))


def font_faces():
    out = []
    for w in (300, 400, 500, 600, 700, 800, 900):
        out.append((f"Archivo", w, f"Archivo{w}"))
    out += [("IBM Plex Mono", 400, "IBMPlexMono400"), ("IBM Plex Mono", 500, "IBMPlexMono500")]
    return "\n".join(f"@font-face{{font-family:'{f}';font-weight:{w};src:url(data:font/ttf;base64,"
                     f"{base64.b64encode(open(os.path.join(SRC, fn + '.ttf'), 'rb').read()).decode()}) format('truetype');}}" for f, w, fn in out)


CSS = "*{box-sizing:border-box;margin:0;padding:0}body{background:#14181C}.m{width:1920px;position:relative;overflow:hidden}.a{position:absolute}"
open(os.path.join(HERE, "presentation.html"), "w").write(
    f'<!doctype html><html><head><meta charset="utf-8"><title>Secsaway Brand Presentation</title><style>{font_faces()}{CSS}</style></head>'
    f'<body>{"".join(M)}<script>document.fonts.ready.then(()=>document.body.dataset.ready=1)</script></body></html>')
print(len(M), "modules")
