# Prepare a HyperFrames trailer project from the finished movie.
# usage: python3 hf_trailer_prep.py full.mp4 poster.png hf_trailer_edl.json PROJECT_DIR TOTAL_SECONDS
# writes PROJECT_DIR/assets/cNN.mp4 (graded, silent clips), assets/poster.jpg, dlg.wav (dialogue in trailer time)
# and tl.json (every segment's start/duration, frame-exact at 24 fps)
import json,sys,os,subprocess as sp
SRC,POSTER,EDL,PRJ,TOTAL=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],float(sys.argv[5])
E=json.load(open(EDL));A=os.path.join(PRJ,'assets');os.makedirs(A,exist_ok=True);os.makedirs('aud',exist_ok=True)
def run(c):sp.run(c,check=True)
FPS=24
GRADE="scale=1920:1080,eq=contrast=1.08:saturation=0.88:gamma=0.97,colorbalance=rs=0.03:bs=-0.03:rh=-0.02:bh=0.03,vignette=PI/5"
fr=lambda s:round(s*FPS)
used=sum(fr(s['out']-s['in']) if s['type']=='clip' else fr(s['sec']) for s in E)
tl=[];F=0;wavs=[]
for i,s in enumerate(E):
  if s['type']=='clip':n=fr(s['out']-s['in'])
  elif s['type']=='poster':n=fr(TOTAL)-used
  else:n=fr(s['sec'])
  d=n/FPS;a=f'aud/{i:02d}.wav'
  if s['type']=='clip':
    run(['ffmpeg','-v','error','-y','-ss',str(s['in']),'-i',SRC,'-frames:v',str(n),'-vf',GRADE+',fps=24,format=yuv420p','-an','-c:v','libx264','-preset','veryfast','-crf','17','-g','12',f'{A}/c{i:02d}.mp4'])
  if s['type']=='clip' and s.get('audio','dia')=='dia':
    run(['ffmpeg','-v','error','-y','-ss',str(s['in']),'-i',SRC,'-t',str(d),'-vn','-ac','2','-ar','48000','-af',f'afade=t=in:d=0.03,afade=t=out:st={d-0.06}:d=0.06,apad,atrim=0:{d}',a])
  else:
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),a])
  tl.append(dict(i=i,type=s['type'],start=F/FPS,dur=d,text=s.get('text'),style=s.get('style'),flash=s.get('flash'),src=f'assets/c{i:02d}.mp4' if s['type']=='clip' else None))
  F+=n;print('seg',i,s['type'],round(d,3),flush=True)
run(['convert',POSTER,'-resize','2400x1350^','-gravity','center','-extent','2400x1350','-quality','92',f'{A}/poster.jpg'])
open('alist.txt','w').write(''.join(f"file 'aud/{i:02d}.wav'\n" for i in range(len(E))))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','alist.txt','-c:a','pcm_s16le','dlg.wav'])
json.dump(tl,open('tl.json','w'),indent=1);print('PREPPED',F/FPS)
