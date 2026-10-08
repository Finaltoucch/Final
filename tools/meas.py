# Speech bounds and loudness of stems: python3 meas.py stem1 stem2 ... > meas.json
import sys,json,subprocess as sp,re
from concurrent.futures import ThreadPoolExecutor
from faster_whisper import WhisperModel
P="https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_"
S=sys.argv[1:]
def dl(s):sp.run(['curl','-sf','--retry','3','-o',s+'.mp4',P+s+'.mp4']);return s
with ThreadPoolExecutor(12) as ex:list(ex.map(dl,S))
def lufs(f):
  e=sp.run(['ffmpeg','-nostats','-i',f,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
  return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1])
def dur(f):return float(sp.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
m=WhisperModel('small.en',compute_type='int8');R={}
for s in S:
  f=s+'.mp4';seg,_=m.transcribe(f,word_timestamps=True,beam_size=5,condition_on_previous_text=False)
  w=[x for g in seg for x in (g.words or [])]
  R[s]=dict(s=round(w[0].start,2) if w else 0,e=round(w[-1].end,2) if w else dur(f),dur=round(dur(f),2),lufs=lufs(f),txt=' '.join(x.word.strip() for x in w))
  print(s,R[s],file=sys.stderr,flush=True)
json.dump(R,open('meas.json','w'))
print('DONE',file=sys.stderr)
