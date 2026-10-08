# Sandbox QA for OTS clips: python3 qa34.py KEY=URL ...  -> qa.txt (words with times) + KEY.jpg (start|mid|end strip)
import sys,subprocess as sp,json
from faster_whisper import WhisperModel
items=[a.split('=',1) for a in sys.argv[1:]]
for k,u in items:sp.run(['curl','-sf','--retry','3','-o',k+'.mp4',u])
m=WhisperModel('medium.en',compute_type='int8')
out=open('qa.txt','a')
for k,u in items:
  d=float(sp.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',k+'.mp4'],capture_output=True,text=True).stdout)
  for i,t in enumerate([0.5,d/2,d-0.3]):
    sp.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',k+'.mp4','-frames:v','1','-vf','scale=320:180',f'{k}_{i}.jpg'])
  sp.run(['ffmpeg','-v','error','-y','-i',f'{k}_0.jpg','-i',f'{k}_1.jpg','-i',f'{k}_2.jpg','-filter_complex','hstack=3',k+'.jpg'])
  s,_=m.transcribe(k+'.mp4',beam_size=5,word_timestamps=True,condition_on_previous_text=False)
  w=[(x.word.strip(),round(x.start,2)) for g in s for x in g.words]
  out.write(k+' | '+' '.join(a for a,b in w)+' | start '+str(w[0][1] if w else '-')+'\n');out.flush()
