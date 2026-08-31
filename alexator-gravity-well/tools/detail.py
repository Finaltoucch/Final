import numpy as np
SR=22050
x=np.fromfile('riseagain.raw',dtype=np.float32)
bpm,beat,bar,off,dur=np.load('grid.npy')
A,B=57.31,99.64
print(f"WINDOW {A}-{B}  ({B-A:.2f}s)  = {(B-A)/bar:.1f} bars = {(B-A)/(8*bar):.2f} phrases\n")

N=1024;H=128
w=np.hanning(N).astype(np.float32)
def frames(a,b):
    s=x[int(a*SR):int(b*SR)]
    nf=(len(s)-N)//H
    S=np.empty((nf,N//2+1),dtype=np.float32)
    for i in range(nf): S[i]=np.abs(np.fft.rfft(s[i*H:i*H+N]*w))
    return S,np.arange(nf)*H/SR+a
S,t=frames(A-3,B+6)
f=np.fft.rfftfreq(N,1/SR)
lowm=(f>=20)&(f<140)
low=S[:,lowm].sum(1); tot=S.sum(1)
# 0.25s resolution
step=0.25
print("TIME    TOTAL                    KICK")
mxT,mxL=tot.max(),low.max()
for tt in np.arange(A-3,B+6,step):
    i=np.argmin(np.abs(t-tt))
    j=slice(i,i+int(step*SR/H))
    T=tot[j].mean()/mxT; L=low[j].mean()/mxL
    mark=""
    for p,nm in ((57.31,"<P4"),(71.42,"<P5 DROP1"),(85.53,"<P6 DROP2/PEAK"),(99.64,"<P7 OUT")):
        if abs(tt-p)<step/2: mark=nm
    print(f"{tt:7.2f} {'#'*int(T*24):<24} {'#'*int(L*16):<16} {mark}")
