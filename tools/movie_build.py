import json,subprocess as sp,os,re,difflib,sys,numpy as np,urllib.request
from concurrent.futures import ThreadPoolExecutor
P="https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_"
M=json.load(open(sys.argv[1]));OUT=sys.argv[2]
os.makedirs('d',exist_ok=True);os.makedirs('amb',exist_ok=True)
SR=48000
def run(c,**k):return sp.run(c,check=True,**k)
def dl(u):
  f='d/'+u.split('_')[-1]+'.mp4'
  if not os.path.exists(f):run(['curl','-sf','--retry','3','-o',f,P+u+'.mp4'])
  return f
with ThreadPoolExecutor(16) as ex:list(ex.map(dl,[u for c in M if 't' in c for u in list(c['t'].values())+([c['vo']] if 'vo' in c else [])]))
print('downloaded',flush=True)
# public-domain only (Wikimedia Commons, PD)
W={'birds':'https://upload.wikimedia.org/wikipedia/commons/0/0e/Gentle_breeze_and_birds_singing.ogg'}
for k,u in W.items():
  if os.path.exists(f'amb/{k}.wav'):continue
  req=urllib.request.Request(u,headers={'User-Agent':'FilmAmbience/1.0 (personal film project)'})
  open(f'amb/{k}.src','wb').write(urllib.request.urlopen(req).read())
  run(['ffmpeg','-v','error','-y','-i',f'amb/{k}.src','-ac','2','-ar',str(SR),'-af','highpass=f=60',f'amb/{k}.wav'])
SYN={'room':"anoisesrc=color=brown:amplitude=0.6:r=48000,lowpass=f=350,volume=0.10",
     'traffic':"anoisesrc=color=brown:amplitude=0.8:r=48000,lowpass=f=250,volume='0.10*(0.6+0.4*sin(2*PI*t/9))':eval=frame",
     'fridge':"sine=f=60:r=48000,volume=0.04[a];sine=f=120:r=48000,volume=0.02[b];anoisesrc=color=brown:amplitude=0.4:r=48000,lowpass=f=200,volume=0.05[c];[a][b][c]amix=inputs=3:normalize=0",
     'dryer':"sine=f=50:r=48000,volume=0.05[a];anoisesrc=color=pink:amplitude=0.3:r=48000,lowpass=f=600,volume='0.06*(0.7+0.3*sin(2*PI*t*1.5))':eval=frame[b];[a][b]amix=inputs=2:normalize=0",
     'cricket':"sine=f=4400:r=48000,volume='0.05*gt(sin(2*PI*t*28),0)*lt(mod(t,0.85),0.22)':eval=frame[a];sine=f=4900:r=48000,volume='0.03*gt(sin(2*PI*t*31),0)*lt(mod(t+0.4,1.1),0.18)':eval=frame[b];[a][b]amix=inputs=2:normalize=0,highpass=f=3000",
     'water':"anoisesrc=color=brown:amplitude=0.8:r=48000,lowpass=f=700,highpass=f=80,volume='0.12*(0.45+0.55*abs(sin(2*PI*t/2.3)*sin(2*PI*t/3.7)))':eval=frame",
     'drone':"sine=f=55:r=48000,volume='0.05*(0.6+0.4*sin(2*PI*t/6))':eval=frame[a];sine=f=82.4:r=48000,volume=0.03[b];sine=f=110.5:r=48000,volume=0.012[c];[a][b][c]amix=inputs=3:normalize=0",
     'crowd':"anoisesrc=color=brown:amplitude=0.5:r=48000,lowpass=f=700,highpass=f=150,volume='0.10*(0.7+0.2*sin(2*PI*t/3.1)+0.1*sin(2*PI*t/1.3))':eval=frame",
     'hvac':"anoisesrc=color=brown:amplitude=0.6:r=48000,lowpass=f=500,highpass=f=60,volume=0.10",
     'monitor':"sine=f=880:r=48000,volume='0.02*lt(mod(t,1.0),0.08)':eval=frame,lowpass=f=1500",
     'siren':"aevalsrc='0.05*sin(2*PI*950*t-250*1.3*cos(2*PI*t/1.3))':s=48000,lowpass=f=1800"}
for k,g in SYN.items():
  run(['ffmpeg','-v','error','-y','-filter_complex',g+',aformat=sample_rates=48000:channel_layouts=stereo','-t','40',f'amb/{k}.wav'])
AMB={'ext_day':[('birds',0.9),('room',0.3)],'int_day':[('room',1.0),('birds',0.12)],'kitchen_day':[('room',0.8),('birds',0.3)],
     'pantry':[('room',1.0),('drone',0.9)],'night_kitchen':[('fridge',1.0),('cricket',0.25),('room',0.6)],
     'apartment':[('room',1.0),('traffic',1.0),('cricket',0.12)],'pool':[('water',1.0),('cricket',0.6),('drone',0.5)],'laundry':[('dryer',1.0),('drone',0.8)],
     'party':[('crowd',1.0),('cricket',0.3),('room',0.3)],'party_drone':[('crowd',0.5),('drone',0.9),('cricket',0.2)],'party_panic':[('crowd',1.0),('drone',0.6)],
     'party_siren':[('crowd',0.5),('siren',0.35),('drone',0.4)],'hospital_rush':[('hvac',1.0),('monitor',0.4),('crowd',0.4)],'hospital_night':[('hvac',1.0),('monitor',0.25)],
     'hospital_day':[('hvac',1.0),('monitor',0.5),('birds',0.08)],'hospital_hall':[('hvac',1.0),('crowd',0.25)],'hospital_day_soft':[('hvac',0.8),('birds',0.2)]}
TGT={'ext_day':-45,'int_day':-56,'kitchen_day':-53,'pantry':-49,'night_kitchen':-52,'apartment':-51,'pool':-46,'laundry':-48,
     'party':-44,'party_drone':-46,'party_panic':-44,'party_siren':-44,'hospital_rush':-47,'hospital_night':-54,'hospital_day':-52,'hospital_hall':-51,'hospital_day_soft':-54}
def amb(key,dur):
  out=np.zeros((int(dur*SR),2),np.float32)
  for src,g in AMB[key]:
    a=np.frombuffer(sp.run(['ffmpeg','-v','error','-stream_loop','-1','-i',f'amb/{src}.wav','-t',str(dur),'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True,check=True).stdout,np.float32).reshape(-1,2)
    a=a/(float(np.sqrt((a**2).mean()))+1e-9)
    n=min(len(a),len(out));out[:n]+=a[:n]*g
  rms=float(np.sqrt((out**2).mean()))+1e-9;out*=10**(TGT[key]/20)/rms
  f=int(.4*SR);r=np.linspace(0,1,f)[:,None];out[:f]*=r;out[-f:]*=r[::-1]
  return out
from faster_whisper import WhisperModel
WM=WhisperModel('base.en',device='cpu',compute_type='int8')
def dur(f):return float(sp.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def vdur(f):
  return int(sp.run(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip())/24-0.001
def rd(f):
  x=np.frombuffer(sp.run(['ffmpeg','-v','error','-i',f,'-vn','-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True).stdout,np.float32).reshape(-1,2).copy()
  return x if len(x) else np.zeros((int(dur(f)*SR),2),np.float32)
N=lambda w:re.sub(r'[^a-z0-9]','',w.lower())
sh=lambda c:sp.run(c,shell=True,capture_output=True,text=True).stdout.strip()
FONT=sh("fc-list | grep -i 'Montserrat' | grep -iE 'Bold' | head -1 | cut -d: -f1") or sh("fc-list | grep -i 'DejaVuSans-Bold' | head -1 | cut -d: -f1") or sh("fc-list | head -1 | cut -d: -f1")
FONTL=FONT
BASE="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24,format=yuv420p,setsar=1"
tc=0
def tf(s):
  global tc;tc+=1;p=f'txt{tc}.txt';open(p,'w').write(s);return p
def lower_third(name,role,t0,t1):
  a=f"if(lt(t,{t0}),0,if(lt(t,{t0+0.5}),(t-{t0})/0.5,if(lt(t,{t1-0.5}),1,if(lt(t,{t1}),({t1}-t)/0.5,0))))"
  return (f",drawbox=x=70:y=ih-250:w=8:h=120:color=0xE8B04A@1:t=fill:enable='between(t,{t0},{t1})'"
          f",drawtext=fontfile='{FONT}':textfile='{tf(name)}':fontsize=60:fontcolor=white:x=100:y=h-250:alpha='{a}':shadowcolor=black@0.7:shadowx=2:shadowy=2"
          f",drawtext=fontfile='{FONTL}':textfile='{tf(role)}':fontsize=36:fontcolor=0xE8B04A:x=102:y=h-170:alpha='{a}':shadowcolor=black@0.7:shadowx=2:shadowy=2")
CS=2.625
def card(text,i,sec=CS):
  o=f'k{i:02d}.mp4';a=f"if(lt(t,0.4),t/0.4,if(lt(t,{sec-0.4}),1,({sec}-t)/0.4))"
  run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=black:s=1920x1080:r=24:d={sec}','-t',str(sec),
       '-vf',f"drawtext=fontfile='{FONT}':textfile='{tf(text)}':fontsize=64:fontcolor=white:x=(w-tw)/2:y=(h-th)/2:alpha='{a}',format=yuv420p",
       '-c:v','libx264','-preset','veryfast','-crf','19','-an',o]);return o
rep=[];outs=[];wavs=[];TL=[];TPOS=0.0
for i,c in enumerate(M,1):
  if 'card' in c:
    outs.append(card(c['card'],i));wavs.append(np.zeros((int(round(CS*SR)),2),np.float32));TL.append(dict(key='c:'+c['card'],start=TPOS,dur=CS));TPOS+=CS;print('card',i,flush=True);continue
  t=c['t'];ks=list(t);f0=dl(t[ks[0]]);D=vdur(f0)
  if 'vo' in c:
    au=rd(dl(c['vo']));rep.append(f"#{c['n']}: VO")
  elif 'l' not in c:
    au=rd(f0);rep.append(f"#{c['n']}: single {ks[0]}")
  else:
    segs,_=WM.transcribe(f0,word_timestamps=True,language='en')
    ww=[(w.word,w.start,w.end) for s in segs for w in (s.words or [])]
    sw=[];spk=[]
    for s,txt in c['l']:
      for w in txt.split():sw.append(N(w));spk.append(s)
    a=[N(x[0]) for x in ww];lab=[None]*len(ww)
    for b in difflib.SequenceMatcher(None,a,sw,autojunk=False).get_matching_blocks():
      for k in range(b.size):lab[b.a+k]=spk[b.b+k]
    last=None
    for k in range(len(lab)):
      if lab[k] is None:lab[k]=last
      else:last=lab[k]
    nx=None
    for k in range(len(lab)-1,-1,-1):
      if lab[k] is None:lab[k]=nx
      else:nx=lab[k]
    lab=[x or c['l'][0][0] for x in lab]
    tr={k:rd(dl(u)) for k,u in t.items()};n=min(len(x) for x in tr.values())
    bd=[((ww[k-1][2]+ww[k][1])/2,lab[k]) for k in range(1,len(ww)) if lab[k]!=lab[k-1]]
    who=lab[0] if lab else c['l'][0][0];pos=0;sg=[]
    for tm,nw in bd+[(n/SR,None)]:
      e=min(n,int(tm*SR));sg.append((pos,e,who));pos=e;who=nw
    au=np.zeros((n,2),np.float32)
    for s0,e0,w in sg:au[s0:e0]=tr[w][s0:e0]
    xf=int(.03*SR)
    for (s0,e0,w0),(s1,e1,w1) in zip(sg,sg[1:]):
      lo=max(0,e0-xf);hi=min(n,e0+xf);r=np.linspace(0,1,hi-lo)[:,None];au[lo:hi]=tr[w0][lo:hi]*(1-r)+tr[w1][lo:hi]*r
    rep.append(f"#{c['n']}: "+' | '.join(f"{w} {s0/SR:.2f}-{e0/SR:.2f}" for s0,e0,w in sg)+"\n   heard: "+' '.join(x[0].strip() for x in ww))
    if c.get('trim_after'):
      key=N(c['trim_after']);hits=[x for x in ww if N(x[0])==key]
      if hits:D=min(D,hits[0][2]+0.5);rep.append(f"   trimmed at {D:.2f}s")
  NF=int(D*24);D=NF/24;n=NF*2000;au=au[:n]
  if len(au)<n:au=np.vstack([au,np.zeros((n-len(au),2),np.float32)])
  vf=BASE+''.join(lower_third(*x) for x in c.get('lt',[]))
  o=f'c{i:02d}.mp4'
  run(['ffmpeg','-v','error','-y','-i',f0,'-map','0:v','-frames:v',str(NF),'-vf',vf,'-c:v','libx264','-preset','veryfast','-crf','19','-an',o])
  wavs.append(au);outs.append(o);TL.append(dict(key='n%s'%c['n'],start=TPOS,dur=D));TPOS+=D;print('done',i,c['n'],flush=True)
open('list.txt','w').write(''.join(f"file '{o}'\n" for o in outs))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','list.txt','-an','-c','copy','vid.mp4'])
full=np.vstack(wavs);run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','dlg.wav'],input=full.tobytes())
json.dump(TL,open('timeline.json','w'))
print('FINISHED',TPOS,flush=True)
