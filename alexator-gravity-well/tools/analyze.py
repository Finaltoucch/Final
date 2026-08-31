import numpy as np

SR=22050
x=np.fromfile('riseagain.raw',dtype=np.float32)
dur=len(x)/SR

# ---------- STFT ----------
N=2048; H=256                      # ~11.6ms hop
w=np.hanning(N).astype(np.float32)
nf=(len(x)-N)//H
S=np.empty((nf,N//2+1),dtype=np.float32)
for i in range(nf):
    S[i]=np.abs(np.fft.rfft(x[i*H:i*H+N]*w))
t=np.arange(nf)*H/SR
freqs=np.fft.rfftfreq(N,1/SR)

# ---------- band energies ----------
def band(lo,hi):
    m=(freqs>=lo)&(freqs<hi)
    return S[:,m].sum(1)
low=band(20,140)      # kick / sub
mid=band(140,2000)    # body / synths
high=band(2000,11000) # hats / air
tot=S.sum(1)

# ---------- spectral flux onsets ----------
d=np.diff(S,axis=0); d[d<0]=0
flux=d.sum(1); flux=np.concatenate([[0],flux])
fl=flux/ (flux.max()+1e-9)

# ---------- tempo via autocorrelation of flux ----------
f=fl-fl.mean()
ac=np.correlate(f,f,'full')[len(f)-1:]
fps=SR/H
lo_lag=int(fps*60/180); hi_lag=int(fps*60/60)   # 60-180 BPM
lag=np.argmax(ac[lo_lag:hi_lag])+lo_lag
bpm=60*fps/lag
print(f"DURATION      {dur:.2f}s")
print(f"TEMPO         {bpm:.2f} BPM   (beat {60/bpm:.4f}s, bar {4*60/bpm:.4f}s)")

# refine bpm by testing candidates around it on a comb filter
best=None
for cand in np.arange(bpm-3,bpm+3,0.01):
    bl=60/cand*fps
    idx=np.arange(0,len(fl),bl).astype(int); idx=idx[idx<len(fl)]
    sc=fl[idx].mean()
    if best is None or sc>best[1]: best=(cand,sc)
bpm=best[0]
beat=60/bpm; bar=4*beat; phrase8=8*bar
print(f"REFINED       {bpm:.2f} BPM   beat {beat:.4f}s  bar {bar:.4f}s  8-bar phrase {phrase8:.3f}s")

# ---------- downbeat offset: best phase for bar grid ----------
bestoff=None
for off in np.arange(0,bar,0.01):
    idx=((np.arange(off,dur-1,bar))*fps).astype(int); idx=idx[idx<len(fl)]
    sc=(fl[idx]*1.0).mean()+low[idx].mean()/ (low.max()+1e-9)
    if bestoff is None or sc>bestoff[1]: bestoff=(off,sc)
off=bestoff[0]
print(f"BAR PHASE     first downbeat at {off:.3f}s")

# ---------- coarse energy map (1s) ----------
def per_sec(a):
    n=int(dur)
    return np.array([a[int(i*fps):int((i+1)*fps)].mean() for i in range(n)])
L=per_sec(low); M=per_sec(mid); Hh=per_sec(high); T=per_sec(tot)
nrm=lambda a:(a-a.min())/(np.ptp(a)+1e-9)
L,M,Hh,T=nrm(L),nrm(M),nrm(Hh),nrm(T)

print("\nSEC  TOTAL              LOW(kick)          HIGH(air)")
for i in range(len(T)):
    bt='#'*int(T[i]*28); bl='#'*int(L[i]*18); bh='#'*int(Hh[i]*18)
    print(f"{i:3d}  {bt:<28} {bl:<18} {bh:<18}")
np.save('env.npy',np.vstack([T,L,M,Hh]))
np.save('grid.npy',np.array([bpm,beat,bar,off,dur]))
