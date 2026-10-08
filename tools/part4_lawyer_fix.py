# Part 4 lawyer scene: Harold now speaks to Grace (OTS, Grace blurred from behind) instead of lecturing the camera.
# Shot 18 (line played over a wide shot) and 21 (to camera) become lip-synced OTS lines; 19 becomes Grace's silent nod.
# usage: python3 part4_lawyer_fix.py meas_fix.json
import json,sys
MS=json.load(open(sys.argv[1]));TARGET=-25;LEAD=0.4;TAIL=0.55
NEW={18:('HJ','20261008_201738_ead2410f-7c87-46b3-9888-9e87b33290c7',None),   # "A judge won't take the word ... We need them on tape."
     19:('X','20261008_175815_8e054b7f-a136-408c-bed0-b47f09e2cbd9','silent'),# Grace listens and nods
     21:('HJ','20261008_201738_f5b28708-96bc-4cbf-9cde-b07d6a93c35b',3.7)}    # "They think he can't understand them ..." (ad-lib before 3.7 s cut)
M=json.load(open('part4_edit_list.json'))
for i,c in enumerate(M):
  n=c.get('n')
  if n not in NEW:continue
  spk,stem,opt=NEW[n];s,e,d,l=MS[stem]
  if opt=='silent':M[i]={'n':n,'t':{spk:stem}};continue
  ss=opt if opt else max(0,round(s-LEAD,2))
  M[i]={'n':n,'t':{spk:stem},'ss':ss,'maxdur':min(d,round(e+TAIL,2)),'gain':round(TARGET-l,1)}
json.dump(M,open('part4_edit_list.json','w'),indent=0,ensure_ascii=False)
print([M[i] for i,c in enumerate(M) if c.get('n') in NEW])
