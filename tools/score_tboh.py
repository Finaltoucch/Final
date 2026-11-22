# Two Boys, One Heart: original procedural score and sound design.
# New instruments, keys, rhythms and effects. Nothing is shared with the previous film's score.
# usage: python3 score_tboh.py timeline.json cues.json dlg.wav vid.mp4 out.mp4
import json,sys,subprocess as sp,numpy as np
SR=48000
rng=np.random.default_rng(23)
TL=json.load(open(sys.argv[1]));CU=json.load(open(sys.argv[2]))
def mf(m):return 440*2**((m-69)/12)
def tt(d):return np.arange(int(d*SR))/SR
def lp(x,fc,order=4):
  X=np.fft.rfft(x,axis=0);f=np.fft.rfftfreq(len(x),1/SR);h=1/np.sqrt(1+(f/fc)**(2*order))
  return np.fft.irfft(X*(h[:,None] if x.ndim>1 else h),n=len(x),axis=0)
def hp(x,fc):return x-lp(x,fc,2)
def bp(x,lo,hi):return hp(lp(x,hi),lo)
def fconv(x,ir):
  n=len(x)+len(ir)-1;N=1<<(n-1).bit_length()
  return np.fft.irfft(np.fft.rfft(x,N)*np.fft.rfft(ir,N),N)[:len(x)]
# a brighter, shorter "room" for intimacy plus a long "hall" for big moments
def mkir(d,dec,fc):
  i=lp(rng.standard_normal(int(d*SR))*np.exp(-tt(d)/dec),fc);return i/np.sqrt((i**2).sum())
ROOM=[mkir(1.4,0.35,7000) for _ in range(2)];HALL=[mkir(4.5,1.4,4200) for _ in range(2)]
def verb(st,wet=0.3,hall=False):
  I=HALL if hall else ROOM
  return st*(1-wet)+np.stack([fconv(st[:,0],I[0]),fconv(st[:,1],I[1])],1)*wet*2.0
def place(buf,x,t0):
  i=int(t0*SR)
  if i>=len(buf) or i<0:return
  j=min(len(buf),i+len(x));buf[i:j]+=x[:j-i]
def pan(m,p=0.0):return np.stack([m*(1-p)*0.7,m*(1+p)*0.7],1)
def env(n,a,r):
  e=np.ones(n);A=min(n,int(a*SR));R=min(n-A,int(r*SR))
  if A:e[:A]=np.linspace(0,1,A)
  if R:e[n-R:]=np.linspace(1,0,R)
  return e
# ---------------- instruments (all new) ----------------
def rhodes(m,dur,vel=0.35):          # FM electric piano: sine carrier + bell modulator
  d=dur+1.2;t=tt(d);f=mf(m);I=2.2*np.exp(-t*3.5)
  x=np.sin(2*np.pi*f*t+I*np.sin(2*np.pi*f*t))*np.exp(-t*1.1)
  x+=0.25*np.sin(2*np.pi*f*14*t)*np.exp(-t*30)  # tine "tick"
  x+=0.4*np.sin(2*np.pi*f*2*t)*np.exp(-t*2.5)
  x*=np.minimum(1,(d-t)/0.3)*vel*(0.8+0.4*np.sin(2*np.pi*4.5*t)*0.05)
  return x
def felt(m,dur,vel=0.3):             # soft felt piano: few partials, muffled, quick hammer thud
  d=dur+2.5;t=tt(d);f=mf(m);x=np.zeros_like(t)
  for k,a in ((1,1),(2,0.35),(3,0.12),(4,0.05)):x+=a*np.sin(2*np.pi*f*k*1.0007*t)*np.exp(-t*(0.45+0.3*k))
  x+=lp(rng.standard_normal(len(t))*np.exp(-t*60),600)*0.25
  return lp(x,2200)*np.minimum(1,(d-t)/0.5)*vel
def celesta(m,dur=1.2,vel=0.25):
  t=tt(dur+1);f=mf(m)
  x=(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*4.07*t)*np.exp(-t*6)+0.2*np.sin(2*np.pi*f*9.2*t)*np.exp(-t*14))*np.exp(-t*2.4)
  return x*vel
def pizz(m,vel=0.3):
  t=tt(0.6);f=mf(m);x=np.zeros_like(t)
  for k in range(1,7):x+=np.sin(2*np.pi*f*k*t)*np.exp(-t*(7+3*k))/k
  return x*vel
def guitar(m,dur=1.6,vel=0.3):       # nylon guitar, additive with bright-to-dark decay
  t=tt(dur+0.5);f=mf(m);x=np.zeros_like(t)
  for k in range(1,12):x+=np.sin(2*np.pi*f*k*t+rng.random())*np.exp(-t*(1.2+0.9*k))/k**1.1
  x+=lp(rng.standard_normal(len(t))*np.exp(-t*200),4000)*0.2
  return x*vel
def cello(ms,dur,vel=0.25,a=0.6,r=1.2):  # bowed: band-limited pulse + slow vibrato + bow noise
  d=dur+r;t=tt(d);out=np.zeros_like(t)
  for m in ms:
    f=mf(m)*(1+0.004*np.sin(2*np.pi*5.5*t)*np.minimum(1,t/0.8))
    ph=np.cumsum(f)/SR;x=np.zeros_like(t)
    for k in range(1,14):x+=np.sin(2*np.pi*k*ph)*(1/k)*(1 if k%2 else 0.55)
    out+=x
  out+=bp(rng.standard_normal(len(t)),800,4000)*0.04
  out=lp(out/len(ms),2400)*env(len(t),a,r)*vel
  return out
def pad(ms,dur,vel=0.12,a=2.0,r=2.5):  # warm detuned sine/triangle pad
  d=dur+r;t=tt(d);L=np.zeros_like(t);R=np.zeros_like(t)
  for m in ms:
    for c,side in ((-9,0),(0,2),(9,1)):
      f=mf(m)*2**(c/1200);s=np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*f*2*t+1)
      if side in (0,2):L+=s
      if side in (1,2):R+=s
  st=np.stack([L,R],1)/len(ms)/3
  return lp(st,1500)*env(len(t),a,r)[:,None]*vel
def brass(ms,dur,vel=0.25):
  t=tt(dur+0.3);x=np.zeros_like(t)
  for m in ms:
    ph=np.cumsum(mf(m)*np.ones_like(t))/SR;x+=2*(ph%1)-1
  ft=600+2600*np.exp(-t*5);x=x/len(ms)
  y=np.zeros_like(x);seg=int(0.02*SR)
  for i in range(0,len(x),seg):y[i:i+seg]=lp(x[i:i+seg+256],float(ft[i]),2)[:len(x[i:i+seg])]
  return y*env(len(t),0.03,0.25)*vel
def kick(vel=0.7):
  t=tt(0.45);f=48+90*np.exp(-t*40);return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)*vel
def snare(vel=0.4):
  t=tt(0.25);return (bp(rng.standard_normal(len(t)),1500,8000)*np.exp(-t*22)+0.4*np.sin(2*np.pi*190*t)*np.exp(-t*30))*vel
def clap(vel=0.35):
  t=tt(0.3);n=bp(rng.standard_normal(len(t)),900,5000);e=np.exp(-t*25)
  for d0 in (0.008,0.017):e+=np.exp(-np.maximum(0,t-d0)*60)*(t>d0)*0.6
  return n*e*vel
def hat(vel=0.15):
  t=tt(0.08);return hp(rng.standard_normal(len(t)),7000)*np.exp(-t*60)*vel
def snap(vel=0.2):
  t=tt(0.12);return bp(rng.standard_normal(len(t)),1800,6000)*np.exp(-t*45)*vel
def tick(vel=0.15):
  t=tt(0.05);return np.sin(2*np.pi*3200*t)*np.exp(-t*120)*vel
def subpulse(f=41,vel=0.5,dur=0.5):
  t=tt(dur);return np.sin(2*np.pi*f*t)*np.exp(-t*5)*np.minimum(1,t/0.01)*vel
# ---------------- new sound effects ----------------
def sub_drop(vel=0.9):
  t=tt(2.2);f=90*np.exp(-t*1.6)+25;return pan(np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*1.1)*vel)
def reverse_swell(dur=2.5,vel=0.5):
  st=pad([57,64,69,72],dur*0.5,0.5,a=0.01,r=dur*0.5);x=verb(st,0.6,True)[:int(dur*SR)]
  return x[::-1]*np.linspace(0,1,len(x))[:,None]**1.5*vel
def shimmer(vel=0.5):
  o=np.zeros((int(4*SR),2))
  for j,m in enumerate((81,84,88,93,96)):place(o,pan(celesta(m,2.5,0.3),0.3*(-1)**j),j*0.04)
  place(o,sub_drop(0.6),0)
  return verb(o,0.5,True)*vel
def swish(vel=0.35,dur=0.9):
  t=tt(dur);n=rng.standard_normal((len(t),2));fc=np.linspace(400,6000,len(t))
  y=np.zeros_like(n);seg=2048
  for i in range(0,len(n),seg):y[i:i+seg]=bp(n[i:i+seg+512],200,float(fc[i]))[:len(n[i:i+seg])]
  return verb(y*np.sin(np.pi*t/dur)[:,None]**2*vel,0.25)
def hit(vel=0.8):   # deep drum hit with body, not a braam
  s=subpulse(36,vel*0.7,1.2);k=kick(vel);s[:len(k)]+=k
  o=np.vstack([pan(s),np.zeros((SR,2))])
  return verb(o,0.4,True)
def riser(dur=3.0,vel=0.5):  # filtered noise + rising pad, distinct from the old saw riser
  t=tt(dur);g=(t/dur)**2.5;n=rng.standard_normal((len(t),2))
  y=lp(n,2500)*0.3+pad([62,69,74],dur,1.0,a=dur*0.8,r=0.01)[:len(t)]
  return verb(y*g[:,None]*vel,0.3,True)
# ---------------- cues (all new) ----------------
def bars(T,bpm,beats):return np.arange(0,T,60/bpm*beats)
def c_hype(T):      # pep rally drumline in E minor, 120 bpm
  o=np.zeros((int(T*SR)+SR*3,2));bt=0.5
  for j,t0 in enumerate(np.arange(0,T,bt/2)):
    if j%2==0:place(o,pan(kick(0.7)),t0)
    if j%4==2:place(o,pan(clap(0.45),0.1),t0)
    place(o,pan(hat(0.12),0.4),t0)
    if j%16 in (13,14,15):place(o,pan(snare(0.3),-0.2),t0)
  for k,t0 in enumerate(bars(T,120,8)):
    place(o,pan(brass([52,59,64],0.35,0.22)),t0);place(o,pan(brass([55,62,67],0.35,0.2)),t0+1.5)
  return verb(o,0.2)
def c_playful(T):   # pizzicato and celesta, F major, 104 bpm
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/104;prog=[[53,57,60],[50,53,57],[46,50,53],[48,52,55]];k=0
  for b0 in bars(T,104,4):
    ch=prog[k%4];k+=1
    for j,m in enumerate([ch[0]-12,ch[2]-12,ch[1],ch[2]]):place(o,pan(pizz(m,0.3),0.3*(-1)**j),b0+j*bt)
    for j,m in enumerate([ch[2]+12,ch[1]+12,ch[0]+24]):place(o,pan(celesta(m,1.0,0.12),0.25),b0+bt*(0.5+j*1.5))
  return verb(o,0.25)
def c_romance(T):   # Rhodes + lo-fi beat, Ab major: Abmaj7 Fm9 Dbmaj7 Eb6, 76 bpm
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/76
  prog=[[56,60,63,67],[53,56,60,63],[49,53,56,60],[51,55,58,60]];mel=[75,72,73,70];k=0
  for b0 in bars(T,76,4):
    ch=prog[k%4]
    for m in ch:place(o,pan(rhodes(m,bt*3.5,0.12),0.15*(m%3-1)),b0)
    place(o,pan(rhodes(ch[0]-12,bt*4,0.2),-0.1),b0)
    if k%2==1:place(o,pan(rhodes(mel[(k//2)%4],bt*1.5,0.1),0.2),b0+bt*2.5)
    for j in range(4):
      if j in (0,2):place(o,pan(kick(0.25)),b0+j*bt)
      if j in (1,3):place(o,pan(snap(0.18),0.15),b0+j*bt)
    place(o,pad([c+12 for c in ch[:3]],bt*4,0.06),b0);k+=1
  return verb(o,0.3)
def c_longing(T):   # solo cello over a soft pad, C minor
  o=np.zeros((int(T*SR)+SR*3,2));prog=[[48,55,63],[44,51,60],[41,48,56],[43,50,59]];mel=[[63,62,60],[60,58,56],[56,55,53],[55,56,55]];k=0
  for b0 in np.arange(0,T,6.0):
    place(o,pad(prog[k%4],6.0,0.1),b0)
    for j,m in enumerate(mel[k%4]):place(o,pan(cello([m-12],1.9,0.18,a=0.5,r=0.9),-0.1),b0+j*2.0)
    k+=1
  return verb(o,0.4,True)
def c_heartbreak(T): # sparse high felt piano + reverse swells, A minor
  o=np.zeros((int(T*SR)+SR*3,2));notes=[76,72,74,71,69,72,67,69];k=0
  for t0 in np.arange(0,T,1.6):
    place(o,pan(felt(notes[k%8],1.4,0.22),0.25*np.sin(k)),t0)
    if k%4==0:place(o,pan(felt(notes[k%8]-24,3.0,0.18),-0.2),t0)
    k+=1
  for t0 in np.arange(4.0,T,8.0):place(o,reverse_swell(2.5,0.25),t0-2.5)
  return verb(o,0.45,True)
def c_tension(T):   # pulsing low synth + ticking clock + slow rising sine
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/96/4
  for j,t0 in enumerate(np.arange(0,T,bt)):
    place(o,pan(subpulse(41 if (j//16)%2==0 else 39,0.35,0.18)),t0)
    if j%4==0:place(o,pan(tick(0.12),0.5),t0)
  t=tt(T);sw=np.sin(2*np.pi*np.cumsum(220*2**(t/max(T,1)*0.5))/SR)*0.04*np.minimum(1,t/2)
  place(o,pan(sw,0.2),0)
  return verb(o,0.2)
def c_dark(T):      # low cello drone + metallic scrape + sub pulses
  o=np.zeros((int(T*SR)+SR*3,2));place(o,pan(cello([31,38],T,0.22,a=2.0,r=2.0)),0)
  for t0 in np.arange(1.0,T,4.0):
    t=tt(1.8);sc=bp(rng.standard_normal(len(t)),2500,6000)*np.sin(np.pi*t/1.8)**3*0.06
    place(o,pan(sc,0.4*(-1)**int(t0)),t0)
  for t0 in np.arange(0,T,2.0):place(o,pan(subpulse(33,0.4,0.9)),t0)
  return verb(o,0.35,True)
def c_resolve(T):   # uplifting: strings pad + felt piano + light pulse, D major
  o=np.zeros((int(T*SR)+SR*3,2));bt=60/84;prog=[[50,57,62,66],[47,54,59,62],[43,50,55,59],[45,52,57,61]];mel=[74,73,71,69];k=0
  for b0 in bars(T,84,4):
    ch=prog[k%4]
    place(o,pad([c+12 for c in ch],bt*4,0.1),b0)
    place(o,pan(cello([ch[0]-12],bt*4,0.12,a=0.8,r=1.0)),b0)
    for j,m in enumerate([ch[1],ch[2],ch[3],ch[2]]):place(o,pan(felt(m+12,bt,0.14),0.2*(j-1.5)),b0+j*bt)
    if k%2==0:place(o,pan(felt(mel[(k//2)%4]+12,bt*2,0.16),0.1),b0+bt*0.5)
    place(o,pan(kick(0.15)),b0);k+=1
  return verb(o,0.35,True)
CUES=dict(hype=c_hype,playful=c_playful,romance=c_romance,longing=c_longing,heartbreak=c_heartbreak,tension=c_tension,dark=c_dark,resolve=c_resolve)
LVL=dict(hype=-38,playful=-42,romance=-41,longing=-40,heartbreak=-40,tension=-41,dark=-40,resolve=-40)
SFX=dict(sub_drop=lambda c:sub_drop(),reverse_swell=lambda c:reverse_swell(c.get('len',2.5)),shimmer=lambda c:shimmer(),
         swish=lambda c:swish(),hit=lambda c:hit(),riser=lambda c:riser(c.get('len',3.0)))
SDB=dict(sub_drop=-27,reverse_swell=-32,shimmer=-29,swish=-38,hit=-26,riser=-32)
def key(k,TL):
  for e in TL:
    if e['key']==k:return e
  raise KeyError(k)
total=TL[-1]['start']+TL[-1]['dur'];N=int(total*SR)
mus=np.zeros((N+SR*6,2));sfx=np.zeros_like(mus)
for c in CU:
  if 'cue' in c:
    a=key(c['from'],TL)['start'];b=key(c['to'],TL);b=b['start']+b['dur'];T=b-a
    x=CUES[c['cue']](T+2.0)[:int((T+2.0)*SR)]
    x*=10**((LVL[c['cue']]+c.get('gain',0))/20)/(np.sqrt((x**2).mean())+1e-9)
    n=len(x);e=np.ones(n);fi=int(1.0*SR);fo=int(2.0*SR);e[:fi]=np.linspace(0,1,fi);e[-fo:]=np.linspace(1,0,fo)
    place(mus,x*e[:,None],a)
  else:
    e=key(c['at'],TL);t0=e['start']+(e['dur'] if c.get('pos')=='end' else 0)+c.get('off',0)
    s=c['sfx'];x=SFX[s](c)
    if s in('riser','reverse_swell'):t0-=len(x)/SR
    w=int(SR*0.5);rms=max(np.sqrt((x[i:i+w]**2).mean()) for i in range(0,max(1,len(x)-w),w//2))
    x=x*10**(c.get('db',SDB[s])/20)/(rms+1e-9);place(sfx,x,max(0,t0))
for e in TL:
  if e['key'].startswith('c:'):
    x=swish();x*=10**(-40/20)/(np.sqrt((x**2).mean())+1e-9);place(sfx,x,max(0,e['start']-0.25))
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
