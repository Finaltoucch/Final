# Write the HyperFrames composition (index.html) for the trailer from tl.json.
# usage: python3 hf_trailer_html.py tl.json PROJECT_DIR/index.html
import json,sys
TL=json.load(open(sys.argv[1]));TOTAL=round(TL[-1]['start']+TL[-1]['dur'],4)
f=lambda x:f"{x:.4f}"
els=[];js=[];nflash=[0]
for s in TL:
  i,st,d=s['i'],s['start'],s['dur']
  if s['type']=='clip':
    els.append(f'<video id="v{i:02d}" class="clip shot" src="{s["src"]}" muted playsinline data-start="{f(st)}" data-duration="{f(d)}" data-media-start="0" data-track-index="1"></video>')
    js.append(f'tl.fromTo("#v{i:02d}",{{scale:1.0}},{{scale:1.045,duration:{f(d)},ease:"none"}},{f(st)});')
  elif s['type']=='card':
    cls='card studio' if s.get('style')=='studio' else 'card'
    els.append(f'<div id="k{i:02d}" class="clip {cls}" data-start="{f(st)}" data-duration="{f(d)}" data-track-index="2"><h1>{s["text"]}</h1></div>')
    js.append(f'tl.fromTo("#k{i:02d} h1",{{opacity:0,scale:1.14,filter:"blur(12px)"}},{{opacity:1,scale:1.0,filter:"blur(0px)",duration:0.65,ease:"power3.out"}},{f(st)});')
    js.append(f'tl.to("#k{i:02d} h1",{{scale:0.97,duration:{f(max(0.01,d-0.65))},ease:"none"}},{f(st+0.65)});')
    js.append(f'tl.to("#k{i:02d} h1",{{opacity:0,filter:"blur(6px)",duration:0.35,ease:"power2.in"}},{f(st+d-0.35)});')
  elif s['type']=='poster':
    els.append(f'<div id="poster" class="clip" data-start="{f(st)}" data-duration="{f(d)}" data-track-index="3"><img id="pimg" src="assets/poster.jpg"/><div id="sweep"></div></div>')
    js.append(f'tl.fromTo("#pimg",{{scale:1.0}},{{scale:1.055,duration:{f(d)},ease:"power1.out"}},{f(st)});')
    js.append(f'tl.fromTo("#sweep",{{xPercent:-120,opacity:0}},{{xPercent:120,opacity:1,duration:1.4,ease:"power2.inOut"}},{f(st+0.7)});')
    js.append(f'tl.to(".bar",{{height:0,duration:0.5,ease:"power2.out"}},{f(st)});')
    js.append(f'tl.fromTo("#fadeout",{{opacity:0}},{{opacity:1,duration:0.7,ease:"power1.in"}},{f(st+d-0.7)});')
  if s.get('flash') is not None:
    t=st+s['flash']
    ir='' if nflash[0]==0 else ',immediateRender:false';nflash[0]+=1
    js.append(f'tl.fromTo("#flash",{{opacity:0}},{{opacity:0.85,duration:0.04,ease:"none"{ir}}},{f(t)});')
    js.append(f'tl.to("#flash",{{opacity:0,duration:0.32,ease:"power2.out"}},{f(t+0.04)});')
html=f'''<!doctype html>
<html lang="en" data-resolution="landscape">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Cinzel"; src: url("assets/Cinzel.ttf"); font-weight: 400 900; }}
      :root {{ --ground: #000; --ink: #f4e7c6; --gold-hi: #fff3cf; --gold: #d8b25a; --gold-lo: #8a6420; --font-display: "Cinzel", serif; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: var(--ground); }}
      #root {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--ground); font-family: var(--font-display); }}
      .clip {{ position: absolute; inset: 0; width: 1920px; height: 1080px; }}
      .shot {{ object-fit: cover; z-index: 1; transform-origin: 50% 50%; }}
      .card {{ z-index: 3; display: flex; align-items: center; justify-content: center; background: #000; }}
      .card h1 {{ font-size: 84px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.24em; padding-left: 0.24em;
                 background: linear-gradient(180deg, var(--gold-hi) 0%, var(--gold) 55%, var(--gold-lo) 100%);
                 -webkit-background-clip: text; background-clip: text; color: transparent;
                 filter: drop-shadow(0 0 18px rgba(216,178,90,0.35)); }}
      .card.studio h1 {{ font-size: 40px; font-weight: 500; letter-spacing: 0.55em; padding-left: 0.55em;
                 background: linear-gradient(180deg, #ffffff 0%, #c9c9c9 100%); -webkit-background-clip: text; background-clip: text; }}
      #poster {{ z-index: 4; overflow: hidden; background: #000; }}
      #pimg {{ position: absolute; inset: 0; width: 1920px; height: 1080px; object-fit: cover; transform-origin: 50% 100%; }}
      #sweep {{ position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; mix-blend-mode: screen;
               background: linear-gradient(105deg, rgba(255,240,200,0) 40%, rgba(255,240,200,0.35) 50%, rgba(255,240,200,0) 60%); }}
      .bar {{ position: absolute; left: 0; width: 1920px; height: 138px; background: #000; z-index: 6; }}
      #bar-top {{ top: 0; }} #bar-bot {{ bottom: 0; }}
      #flash {{ position: absolute; inset: 0; background: #fff8ec; opacity: 0; z-index: 8; }}
      #fadeout {{ position: absolute; inset: 0; background: #000; opacity: 0; z-index: 9; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{f(TOTAL)}" data-width="1920" data-height="1080">
      {chr(10).join("      "+e for e in els).strip()}
      <audio id="mix" class="clip" src="assets/mix.wav" data-start="0" data-duration="{f(TOTAL)}" data-has-audio="true" data-track-index="4"></audio>
      <div id="bar-top" class="bar"></div>
      <div id="bar-bot" class="bar"></div>
      <div id="flash"></div>
      <div id="fadeout"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join("      "+j for j in js).strip()}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
open(sys.argv[2],'w').write(html);print('HTML',TOTAL,len(els))
