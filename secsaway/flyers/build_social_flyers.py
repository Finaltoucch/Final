"""Three 4:5 Secsaway flyers in the bold bold social style, full-colour photography."""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "src")
PH = os.path.join(HERE, "photos")

NAVY, ORANGE, INK, PAPER, WHITE, MUTE, TONE = "#0F2B46", "#E8551C", "#14181C", "#F4F4F1", "#FFFFFF", "#8FA3B6", "#1B4166"

ICON_D = ("M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
          "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z")
with open(os.path.join(SRC, "wordmark.txt")) as f:
    wm_w, wm_cap = map(float, f.readline().split())
    WM_D = f.read().strip()
LOCK_W = 120 + 40 + 60 * wm_w / wm_cap


def lockup(width, ic, wc):
    h = width * 120 / LOCK_W
    s = 60 / wm_cap
    return (f'<svg width="{width:.1f}" height="{h:.1f}" viewBox="0 0 {LOCK_W:.2f} 120"><path d="{ICON_D}" fill="{ic}"/>'
            f'<g transform="translate(160,30) scale({s:.6f})"><path d="{WM_D}" fill="{wc}"/></g></svg>')


def data(fn, mime):
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(PH, fn), "rb").read()).decode()


def fonts():
    out = []
    for fam, w, st, fn in [("Archivo", 400, "normal", "Archivo400"), ("Archivo", 600, "normal", "Archivo600"),
                           ("Archivo", 800, "normal", "Archivo800"), ("Archivo XCond", 900, "italic", "ArchivoXCondBlackItalic"),
                           ("Archivo Cond", 800, "italic", "ArchivoCondExtraBoldItalic"),
                           ("IBM Plex Mono", 500, "normal", "IBMPlexMono500")]:
        b = base64.b64encode(open(os.path.join(SRC, fn + ".ttf"), "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url(data:font/ttf;base64,{b}) format('truetype');}}")
    return "\n".join(out)


TICK = f'<svg width="14" height="14" viewBox="0 0 14 14"><path d="M2.5 7.5L5.5 10.5L11.5 3.5" fill="none" stroke="{WHITE}" stroke-width="2.4"/></svg>'


def check(label, on=True, size=26, color=WHITE):
    box = (f'<span style="width:26px;height:26px;flex:none;display:inline-flex;align-items:center;justify-content:center;'
           f'background:{ORANGE if on else "transparent"};border:2px solid {ORANGE}">{TICK if on else ""}</span>')
    return f'<div style="display:flex;align-items:center;gap:16px;font-size:{size}px;font-weight:600;color:{color};letter-spacing:-.01em">{box}{label}</div>'


PHONE, WEB = "+000 000 000 0000", "secsaway.com"  # placeholders: replace before posting

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #666; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.fl { width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Archivo', sans-serif; }
.a { position: absolute; }
.mono { font-family: 'IBM Plex Mono', monospace; font-weight: 500; text-transform: uppercase; letter-spacing: .14em; }
.giant { font-family: 'Archivo XCond'; font-style: italic; font-weight: 900; line-height: .82; white-space: nowrap; letter-spacing: -.01em; }
.cond { font-family: 'Archivo Cond'; font-style: italic; font-weight: 800; letter-spacing: -.01em; }
"""

# 1 — ON TIME. (orange field, cutout in front of giant type)
f1 = f'''
<section class="fl" style="background:{ORANGE}">
  <div class="a giant fit" data-w="1010" style="left:34px;top:70px;color:{NAVY}">ON TIME.</div>
  <img class="a" src="{data('31_driver_cut.png','image/png')}" style="left:350px;top:236px;height:1114px">
  <div class="a" style="left:60px;top:700px;width:430px;background:rgba(15,43,70,.92);padding:34px 34px 30px">
    <div class="mono" style="font-size:15px;color:{ORANGE}">This week's promise</div>
    <div style="font-size:24px;line-height:1.35;color:{WHITE};margin-top:14px;font-weight:600">Collected today. Delivered on the day we quote.</div>
    <div style="display:grid;gap:16px;margin-top:26px">
      {check("Pickup booked", True, 22)}{check("Waybill issued", True, 22)}{check("Tracked live", True, 22)}{check("Signed handover", False, 22)}
    </div>
  </div>
  <div class="a" style="left:60px;top:1196px">{lockup(250, NAVY, NAVY)}</div>
  <div class="a mono" style="left:60px;top:1268px;font-size:15px;color:{NAVY};letter-spacing:.08em">{PHONE} · {WEB}</div>
</section>'''

# 2 — Ready to ship this week? (full B/W photo, dark checklist card)
f2 = f'''
<section class="fl" style="background:{INK}">
  <img class="a" src="{data('32_scanner.jpg','image/jpeg')}" style="left:-13px;top:-120px;width:1560px;height:1950px">
  <div class="a" style="left:0;top:0;width:1080px;height:1350px;background:rgba(15,43,70,.18)"></div>
  <div class="a" style="left:60px;top:60px">{lockup(220, ORANGE, WHITE)}</div>
  <div class="a cond" style="left:60px;top:150px;font-size:96px;line-height:.98;color:{WHITE}">Ready to<br><span style="color:{ORANGE}">ship</span> this<br>week?</div>
  <div class="a" style="left:540px;top:780px;width:480px;background:rgba(15,43,70,.82);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);padding:36px 36px 34px;border-top:6px solid {ORANGE}">
    <div class="mono" style="font-size:15px;color:{MUTE}">Your shipping checklist</div>
    <div style="display:grid;gap:20px;margin-top:24px">
      {check("Book a pickup")}{check("Print the waybill")}{check("Seal and label")}{check("Track it live")}{check("Get a signed handover")}
    </div>
  </div>
  <div class="a mono" style="left:60px;top:1262px;font-size:16px;color:{WHITE};letter-spacing:.08em">We handle every step &nbsp;·&nbsp; {WEB}</div>
</section>'''

# 3 — 5 reasons / IN SAFE HANDS (navy field, giant type behind cutout, callouts)
callouts = [  # (x, y, text, side, line-to-x)
    (60, 470, "Live tracking<br>at every stage", "L"),
    (60, 700, "Signed handover<br>on delivery", "L"),
    (60, 930, "Customs handled<br>in-house", "L"),
    (790, 300, "Road, sea and air<br>under one team", "R"),
    (790, 470, "Secure<br>warehousing", "R"),
]
co = ""
for x, y, t, side in callouts:
    if side == "L":
        co += (f'<div class="a" style="left:{x}px;top:{y}px;width:230px;text-align:left">'
               f'<div style="font-size:23px;line-height:1.25;font-weight:600;color:{WHITE}">{t}</div></div>'
               f'<div class="a" style="left:{x}px;top:{y+70}px;width:190px;height:2px;background:{ORANGE}"></div>'
               f'<div class="a" style="left:{x+184}px;top:{y+65}px;width:12px;height:12px;border-radius:6px;background:{ORANGE}"></div>')
    else:
        co += (f'<div class="a" style="left:{x}px;top:{y}px;width:230px;text-align:right">'
               f'<div style="font-size:23px;line-height:1.25;font-weight:600;color:{WHITE}">{t}</div></div>'
               f'<div class="a" style="left:{x+40}px;top:{y+70}px;width:190px;height:2px;background:{ORANGE}"></div>'
               f'<div class="a" style="left:{x+34}px;top:{y+65}px;width:12px;height:12px;border-radius:6px;background:{ORANGE}"></div>')
f3 = f'''
<section class="fl" style="background:{NAVY}">
  <div class="a mono" style="left:0;top:70px;width:1080px;text-align:center;font-size:17px;color:{WHITE}">5 reasons to ship with us</div>
  <div class="a giant fit" data-w="1010" style="left:34px;top:120px;color:{ORANGE}">SAFE HANDS.</div>
  <img class="a" src="{data('33_hivis_cut.png','image/png')}" style="left:178px;top:262px;height:1088px">
  {co}
  <div class="a" style="left:0;top:1250px;width:1080px;height:100px;background:{ORANGE};display:flex;align-items:center;justify-content:space-between;padding:0 60px">
    {lockup(230, NAVY, NAVY)}
    <span class="mono" style="font-size:16px;color:{INK};letter-spacing:.08em">Request a quote · {PHONE}</span>
  </div>
</section>'''

FIT = """<script>
document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(el=>{const t=+el.dataset.w;let s=100;el.style.fontSize=s+'px';s=s*t/el.getBoundingClientRect().width;el.style.fontSize=s+'px';});document.body.dataset.ready=1;});
</script>"""

html = (f'<!doctype html><html><head><meta charset="utf-8"><title>Secsaway Social Flyers</title><style>{fonts()}{CSS}</style></head>'
        f'<body>{f1}{f2}{f3}{FIT}</body></html>')
open(os.path.join(HERE, "social_flyers.html"), "w").write(html)
print("ok")
