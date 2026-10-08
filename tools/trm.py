# Accurate transcript (whisper medium.en) of clips: python3 trm.py a.mp4 b.mp4 ...
import sys
from faster_whisper import WhisperModel as W
m=W('medium.en',compute_type='int8')
for f in sys.argv[1:]:
  try:
    s,_=m.transcribe(f,condition_on_previous_text=False,beam_size=5)
    print(f,'|',' '.join(x.text.strip() for x in s),flush=True)
  except Exception as e: print(f,'ERR',e,flush=True)
