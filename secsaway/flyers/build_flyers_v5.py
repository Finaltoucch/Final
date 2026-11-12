"""Secsaway flyers v5 — follows the user's three Pinterest references closely
(Substrates rail layout, VisionNav top-down route layout, Accentric new-month layout)."""
import base64, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_flyers_v4 import lockup, fonts, homography, sub_quad, NAVY, ORANGE, INK, WHITE, PH  # noqa: E402

W, H = 1080, 1350
INKT = "#111418"
PHONE, WEB, EMAIL = "+000 000 000 0000", "www.secsaway.com", "hello@secsaway.com"  # placeholders


def img(fn):
    return "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(PH, fn), "rb").read()).decode()


ARROW = f'<svg width="20" height="20" viewBox="0 0 20 20"><path d="M5 15L15 5M7 5H15V13" fill="none" stroke="{INKT}" stroke-width="2.2"/></svg>'
WA = (f'<svg width="30" height="30" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="none" stroke="{ORANGE}" stroke-width="2.4"/>'
      f'<path d="M11 9.5H14L15.4 13L13.6 14.2C14.4 16 16 17.6 17.8 18.4L19 16.6L22.5 18V21C22.5 22 21.7 22.5 21 22.5C14.6 22.5 9.5 17.4 9.5 11C9.5 10.2 10.1 9.5 11 9.5Z" fill="{ORANGE}"/></svg>')


def circ(path):
    return f'<svg width="34" height="34" viewBox="0 0 34 34"><circle cx="17" cy="17" r="17" fill="{NAVY}"/><g transform="translate(5,5)" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round">{path}</g></svg>'


I_PHONE = circ('<path d="M5 3H9L11 8L8.5 9.5C9.6 11.8 12.2 14.4 14.5 15.5L16 13L21 15V19C21 20.1 20.1 21 19 21C10.2 21 3 13.8 3 5C3 3.9 3.9 3 5 3Z" transform="scale(.9) translate(1,1)"/>')
I_MAIL = circ('<rect x="3" y="6" width="18" height="12" rx="1.5"/><path d="M3.5 7L12 13L20.5 7"/>')
I_WEB = circ('<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12H20.5M12 3.5C14.6 6.5 14.6 17.5 12 20.5M12 3.5C9.4 6.5 9.4 17.5 12 20.5"/>')

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #555; }
.fl { width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Archivo', sans-serif; background: #fff; }
.a { position: absolute; }
.hl { font-family: 'Archivo XC'; font-weight: 900; line-height: .9; text-transform: uppercase; }
.big { font-family: 'Archivo'; font-weight: 800; letter-spacing: -.055em; line-height: .95; }
.track { letter-spacing: .32em; font-weight: 600; font-size: 17px; }
"""

# ---------- 1. Rail (Substrates layout) ----------
oy = 120  # photo pushed down to open white space at top
side = [(0.611 * W, 0.288 * H + oy), (0.868 * W, 0.324 * H + oy), (0.868 * W, 0.442 * H + oy), (0.611 * W, 0.447 * H + oy)]
lw = 300; lh = lw * 120 / 700.44
m1 = homography(lw, lh, sub_quad(side, 0.08, 0.92, 0.30, 0.66))
F1 = f'''
<section class="fl">
  <img class="a" src="{img('61_rail.jpg')}" style="left:0;top:{oy}px;width:{W}px;height:{H}px">
  <div class="a" style="left:0;top:0;width:{lw}px;height:{lh:.1f}px;transform-origin:0 0;transform:{m1};opacity:.95">{lockup(lw, ORANGE, WHITE)}</div>
  <div class="a" style="left:0;top:1040px;width:{W}px;height:310px;background:linear-gradient(to bottom,rgba(255,255,255,0),#fff 42%)"></div>
  <div class="a" style="left:0;top:52px;width:{W}px;display:flex;justify-content:center">{lockup(260, ORANGE, INKT)}</div>
  <div class="a" style="left:62px;top:150px">
    <div class="hl" style="font-size:136px;color:{INKT}">Never<br>go off<br>route.</div>
    <div style="width:96px;height:6px;background:{ORANGE};margin-top:34px"></div>
    <p style="font-size:24px;line-height:1.42;color:{INKT};margin-top:28px;width:410px">At <b>SECSAWAY</b>, we keep your freight moving forward with careful planning, live tracking and signed handovers.</p>
    <p style="font-size:24px;line-height:1.42;color:{INKT};margin-top:20px">Clear routes.<br>On-time delivery.</p>
  </div>
  <div class="a" style="left:60px;right:60px;top:1204px;display:flex;align-items:center;gap:26px">
    <div style="flex:1;height:1.5px;background:{INKT};opacity:.35"></div>
    <div class="track" style="color:{INKT}">ROAD. <span style="color:{ORANGE}">SEA.</span> AIR.</div>
    <div style="flex:1;height:1.5px;background:{INKT};opacity:.35"></div>
  </div>
  <div class="a" style="left:0;top:1262px;width:{W}px;display:flex;justify-content:center;align-items:center;gap:30px;font-size:22px;color:{INKT}">
    <span style="display:flex;align-items:center;gap:10px;font-weight:600">{ARROW} Visit</span><span>{WEB}</span>
    <span style="width:1.5px;height:34px;background:{INKT};opacity:.35"></span>
    <span style="display:flex;align-items:center;gap:12px">{WA}{PHONE}</span>
  </div>
</section>'''

# ---------- 2. Forklift route (VisionNav layout) ----------
F2 = f'''
<section class="fl">
  <img class="a" src="{img('62_forklift.jpg')}" style="left:0;top:0;width:{W}px;height:{H}px">
  <div class="a" style="left:66px;top:560px">
    <div class="hl" style="font-size:104px;color:{INKT}">Every pallet,<br>every parcel</div>
    <div class="hl" style="font-size:104px;color:{ORANGE};margin-top:8px">always<br>accounted for.</div>
    <div style="width:64px;height:5px;background:{ORANGE};margin-top:40px"></div>
    <p style="font-size:26px;line-height:1.45;color:#2A2F35;margin-top:30px;width:520px">Warehousing you can see in real time, from receiving to dispatch.</p>
  </div>
  <div class="a" style="left:66px;top:1226px">{lockup(270, ORANGE, NAVY)}</div>
</section>'''

# ---------- 3. New month (Accentric layout) ----------
SWOOSH = (f'<svg width="330" height="34" viewBox="0 0 330 34"><path d="M6 14C90 6 220 4 322 10" fill="none" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round"/>'
          f'<path d="M40 27C120 21 210 20 286 24" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/></svg>')
F3 = f'''
<section class="fl">
  <img class="a" src="{img('63_flatbed.jpg')}" style="left:0;top:0;width:{W}px;height:{H}px">
  <div class="a" style="left:76px;top:78px;background:#fff;border:1.5px solid #DCE6F0;border-radius:12px;padding:18px 24px;box-shadow:0 6px 18px rgba(15,43,70,.10)">{lockup(200, ORANGE, NAVY)}</div>
  <div class="a" style="right:76px;top:94px;background:{NAVY};color:#fff;border-radius:30px;padding:11px 20px;font-size:16px;font-weight:600;display:flex;align-items:center;gap:10px">
    <span style="width:10px;height:10px;border-radius:5px;background:{ORANGE}"></span>Road · Sea · Air</div>
  <div class="a big" style="left:72px;top:230px;font-size:138px;color:{NAVY}">December<br>in Motion</div>
  <div class="a" style="left:80px;top:500px">{SWOOSH}</div>
  <p class="a" style="left:78px;top:560px;width:640px;font-size:24px;line-height:1.42;color:{INKT}">This <b>December</b>, let <b>Secsaway</b> keep your logistics moving with dependable freight services built on precision and commitment.</p>
  <div class="a" style="left:760px;top:700px;background:{ORANGE};color:#fff;border-radius:24px;padding:11px 20px;font-size:17px;font-weight:600">Happy New Month</div>
  <div class="a" style="left:0;top:1196px;width:{W}px;height:154px;background:#fff;border-top:3px solid {NAVY}"></div>
  <div class="a" style="left:76px;top:1170px;background:{NAVY};color:#fff;font-size:20px;font-weight:800;padding:12px 22px;letter-spacing:-.01em">CONTACT US</div>
  <div class="a" style="left:76px;right:76px;top:1256px;display:flex;justify-content:space-between;align-items:center;font-size:21px;color:{INKT};font-weight:600">
    <span style="display:flex;align-items:center;gap:12px">{I_PHONE}{PHONE}</span>
    <span style="display:flex;align-items:center;gap:12px">{I_MAIL}{EMAIL}</span>
    <span style="display:flex;align-items:center;gap:12px">{I_WEB}{WEB}</span>
  </div>
</section>'''

def fonts_v5():
    b = base64.b64encode(open(os.path.join(os.path.dirname(PH), "..", "src", "Archivo800.ttf"), "rb").read()).decode()
    return fonts() + f"@font-face{{font-family:'Archivo';font-weight:800;src:url(data:font/ttf;base64,{b}) format('truetype');}}"


HERE = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(HERE, "flyers_v5.html"), "w").write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts_v5()}{CSS}</style></head><body>{F1}{F2}{F3}'
    '<script>document.fonts.ready.then(()=>document.body.dataset.ready=1)</script></body></html>')
print("ok")
