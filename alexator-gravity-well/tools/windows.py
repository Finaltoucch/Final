import numpy as np
SR=22050
x=np.fromfile('riseagain.raw',dtype=np.float32)
dur=len(x)/SR
bpm,beat,bar,off,_=np.load('grid.npy')
phrase=8*bar

# true audio end (last sample above -60dBFS, 10ms frames)
fr=int(SR*0.01)
rms=np.sqrt(np.array([np.mean(x[i:i+fr]**2) for i in range(0,len(x)-fr,fr)])+1e-12)
db=20*np.log10(rms+1e-12)
last=np.where(db>-60)[0][-1]*0.01
first=np.where(db>-60)[0][0]*0.01
print(f"audio starts {first:.2f}s   ends {last:.2f}s   file {dur:.2f}s")
print(f"tail: last 6s dBFS -> ", " ".join(f"{db[int(t*100)]:.0f}" for t in np.arange(last-5,last+0.5,0.5)))

# energy per phrase
def seg(a,b):
    s=x[int(a*SR):int(b*SR)]
    return float(np.sqrt(np.mean(s**2)+1e-12))
ph=[]
k=0
while off+k*phrase < last:
    a=off+k*phrase; b=min(a+phrase,last)
    if b-a>1: ph.append((k,a,b,seg(a,b)))
    k+=1
mx=max(p[3] for p in ph)
print("\n8-BAR PHRASES")
for k,a,b,e in ph:
    print(f"  P{k:<3} {a:7.2f}-{b:7.2f}  rms {e/mx:.2f} {'#'*int(e/mx*40)}")

# candidate windows: start on a phrase boundary, 30-60s, end at track end or phrase boundary
print("\nCANDIDATE WINDOWS (start on 8-bar phrase)")
cands=[]
for k,a,_,_ in ph:
    for endk,b,_,_ in ph:
        if b<=a: continue
        for end,label in ((b,f"phrase P{endk}"),(last,"TRACK END")):
            L=end-a
            if 30<=L<=60:
                e=seg(a,end)
                # escalation: rms of last third vs first third
                t1=seg(a,a+L/3); t3=seg(end-L/3,end)
                cands.append((a,end,L,e/mx,t3/max(t1,1e-9),label))
seen=set(); out=[]
for c in sorted(cands,key=lambda c:-(c[3]*1.0+min(c[4],2)*0.35)):
    key=(round(c[0],1),round(c[1],1))
    if key in seen: continue
    seen.add(key); out.append(c)
for a,b,L,e,esc,lab in out[:14]:
    print(f"  {a:7.2f} -> {b:7.2f}  len {L:5.2f}s  energy {e:.2f}  escalation x{esc:4.2f}  end={lab}")
