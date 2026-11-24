import json,subprocess as sp,numpy as np
W='/home/user/tr/w'; SR=48000
P=json.load(open(W+'/plan.json')); TT=P['T']; N=int((TT+0.5)*SR)
def load(f,a=None,ln=None):
  c=['ffmpeg','-v','error']+(['-ss','%.3f'%a] if a is not None else [])+['-i',f]+(['-t','%.3f'%ln] if ln else [])+['-f','f32le','-ac','2','-ar',str(SR),'-']
  return np.frombuffer(sp.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
def put(buf,x,T,g=1.0,fi=0.0,fo=0.0):
  x=x*g; n=len(x)
  if fi>0: k=min(n,int(fi*SR)); x[:k]*=np.linspace(0,1,k)[:,None]
  if fo>0: k=min(n,int(fo*SR)); x[n-k:]*=np.linspace(1,0,k)[:,None]
  s=int(T*SR)
  if s<0: x=x[-s:]; s=0
  e=min(len(buf),s+len(x)); buf[s:e]+=x[:e-s]
db=lambda d:10**(d/20)
M=load('/home/user/tr/music.mp3')
mk={m[0]+':'+str(m[3]):m for m in P['marks']}
cards=[m for m in P['marks'] if m[0] in('card','title','poster')]
T2=[m for m in cards if m[3]=='TWO BOYS.'][0][1]
T1c=[m for m in cards if m[3]=='ONE CHOICE.'][0]
Tt=[m for m in cards if m[0]=='title'][0][1]
Tend=[m for m in cards if m[0]=='poster'][0][1]
Tbut=Tt+[m for m in cards if m[0]=='title'][0][2]
mus=np.zeros((N,2),np.float32)
seg=lambda a,b:M[int(a*SR):int(b*SR)].copy()
# A: soft piano, ends right before the build
put(mus,seg(19.6-T2,19.6),0,db(-1),fi=1.0,fo=0.4)
# B: hit at M30 lands on TWO BOYS card
put(mus,seg(29.85,39.5),T2-0.15,db(0))
# C/D: M70 hit lands on title; runs into button then fades
c0=Tt-30.0
put(mus,seg(40.0,70.0+(Tbut-Tt)+0.4),c0,db(0),fo=1.2)
# E: soft outro under button + end card
put(mus,seg(83.4,89.0),Tbut-0.2,db(-4),fi=0.6,fo=1.5)
# dialogue
dl=np.zeros((N,2),np.float32); act=np.zeros(N,bool)
for T,a,t,ln in P['dlg']:
  x=load(a,t,ln); put(dl,x,T,db(5),fi=0.05,fo=0.08)
  r=np.sqrt((x**2).mean(1)); 
  k=int(0.05*SR)
  for i in range(0,len(r),k):
    if r[i:i+k].mean()>0.01: act[int(T*SR)+i:int(T*SR)+i+k]=True
# smooth duck envelope (-9 dB under speech)
env=np.where(act,db(-15),1.0).astype(np.float32)
k=int(0.25*SR); env=np.convolve(env,np.ones(k)/k,'same').astype(np.float32)
mus*=env[:,None]
# SFX
fx=np.zeros((N,2),np.float32); S='/home/user/tr/sfx/'
wh=load(S+'whoosh.mp3'); bo=load(S+'boom.mp3'); br=load(S+'braam.mp3'); ri=load(S+'riser.mp3')
wpk=np.argmax(np.abs(wh).sum(1))/SR
for m in cards:
  if m[0]!='poster' and m[1]>1: put(fx,wh,m[1]-wpk,db(-8))
put(fx,bo,T2-0.02,db(-3)); put(fx,bo,T1c[1]-0.02,db(-5))
put(fx,br,Tt-0.03,db(-2))
stop=[d for d in P['dlg'] if abs(d[2]-(533.4-439.483))<0.01]
for d in stop: put(fx,bo,d[0],db(-9))
put(fx,ri,Tt-2.0-len(ri)/SR,db(-10),fi=2.0)
mix=mus+dl+fx
sp.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','-af','loudnorm=I=-14:TP=-1.0:LRA=11','-ar','48000',W+'/mix.wav'],input=mix.astype(np.float32).tobytes(),check=True)
sp.run(['ffmpeg','-v','error','-y','-i',W+'/video.mp4','-i',W+'/mix.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','256k','-shortest','-movflags','+faststart','/home/user/tr/TBOH_trailer.mp4'],check=True)
print('done',TT,'T2',T2,'title',Tt,'button',Tbut)
