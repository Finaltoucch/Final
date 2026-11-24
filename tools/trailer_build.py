# Cut a cinematic trailer from the finished movie: letterboxed, graded clips plus serif title cards.
# usage: python3 trailer_build.py full.mp4 poster.png Cinzel.ttf trailer_edl.json
# writes segs/*.mp4, vid.mp4, dlg.wav (movie audio of the kept lines) and tl.json (segment start times)
import json,sys,os,subprocess as sp
SRC,POSTER,FONT,EDL=sys.argv[1:5]
E=json.load(open(EDL));os.makedirs('segs',exist_ok=True)
def run(c):sp.run(c,check=True)
LB="scale=1920:1080,eq=contrast=1.07:saturation=0.9:gamma=0.98,vignette=PI/5,noise=alls=5:allf=t,drawbox=x=0:y=0:w=iw:h=138:color=black:t=fill,drawbox=x=0:y=ih-138:w=iw:h=138:color=black:t=fill,fps=24,format=yuv420p"
tl=[];T=0.0;wavs=[]
for i,s in enumerate(E):
  o=f'segs/{i:02d}.mp4';a=f'segs/{i:02d}.wav'
  if s['type']=='clip':
    d=round(s['out']-s['in'],3)
    run(['ffmpeg','-v','error','-y','-ss',str(s['in']),'-i',SRC,'-t',str(d),'-vf',LB+f",fade=t=in:st=0:d=0.08,fade=t=out:st={d-0.08}:d=0.08",'-an','-c:v','libx264','-preset','veryfast','-crf','18',o])
    if s.get('audio','dia')=='dia':
      run(['ffmpeg','-v','error','-y','-ss',str(s['in']),'-i',SRC,'-t',str(d),'-vn','-ac','2','-ar','48000','-af','afade=t=in:d=0.03,afade=t=out:st=%f:d=0.06'%(d-0.06),a])
    else:
      run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),a])
  elif s['type']=='card':
    d=s['sec'];open('c.txt','w').write(s['text'])
    al=f"if(lt(t,0.35),t/0.35,if(lt(t,{d-0.35}),1,({d}-t)/0.35))"
    fs=s.get('size',72)
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=black:s=1920x1080:r=24:d={d}','-vf',
         f"drawtext=fontfile={FONT}:textfile=c.txt:fontsize={fs}:fontcolor=0xF2E6C8:x=(w-tw)/2:y=(h-th)/2:alpha='{al}':shadowcolor=0xC9A24A@0.35:shadowx=0:shadowy=0,format=yuv420p",
         '-c:v','libx264','-preset','veryfast','-crf','18',o])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),a])
  elif s['type']=='black':
    d=s['sec']
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=black:s=1920x1080:r=24:d={d}','-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','18',o])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),a])
  elif s['type']=='poster':
    d=s['sec'];n=int(d*24)
    run(['ffmpeg','-v','error','-y','-loop','1','-i',POSTER,'-t',str(d),'-vf',
         f"scale=3840:-2,zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=24,fade=t=in:st=0:d=0.25,fade=t=out:st={d-0.8}:d=0.8,format=yuv420p",
         '-frames:v',str(n),'-c:v','libx264','-preset','veryfast','-crf','16',o])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),a])
    d=n/24
  # exact duration from the rendered video
  d=float(sp.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',o],capture_output=True,text=True).stdout)
  run(['ffmpeg','-v','error','-y','-i',a,'-af',f'apad,atrim=0:{d}','-ar','48000','-ac','2',a+'.fit.wav'])
  tl.append(dict(i=i,type=s['type'],start=T,dur=d,text=s.get('text')));T+=d;print('seg',i,s['type'],round(d,2),flush=True)
open('list.txt','w').write(''.join(f"file 'segs/{i:02d}.mp4'\n" for i in range(len(E))))
open('alist.txt','w').write(''.join(f"file 'segs/{i:02d}.wav.fit.wav'\n" for i in range(len(E))))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','list.txt','-c','copy','vid.mp4'])
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','alist.txt','-c:a','pcm_s16le','dlg.wav'])
json.dump(tl,open('tl.json','w'),indent=1);print('BUILT',round(T,2))
