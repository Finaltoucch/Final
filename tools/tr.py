import sys
from faster_whisper import WhisperModel as W
m=W('small.en',compute_type='int8')
for f in sys.argv[1:]:
  try: print(f,'|',' '.join(x.text for x in m.transcribe(f)[0]))
  except Exception as e: print(f,'ERR',e)
