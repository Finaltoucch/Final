# Trailer score + sound design (original, procedural: uses the synths from score.py) mixed under the dialogue stem.
# usage: python3 trailer_mix.py score.py tl.json vocals.wav vid.mp4 out.mp4
import json,sys,subprocess as sp,numpy as np
src=open(sys.argv[1]).read()
head,rest=src.split('# ---- cues ----')
head=head.replace("TL=json.load(open(sys.argv[1]));CU=json.load(open(sys.argv[2]))","")
exec(head+'# ---- cues ----'+rest.split('LVL=dict')[0])
TL=json.load(open(sys.argv[2]));S=lambda i:TL[i]['start'];E=lambda i:TL[i]['start']+TL[i]['dur']
total=E(len(TL)-1);N=int(total*SR)
mus=np.zeros((N+SR*6,2));sfx=np.zeros_like(mus)
def rms(x):return np.sqrt((x**2).mean())+1e-9
def cue(name,a,b,db,fi=0.3,fo=0.35):
  T=b-a;x=CUES[name](T+1.0)[:int(T*SR)]
  x=x*10**(db/20)/rms(x);n=len(x);e=np.ones(n);fi=int(fi*SR);fo=int(fo*SR)
  e[:fi]=np.linspace(0,1,fi);e[-fo:]=np.linspace(1,0,fo);place(mus,x*e[:,None],a)
def fx(kind,t,db,**k):
  x={'impact':impact,'stinger':stinger,'whoosh':whoosh,'braam':lambda:braam(0.8,4.5),'boom':lambda:boom(1.0,4.0),'riser':lambda:riser(k.get('len',4.0),0.7)}[kind]()
  if kind=='riser':t-=len(x)/SR
  pk=max(rms(x[i:i+SR//2]) for i in range(0,max(1,len(x)-SR//2),SR//4))
  place(sfx,x*10**(db/20)/pk,max(0,t))
# act 1: warm piano
cue('hope',S(0)+0.2,E(4),-25)
# act 2: the rival, the toast, the fall
fx('stinger',S(5),-20)
cue('tension',S(5),E(8),-27)
fx('riser',S(7)+1.3,-22,len=3.5)
fx('impact',S(7)+1.3,-14);fx('impact',S(8)+0.05,-18)
cue('dark',S(9),E(12),-26)
# act 3: the fight back, building to the card
cue('panic',S(13),E(19),-26)
fx('riser',S(20)+0.05,-19,len=4.5)
fx('impact',S(20)+0.05,-13);fx('braam',S(20)+0.05,-17)
cue('panic',S(21),E(22),-24)
fx('impact',S(22)+0.1,-19)
# the proposal: tender, then silence
cue('tender',S(23),E(23)+0.1,-27,fo=0.25)
# the poster: boom + braam
fx('boom',S(25)+0.02,-11);fx('impact',S(25)+0.02,-13);fx('braam',S(25)+0.1,-16)
cue('tension',S(25)+0.4,total,-33,fi=0.8,fo=1.2)
for e in TL:
  if e['type']=='card':fx('whoosh',e['start']-0.25,-26)
mus=mus[:N];sfx=sfx[:N]
dlg=np.frombuffer(sp.run(['ffmpeg','-v','error','-i',sys.argv[3],'-f','f32le','-ac','2','-ar','48000','-'],capture_output=True).stdout,np.float32).reshape(-1,2)[:N]
if len(dlg)<N:dlg=np.vstack([dlg,np.zeros((N-len(dlg),2),np.float32)])
dlg=dlg*10**(-16/20)/max(1e-6,np.percentile(np.abs(dlg),99.9))*0.9*3
e=np.sqrt(np.convolve((dlg**2).mean(1),np.ones(2400)/2400,'same'));spk=e>max(0.004,0.1*np.percentile(e,99))
g=np.ones(N,np.float32);lvl=1.0;hop=480
for j in range(0,N,hop):
  tgt=0.3 if spk[j:j+hop].any() else 1.0;lvl+=(tgt-lvl)*(0.4 if tgt<lvl else 0.06);g[j:j+hop]=lvl
mix=dlg+mus*g[:,None]+sfx*(0.5+0.5*g[:,None])
mix=np.tanh(mix*0.95)/0.95
sp.run(['ffmpeg','-v','error','-y','-f','f32le','-ar','48000','-ac','2','-i','-','tmix.wav'],input=mix.astype(np.float32).tobytes(),check=True)
sp.run(['ffmpeg','-v','error','-y','-i',sys.argv[4],'-i','tmix.wav','-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-14:TP=-1.0:LRA=11','-c:a','aac','-b:a','256k','-ar','48000','-movflags','+faststart','-shortest',sys.argv[5]],check=True)
print('MIXED',round(total,2))
