# Original procedural film score + sound design (no samples, nothing licensed).
# usage: python3 score.py timeline.json cues.json dlg.wav vid.mp4 out.mp4
import json,sys,subprocess as sp,numpy as np
SR=48000
rng=np.random.default_rng(7)
TL=json.load(open(sys.argv[1]));CU=json.load(open(sys.argv[2]))
def mf(m):return 440*2**((m-69)/12)
def tt(d):return np.arange(int(d*SR))/SR
def lp(x,fc,order=4):
  X=np.fft.rfft(x,axis=0);f=np.fft.rfftfreq(len(x),1/SR);h=1/np.sqrt(1+(f/fc)**(2*order))
  return np.fft.irfft(X*(h[:,None] if x.ndim>1 else h),n=len(x),axis=0)
def hp(x,fc):return x-lp(x,fc,2)
def fconv(x,ir):
  n=len(x)+len(ir)-1;N=1<<(n-1).bit_length()
  return np.fft.irfft(np.fft.rfft(x,N)*np.fft.rfft(ir,N),N)[:len(x)]
IR=[lp(rng.standard_normal(int(3.2*SR))*np.exp(-tt(3.2)/0.9),5000) for _ in range(2)]
IR=[i/np.sqrt((i**2).sum()) for i in IR]
def verb(st,wet=0.3):
  return st*(1-wet)+np.stack([fconv(st[:,0],IR[0]),fconv(st[:,1],IR[1])],1)*wet*2.2
def place(buf,x,t0):
  i=int(t0*SR)
  if i>=len(buf):return
  j=min(len(buf),i+len(x));buf[i:j]+=x[:j-i]
def pan(m,p=0.0):return np.stack([m*(1-p)*0.7,m*(1+p)*0.7],1)
def env(n,a,r):
  e=np.ones(n);A=min(n,int(a*SR));R=min(n-A,int(r*SR))
  if A:e[:A]=np.linspace(0,1,A)
  if R:e[n-R:]=np.linspace(1,0,R)
  return e
# ---- instruments ----
def piano(m,dur,vel=0.4):
  d=dur+1.6;t=tt(d);f=mf(m);x=np.zeros_like(t)
  for k in range(1,11):
    fk=f*k*np.sqrt(1+0.0004*k*k)
    if fk>15000:break
    x+=np.sin(2*np.pi*fk*t)*np.exp(-t*(0.6+0.55*k)*(1+f/900))/k**1.3
  x+=lp(rng.standard_normal(len(t))*np.exp(-t*120),3000)*0.15
  x*=np.minimum(1,np.maximum(0,(d-t)/0.4))*vel
  return x
def saw(f,t,vib=0.0):
  ph=np.cumsum(f*(1+vib*np.sin(2*np.pi*5.2*t+rng.random()*6)))/SR
  return 2*(ph%1)-1
def strings(ms,dur,vel=0.3,a=1.5,r=1.8,fc=1800):
  d=dur+r;t=tt(d);L=np.zeros_like(t);R=np.zeros_like(t)
  for m in ms:
    f=mf(m)
    for c in (-7,0,7):
      s=saw(f*2**(c/1200),t,0.0025)
      if c<=0:L+=s
      if c>=0:R+=s
  st=np.stack([L,R],1)/len(ms)/2
  st=lp(st,fc)*env(len(t),a,r)[:,None]*vel
  return st
def pluck(m,vel=0.4,dur=0.5):
  t=tt(dur);x=saw(mf(m),t)*np.exp(-t*9)
  return lp(x,1400)*vel
def thump(f0=60,vel=0.6,dur=0.35):
  t=tt(dur);f=f0*(1+1.2*np.exp(-t*25));x=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*12)
  return x*vel
def tom(vel=0.5):
  t=tt(0.5);x=thump(110,1,0.5)+lp(rng.standard_normal(len(t)),800)*np.exp(-t*30)*0.4
  return x*vel
def heartbeat(vel=0.7):
  x=np.zeros(int(0.8*SR));a=thump(55,vel,0.3);b=thump(48,vel*0.7,0.3)
  x[:len(a)]+=a;x[int(0.27*SR):int(0.27*SR)+len(b)]+=b;return x
def braam(vel=0.6,dur=3.5):
  t=tt(dur);x=np.zeros_like(t)
  for m in (26,38,45,50):x+=saw(mf(m),t,0.001)
  x=np.tanh(x*1.6);x=lp(x,700)*np.exp(-t*0.9)*np.minimum(1,t/0.04)
  return pan(x*vel*0.5)
def boom(vel=0.8,dur=2.5):
  t=tt(dur);f=50*np.exp(-t*0.4)+28;x=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*1.4)
  n=lp(rng.standard_normal(len(t)),300)*np.exp(-t*6)*0.6
  return pan((x+n)*vel)
def impact(vel=1.0):
  b=boom(vel);r=braam(vel*0.9);n=max(len(b),len(r));o=np.zeros((n,2));o[:len(b)]+=b;o[:len(r)]+=r
  return verb(o,0.35)
def stinger(vel=0.7):
  s=strings([74,75,81],1.2,vel*0.9,a=0.02,r=1.4,fc=4000);h=pan(thump(70,vel*0.8,0.6))
  o=np.zeros((max(len(s),len(h)),2));o[:len(s)]+=s;o[:len(h)]+=h
  return verb(o,0.4)
def riser(dur=4.0,vel=0.6):
  t=tt(dur);g=(t/dur)**2.2
  nz=hp(rng.standard_normal((len(t),2)),2500)*0.25
  tone=sum(saw(mf(m)*2**(t/dur),t) for m in (50,57,62))/3
  x=(nz+pan(lp(tone,3000))*0.9)*g[:,None]*vel
  return verb(x,0.25)
def whoosh(vel=0.35,dur=1.2):
  t=tt(dur);e=np.sin(np.pi*t/dur)**2;n=rng.standard_normal((len(t),2))
  x=lp(n,500)*(1-t/dur)[:,None]+lp(n,3500)*(t/dur)[:,None]
  return verb(x*e[:,None]*vel,0.3)
# ---- cues ----
def bars(T,bpm,beats):return np.arange(0,T,60/bpm*beats)
def c_hope(T):
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/72;prog=[[50,54,57],[47,50,54],[43,47,50],[45,49,52]];k=0
  for b0 in bars(T,72,4):
    ch=prog[(k//2)%4];k+=1
    place(o,pan(piano(ch[0]-12,bt*4,0.35),-0.2),b0)
    pat=[ch[0],ch[2],ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12,ch[0]+12,ch[2]]
    for j,m in enumerate(pat):place(o,pan(piano(m,bt/2,0.22),0.2*np.sin(j)),b0+j*bt/2)
    place(o,strings([c+12 for c in ch],bt*4,0.08),b0)
  return verb(o,0.3)
def c_tender(T):
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/66;prog=[[50,53,57],[46,50,53],[41,45,48],[48,52,55]];mel=[69,65,67,64];k=0
  for b0 in bars(T,66,4):
    ch=prog[k%4]
    place(o,pan(piano(ch[0]-12,bt*4,0.3)),b0)
    for j,m in enumerate([ch[0],ch[1],ch[2],ch[1]]):place(o,pan(piano(m,bt,0.2),0.15*(j-1.5)),b0+j*bt)
    if k%2==0:place(o,pan(piano(mel[(k//2)%4]+12,bt*2,0.18),0.1),b0+bt*0.5)
    place(o,strings([c+12 for c in ch],bt*4,0.1),b0);k+=1
  return verb(o,0.35)
def c_elegant(T):
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/92;prog=[[50,54,57],[47,50,54],[43,47,50],[45,49,52]];k=0
  for b0 in bars(T,92,3):
    ch=prog[(k//2)%4]
    place(o,pan(piano(ch[0]-12,bt,0.3),-0.2),b0)
    for j in (1,2):
      for m in ch:place(o,pan(piano(m+12,bt*0.6,0.11),0.2),b0+j*bt)
    k+=1
  return verb(o,0.3)
def c_sad(T):
  o=np.zeros((int(T*SR)+SR*3,2));prog=[[38,50,53,57],[34,46,50,53],[31,43,46,50],[33,45,49,52]];mel=[81,77,79,76];k=0
  for b0 in np.arange(0,T,5.0):
    place(o,strings(prog[k%4],5.0,0.22,a=1.8,r=2.2),b0)
    place(o,strings([mel[k%4]],5.0,0.07,a=1.2,r=2.0,fc=3500),b0+0.5);k+=1
  return verb(o,0.4)
def c_tension(T):
  o=np.zeros((int(T*SR)+SR*3,2));place(o,strings([26,38],T,0.3,a=3,r=2.5,fc=500),0)
  place(o,strings([74,75],T,0.05,a=4,r=3,fc=5000),0)
  for t0 in np.arange(0.5,T,1.05):place(o,pan(heartbeat(0.55)),t0)
  return verb(o,0.25)
def c_suspense(T):
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/112/2;pat=[50,50,53,52,50,50,55,53]
  place(o,strings([38,45],T,0.18,a=2,r=2,fc=700),0)
  for j,t0 in enumerate(np.arange(0,T,bt)):
    g=0.25+0.25*min(1,t0/max(T,1));place(o,pan(pluck(pat[j%8],g),0.3*(-1)**j),t0)
    if j%8==0:place(o,pan(tom(0.35)),t0)
  return verb(o,0.25)
def c_dark(T):
  o=np.zeros((int(T*SR)+SR*3,2));place(o,strings([26,27,38],T,0.28,a=2.5,r=2.5,fc=450),0)
  for t0 in np.arange(0,T,5.0):place(o,braam(0.35),t0)
  for t0 in np.arange(0.4,T,1.4):place(o,pan(heartbeat(0.5)),t0)
  return verb(o,0.3)
def c_panic(T):
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/132/4
  place(o,strings([26,38,39],T,0.22,a=1,r=2,fc=900),0)
  for j,t0 in enumerate(np.arange(0,T,bt)):
    g=0.15+0.2*min(1,t0/max(T,1));place(o,pan(pluck([50,51][j%2]+(12 if (j//16)%2 else 0),g,0.25),0.2*(-1)**j),t0)
    if j%4==0:place(o,pan(tom(0.4 if j%8==0 else 0.25)),t0)
  return verb(o,0.2)
CUES=dict(hope=c_hope,tender=c_tender,elegant=c_elegant,sad=c_sad,tension=c_tension,suspense=c_suspense,dark=c_dark,panic=c_panic)
LVL=dict(hope=-41,tender=-41,elegant=-43,sad=-40,tension=-41,suspense=-41,dark=-40,panic=-39)
def key(k,TL):
  for e in TL:
    if e['key']==k:return e
  raise KeyError(k)
total=TL[-1]['start']+TL[-1]['dur'];N=int(total*SR)
mus=np.zeros((N+SR*4,2));sfx=np.zeros_like(mus)
for c in CU:
  if 'cue' in c:
    a=key(c['from'],TL)['start'];b=key(c['to'],TL);b=b['start']+b['dur'];T=b-a
    x=CUES[c['cue']](T+2.0)[:int((T+2.0)*SR)]
    x*=10**((LVL[c['cue']]+c.get('gain',0))/20)/(np.sqrt((x**2).mean())+1e-9)
    n=len(x);e=np.ones(n);fi=int(1.0*SR);fo=int(2.0*SR);e[:fi]=np.linspace(0,1,fi);e[-fo:]=np.linspace(1,0,fo)
    place(mus,x*e[:,None],a)
  else:
    e=key(c['at'],TL);t0=e['start']+(e['dur'] if c.get('pos')=='end' else 0)+c.get('off',0)
    s=c['sfx']
    if s=='riser':x=riser(c.get('len',4.0),0.6);t0-=len(x)/SR
    else:x={'impact':impact,'stinger':stinger,'whoosh':whoosh,'braam':lambda:braam(0.7)}[s]()
    x*=10**(c.get('db',{'impact':-26,'stinger':-30,'whoosh':-38,'riser':-32,'braam':-28}[s])/20)/(max(np.sqrt((x[i:i+int(SR*0.5)]**2).mean()) for i in range(0,max(1,len(x)-int(SR*0.5)),int(SR*0.25)))+1e-9)
    place(sfx,x,max(0,t0))
for e in TL:
  if e['key'].startswith('c:'):
    x=whoosh();x*=10**(-42/20)/(np.sqrt((x**2).mean())+1e-9);place(sfx,x,max(0,e['start']-0.3))
mus=mus[:N];sfx=sfx[:N]
dlg=np.frombuffer(sp.run(['ffmpeg','-v','error','-i',sys.argv[3],'-f','f32le','-ac','2','-ar','48000','-'],capture_output=True).stdout,np.float32).reshape(-1,2)[:N]
if len(dlg)<N:dlg=np.vstack([dlg,np.zeros((N-len(dlg),2),np.float32)])
e=np.sqrt(np.convolve((dlg**2).mean(1),np.ones(2400)/2400,'same'));spk=e>max(0.004,0.12*np.percentile(e,99))
g=np.ones(N,np.float32);lvl=1.0;hop=480
for j in range(0,N,hop):
  tgt=0.25 if spk[j:j+hop].any() else 1.0;lvl+=(tgt-lvl)*(0.35 if tgt<lvl else 0.05);g[j:j+hop]=lvl
mix=dlg+mus*g[:,None]+sfx*g[:,None]
mix=np.tanh(mix*0.98)/0.98
sp.run(['ffmpeg','-v','error','-y','-f','f32le','-ar','48000','-ac','2','-i','-','mix.wav'],input=mix.astype(np.float32).tobytes(),check=True)
if sys.argv[4]!='-':sp.run(['ffmpeg','-v','error','-y','-i',sys.argv[4],'-i','mix.wav','-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',sys.argv[5]],check=True)
print('SCORED',total,flush=True)
