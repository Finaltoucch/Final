import numpy as np
SR=22050
x=np.fromfile('riseagain.raw',dtype=np.float32)
N=512;H=64                      # 2.9ms hop
w=np.hanning(N).astype(np.float32)
nf=(len(x)-N)//H
f=np.fft.rfftfreq(N,1/SR)
lowm=(f>=25)&(f<130)
env=np.empty(nf,dtype=np.float32)
for i in range(nf):
    env[i]=np.abs(np.fft.rfft(x[i*H:i*H+N]*w))[lowm].sum()
fps=SR/H
d=np.diff(env); d[d<0]=0; d=np.concatenate([[0],d])
# peak pick
thr=d.mean()+1.2*d.std()
pk=[]
i=1
while i<len(d)-1:
    if d[i]>thr and d[i]>=d[i-1] and d[i]>=d[i+1]:
        pk.append(i/fps); i+=int(0.12*fps)
    else: i+=1
pk=np.array(pk)
print(f"{len(pk)} kick onsets detected")

# fit bar grid: search beat period near 60/136.09 and phase
best=None
for bpm in np.arange(135.0,137.2,0.005):
    b=60/bpm
    for ph in np.arange(0,b,0.004):
        q=np.abs((pk-ph+b/2)%b - b/2)
        sc=(q<0.045).sum()
        if best is None or sc>best[2]: best=(bpm,ph,sc)
bpm,ph,sc=best
beat=60/bpm; bar=4*beat
print(f"BEAT GRID  {bpm:.3f} BPM  beat {beat:.5f}s  phase {ph:.4f}s  ({sc}/{len(pk)} onsets on-grid)")

# downbeat phase: which of 4 beat positions carries most energy
sel=pk[(pk>72)&(pk<115)]
score=[0]*4
for p in pk:
    n=round((p-ph)/beat)
    score[int(n)%4]+=1
print("beat-class histogram:",score)
db=int(np.argmax(score))
bar_ph=ph+db*beat
while bar_ph-bar>0: bar_ph-=bar
print(f"BAR GRID   bar {bar:.5f}s  first downbeat {bar_ph:.4f}s")

def bar_at(t): return (t-bar_ph)/bar
def t_of_bar(n): return bar_ph+n*bar
for t in (57.31,71.42,72.81,73.18,85.53,87.06,99.64):
    print(f"  t={t:7.2f}  bar {bar_at(t):8.3f}")

# where does the kick actually start/stop? density per bar
print("\nBAR  START   KICKS  (kick density per bar, bars 28-60)")
for n in range(28,60):
    a,b=t_of_bar(n),t_of_bar(n+1)
    k=((pk>=a)&(pk<b)).sum()
    print(f" {n:3d} {a:7.2f}   {'*'*k}{'' if k else '-'}   {'<<< 8-bar' if n%8==int(round(bar_at(73.18)))%8 else ''}")
np.save('pk.npy',pk); np.save('grid2.npy',np.array([bpm,beat,bar,bar_ph]))
