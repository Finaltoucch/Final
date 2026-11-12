"""Secsaway flyers v4 — clean conceptual style: one strong photo idea, bold condensed headline with an
orange accent line, short copy, contact strip. Vector logo applied onto surfaces (perspective-mapped)."""
import base64, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "src")
PH = os.path.join(HERE, "photos")
NAVY, ORANGE, INK, PAPER, WHITE, CONCRETE = "#0F2B46", "#E8551C", "#14181C", "#F4F4F1", "#FFFFFF", "#646C75"
ICON_D = ("M120 0H35A35 35 0 0 0 35 70H50V50H35A15 15 0 0 1 35 20H120Z"
          "M0 120H85A35 35 0 0 0 85 50H70V70H85A15 15 0 0 1 85 100H0Z")
with open(os.path.join(SRC, "wordmark.txt")) as f:
    wm_w, wm_cap = map(float, f.readline().split())
    WM_D = f.read().strip()
LOCK_W = 120 + 40 + 60 * wm_w / wm_cap
W, H = 1080, 1350


def lockup(width, ic, wc, style=""):
    h = width * 120 / LOCK_W
    return (f'<svg width="{width:.1f}" height="{h:.1f}" viewBox="0 0 {LOCK_W:.2f} 120" style="display:block;{style}">'
            f'<path d="{ICON_D}" fill="{ic}"/><g transform="translate(160,30) scale({60 / wm_cap:.6f})"><path d="{WM_D}" fill="{wc}"/></g></svg>')


def img(fn):
    return "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(PH, fn), "rb").read()).decode()


def fonts():
    out = []
    for fam, w, fn in [("Archivo", 400, "Archivo400"), ("Archivo", 600, "Archivo600"), ("Archivo XC", 900, "ArchivoXCondBlack"),
                       ("IBM Plex Mono", 500, "IBMPlexMono500")]:
        b = base64.b64encode(open(os.path.join(SRC, fn + ".ttf"), "rb").read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/ttf;base64,{b}) format('truetype');}}")
    return "\n".join(out)


def homography(w, h, quad):
    """CSS matrix3d mapping rect (0,0,w,h) onto quad [(x0,y0) TL, TR, BR, BL]."""
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    A, b = [], []
    for (x, y), (u, v) in zip(src, quad):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    a, bb, c, d, e, f, g, hh = np.linalg.solve(np.array(A, float), np.array(b, float))
    m = [a, d, 0, g, bb, e, 0, hh, 0, 0, 1, 0, c, f, 0, 1]
    return "matrix3d(" + ",".join(f"{v:.8f}" for v in m) + ")"


def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def sub_quad(quad, u0, u1, v0, v1):
    tl, tr, br, bl = quad
    top0, top1 = lerp(tl, tr, u0), lerp(tl, tr, u1)
    bot0, bot1 = lerp(bl, br, u0), lerp(bl, br, u1)
    return [lerp(top0, bot0, v0), lerp(top1, bot1, v0), lerp(top1, bot1, v1), lerp(top0, bot0, v1)]


GLOBE = f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{NAVY}" stroke-width="1.8"><circle cx="12" cy="12" r="9.5"/><path d="M2.5 12H21.5M12 2.5C15 6 15 18 12 21.5M12 2.5C9 6 9 18 12 21.5"/></svg>'
PHONE_I = f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-linejoin="round"><path d="M5 3H9L11 8L8.5 9.5C9.6 11.8 12.2 14.4 14.5 15.5L16 13L21 15V19C21 20.1 20.1 21 19 21C10.2 21 3 13.8 3 5C3 3.9 3.9 3 5 3Z"/></svg>'
PHONE, WEB = "+000 000 000 0000", "www.secsaway.com"  # placeholders — replace before posting


def footer():
    return f'''<div class="a" style="left:0;top:1206px;width:{W}px;height:144px;background:{WHITE}">
  <div class="a" style="left:60px;right:60px;top:30px;display:flex;align-items:center;gap:22px">
    <div style="flex:1;height:1.5px;background:{INK};opacity:.25"></div>
    <div class="mono" style="font-size:15px;color:{INK}">ROAD. <span style="color:{ORANGE}">SEA.</span> AIR.</div>
    <div style="flex:1;height:1.5px;background:{INK};opacity:.25"></div></div>
  <div class="a" style="left:60px;right:60px;top:78px;display:flex;align-items:center;justify-content:space-between">
    <div style="display:flex;align-items:center;gap:12px;font-size:21px;color:{INK}">{GLOBE}{WEB}</div>
    <div style="width:1.5px;height:34px;background:{INK};opacity:.25"></div>
    <div style="display:flex;align-items:center;gap:12px;font-size:21px;color:{INK}">{PHONE_I}{PHONE}</div>
    <div style="width:1.5px;height:34px;background:{INK};opacity:.25"></div>
    {lockup(150, ORANGE, NAVY)}
  </div></div>'''


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #555; }
.fl { width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Archivo', sans-serif; }
.a { position: absolute; }
.mono { font-family: 'IBM Plex Mono', monospace; font-weight: 500; letter-spacing: .3em; }
.hl { font-family: 'Archivo XC'; font-weight: 900; line-height: .9; letter-spacing: -.005em; text-transform: uppercase; }
.body { font-size: 23px; line-height: 1.45; }
.rule { width: 74px; height: 5px; background: #E8551C; }
.paint { mix-blend-mode: normal; }
"""

# --- 1: Route (top-down) ---
# van roof (fractions of 1080x1350): x .70-.81, y .645-.85 ; lockup rotated to run along the roof
rx, ry = 0.755 * W, 0.748 * H
F1 = f'''
<section class="fl" style="background:{PAPER}">
  <img class="a" src="{img('51_route.jpg')}" style="left:0;top:0;width:{W}px;height:{H}px">
  <div class="a" style="left:{rx}px;top:{ry}px;transform:translate(-50%,-50%) rotate(-90deg);opacity:.95">{lockup(222, ORANGE, WHITE)}</div>
  <div class="a" style="left:62px;top:330px;width:560px">
    <div class="hl" style="font-size:104px;color:{INK}">The shortest<br>route is the</div>
    <div class="hl" style="font-size:104px;color:{ORANGE};margin-top:6px">one we<br>planned.</div>
    <div class="rule" style="margin-top:38px"></div>
    <p class="body" style="color:#2B3138;margin-top:30px;width:400px">Every pickup, turn and handover is mapped before your goods move. No guesswork, no detours.</p>
  </div>
  {footer()}
</section>'''

# --- 2: Container (flat side panel): x .44-.965, y .43-.60 ---
cx, cy = 0.703 * W, 0.515 * H
F2 = f'''
<section class="fl" style="background:#C9D6E6">
  <img class="a" src="{img('52_container.jpg')}" style="left:0;top:0;width:{W}px;height:{H}px">
  <div class="a" style="left:{cx}px;top:{cy}px;transform:translate(-50%,-50%);opacity:.93">{lockup(330, ORANGE, WHITE)}</div>
  <div class="a" style="left:62px;top:96px">{lockup(210, ORANGE, NAVY)}</div>
  <div class="a" style="left:62px;top:196px">
    <div class="hl" style="font-size:104px;color:{NAVY}">Handled<br>with</div>
    <div class="hl" style="font-size:104px;color:{ORANGE}">precision.</div>
  </div>
  <div class="a" style="left:62px;top:840px;width:400px">
    <div class="rule"></div>
    <p class="body" style="color:{NAVY};margin-top:28px">From port to door, every lift, load and handover is planned, checked and recorded.</p>
    <p class="body" style="color:{NAVY};margin-top:18px;font-weight:600">Clear process.<br>Careful hands.</p>
  </div>
  {footer()}
</section>'''

# --- 3: Truck (perspective trailer side) ---
quad = [(0.382 * W, 0.442 * H), (0.976 * W, 0.507 * H), (0.976 * W, 0.650 * H), (0.382 * W, 0.660 * H)]
lw = 420; lh = lw * 120 / LOCK_W
q = sub_quad(quad, 0.10, 0.62, 0.36, 0.64)
m3 = homography(lw, lh, q)
F3 = f'''
<section class="fl" style="background:#7FB2E8">
  <img class="a" src="{img('53_truck.jpg')}" style="left:0;top:0;width:{W}px;height:{H}px">
  <div class="a" style="left:0;top:0;width:{lw}px;height:{lh:.1f}px;transform-origin:0 0;transform:{m3};opacity:.94">{lockup(lw, ORANGE, WHITE)}</div>
  <div class="a" style="left:62px;top:72px;background:{WHITE};padding:16px 22px">{lockup(190, ORANGE, NAVY)}</div>
  <div class="a" style="left:62px;top:196px">
    <div class="hl" style="font-size:138px;color:{NAVY}">December,</div>
    <div class="hl" style="font-size:138px;color:{ORANGE}">delivered.</div>
    <div class="rule" style="margin-top:26px;background:{NAVY}"></div>
    <p class="body" style="color:{NAVY};margin-top:24px;width:560px">A new month and a busy season. Let Secsaway move your freight on time, with every handover tracked and signed.</p>
  </div>
  <div class="a mono" style="left:744px;top:578px;background:{ORANGE};color:{WHITE};font-size:15px;letter-spacing:.12em;padding:12px 20px;border-radius:24px">HAPPY NEW MONTH</div>
  {footer()}
</section>'''

if __name__ == "__main__":
    open(os.path.join(HERE, "flyers_v4.html"), "w").write(
        f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts()}{CSS}</style></head><body>{F1}{F2}{F3}'
        '<script>document.fonts.ready.then(()=>document.body.dataset.ready=1)</script></body></html>')
    print("ok")
