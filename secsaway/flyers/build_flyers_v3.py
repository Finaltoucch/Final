"""Secsaway flyers v3 — bold social style: cropped giant type, text-on-bars, diagonal shapes,
photo-strip collage, cutouts layered in front of type. Full-colour photography, brand colours only."""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "src")
P1 = os.path.join(HERE, "photos")
P2 = os.path.join(os.path.dirname(HERE), "photos-v2")

NAVY, ORANGE, INK, PAPER, WHITE, MUTE = "#0F2B46", "#E8551C", "#14181C", "#F4F4F1", "#FFFFFF", "#8FA3B6"
ICON_D = ("M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
          "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z")
with open(os.path.join(SRC, "wordmark.txt")) as f:
    wm_w, wm_cap = map(float, f.readline().split())
    WM_D = f.read().strip()
LOCK_W = 120 + 40 + 60 * wm_w / wm_cap


def lockup(width, ic, wc):
    h = width * 120 / LOCK_W
    return (f'<svg width="{width:.1f}" height="{h:.1f}" viewBox="0 0 {LOCK_W:.2f} 120"><path d="{ICON_D}" fill="{ic}"/>'
            f'<g transform="translate(160,30) scale({60 / wm_cap:.6f})"><path d="{WM_D}" fill="{wc}"/></g></svg>')


def img(path):
    mime = "image/png" if path.endswith(".png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def fonts():
    out = []
    for fam, w, st, fn in [("Archivo", 400, "normal", "Archivo400"), ("Archivo", 600, "normal", "Archivo600"),
                           ("Archivo", 300, "italic", "ArchivoLightItalic"), ("Archivo", 500, "italic", "ArchivoMediumItalic"),
                           ("Archivo XCond", 900, "italic", "ArchivoXCondBlackItalic"),
                           ("IBM Plex Mono", 500, "normal", "IBMPlexMono500")]:
        b = base64.b64encode(open(os.path.join(SRC, fn + ".ttf"), "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url(data:font/ttf;base64,{b}) format('truetype');}}")
    return "\n".join(out)


PHONE, WEB = "+000 000 000 0000", "secsaway.com"  # placeholders — replace before posting

CSS = f"""
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #555; }}
.fl {{ width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Archivo', sans-serif; }}
.a {{ position: absolute; }}
.mono {{ font-family: 'IBM Plex Mono', monospace; font-weight: 500; text-transform: uppercase; letter-spacing: .14em; }}
.x {{ font-family: 'Archivo XCond'; font-style: italic; font-weight: 900; line-height: .84; white-space: nowrap; }}
.li {{ font-style: italic; font-weight: 300; }}
.bar {{ display: inline-block; padding: 6px 22px 2px 16px; margin-bottom: 8px; }}
.cut {{ filter: drop-shadow(0 26px 30px rgba(10,20,35,.35)); }}
"""

# ---------- A: ON TIME. ----------
A = f'''
<section class="fl" style="background:{ORANGE}">
  <div class="a x fit" data-w="1190" style="left:-22px;top:34px;color:{NAVY}">ON TIME.</div>
  <div class="a" style="left:-260px;top:1010px;width:1700px;height:620px;background:{NAVY};transform:rotate(-11deg);transform-origin:0 0"></div>
  <img class="a cut" src="{img(os.path.join(P1, '31_driver_cut.png'))}" style="left:300px;top:196px;height:1154px">
  <div class="a" style="left:46px;top:640px;transform:rotate(-6deg);transform-origin:0 0">
    <div><span class="bar x" style="font-size:82px;background:{WHITE};color:{NAVY}">COLLECTED</span></div>
    <div><span class="bar x" style="font-size:82px;background:{WHITE};color:{NAVY}">TODAY.</span></div>
    <div><span class="bar x" style="font-size:82px;background:{INK};color:{ORANGE}">DELIVERED</span></div>
    <div><span class="bar x" style="font-size:82px;background:{INK};color:{ORANGE}">AS PROMISED.</span></div>
  </div>
  <div class="a" style="left:56px;top:1218px">{lockup(250, ORANGE, WHITE)}</div>
  <div class="a mono" style="left:58px;top:1290px;font-size:14px;color:{WHITE};letter-spacing:.1em;opacity:.85">{PHONE} · {WEB}</div>
</section>'''

# ---------- B: One partner. Every route. (slanted photo strips) ----------
strips = [(os.path.join(P2, "21_highway.jpg"), "Road", "50% 50%"), (os.path.join(P2, "25_port.jpg"), "Sea", "62% 50%"),
          (os.path.join(P1, "41_air.jpg"), "Air", "40% 50%"), (os.path.join(P1, "32_scanner.jpg"), "Storage", "45% 40%"),
          (os.path.join(P2, "22_handover.jpg"), "Last mile", "18% 50%")]
sw, sk, gap, sh, top = 196, 60, 12, 600, 468
x0 = (1080 - (5 * sw + 4 * gap + sk)) / 2
stp = ""
for i, (p, label, pos) in enumerate(strips):
    x = x0 + i * (sw + gap)
    dy = (-26, 18, -10, 26, -18)[i]
    stp += (f'<div class="a" style="left:{x:.0f}px;top:{top + dy}px;width:{sw + sk}px;height:{sh}px;'
            f'clip-path:polygon({sk}px 0,100% 0,{sw}px 100%,0 100%);background:url({img(p)}) {pos}/cover"></div>'
            f'<div class="a mono" style="left:{x + 14:.0f}px;top:{top + sh + 46}px;font-size:14px;color:{WHITE}">'
            f'<span style="color:{ORANGE}">0{i + 1}</span>&nbsp; {label}</div>')
B = f'''
<section class="fl" style="background:{NAVY}">
  <div class="a" style="left:60px;top:60px">{lockup(210, ORANGE, WHITE)}</div>
  <div class="a mono" style="right:60px;top:70px;font-size:13px;color:{MUTE}">Freight & logistics</div>
  <div class="a li" style="left:58px;top:150px;font-size:66px;color:{WHITE};letter-spacing:-.02em">One partner.</div>
  <div class="a x fit" data-w="966" style="left:56px;top:236px;color:{ORANGE}">EVERY ROUTE.</div>
  {stp}
  <div class="a" style="left:0;top:1192px;width:1080px;text-align:center">
    <div style="font-style:italic;font-weight:500;font-size:30px;color:{WHITE};letter-spacing:-.01em">Road, sea and air — handled by one team, end to end.</div>
    <div class="mono" style="display:inline-block;margin-top:26px;background:{ORANGE};color:{INK};font-size:16px;padding:14px 26px;letter-spacing:.08em">Request a quote · {PHONE}</div>
  </div>
</section>'''

# ---------- C: Your freight, in safe hands. (diagonal band + callouts) ----------
def tag(x, y, t, side="L"):
    dot = f'<span style="width:12px;height:12px;border-radius:6px;background:{ORANGE};flex:none"></span>'
    inner = f'{dot}<span>{t}</span>' if side == "L" else f'<span>{t}</span>{dot}'
    return (f'<div class="a" style="left:{x}px;top:{y}px;display:flex;align-items:center;gap:12px;background:rgba(15,43,70,.9);'
            f'border:1.5px solid rgba(255,255,255,.18);padding:12px 18px;font-size:21px;font-weight:600;color:{WHITE}">{inner}</div>')


C = f'''
<section class="fl" style="background:{NAVY}">
  <div class="a x" style="left:-40px;top:300px;font-size:560px;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.14)">SAFE</div>
  <div class="a" style="left:-300px;top:820px;width:1800px;height:300px;background:{ORANGE};transform:rotate(-14deg);transform-origin:50% 50%"></div>
  <img class="a cut" src="{img(os.path.join(P1, '33_hivis_cut.png'))}" style="left:84px;top:290px;height:1060px">
  <div class="a li" style="left:58px;top:58px;font-size:56px;color:{WHITE};letter-spacing:-.02em">Your freight,</div>
  <div class="a x" style="left:52px;top:128px;font-size:150px;color:{WHITE}">IN <span style="color:{ORANGE}">SAFE</span> HANDS.</div>
  <div class="a" style="right:58px;top:70px">{lockup(170, ORANGE, WHITE)}</div>
  {tag(40, 560, "Live tracking")}
  {tag(40, 650, "Signed handover")}
  {tag(800, 540, "Customs in-house", "R")}
  {tag(812, 630, "Road · Sea · Air", "R")}
  <div class="a" style="left:0;top:1262px;width:1080px;height:88px;background:{WHITE};display:flex;align-items:center;justify-content:space-between;padding:0 58px">
    <span class="mono" style="font-size:15px;color:{NAVY};letter-spacing:.08em">Request a quote</span>
    <span class="mono" style="font-size:15px;color:{NAVY};letter-spacing:.08em">{PHONE} · {WEB}</span>
  </div>
</section>'''

FIT = """<script>document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(el=>{el.style.fontSize='100px';
el.style.fontSize=(100*(+el.dataset.w)/el.getBoundingClientRect().width)+'px';});document.body.dataset.ready=1;});</script>"""
open(os.path.join(HERE, "flyers_v3.html"), "w").write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts()}{CSS}</style></head><body>{A}{B}{C}{FIT}</body></html>')
print("ok")
