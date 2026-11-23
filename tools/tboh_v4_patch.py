# Two Boys, One Heart: v4 review fixes (owner notes on v3).
# Patches the sandbox Part 1-4 edit lists (elx_v3.json -> elx.json).
# Rain ride: side-by-side two-shot. 6-03: side by side. 9-01, 13-03 and 16-23 are clean single-voice takes.
# 16-08 is split into two single-speaker clips.
import json
R={'p1b':{302:{"t":{"X":"20261123_083922_c59571ec-ae4c-4c4d-8b9a-1b1673b53b46"},"mute":[[0,30]],"gain":-6},
 303:{"t":{"X":"20261123_084315_c9de77e8-e87a-4763-97c9-32b80d44cd57"},"ss":2.9},
 304:{"t":{"X":"20261123_084319_a31ba7f9-187f-4243-bf4e-20d7953313aa"},"ss":1.7},
 305:{"t":{"X":"20261123_084415_7e0b4d02-ad88-43ec-b472-40b1a0c0ea4a"},"ss":0.5},
 306:{"t":{"X":"20261123_084928_c3920873-0cb2-4e37-9d02-907ba6ea80fd"},"mute":[[0,30]]},
 307:{"t":{"X":"20261123_085312_791d0fd5-8ba3-4b5d-934f-363f401d0843"},"ss":0.4},
 308:{"t":{"X":"20261123_085134_651661fa-89fd-4431-b1ff-b97edc76672a"},"ss":0.9},
 309:{"t":{"X":"20261123_085314_f44ca6d0-a1d1-4f0b-9015-07ed9cbe76e2"},"ss":0.5},
 310:{"t":{"X":"20261123_085309_175ffe53-7b4e-4f17-9730-5485927be5a4"},"ss":1.2},
 311:{"t":{"X":"20261123_085316_26e06c5f-7ac8-4d58-a861-ce45d976b106"},"ss":1.4},
 313:{"t":{"X":"20261123_085321_9e458d86-adc6-42dc-b9b4-8d5bfb3659dc"},"ss":0.9},
 314:{"t":{"X":"20261123_085139_12c37580-60b2-464b-8a37-b0320868a1bb"},"ss":0.9},
 315:{"t":{"X":"20261123_084139_2da63bf2-1915-4103-ae98-634628344a7d"},"mute":[[0,30]]},
 "X10":{"t":{"X":"20261123_084139_cd9a96b8-2644-4ab6-a2b7-b4ab8ca0bbda"},"mute":[[0,30]],"maxdur":3.5}},
 'p2b':{603:{"t":{"X":"20261123_084536_10454c0f-fd16-4835-ad4e-de556a0e67e2"},"ss":1.0}},
 'p3b':{901:{"t":{"X":"20261123_085130_afd75ba3-996a-4add-bd6f-01cf06db8c1b"},"ss":0.8}},
 # 13031: Trey-clone swap fda804df with "my" (6.15 s) from Trey-clone 11032 b1dbea1d over "our" (5.72-5.88 s)
 'p4b':{13031:{"t":{"X":"/home/user/v4/s13031v4.mp4"},"ss":0.1},
 16023:{"t":{"X":"20261123_090206_74b2d07d-dcda-45d0-93c7-2a26409a4b0a"}},
 16051:{"t":{"X":"20261123_094606_d18acebf-fa5e-46cb-9b2f-86782d22571e"},"ss":1.3}}}  # was garbled "I tell all the dads"
SPLIT1608=((16081,"20261123_085833_4f7d53bb-43d2-471d-8928-5c577ef85143",0.6),(16082,"20261123_085835_197459a4-5f27-428d-bcd7-13a5576cbfad",1.3))
for p,m in R.items():
  L=json.load(open('/home/user/%s/elx_v3.json'%p)); out=[]
  for c in L:
    n=c.get('n')
    if n in m:
      d={"n":n}; d.update(m[n])
      if 'pre' in c: d['pre']=c['pre']
      out.append(d)
    elif p=='p4b' and n==1608:
      for nn,st,ss in SPLIT1608:
        d={"n":nn,"t":{"X":st},"ss":ss}
        if 'pre' in c: d['pre']=c['pre']
        out.append(d)
    else: out.append(c)
  json.dump(out,open('/home/user/%s/elx.json'%p,'w'))
