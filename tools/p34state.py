# Tracks the Parts 3-4 OTS pass: frame edit, Kling clip and voice-change job per line.
# usage: python3 p34state.py set <key> <field> <value> ...   |   python3 p34state.py show
import json,sys,os
F='p34state.json';S=json.load(open(F)) if os.path.exists(F) else {}
if sys.argv[1]=='set':
  a=sys.argv[2:]
  for i in range(0,len(a),3):S.setdefault(a[i],{})[a[i+1]]=a[i+2]
  json.dump(S,open(F,'w'),indent=1,sort_keys=True)
else:
  for k in sorted(S):print(k,S[k])
