"""Builds the Secsaway brand book (HTML) and the standalone logo SVGs."""
import base64, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

# ---------- Palette ----------
NAVY, ORANGE, INK, CONCRETE, STEEL, PAPER, WHITE = (
    "#0F2B46", "#E8551C", "#14181C", "#646C75", "#D5D9DD", "#F4F4F1", "#FFFFFF")
NAVY_TONE = "#16395A"   # pattern tone on navy (navy +8% white)
KRAFT = "#C8A57A"       # packaging substrate, not a brand colour

# ---------- Geometry ----------
# Icon: 6x by 6x, x = 20 units. Two identical strokes, rotated 180 degrees, 1x gap at centre.
TOP_D = "M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
BOT_D = "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z"
ICON_D = TOP_D + BOT_D

wm_w, wm_cap, WM_D = None, None, None
with open(os.path.join(HERE, "wordmark.txt")) as f:
    a, b = f.readline().split()
    wm_w, wm_cap = float(a), float(b)
    WM_D = f.read().strip()
WM_RATIO = wm_w / wm_cap  # width per unit cap height


def icon(x, y, size, fill, extra=""):
    s = size / 120
    return f'<g transform="translate({x:.2f},{y:.2f}) scale({s:.5f})" {extra}><path d="{ICON_D}" fill="{fill}"/></g>'


def icon_r(x, y, size, fill):
    s = size / 120
    return f'<g transform="translate({x:.2f},{y:.2f}) rotate(90 {size/2:.2f} {size/2:.2f}) scale({s:.5f})"><path d="{ICON_D}" fill="{fill}"/></g>'


def wm(x, y, cap, fill):
    s = cap / wm_cap
    return f'<g transform="translate({x:.2f},{y:.2f}) scale({s:.5f})"><path d="{WM_D}" fill="{fill}"/></g>'


def lockup_h(x, y, h, ic, wc):
    u = h / 6
    return icon(x, y, h, ic) + wm(x + h + 2 * u, y + 1.5 * u, 3 * u, wc)


def lockup_h_w(h):
    u = h / 6
    return h + 2 * u + 3 * u * WM_RATIO


def lockup_v(x, y, w, ic, wc):
    """Stacked lockup, w = wordmark width."""
    cap = w / WM_RATIO
    u = cap / 3
    return icon(x + (w - 6 * u) / 2, y, 6 * u, ic) + wm(x, y + 8 * u, cap, wc)


def svg(w, h, body, cls="", style=""):
    return f'<svg class="{cls}" style="{style}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


# ---------- Icon set (48 grid, 3 stroke) ----------
ICONS = {
    "Shipment": '<path d="M8 15L24 7L40 15V33L24 41L8 33Z M8 15L24 23L40 15 M24 23V41 M16 11L32 19"/>',
    "Warehouse": '<path d="M6 19L24 7L42 19V41H6Z M14 41V26H34V41 M14 31.5H34"/>',
    "Truck": '<path d="M9 33H4V11H30V33H17 M30 17H38L44 24V33H41 M33 33H30"/><circle cx="13" cy="34" r="4"/><circle cx="37" cy="34" r="4"/>',
    "Container": '<rect x="4" y="12" width="40" height="24"/><path d="M12 17V31 M20 17V31 M28 17V31 M36 17V31"/>',
    "Air freight": '<path d="M24 4C26 4 27 6 27 9V18L44 28V32L27 26V36L32 40V43L24 41L16 43V40L21 36V26L4 32V28L21 18V9C21 6 22 4 24 4Z"/>',
    "Sea freight": '<path d="M4 30H44L38 41H10Z M12 30V21H22V30 M22 30V14H32V30 M32 30V21H38V30"/>',
    "Tracking": '<path d="M24 44C24 44 10 30 10 19A14 14 0 0 1 38 19C38 30 24 44 24 44Z"/><circle cx="24" cy="19" r="5"/>',
    "On time": '<circle cx="24" cy="24" r="18"/><path d="M24 13V24L32 29"/>',
    "Customs": '<path d="M10 4H30L38 12V44H10Z M30 4V12H38 M16 19H32 M16 25H32 M16 31H23"/><circle cx="30" cy="35" r="5"/>',
    "Pallet": '<path d="M4 19H44V25H4Z M4 34H44V40H4Z M7 25V34 M21 25V34 M27 25V34 M41 25V34"/>',
    "Route": '<path d="M10 40H27A8 8 0 0 0 27 24H21A8 8 0 0 1 21 8H38"/><circle cx="6.5" cy="40" r="3.5"/><circle cx="41.5" cy="8" r="3.5"/>',
    "Secure parcel": '<path d="M6 13H32V27 M6 13V39H24 M6 21H32 M19 13V21"/><rect x="27" y="29" width="17" height="13"/><path d="M30.5 29V25A5 5 0 0 1 40.5 25V29"/>',
}


def ic48(name, x, y, size, color, sw=3):
    s = size / 48
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="butt">{ICONS[name]}</g>')


# ---------- Patterns ----------
DEFS = f'''<svg width="0" height="0" style="position:absolute"><defs>
<pattern id="patA" width="280" height="280" patternUnits="userSpaceOnUse">{icon(0,0,120,NAVY_TONE)}{icon_r(140,0,120,NAVY_TONE)}{icon_r(0,140,120,NAVY_TONE)}{icon(140,140,120,NAVY_TONE)}</pattern>
<pattern id="patA-paper" width="280" height="280" patternUnits="userSpaceOnUse">{icon(0,0,120,STEEL)}{icon_r(140,0,120,STEEL)}{icon_r(0,140,120,STEEL)}{icon(140,140,120,STEEL)}</pattern>
<pattern id="patA-small" width="70" height="70" patternUnits="userSpaceOnUse">{icon(0,0,30,NAVY_TONE)}{icon_r(35,0,30,NAVY_TONE)}{icon_r(0,35,30,NAVY_TONE)}{icon(35,35,30,NAVY_TONE)}</pattern>
<pattern id="patB" width="480" height="480" patternUnits="userSpaceOnUse">
  <g transform="translate(40,40) scale(1.5)"><path d="{TOP_D}" fill="{STEEL}"/></g>
  <g transform="translate(260,260) scale(1.5)"><path d="{BOT_D}" fill="{STEEL}"/></g>
</pattern>
<pattern id="patB-navy" width="480" height="480" patternUnits="userSpaceOnUse">
  <g transform="translate(40,40) scale(1.5)"><path d="{TOP_D}" fill="{NAVY_TONE}"/></g>
  <g transform="translate(260,260) scale(1.5)"><path d="{BOT_D}" fill="{NAVY_TONE}"/></g>
</pattern>

<pattern id="tapeText" width="420" height="44" patternUnits="userSpaceOnUse">
  {icon(14,10,24,INK)}<text x="52" y="29" font-family="IBM Plex Mono" font-weight="500" font-size="14" letter-spacing="2" fill="{INK}">SECSAWAY · HANDLE WITH CARE ·</text>
</pattern>
<pattern id="busy" width="40" height="40" patternUnits="userSpaceOnUse">
  <rect width="40" height="40" fill="#8A9AA8"/><path d="M0 40L40 0" stroke="#B8C2CA" stroke-width="10"/>
</pattern>
<filter id="glow"><feDropShadow dx="6" dy="8" stdDeviation="6" flood-color="#000" flood-opacity=".45"/></filter>
</defs></svg>'''


def font_face():
    out = []
    for fam, w, fn in [("Archivo", 400, "Archivo400"), ("Archivo", 500, "Archivo500"), ("Archivo", 600, "Archivo600"),
                       ("Archivo", 800, "Archivo800"), ("IBM Plex Mono", 400, "IBMPlexMono400"),
                       ("IBM Plex Mono", 500, "IBMPlexMono500")]:
        b = base64.b64encode(open(os.path.join(HERE, fn + ".ttf"), "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:normal;src:url(data:font/ttf;base64,{b}) format('truetype');}}")
    return "\n".join(out)


CSS = """
@page { size: 1920px 1080px; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #888; }
body { font-family: 'Archivo', sans-serif; color: %(INK)s; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.slide { width: 1920px; height: 1080px; position: relative; overflow: hidden; background: %(PAPER)s; page-break-after: always; break-after: page; }
.slide:last-child { page-break-after: auto; break-after: auto; }
.dark { background: %(NAVY)s; color: %(WHITE)s; }
.hd, .ft { position: absolute; left: 120px; right: 120px; display: flex; justify-content: space-between;
  font: 500 13px/1 'IBM Plex Mono', monospace; letter-spacing: .1em; text-transform: uppercase; color: %(CONCRETE)s; }
.hd { top: 60px; z-index: 5; } .ft { bottom: 56px; z-index: 5; } .rule { z-index: 5; }
.dark .hd, .dark .ft { color: #8FA3B6; }
.hd b { color: %(INK)s; font-weight: 500; } .dark .hd b { color: %(WHITE)s; }
.rule { position: absolute; left: 120px; right: 120px; top: 96px; height: 1px; background: %(STEEL)s; }
.dark .rule { background: #2A4562; }
.c { position: absolute; left: 120px; right: 120px; top: 168px; bottom: 140px; }
.label { font: 500 13px/1.4 'IBM Plex Mono', monospace; letter-spacing: .1em; text-transform: uppercase; color: %(ORANGE)s; }
h1 { font-weight: 800; font-size: 120px; line-height: .95; letter-spacing: -.035em; }
h2 { font-weight: 600; font-size: 56px; line-height: 1.04; letter-spacing: -.025em; color: %(NAVY)s; margin-top: 18px; }
.dark h2 { color: %(WHITE)s; }
h3 { font-weight: 600; font-size: 22px; line-height: 1.25; letter-spacing: -.01em; color: %(NAVY)s; }
.dark h3 { color: %(WHITE)s; }
p { font-size: 19px; line-height: 1.55; color: #3A424A; max-width: 560px; }
.dark p { color: #C3CED8; }
.lede { font-size: 22px; line-height: 1.5; margin-top: 24px; }
.small { font-size: 15px; line-height: 1.5; color: %(CONCRETE)s; }
.mono { font-family: 'IBM Plex Mono', monospace; }
.cap { font: 400 14px/1.45 'IBM Plex Mono', monospace; color: %(CONCRETE)s; margin-top: 14px; letter-spacing: .02em; }
.dark .cap { color: #8FA3B6; }
.grid { display: grid; grid-template-columns: repeat(12, 1fr); column-gap: 24px; height: 100%%; }
.l4 { grid-column: 1 / span 4; } .l5 { grid-column: 1 / span 5; }
.r7 { grid-column: 6 / span 7; } .r8 { grid-column: 5 / span 8; }
.tbl { width: 100%%; border-collapse: collapse; }
.tbl td, .tbl th { text-align: left; padding: 16px 0; border-top: 1px solid %(STEEL)s; vertical-align: baseline; }
.tbl th { font: 500 12px 'IBM Plex Mono', monospace; letter-spacing: .1em; text-transform: uppercase; color: %(CONCRETE)s; font-weight: 500; }
.n { font-family: 'IBM Plex Mono', monospace; font-size: 15px; color: %(CONCRETE)s; font-variant-numeric: tabular-nums; }
""" % dict(INK=INK, PAPER=PAPER, NAVY=NAVY, WHITE=WHITE, CONCRETE=CONCRETE, ORANGE=ORANGE, STEEL=STEEL)

TOTAL = 20
SECTIONS = {}


def slide(n, section, body, dark=False, chrome=True, bg=None):
    style = f' style="background:{bg}"' if bg else ""
    ch = ""
    if chrome:
        ch = (f'<div class="hd"><b>Secsaway — Brand Guidelines v1.0</b><span>{section}</span></div><div class="rule"></div>'
              f'<div class="ft"><span>Secsaway Logistics Company</span><span>{n:02d} / {TOTAL:02d}</span></div>')
    return f'<section class="slide{" dark" if dark else ""}" id="p{n}"{style}>{ch}{body}</section>'


pages = []
names = []

# 1 ---------- Cover
names.append("Cover")
pages.append(slide(1, "", f'''
<svg width="1920" height="1080" style="position:absolute;inset:0"><rect x="1100" y="0" width="820" height="1080" fill="url(#patA)"/></svg>
<div style="position:absolute;left:120px;top:120px">{svg(420,70, lockup_h(0,0,70,ORANGE,WHITE))}</div>
<div style="position:absolute;left:120px;bottom:120px">
  <div class="label">Brand Guidelines</div>
  <h1 style="margin-top:28px;color:#fff">Identity<br>Standards</h1>
  <p class="mono" style="margin-top:40px;font-size:15px;letter-spacing:.08em;color:#8FA3B6">VERSION 1.0 — 2026</p>
</div>''', dark=True, chrome=False))

# 2 ---------- Contents
names.append("Contents")
toc = [("01", "Brand foundation", "03"), ("02", "Logo", "04"), ("", "Concept", "05"), ("", "Construction", "06"),
       ("", "Clear space &amp; minimum size", "07"), ("", "Variations", "08"), ("", "Misuse", "09"),
       ("03", "Colour", "10"), ("04", "Typography", "11"), ("05", "Brand pattern", "12"), ("06", "Iconography", "13"),
       ("07", "Photography", "14"), ("08", "Applications", "15"), ("", "Stationery", "15"), ("", "Digital", "16"),
       ("", "Fleet &amp; signage", "17"), ("", "Packaging", "18"), ("", "Merchandise &amp; uniform", "19")]
rows = ""
for num, t, pg in toc:
    sub = num == ""
    rows += (f'<tr><td class="n" style="width:80px;padding:10px 0">{num}</td>'
             f'<td style="padding:10px 0;font-size:{19 if sub else 24}px;font-weight:{400 if sub else 600};'
             f'color:{CONCRETE if sub else NAVY};padding-left:{24 if sub else 0}px">{t}</td>'
             f'<td class="n" style="text-align:right;padding:10px 0">{pg}</td></tr>')
pages.append(slide(2, "Contents", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">Contents</div><h2>What this<br>book covers</h2>
<p class="lede">The rules for using the Secsaway identity consistently, from a 16-pixel app icon to the side of a 40-foot container.</p></div>
<div class="r7" style="grid-column:6/span 7;margin-top:-12px"><table class="tbl">{rows}</table></div>
</div></div>'''))

# 3 ---------- Brand foundation
names.append("Brand_Foundation")
vals = [("Punctual", "We give a time and we keep it. When we can't, the client hears it from us first."),
        ("Accountable", "Every handover is signed, scanned and recorded. We own the shipment until it is delivered."),
        ("Precise", "Correct paperwork, correct weights, correct address. Small errors cost our clients days."),
        ("Steady", "Customs holds and road closures happen. We stay calm and find the next route.")]
vhtml = "".join(f'<div style="border-top:1px solid {STEEL};padding-top:20px"><h3>{t}</h3><p class="small" style="margin-top:10px;color:#3A424A">{d}</p></div>' for t, d in vals)
pages.append(slide(3, "01 — Brand foundation", f'''<div class="c"><div class="grid">
<div class="l5"><div class="label">01 — Brand foundation</div>
<h2>Every handover<br>is a promise.</h2>
<p class="lede">For businesses and individuals who cannot afford a missed delivery, Secsaway is the logistics partner that treats every handover as a commitment: tracked, documented and on time.</p>
<div style="margin-top:56px;display:grid;grid-template-columns:1fr 1fr;gap:32px">
<div><div class="label" style="color:{CONCRETE}">Mission</div><p style="margin-top:10px;font-size:18px">Move our clients' goods on time, in full, with a clear record of every handover.</p></div>
<div><div class="label" style="color:{CONCRETE}">Vision</div><p style="margin-top:10px;font-size:18px">Be the logistics company our clients never need to chase.</p></div>
</div></div>
<div class="r7" style="grid-column:7/span 6;display:flex;flex-direction:column;justify-content:space-between">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px 32px">{vhtml}</div>
<div style="background:{NAVY};padding:36px 40px;display:flex;justify-content:space-between;align-items:center">
<span class="label" style="color:#8FA3B6">Brand voice</span>
<span style="color:#fff;font-size:40px;font-weight:600;letter-spacing:-.02em">Clear. Calm. Exact.</span></div>
</div></div></div>'''))

# 4 ---------- Primary logo
names.append("Primary_Logo")
H = 190
W = lockup_h_w(H)
pages.append(slide(4, "02 — Logo", f'''
<div style="position:absolute;left:120px;top:168px"><div class="label">02 — Logo</div><h2>Primary logo</h2></div>
<div style="position:absolute;left:{(1920-W)/2:.0f}px;top:{(1080-H)/2+20:.0f}px">{svg(round(W)+2,H, lockup_h(0,0,H,ORANGE,NAVY))}</div>
<div style="position:absolute;left:120px;right:120px;bottom:140px;display:flex;justify-content:space-between;align-items:flex-end">
<p class="small" style="max-width:520px">The horizontal lockup is the default. Use it wherever there is enough width. The orange mark and navy wordmark are the only full-colour combination on light backgrounds.</p>
<span class="cap">Signal Orange mark · Depot Navy wordmark</span></div>'''))

# 5 ---------- Concept
names.append("Logo_Concept")
CENTER_D = "M120 10H35A25 25 0 0 0 35 60H50 M70 60H85A25 25 0 0 1 85 110H0"
grid_lines = "".join(f'<path d="M{i*20} 0V120 M0 {i*20}H120" stroke="{STEEL}" stroke-width="0.6"/>' for i in range(7))
step1 = f'''<g transform="translate(60,40) scale(2.6)"><path d="M120 10H35A25 25 0 0 0 35 60H85A25 25 0 0 1 85 110H0" fill="none" stroke="{CONCRETE}" stroke-width="1.2" stroke-dasharray="4 3"/>
<circle cx="120" cy="10" r="3" fill="{INK}"/><circle cx="0" cy="110" r="3" fill="{INK}"/></g>'''
step2 = f'''<g transform="translate(60,40) scale(2.6)">{grid_lines}<path d="{TOP_D}" fill="none" stroke="{NAVY}" stroke-width="1.2"/><path d="{BOT_D}" fill="none" stroke="{NAVY}" stroke-width="1.2"/>
<rect x="50" y="50" width="20" height="20" fill="{ORANGE}" opacity=".9"/></g>'''
step3 = icon(60, 40, 312, ORANGE)
panels = ""
for i, (art, t, d) in enumerate([(step1, "Route", "A single delivery route: a straight run, one turn, a straight run. Drawn as one line from sender to receiver."),
                                  (step2, "Handover", "The route is split into two identical strokes. The gap between them is the handover point, where Secsaway takes responsibility."),
                                  (step3, "Mark", "Set at a heavy, even weight on a 6x grid. The result reads as an S at 16 px and as a route at 16 m.")]):
    panels += f'''<div><div style="background:#fff;border:1px solid {STEEL}">{svg(432,440,f'<g transform="translate(0,24)">{art}</g>')}</div>
<div style="display:flex;gap:16px;margin-top:24px"><span class="n" style="color:{ORANGE}">0{i+1}</span><div><h3>{t}</h3><p class="small" style="margin-top:8px;color:#3A424A;max-width:400px">{d}</p></div></div></div>'''
pages.append(slide(5, "02 — Logo", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">02 — Logo concept</div><h2>Two routes, one handover</h2></div>
<p class="small" style="max-width:520px;color:#3A424A">The mark is rotationally symmetric. Turned 180°, it is unchanged: the sender's route and the receiver's route carry equal weight.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:56px;margin-top:48px">{panels}</div></div>'''))

# 6 ---------- Construction grid
names.append("Logo_Grid")
S = 4  # 480px icon
g = ""
for i in range(7):
    g += f'<path d="M{i*20*S} 0V{120*S} M0 {i*20*S}H{120*S}" stroke="{STEEL}" stroke-width="1"/>'
g += f'<path d="{ICON_D}" fill="{ORANGE}" opacity=".92" transform="scale({S})"/>'
g += f'<circle cx="{35*S}" cy="{35*S}" r="{35*S}" fill="none" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="6 5"/>'
g += f'<circle cx="{35*S}" cy="{35*S}" r="{15*S}" fill="none" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="6 5"/>'
g += f'<circle cx="{85*S}" cy="{85*S}" r="{35*S}" fill="none" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="6 5"/>'
g += f'<circle cx="{85*S}" cy="{85*S}" r="{15*S}" fill="none" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="6 5"/>'
g += f'<circle cx="{35*S}" cy="{35*S}" r="4" fill="{NAVY}"/><circle cx="{85*S}" cy="{85*S}" r="4" fill="{NAVY}"/>'
ann = (f'<g font-family="IBM Plex Mono" font-size="15" fill="{INK}">'
       f'<path d="M500 0V80" stroke="{INK}"/><path d="M494 0H506M494 80H506" stroke="{INK}"/><text x="514" y="45">1x stroke</text>'
       f'<path d="M200 520H280" stroke="{INK}"/><path d="M200 514V526M280 514V526" stroke="{INK}"/><text x="210" y="548">1x gap</text>'
       f'<path d="M0 520H120" stroke="{INK}" opacity="0"/>'
       f'<path d="M-24 0V480" stroke="{INK}"/><path d="M-30 0H-18M-30 480H-18" stroke="{INK}"/><text x="-40" y="246" text-anchor="end">6x</text>'
       f'<text x="514" y="160">r 1.75x outer</text><text x="514" y="184">r 0.75x inner</text>'
       f'<path d="M{35*S+5} {35*S}L506 154" stroke="{NAVY}" stroke-width=".8"/></g>')
LH = 120
LW = lockup_h_w(LH)
u = LH / 6
lk = lockup_h(0, 0, LH, ORANGE, NAVY)
lk += f'<g font-family="IBM Plex Mono" font-size="14" fill="{INK}" stroke-width="1">'
lk += f'<path d="M{LH} {LH+24}H{LH+2*u}" stroke="{INK}"/><path d="M{LH} {LH+18}V{LH+30}M{LH+2*u} {LH+18}V{LH+30}" stroke="{INK}"/><text x="{LH-6}" y="{LH+52}">2x</text>'
lk += f'<path d="M{LW+16} {1.5*u}V{4.5*u}" stroke="{INK}"/><path d="M{LW+10} {1.5*u}H{LW+22}M{LW+10} {4.5*u}H{LW+22}" stroke="{INK}"/><text x="{LW+30}" y="{3*u+5}">3x cap height</text>'
lk += f'<path d="M0 {1.5*u}H{LW}M0 {4.5*u}H{LW}" stroke="{NAVY}" stroke-dasharray="4 4" opacity=".6"/></g>'
pages.append(slide(6, "02 — Logo", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">02 — Construction</div><h2>Built on<br>a 6x grid</h2>
<p class="lede">One unit, x, controls every proportion. x equals the stroke weight of the mark.</p>
<table class="tbl" style="margin-top:40px">
<tr><td>Mark</td><td class="n" style="text-align:right">6x × 6x</td></tr>
<tr><td>Stroke &amp; handover gap</td><td class="n" style="text-align:right">1x</td></tr>
<tr><td>Turn radius (outer / inner)</td><td class="n" style="text-align:right">1.75x / 0.75x</td></tr>
<tr><td>Mark to wordmark</td><td class="n" style="text-align:right">2x</td></tr>
<tr><td>Wordmark cap height</td><td class="n" style="text-align:right">3x</td></tr>
<tr><td>Angles</td><td class="n" style="text-align:right">0° / 90° only</td></tr></table></div>
<div style="grid-column:6/span 7;position:relative">
<div style="position:absolute;left:60px;top:10px">{svg(700,580, f'<g transform="translate(60,10)">{g}{ann}</g>')}</div>
<div style="position:absolute;left:60px;bottom:-10px">{svg(round(LW)+200,LH+60, lk)}</div>
</div></div></div>'''))

# 7 ---------- Clear space & min size
names.append("Clear_Space")
LH = 120; u = LH / 6; LW = lockup_h_w(LH); pad = 2 * u
cs = f'<rect x="0" y="0" width="{LW+2*pad}" height="{LH+2*pad}" fill="none" stroke="{ORANGE}" stroke-dasharray="6 5"/>'
cs += f'<rect x="{pad}" y="{pad}" width="{LW}" height="{LH}" fill="none" stroke="{STEEL}"/>'
cs += f'<g transform="translate({pad},{pad})">{lockup_h(0,0,LH,ORANGE,NAVY)}</g>'
for (x, y) in [(0, 0), (LW + pad, 0), (0, LH + pad), (LW + pad, LH + pad)]:
    cs += f'<rect x="{x}" y="{y}" width="{pad}" height="{pad}" fill="{ORANGE}" opacity=".12"/><text x="{x+pad/2}" y="{y+pad/2+5}" text-anchor="middle" font-family="IBM Plex Mono" font-size="14" fill="{ORANGE}">2x</text>'
mins = ""
for sz in (16, 24, 32, 48):
    mins += f'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:14px">{svg(sz,sz,icon(0,0,sz,NAVY))}<span class="n">{sz} px</span></div>'
pages.append(slide(7, "02 — Logo", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">02 — Clear space &amp; minimum size</div><h2>Room to<br>be seen</h2>
<p class="lede">Keep 2x of clear space on every side. No text, edge or other graphic may enter it.</p></div>
<div style="grid-column:6/span 7">
<div>{svg(round(LW+2*pad)+2, round(LH+2*pad)+2, cs)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:72px">
<div><h3>Minimum size</h3><table class="tbl" style="margin-top:16px">
<tr><th></th><th>Print</th><th>Screen</th></tr>
<tr><td>Horizontal lockup</td><td class="n">35 mm</td><td class="n">140 px</td></tr>
<tr><td>Stacked lockup</td><td class="n">22 mm</td><td class="n">96 px</td></tr>
<tr><td>Mark only</td><td class="n">6 mm</td><td class="n">16 px</td></tr></table></div>
<div><h3>Mark at actual size</h3><div style="display:flex;gap:40px;align-items:flex-end;margin-top:32px">{mins}</div>
<p class="small" style="margin-top:24px">Below 24 px, use the single-colour mark. The 1x handover gap stays open at 16 px.</p></div>
</div></div></div></div>'''))

# 8 ---------- Variations
names.append("Logo_Variations")
def tile(bg, art, label, border=False):
    b = f"border:1px solid {STEEL};" if border else ""
    return f'<div><div style="background:{bg};{b}height:290px;display:flex;align-items:center;justify-content:center">{art}</div><div class="cap">{label}</div></div>'
LH = 66; LW = lockup_h_w(LH)
VW = 260
var = [
    tile("#fff", svg(round(LW)+1, LH, lockup_h(0,0,LH,ORANGE,NAVY)), "Horizontal · full colour", True),
    tile("#fff", svg(VW, round(VW/WM_RATIO/3*11)+2, lockup_v(0,0,VW,ORANGE,NAVY)), "Stacked · full colour", True),
    tile("#fff", svg(120,120, icon(0,0,120,ORANGE)), "Mark only", True),
    tile(PAPER, svg(round(LW)+1, LH, lockup_h(0,0,LH,INK,INK)), "Single colour · Ink", True),
    tile(INK, svg(round(LW)+1, LH, lockup_h(0,0,LH,WHITE,WHITE)), "Single colour · reversed"),
    tile(NAVY, svg(round(LW)+1, LH, lockup_h(0,0,LH,ORANGE,WHITE)), "On Depot Navy"),
]
pages.append(slide(8, "02 — Logo", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">02 — Variations</div><h2>Logo variations</h2></div>
<p class="small" style="max-width:520px;color:#3A424A">Use full colour wherever possible. Single-colour versions are for one-colour print, embossing, engraving and vehicle vinyl.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px 24px;margin-top:40px">{"".join(var)}</div></div>'''))

# 9 ---------- Misuse
names.append("Logo_Misuse")
LH = 56; LW = lockup_h_w(LH)
base = lockup_h(0, 0, LH, ORANGE, NAVY)
def dont(art, label, bg="#fff"):
    x = f'<svg width="22" height="22" viewBox="0 0 22 22" style="position:absolute;top:18px;right:18px"><path d="M3 3L19 19M19 3L3 19" stroke="{ORANGE}" stroke-width="2.5"/></svg>'
    return f'<div><div style="position:relative;background:{bg};border:1px solid {STEEL};height:290px;display:flex;align-items:center;justify-content:center;overflow:hidden">{art}{x}</div><div class="cap">{label}</div></div>'
OUTLINED = lockup_h(0, 0, LH, "none", "none").replace('fill="none"', f'fill="none" stroke="{NAVY}" stroke-width="1.5" vector-effect="non-scaling-stroke"')
mis = [
    dont(svg(round(LW*1.35)+1, LH, f'<g transform="scale(1.35,1)">{base}</g>'), "Don't stretch or squash"),
    dont(svg(round(LW)+1, LH, lockup_h(0,0,LH,"#2E9E5B","#6A3FA0")), "Don't recolour"),
    dont(svg(round(LW)+40, LH+120, f'<g transform="translate(20,80) rotate(-10)">{base}</g>'), "Don't rotate"),
    dont(svg(round(LW)+4, LH+4, f'<g transform="translate(2,2)">{OUTLINED}</g>'), "Don't outline"),
    dont(svg(round(LW)+30, LH+30, f'<g filter="url(#glow)">{base}</g>'), "Don't add shadows or effects"),
    dont(f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(135deg,#7E8F9E 0 14px,#B6C1CA 14px 28px)"></div><div style="position:relative">{svg(round(LW)+1, LH, base)}</div>', "Don't place on busy backgrounds"),
]
pages.append(slide(9, "02 — Logo", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">02 — Misuse</div><h2>What not to do</h2></div>
<p class="small" style="max-width:520px;color:#3A424A">Always use the master artwork files. Never redraw, retype or modify the logo.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px 24px;margin-top:40px">{"".join(mis)}</div></div>'''))

# 10 ---------- Colour
names.append("Colour_Palette")
def sw(name, hx, rgb, cmyk, pms, fg, h, extra=""):
    return f'''<div style="background:{hx};color:{fg};height:{h}px;padding:28px;display:flex;flex-direction:column;justify-content:space-between;{extra}">
<div style="font-size:24px;font-weight:600;letter-spacing:-.01em">{name}</div>
<div class="mono" style="font-size:13px;line-height:1.7;letter-spacing:.02em">HEX {hx}<br>RGB {rgb}<br>CMYK {cmyk}<br>{pms}</div></div>'''
pages.append(slide(10, "03 — Colour", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">03 — Colour</div><h2>Navy for trust,<br>orange for action</h2>
<p class="lede">Depot Navy carries the brand. Signal Orange is the colour of hi-vis and safety markings, used sparingly for the mark and calls to action.</p>
<div style="margin-top:40px"><div class="label" style="color:{CONCRETE}">Usage ratio</div>
<div style="display:flex;height:40px;margin-top:14px">
<div style="flex:55;background:{NAVY}"></div><div style="flex:25;background:{PAPER};border:1px solid {STEEL}"></div><div style="flex:10;background:{STEEL}"></div><div style="flex:5;background:{INK}"></div><div style="flex:5;background:{ORANGE}"></div></div>
<div class="n" style="display:flex;margin-top:8px;font-size:12px"><span style="flex:55">55</span><span style="flex:25">25</span><span style="flex:10">10</span><span style="flex:5">5</span><span style="flex:5">5</span></div></div>
<div style="margin-top:32px"><div class="label" style="color:{CONCRETE}">Contrast (WCAG 2.1)</div>
<table class="tbl" style="margin-top:8px;font-size:15px">
<tr><td style="padding:9px 0">Navy on Paper</td><td class="n" style="text-align:right;padding:9px 0">13.1 : 1 · AAA</td></tr>
<tr><td style="padding:9px 0">White on Navy</td><td class="n" style="text-align:right;padding:9px 0">14.4 : 1 · AAA</td></tr>
<tr><td style="padding:9px 0">Ink on Orange</td><td class="n" style="text-align:right;padding:9px 0">4.9 : 1 · AA</td></tr>
<tr><td style="padding:9px 0">Orange on White</td><td class="n" style="text-align:right;padding:9px 0">3.7 : 1 · large text / graphics only</td></tr></table></div></div>
<div style="grid-column:6/span 7;display:grid;grid-template-columns:2fr 1fr;grid-template-rows:auto auto;gap:16px;align-content:start">
{sw("Depot Navy", NAVY, "15 43 70", "100 80 40 45", "PMS 2965 C", "#fff", 440)}
{sw("Signal Orange", ORANGE, "232 85 28", "0 75 95 0", "PMS 1665 C", INK, 440)}
<div style="grid-column:1/span 2;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
{sw("Ink", INK, "20 24 28", "75 65 60 85", "PMS Black 6 C", "#fff", 250)}
{sw("Concrete", CONCRETE, "100 108 117", "55 42 35 20", "PMS Cool Gray 10 C", "#fff", 250)}
{sw("Steel", STEEL, "213 217 221", "15 10 8 0", "PMS Cool Gray 1 C", INK, 250)}
{sw("Paper", PAPER, "244 244 241", "3 2 4 0", "Uncoated white stock", INK, 250, f"border:1px solid {STEEL}")}
</div></div></div></div>'''))

# 11 ---------- Typography
names.append("Typography")
hier = [("H1 · Display", "Archivo ExtraBold", "96 / 96 · −3%", f'<span style="font-weight:800;font-size:76px;letter-spacing:-.03em;line-height:1">On time.</span>'),
        ("H2 · Heading", "Archivo SemiBold", "48 / 52 · −2%", f'<span style="font-weight:600;font-size:44px;letter-spacing:-.02em">Freight, cleared and delivered</span>'),
        ("Body", "Archivo Regular", "18 / 28 · 0%", f'<span style="font-size:18px;line-height:28px;color:#3A424A">Your shipment left our Apapa depot at 06:40 and is on schedule for delivery before noon.</span>'),
        ("Caption · Data", "IBM Plex Mono Medium", "13 / 20 · +8%", f'<span class="mono" style="font-weight:500;font-size:14px;letter-spacing:.08em">AWB 176-48210395 · ETA 11:30 · 1,240 KG</span>')]
hr = "".join(f'<tr><td style="width:190px;padding:26px 0"><div class="label" style="color:{CONCRETE}">{a}</div><div class="n" style="font-size:13px;margin-top:8px">{b}<br>{c}</div></td><td style="padding:26px 0;color:{NAVY}">{d}</td></tr>' for a, b, c, d in hier)
pages.append(slide(11, "04 — Typography", f'''<div class="c"><div class="grid">
<div class="l5"><div class="label">04 — Typography</div><h2>Two typefaces,<br>clear roles</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:48px">
<div style="border-top:2px solid {NAVY};padding-top:20px"><div style="font-weight:800;font-size:120px;line-height:1;color:{NAVY};letter-spacing:-.03em">Aa</div>
<h3 style="margin-top:18px">Archivo</h3><p class="small" style="margin-top:6px">Primary. Headlines, body text and interfaces. The wordmark is drawn from its ExtraBold weight.</p></div>
<div style="border-top:2px solid {NAVY};padding-top:20px"><div class="mono" style="font-weight:500;font-size:120px;line-height:1;color:{NAVY};letter-spacing:-.04em">Aa</div>
<h3 style="margin-top:18px">IBM Plex Mono</h3><p class="small" style="margin-top:6px">Secondary. Tracking numbers, weights, times and labels: anything a driver or clerk must read exactly.</p></div></div>
<p class="small" style="margin-top:32px">Both are free under the SIL Open Font License from Google Fonts. Fallback: Arial and Courier New.</p></div>
<div style="grid-column:7/span 6"><table class="tbl">{hr}</table></div>
</div></div>'''))

# 12 ---------- Pattern
names.append("Brand_Pattern")
pages.append(slide(12, "05 — Brand pattern", f'''
<svg width="1920" height="1080" style="position:absolute;inset:0"><rect x="960" y="0" width="960" height="1080" fill="{NAVY}"/><rect x="960" y="0" width="960" height="1080" fill="url(#patA)"/></svg>
<div class="c" style="right:1080px"><div class="label">05 — Brand pattern</div><h2>Patterns from<br>the mark</h2>
<p class="lede">Both patterns use the mark's own geometry, so they can fill large surfaces without adding a new graphic language.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:48px">
<div><div style="height:220px;background:{NAVY};overflow:hidden">{svg(380,220,f'<rect width="380" height="220" fill="url(#patA)"/>')}</div>
<h3 style="margin-top:18px">A · Network</h3><p class="small" style="margin-top:6px">The mark tiled with alternate 90° turns, 1x apart. Tone-on-tone only: Navy on Navy +8%. For cover pages, vehicle rears and packaging.</p></div>
<div><div style="height:220px;background:{PAPER};border:1px solid {STEEL};overflow:hidden">{svg(380,220,f'<g transform="scale(.42)"><rect width="905" height="524" fill="url(#patB)"/></g>')}</div>
<h3 style="margin-top:18px">B · Route</h3><p class="small" style="margin-top:6px">Single strokes from the mark at 1.5× scale, widely spaced. Steel on Paper. For documents, the website and interiors.</p></div>
</div></div>
<div style="position:absolute;left:1080px;bottom:120px;background:{PAPER};padding:28px 32px;width:420px">
<div class="label" style="color:{CONCRETE}">Rule</div><p style="font-size:16px;margin-top:8px">Never place the logo on top of the pattern without a clear-space panel, and never combine the two patterns on one surface.</p></div>
''', chrome=True))

# 13 ---------- Iconography
names.append("Iconography")
cells = ""
for nme in ICONS:
    cells += f'<div style="border:1px solid {STEEL};background:#fff;height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">{svg(72,72,ic48(nme,0,0,72,NAVY,3))}<span class="cap" style="margin:0">{nme}</span></div>'
spec = f'<g transform="translate(0,0)">'
for i in range(13):
    spec += f'<path d="M{i*15} 0V180 M0 {i*15}H180" stroke="{STEEL}" stroke-width=".8"/>'
spec += f'<rect x="15" y="15" width="150" height="150" fill="none" stroke="{ORANGE}" stroke-dasharray="4 4"/>'
spec += ic48("Route", 0, 0, 180, NAVY, 3) + '</g>'
pages.append(slide(13, "06 — Iconography", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">06 — Iconography</div><h2>A matching<br>line icon set</h2>
<p class="lede">Twelve service icons drawn with the same rules as the mark.</p>
<div style="margin-top:36px;display:flex;gap:32px;align-items:flex-start">{svg(180,180,spec)}
<table class="tbl" style="font-size:15px"><tr><td style="padding:10px 0">Grid</td><td class="n" style="text-align:right;padding:10px 0">48 × 48</td></tr>
<tr><td style="padding:10px 0">Live area</td><td class="n" style="text-align:right;padding:10px 0">40 × 40</td></tr>
<tr><td style="padding:10px 0">Stroke</td><td class="n" style="text-align:right;padding:10px 0">3 px</td></tr>
<tr><td style="padding:10px 0">Ends / turns</td><td class="n" style="text-align:right;padding:10px 0">Square / round</td></tr></table></div>
<p class="small" style="margin-top:28px">The Route icon reuses the S turn from the mark. Icons are Navy or Ink; Orange only for an active state.</p></div>
<div style="grid-column:6/span 7;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-content:start">{cells}</div>
</div></div>'''))

# 14 ---------- Photography
names.append("Photography")
def photo(w, h, title, desc, tone, fg="#fff", avoid=False):
    cross = "" if avoid else f'<path d="M0 0L{w} {h} M{w} 0L0 {h}" stroke="{fg}" stroke-opacity=".12"/>'
    frame = f'<div style="position:relative;height:{h}px;background:{tone}">{svg(w,h,cross,style="position:absolute;inset:0;width:100%;height:100%")}<div style="position:absolute;left:24px;bottom:22px;right:24px;color:{fg}"><div class="mono" style="font-size:12px;letter-spacing:.1em;opacity:.75">{"AVOID" if avoid else "IMAGE BRIEF"}</div><div style="font-size:24px;font-weight:600;margin-top:6px">{title}</div></div></div>'
    return f'<div>{frame}<p class="small" style="margin-top:14px;color:#3A424A;max-width:none">{desc}</p></div>'
pages.append(slide(14, "07 — Photography", f'''<div class="c"><div class="grid">
<div class="l4"><div class="label">07 — Photography</div><h2>Real work,<br>real places</h2>
<p class="lede">Photograph Secsaway's own people, vehicles and depots. The images should look like evidence that the work is being done.</p>
<table class="tbl" style="margin-top:40px;font-size:16px">
<tr><td style="padding:12px 0">Light</td><td style="padding:12px 0;text-align:right;color:{CONCRETE}">Natural daylight, early or overcast</td></tr>
<tr><td style="padding:12px 0">Grade</td><td style="padding:12px 0;text-align:right;color:{CONCRETE}">Neutral to slightly cool, true colour</td></tr>
<tr><td style="padding:12px 0">Framing</td><td style="padding:12px 0;text-align:right;color:{CONCRETE}">Eye level, horizon straight</td></tr>
<tr><td style="padding:12px 0">People</td><td style="padding:12px 0;text-align:right;color:{CONCRETE}">Staff in uniform, mid-task, not posing</td></tr></table></div>
<div style="grid-column:6/span 7;display:grid;grid-template-columns:1.4fr 1fr;gap:24px">
{photo(560,350,"Operations","A loader checks a pallet label against the waybill. Hands, scanner and paperwork in frame.","#2C3E50")}
{photo(400,350,"Scale","A row of Secsaway trucks at the depot gate at dawn, shot square-on.","#4A5A68")}
{photo(560,350,"Detail","Close-up of a sealed container door, seal number legible.","#6E7B86")}
{photo(400,350,"Stock clichés","Handshakes, glowing globes, network lines, generic smiling couriers.",STEEL,INK,True)}
</div></div></div>'''))

# 15 ---------- Stationery
names.append("Stationery")
# business card 85x55 -> 340x220
bc_front = svg(340, 220, f'<rect width="340" height="220" fill="{NAVY}"/><rect x="200" width="140" height="220" fill="url(#patA-small)"/>' + icon(28, 152, 40, ORANGE))
bc_back = svg(340, 220, f'<rect width="340" height="220" fill="#fff"/>' + lockup_h(28, 28, 24, ORANGE, NAVY) +
              f'<g font-family="Archivo"><text x="28" y="132" font-size="15" font-weight="600" fill="{NAVY}">Chidinma Eze</text><text x="28" y="152" font-size="11" fill="{CONCRETE}">Head of Freight Operations</text></g>'
              f'<g font-family="IBM Plex Mono" font-size="9" fill="{INK}" letter-spacing=".3"><text x="28" y="182">+000 000 000 0000</text><text x="28" y="196">name@secsaway.com</text></g>'
              f'<rect x="0" y="216" width="340" height="4" fill="{ORANGE}"/>')
lines = "".join(f'<rect x="40" y="{y}" width="{w}" height="4" fill="{STEEL}"/>' for y, w in [(176, 130), (196, 90), (250, 300), (264, 310), (278, 290), (292, 305), (306, 180), (334, 300), (348, 296), (362, 240)])
letter = svg(420, 594, f'<rect width="420" height="594" fill="#fff"/>' + lockup_h(40, 40, 26, ORANGE, NAVY) +
             f'<text x="380" y="58" text-anchor="end" font-family="IBM Plex Mono" font-size="7" fill="{CONCRETE}">REF SCW/2026/0412</text>{lines}'
             f'<rect x="40" y="540" width="340" height=".8" fill="{STEEL}"/><g font-family="IBM Plex Mono" font-size="6.5" fill="{CONCRETE}"><text x="40" y="556">Secsaway Logistics Company · [Registered address] · [City, Country]</text><text x="40" y="566">[Phone] · [Email] · [Website] · RC [Company registration no.]</text></g>'
             f'<rect x="0" y="590" width="420" height="4" fill="{ORANGE}"/>')
env = svg(440, 220, f'<rect width="440" height="220" fill="#fff"/>' + lockup_h(24, 24, 22, ORANGE, NAVY) +
          f'<rect x="240" y="120" width="170" height="4" fill="{STEEL}"/><rect x="240" y="132" width="140" height="4" fill="{STEEL}"/><rect x="240" y="144" width="110" height="4" fill="{STEEL}"/>'
          f'<rect x="372" y="20" width="44" height="52" fill="none" stroke="{STEEL}" stroke-dasharray="3 3"/><rect x="0" y="216" width="440" height="4" fill="{NAVY}"/>')
sig = f'''<div style="background:#fff;border:1px solid {STEEL};padding:24px 28px;width:440px">
<div style="font-size:15px;font-weight:600;color:{NAVY}">Chidinma Eze</div><div style="font-size:12px;color:{CONCRETE};margin-top:2px">Head of Freight Operations</div>
<div class="mono" style="font-size:11px;color:{INK};margin-top:12px;line-height:1.6">+000 000 000 0000 · name@secsaway.com</div>
<div style="height:1px;background:{STEEL};margin:16px 0"></div>{svg(220,24,lockup_h(0,0,24,ORANGE,NAVY))}</div>'''
pages.append(slide(15, "08 — Applications", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">08 — Stationery</div><h2>Stationery</h2></div>
<p class="small" style="max-width:520px;color:#3A424A">One-colour orange base rule on every printed item. Business card 85 × 55 mm, letterhead A4, envelope DL. Names and contacts are placeholders.</p></div>
<div style="display:flex;gap:56px;margin-top:40px;align-items:flex-start">
<div><div style="box-shadow:0 0 0 1px {STEEL}">{letter}</div><div class="cap">Letterhead · A4</div></div>
<div style="display:flex;flex-direction:column;gap:36px;zoom:1.2">
<div style="display:flex;gap:24px"><div><div>{bc_front}</div><div class="cap">Business card · front</div></div><div><div style="box-shadow:0 0 0 1px {STEEL}">{bc_back}</div><div class="cap">Business card · back</div></div></div>
<div style="display:flex;gap:24px;align-items:flex-start"><div><div style="box-shadow:0 0 0 1px {STEEL}">{env}</div><div class="cap">Envelope · DL</div></div>
<div>{sig}<div class="cap">Email signature</div></div></div>
</div></div></div>'''))

# 16 ---------- Digital
names.append("Digital")
web = svg(900, 540, f'''<rect width="900" height="540" fill="#fff"/><rect width="900" height="34" fill="{STEEL}"/>
<circle cx="20" cy="17" r="5" fill="#fff"/><circle cx="38" cy="17" r="5" fill="#fff"/><circle cx="56" cy="17" r="5" fill="#fff"/>
<rect x="200" y="9" width="500" height="16" rx="8" fill="#fff"/><text x="450" y="21" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="{CONCRETE}">secsaway.com</text>
<rect y="34" width="900" height="506" fill="{NAVY}"/><rect x="560" y="34" width="340" height="506" fill="url(#patA-small)"/>
{lockup_h(40, 58, 26, ORANGE, WHITE)}
<g font-family="Archivo" font-size="12" fill="#C3CED8"><text x="520" y="76">Services</text><text x="590" y="76">Tracking</text><text x="660" y="76">Industries</text><text x="740" y="76">Contact</text></g>
<text x="40" y="200" font-family="Archivo" font-weight="800" font-size="46" fill="#fff" letter-spacing="-1.5">Freight that arrives</text>
<text x="40" y="250" font-family="Archivo" font-weight="800" font-size="46" fill="#fff" letter-spacing="-1.5">when we said it would.</text>
<text x="40" y="290" font-family="Archivo" font-size="15" fill="#C3CED8">Haulage, warehousing and customs clearance, tracked end to end.</text>
<rect x="40" y="330" width="330" height="48" fill="#fff"/><text x="58" y="359" font-family="IBM Plex Mono" font-size="12" fill="{CONCRETE}">Enter tracking number</text>
<rect x="370" y="330" width="110" height="48" fill="{ORANGE}"/><text x="425" y="359" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="14" fill="{INK}">Track</text>
<rect y="460" width="900" height="80" fill="#fff"/>
''' + "".join(ic48(n, 40 + i * 215, 478, 28, NAVY) + f'<text x="{78+i*215}" y="497" font-family="Archivo" font-weight="600" font-size="13" fill="{NAVY}">{t}</text>' for i, (n, t) in enumerate([("Truck", "Road haulage"), ("Warehouse", "Warehousing"), ("Customs", "Customs clearance"), ("Sea freight", "Freight forwarding")])))
steps = [("Picked up", "Lagos depot · 06:40", True), ("In transit", "Lagos–Ibadan expressway", True), ("Out for delivery", "Driver assigned", False), ("Delivered", "Signature required", False)]
st = ""
for i, (t, d, done) in enumerate(steps):
    y = 300 + i * 62
    c = ORANGE if done else STEEL
    st += f'<circle cx="34" cy="{y}" r="7" fill="{c}"/>'
    if i < 3:
        st += f'<rect x="33" y="{y+7}" width="2" height="48" fill="{ORANGE if i == 0 else STEEL}"/>'
    st += f'<text x="56" y="{y+4}" font-family="Archivo" font-weight="600" font-size="14" fill="{NAVY if done else CONCRETE}">{t}</text><text x="56" y="{y+22}" font-family="IBM Plex Mono" font-size="10" fill="{CONCRETE}">{d}</text>'
phone = svg(290, 590, f'''<rect width="290" height="590" rx="36" fill="{INK}"/><rect x="10" y="10" width="270" height="570" rx="28" fill="{PAPER}"/>
<rect x="10" y="10" width="270" height="200" rx="28" fill="{NAVY}"/><rect x="10" y="150" width="270" height="60" fill="{NAVY}"/>
{icon(30, 50, 22, ORANGE)}<text x="30" y="110" font-family="IBM Plex Mono" font-size="10" fill="#8FA3B6" letter-spacing="1">SHIPMENT</text>
<text x="30" y="134" font-family="IBM Plex Mono" font-weight="500" font-size="16" fill="#fff">SCW-2026-048213</text>
<text x="30" y="178" font-family="Archivo" font-weight="800" font-size="26" fill="#fff" letter-spacing="-.5">Arriving today</text>
<text x="30" y="198" font-family="Archivo" font-size="12" fill="#C3CED8">Estimated 11:30–12:00</text>
<g transform="translate(-6,-50)">{st}</g>
<rect x="30" y="520" width="230" height="44" fill="{NAVY}"/><text x="145" y="547" text-anchor="middle" font-family="Archivo" font-weight="600" font-size="13" fill="#fff">Contact driver</text>''')
post1 = svg(250, 250, f'<rect width="250" height="250" fill="{NAVY}"/><rect width="250" height="250" fill="url(#patA-small)" opacity=".9"/><rect x="20" y="130" width="210" height="100" fill="{NAVY}"/><text x="32" y="172" font-family="Archivo" font-weight="800" font-size="27" fill="#fff" letter-spacing="-.8">On time.</text><text x="32" y="204" font-family="Archivo" font-weight="800" font-size="27" fill="{ORANGE}" letter-spacing="-.8">In full.</text>' + icon(206, 24, 20, ORANGE))
post2 = svg(250, 250, f'<rect width="250" height="250" fill="{PAPER}"/>' + ic48("Customs", 24, 24, 44, NAVY) + f'<text x="24" y="156" font-family="Archivo" font-weight="800" font-size="22" fill="{NAVY}" letter-spacing="-.5">Customs cleared</text><text x="24" y="182" font-family="Archivo" font-weight="800" font-size="22" fill="{NAVY}" letter-spacing="-.5">in 48 hours.</text><text x="24" y="226" font-family="IBM Plex Mono" font-size="9" fill="{CONCRETE}" letter-spacing=".8">SERVICE UPDATE</text>' + icon(206, 24, 20, ORANGE))
avatar = svg(120, 120, f'<circle cx="60" cy="60" r="60" fill="{NAVY}"/>' + icon(34, 34, 52, ORANGE))
pages.append(slide(16, "08 — Applications", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">08 — Digital</div><h2>Digital</h2></div>
<p class="small" style="max-width:520px;color:#3A424A">Navy grounds, white type, one orange action per screen. Tracking data is always set in IBM Plex Mono.</p></div>
<div style="display:flex;gap:30px;margin-top:36px;align-items:flex-start">
<div><div style="box-shadow:0 0 0 1px {STEEL}">{web}</div><div class="cap">Website · home hero</div></div>
<div><div>{phone}</div><div class="cap">App · shipment tracking</div></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div style="display:flex;gap:16px"><div>{post1}</div></div>
<div style="display:flex;gap:16px;align-items:flex-end"><div style="box-shadow:0 0 0 1px {STEEL}">{post2}</div></div>
<div class="cap" style="margin-top:0">Social posts · 1:1</div>
</div>
<div>{avatar}<div class="cap">Profile picture</div></div></div>
</div>'''))

# 17 ---------- Fleet
names.append("Fleet_Signage")
truck = svg(860, 300, f'''
<rect x="10" y="20" width="600" height="220" fill="#fff" stroke="{STEEL}" stroke-width="2"/>
<rect x="10" y="20" width="110" height="220" fill="{NAVY}"/><rect x="10" y="20" width="110" height="220" fill="url(#patA-small)"/>
{lockup_h(160, 102, 56, ORANGE, NAVY)}
<rect x="10" y="232" width="600" height="8" fill="{ORANGE}"/>
<path d="M620 70H730L790 150V250H620Z" fill="{NAVY}"/><path d="M640 88H722L768 150H640Z" fill="#8FA3B6"/>
<rect x="610" y="236" width="190" height="16" fill="{INK}"/><rect x="0" y="240" width="620" height="12" fill="{INK}"/>
{"".join(f'<circle cx="{cx}" cy="262" r="30" fill="{INK}"/><circle cx="{cx}" cy="262" r="12" fill="{CONCRETE}"/>' for cx in (110, 180, 520, 700))}
<text x="760" y="228" font-family="IBM Plex Mono" font-size="9" fill="#fff" text-anchor="end">FLEET 018</text>''')
van = svg(470, 220, f'''<path d="M10 40H300L380 110L440 120V180H10Z" fill="{NAVY}"/><path d="M308 52L366 108H308Z" fill="#8FA3B6"/>
{lockup_h(30, 90, 34, ORANGE, WHITE)}<rect x="10" y="168" width="430" height="6" fill="{ORANGE}"/>
<circle cx="90" cy="184" r="24" fill="{INK}"/><circle cx="90" cy="184" r="9" fill="{CONCRETE}"/><circle cx="370" cy="184" r="24" fill="{INK}"/><circle cx="370" cy="184" r="9" fill="{CONCRETE}"/>''')
ribs = "".join(f'<rect x="{x}" y="14" width="3" height="172" fill="#0B2238"/>' for x in range(30, 760, 22))
cont = svg(780, 200, f'''<rect width="780" height="200" fill="{NAVY}"/>{ribs}<rect x="0" y="0" width="780" height="14" fill="#0B2238"/><rect x="0" y="186" width="780" height="14" fill="#0B2238"/>
<rect x="0" y="0" width="18" height="200" fill="#0B2238"/><rect x="762" y="0" width="18" height="200" fill="#0B2238"/>
<rect x="150" y="62" width="{lockup_h_w(76)+40:.0f}" height="96" fill="{NAVY}"/>{lockup_h(170, 72, 76, ORANGE, WHITE)}
<g font-family="IBM Plex Mono" font-weight="500" fill="#fff"><text x="660" y="44" font-size="14">SCWU 482193 0</text><text x="660" y="62" font-size="11">45G1</text></g>''')
doors = "".join(f'<rect x="{x}" y="150" width="200" height="190" fill="{STEEL}"/>' + "".join(f'<rect x="{x}" y="{y}" width="200" height="1.5" fill="#B9C0C6"/>' for y in range(160, 340, 12)) + f'<text x="{x+100}" y="142" text-anchor="middle" font-family="IBM Plex Mono" font-weight="500" font-size="12" fill="{INK}">BAY 0{i+1}</text>' for i, x in enumerate((60, 300, 540)))
wh = svg(800, 340, f'''<rect width="800" height="340" fill="#E6E8EA"/><rect width="800" height="110" fill="{NAVY}"/>{lockup_h(40, 34, 44, ORANGE, WHITE)}
<text x="760" y="64" text-anchor="end" font-family="IBM Plex Mono" font-size="12" fill="#8FA3B6" letter-spacing="1.5">DEPOT 01</text>{doors}<rect y="110" width="800" height="6" fill="{ORANGE}"/>''')
pages.append(slide(17, "08 — Applications", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">08 — Fleet &amp; signage</div><h2>Fleet &amp; signage</h2></div>
<p class="small" style="max-width:560px;color:#3A424A">Vehicles are the most visible brand asset. White box bodies keep the wordmark readable at distance; navy cabs, an orange base stripe and the Network pattern on the rear.</p></div>
<div style="display:grid;grid-template-columns:820px 1fr;gap:36px 80px;margin-top:32px;align-items:end">
<div><div>{truck.replace('width="860" height="300"','width="820" height="286"')}</div><div class="cap">Rigid truck · side livery</div></div>
<div><div>{van}</div><div class="cap">Delivery van · side livery</div></div>
<div><div>{cont.replace('width="780" height="200"','width="820" height="210"')}</div><div class="cap">40 ft container · owner code SCWU</div></div>
<div><div>{wh.replace('width="800" height="340"','width="640" height="272"')}</div><div class="cap">Depot facade &amp; loading bays</div></div>
</div></div>'''))

# 18 ---------- Packaging
names.append("Packaging")
box = svg(520, 420, f'''
<path d="M40 120L260 60L480 120L260 180Z" fill="#D7B88E"/>
<path d="M40 120L260 180V400L40 340Z" fill="{KRAFT}"/>
<path d="M480 120L260 180V400L480 340Z" fill="#B48F63"/>
<path d="M163.5 86.3L383.5 146.3L356.5 153.7L136.5 93.7Z" fill="{ORANGE}"/>
<g transform="matrix(1 .2727 0 1 70 185)">{lockup_h(0, 0, 26, NAVY, NAVY)}</g>
<g transform="matrix(1 -.2727 0 1 300 270)">{icon(0, 0, 70, NAVY)}</g>
<g transform="matrix(1 .2727 0 1 70 300)"><text font-family="IBM Plex Mono" font-size="10" fill="{NAVY}" letter-spacing="1">THIS WAY UP ↑   FRAGILE</text></g>''')
tape = svg(820, 44, f'<rect width="820" height="44" fill="{ORANGE}"/><rect width="820" height="44" fill="url(#tapeText)"/>')
random.seed(7)
bars, x = "", 24
while x < 360:
    w = random.choice([2, 2, 3, 4, 6])
    bars += f'<rect x="{x}" y="380" width="{w}" height="70" fill="{INK}"/>'
    x += w + random.choice([2, 3, 4])
label = svg(400, 600, f'''<rect width="400" height="600" fill="#fff"/>
<rect width="400" height="76" fill="{NAVY}"/>{lockup_h(24, 24, 28, ORANGE, WHITE)}<text x="376" y="46" text-anchor="end" font-family="IBM Plex Mono" font-weight="500" font-size="12" fill="#fff">EXPRESS</text>
<g font-family="IBM Plex Mono" fill="{INK}">
<text x="24" y="112" font-size="10" fill="{CONCRETE}">FROM</text><text x="24" y="130" font-size="13">[Sender name]</text><text x="24" y="148" font-size="13">[Sender address]</text>
<rect x="0" y="166" width="400" height="1" fill="{INK}"/>
<text x="24" y="192" font-size="10" fill="{CONCRETE}">TO</text><text x="24" y="218" font-size="18" font-weight="500">[Recipient name]</text><text x="24" y="242" font-size="15">[Delivery address line 1]</text><text x="24" y="264" font-size="15">[City, Region]</text>
<rect x="0" y="286" width="400" height="1" fill="{INK}"/>
<text x="24" y="312" font-size="10" fill="{CONCRETE}">WEIGHT</text><text x="24" y="336" font-size="18" font-weight="500">12.4 KG</text>
<text x="150" y="312" font-size="10" fill="{CONCRETE}">PIECES</text><text x="150" y="336" font-size="18" font-weight="500">1 / 3</text>
<text x="260" y="312" font-size="10" fill="{CONCRETE}">ROUTE</text><text x="260" y="336" font-size="18" font-weight="500">LOS-IBA</text>
<rect x="0" y="356" width="400" height="1" fill="{INK}"/>{bars}
<text x="200" y="476" text-anchor="middle" font-size="14" letter-spacing="3">SCW 2026 0482 13</text></g>
<rect y="540" width="400" height="60" fill="{ORANGE}"/><text x="24" y="577" font-family="Archivo" font-weight="800" font-size="20" fill="{INK}">HANDLE WITH CARE</text>''')
wrows = "".join(f'<rect x="24" y="{y}" width="452" height="1" fill="{STEEL}"/>' for y in range(150, 330, 30))
waybill = svg(500, 360, f'''<rect width="500" height="360" fill="#fff"/>{lockup_h(24, 24, 22, ORANGE, NAVY)}
<text x="476" y="38" text-anchor="end" font-family="Archivo" font-weight="600" font-size="15" fill="{NAVY}">Waybill</text>
<text x="476" y="56" text-anchor="end" font-family="IBM Plex Mono" font-size="10" fill="{CONCRETE}">No. 0048213</text>
<rect x="24" y="76" width="452" height="1.5" fill="{NAVY}"/>
<g font-family="IBM Plex Mono" font-size="9" fill="{CONCRETE}" letter-spacing=".8"><text x="24" y="100">SHIPPER</text><text x="260" y="100">CONSIGNEE</text><text x="24" y="140">DESCRIPTION OF GOODS</text><text x="300" y="140">QTY</text><text x="360" y="140">WEIGHT</text><text x="430" y="140">VALUE</text></g>
<rect x="24" y="108" width="210" height="18" fill="{PAPER}"/><rect x="260" y="108" width="216" height="18" fill="{PAPER}"/>{wrows}
<g font-family="IBM Plex Mono" font-size="9" fill="{CONCRETE}"><text x="24" y="346">Received in good condition: signature / date</text></g><rect x="300" y="336" width="176" height="1" fill="{INK}"/>''')
pages.append(slide(18, "08 — Applications", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">08 — Packaging</div><h2>Packaging &amp; documents</h2></div>
<p class="small" style="max-width:560px;color:#3A424A">Corrugated boxes print one colour, Navy, on natural kraft. Labels and waybills keep the logo at the top and every variable field in IBM Plex Mono.</p></div>
<div style="display:flex;gap:48px;margin-top:28px;align-items:flex-start;zoom:1.12">
<div><div>{box}</div><div class="cap">Shipping carton · 1-colour flexo on kraft</div>
<div style="margin-top:28px;width:520px;overflow:hidden">{tape}</div><div class="cap">Packing tape · 48 mm</div></div>
<div><div style="box-shadow:0 0 0 1px {STEEL};transform:scale(.9);transform-origin:top left;width:400px;height:540px">{label}</div><div class="cap">Shipping label · 4 × 6 in</div></div>
<div style="margin-left:-20px"><div style="box-shadow:0 0 0 1px {STEEL}">{waybill}</div><div class="cap">Waybill · A5 landscape</div></div>
</div></div>'''))

# 19 ---------- Merchandise
names.append("Merchandise_Uniform")
polo = svg(300, 320, f'''<path d="M95 20L125 8H175L205 20L280 62L254 118L222 102V290H78V102L46 118L20 62Z" fill="{NAVY}"/>
<path d="M125 8L150 46L175 8" fill="none" stroke="#0B2238" stroke-width="4"/><path d="M150 46V96" stroke="#0B2238" stroke-width="3"/>
<circle cx="150" cy="62" r="2.5" fill="#8FA3B6"/><circle cx="150" cy="80" r="2.5" fill="#8FA3B6"/>{icon(180, 74, 26, ORANGE)}
<rect x="20" y="62" width="0" height="0"/>''')
vest = svg(300, 320, f'''<path d="M80 10H120L150 90L180 10H220L232 70L250 110V290H50V110L68 70Z" fill="{ORANGE}"/>
<path d="M150 90V290" stroke="#C4461A" stroke-width="2"/>
<rect x="50" y="200" width="200" height="22" fill="{STEEL}"/><rect x="50" y="246" width="200" height="22" fill="{STEEL}"/>
<path d="M90 12L112 64" stroke="{STEEL}" stroke-width="18"/><path d="M210 12L188 64" stroke="{STEEL}" stroke-width="18"/>
<rect x="58" y="112" width="84" height="0"/>{lockup_h(162, 130, 12, NAVY, NAVY)}''')
cap_ = svg(300, 220, f'''<path d="M50 140A100 100 0 0 1 250 140Z" fill="{NAVY}"/><path d="M150 40V140" stroke="#0B2238" stroke-width="2"/>
<path d="M30 140H270C250 172 50 172 30 140Z" fill="#0B2238"/><circle cx="150" cy="42" r="6" fill="#0B2238"/>{icon(126, 76, 48, ORANGE)}''')
tote = svg(260, 320, f'''<path d="M80 110V60A50 50 0 0 1 180 60V110" fill="none" stroke="{NAVY}" stroke-width="12"/>
<rect x="30" y="100" width="200" height="210" fill="#EAE4D8"/>{icon(80, 160, 100, NAVY)}''')
mug = svg(240, 260, f'''<path d="M170 80H195A35 35 0 0 1 195 180H170" fill="none" stroke="{NAVY}" stroke-width="16"/>
<rect x="30" y="50" width="150" height="180" fill="{NAVY}"/><rect x="30" y="50" width="150" height="10" fill="#0B2238"/>{icon(75, 110, 60, ORANGE)}''')
lan = "".join(f'<g transform="translate({cx},{0}) rotate({rot})">' + "".join(icon(-5, y, 10, "#fff") for y in range(10, 150, 26)) + "</g>" for cx, rot in ((0, 0),))
badge = svg(240, 340, f'''<path d="M70 0L110 150 M170 0L130 150" stroke="{NAVY}" stroke-width="22"/>
<rect x="110" y="140" width="20" height="26" fill="{CONCRETE}"/>
<rect x="45" y="160" width="150" height="176" rx="0" fill="#fff" stroke="{STEEL}" stroke-width="2"/><rect x="45" y="160" width="150" height="40" fill="{NAVY}"/>{lockup_h(58, 173, 14, ORANGE, WHITE)}
<rect x="65" y="214" width="56" height="66" fill="{STEEL}"/><text x="65" y="300" font-family="Archivo" font-weight="600" font-size="12" fill="{NAVY}">Chidinma Eze</text>
<text x="65" y="316" font-family="IBM Plex Mono" font-size="8" fill="{CONCRETE}">ID 00418 · OPS</text><rect x="45" y="330" width="150" height="6" fill="{ORANGE}"/>''')
def m(art, c):
    return f'<div style="background:#fff;border:1px solid {STEEL};height:300px;display:flex;align-items:center;justify-content:center">{art}</div><div class="cap">{c}</div>'
pages.append(slide(19, "08 — Applications", f'''<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="label">08 — Merchandise &amp; uniform</div><h2>Uniform &amp; merchandise</h2></div>
<p class="small" style="max-width:560px;color:#3A424A">Uniforms carry the mark small and the role large. Hi-vis garments follow EN ISO 20471 colours; the logo is printed in Navy, never reflective.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px 24px;margin-top:28px">
<div>{m(polo.replace('width="300" height="320"','width="254" height="270"'),"Staff polo · Navy, embroidered mark")}</div><div>{m(vest.replace('width="300" height="320"','width="254" height="270"'),"Hi-vis vest · Class 2, printed lockup")}</div><div>{m(badge.replace('width="240" height="340"','width="190" height="270"'),"ID badge &amp; lanyard")}</div>
<div>{m(cap_.replace('width="300" height="220"','width="240" height="176"'),"Cap · Navy twill, embroidered mark")}</div>
<div>{m(tote.replace('width="260" height="320"','width="190" height="234"'),"Tote · natural cotton, 1-colour print")}</div>
<div>{m(mug.replace('width="240" height="260"','width="170" height="184"'),"Mug · Navy glaze, orange mark")}</div>
</div></div>'''))

# 20 ---------- Closing
names.append("Closing")
H = 110; W = lockup_h_w(H)
pages.append(slide(20, "", f'''
<div style="position:absolute;left:{(1920-W)/2:.0f}px;top:400px">{svg(round(W)+2,H, lockup_h(0,0,H,ORANGE,WHITE))}</div>
<div style="position:absolute;left:120px;right:120px;bottom:110px;display:flex;justify-content:space-between;align-items:flex-end">
<div class="mono" style="font-size:14px;line-height:1.8;color:#8FA3B6;letter-spacing:.04em">BRAND QUESTIONS AND MASTER ARTWORK<br><span style="color:#fff">[Brand contact name] · [email] · [phone]</span></div>
<div class="mono" style="font-size:14px;color:#8FA3B6;letter-spacing:.04em;text-align:right">SECSAWAY BRAND GUIDELINES<br>VERSION 1.0 — 2026</div></div>''', dark=True, chrome=False))

assert len(pages) == TOTAL, len(pages)

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Secsaway Brand Guidelines</title>
<style>{font_face()}\n{CSS}</style></head><body>{DEFS}{"".join(pages)}</body></html>'''
open(os.path.join(OUT, "brand-book.html"), "w").write(html)
open(os.path.join(OUT, "pages.txt"), "w").write("\n".join(names))

# ---------- Logo pack SVGs ----------
lp = os.path.join(OUT, "logo-pack")
os.makedirs(lp, exist_ok=True)
H = 120
W = lockup_h_w(H)
pad = 0
def save(name, w, h, body):
    open(os.path.join(lp, name + ".svg"), "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.2f}" height="{h:.2f}">{body}</svg>')
save("Secsaway_Logo_Primary", W, H, lockup_h(0, 0, H, ORANGE, NAVY))
save("Secsaway_Logo_White", W, H, lockup_h(0, 0, H, WHITE, WHITE))
save("Secsaway_Logo_Black", W, H, lockup_h(0, 0, H, INK, INK))
save("Secsaway_Logo_Reversed_OnNavy", W, H, lockup_h(0, 0, H, ORANGE, WHITE))
VW = 541.2
save("Secsaway_Logo_Stacked", VW, VW / WM_RATIO / 3 * 11, lockup_v(0, 0, VW, ORANGE, NAVY))
save("Secsaway_Icon", 120, 120, icon(0, 0, 120, ORANGE))
save("Secsaway_Icon_White", 120, 120, icon(0, 0, 120, WHITE))
save("Secsaway_Icon_Black", 120, 120, icon(0, 0, 120, INK))
print("built", len(pages), "pages")
