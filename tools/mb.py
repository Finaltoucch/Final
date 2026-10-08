import json,subprocess as sp,os,re,difflib,sys,numpy as np
from concurrent.futures import ThreadPoolExecutor
P="https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_"
M=json.load(open(sys.argv[1]))
os.makedirs('d',exist_ok=True)
SR=48000
def run(c,**k):return sp.run(c,check=True,**k)
def dl(u):
  f='d/'+u.split('_')[-1]+'.mp4'
  if not os.path.exists(f):run(['curl','-sf','--retry','3','-o',f,P+u+'.mp4'])
  return f
with ThreadPoolExecutor(16) as ex:list(ex.map(dl,[u for c in M if 't' in c for u in list(c['t'].values())+([c['vo']] if 'vo' in c else [])]))
print('downloaded',flush=True)
WM=None
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
    cs=c.get('sec',CS);outs.append(card(c['card'],i,cs));wavs.append(np.zeros((int(round(cs*SR)),2),np.float32));TL.append(dict(key='c:'+c['card'],start=TPOS,dur=cs));TPOS+=cs;print('card',i,flush=True);continue
  t=c['t'];ks=list(t);f0=dl(t[ks[0]]);D=vdur(f0)
  if 'vo' in c:
    au=rd(dl(c['vo']))
    if c.get('vo_ss'):au=au[int(c['vo_ss']*SR):]
    rep.append(f"#{c['n']}: VO")
  elif 'l' not in c:
    au=rd(f0);rep.append(f"#{c['n']}: single {ks[0]}")
  else:
    if WM is None:
      from faster_whisper import WhisperModel;WM=WhisperModel('base.en',device='cpu',compute_type='int8')
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
  if c.get('maxdur'):D=min(D,c['maxdur'])
  if c.get('trim_after') and 'l' not in c:
    if WM is None:
      from faster_whisper import WhisperModel;WM=WhisperModel('base.en',device='cpu',compute_type='int8')
    segs,_=WM.transcribe(f0,word_timestamps=True,language='en');ww=[w for s in segs for w in (s.words or [])]
    hits=[w for w in ww if N(w.word)==N(c['trim_after'])]
    if hits:D=min(D,hits[-1].end+0.35);rep.append(f"   trimmed at {D:.2f}s")
  if c.get('gain'):
    pk=float(np.abs(au).max())+1e-9;g=min(c['gain'],-1-20*np.log10(pk));au=au*10**(g/20);rep.append(f"   gain {g:+.1f} dB")
  ss=c.get('ss',0)
  if ss:D-=ss;au=au[int(ss*SR):];rep.append(f"   skip first {ss:.2f}s")
  NF=int(D*24);D=NF/24;n=NF*2000;au=au[:n]
  if len(au)<n:au=np.vstack([au,np.zeros((n-len(au),2),np.float32)])
  vf=(c['pre']+',' if c.get('pre') else '')+BASE+''.join(lower_third(*x) for x in c.get('lt',[]))
  o=f'c{i:02d}.mp4'
  run(['ffmpeg','-v','error','-y']+(['-ss',str(ss)] if ss else [])+['-i',f0,'-map','0:v','-frames:v',str(NF),'-vf',vf,'-c:v','libx264','-preset','veryfast','-crf','19','-an',o])
  wavs.append(au);outs.append(o);TL.append(dict(key='n%s'%c['n'],start=TPOS,dur=D));TPOS+=D;print('done',i,c['n'],flush=True)
open('list.txt','w').write(''.join(f"file '{o}'\n" for o in outs))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','list.txt','-an','-c','copy','vid.mp4'])
full=np.vstack(wavs);run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','dlg.wav'],input=full.tobytes())
json.dump(TL,open('timeline.json','w'))
print('FINISHED',TPOS,flush=True)
