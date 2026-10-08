# Builds part1/part2 edit lists for the over-the-shoulder remake.
# Every old dialogue clip is replaced by its remade OTS lines (one clip per line, trimmed to the
# speech with a short lead-in and tail, loudness-matched); silent shots and cards stay.
# usage: python3 mkremake.py <part> meas.json
import json,sys
part=sys.argv[1];MS={k:dict(zip(('s','e','dur','lufs'),v)) for k,v in json.load(open(sys.argv[2])).items()}
S=json.load(open('remake_stems.json'))
OLD=json.load(open(f'part{part}_edit_list_pre_ots.json'));CUES=json.load(open(f'part{part}_cues_pre_ots.json'))
TARGET=-25;LOUD={'2:6':-22}            # the leg-panic shout sits higher
LEAD=0.3;TAIL=0.55
LT={'1:3':['VANESSA PIERCE',"Ethan Caldwell's fiancée"],'1:11':['MRS. HAYES','Head housekeeper'],
    '1:23':['ETHAN CALDWELL','CEO, Caldwell Freight'],'1:31':['BRADLEY CALDWELL',"Ethan's younger brother"],
    '1:60':['MAMA RUTH',"Grace's mother"]}
EXTRA={'1:16':{'ss':1.7},                                   # ad-libbed "Oh" before the line
       '1:60':{'pre':'crop=iw*0.84:ih*0.84:iw*0.08:0'}}     # stray card at the frame edge
# Part 2 silent additions: spoon-feeding beat (replaces old 42, uniform sleeve) and Ethan's look (replaces old 47, daylight)
NEW_SILENT={'2':{42:[{'n':'42.1','t':{'X':'20261008_155934_48fdb850-c811-4a4e-9929-e5ed35398059'},'ss':1.0}],47:[{'n':'47.1','t':{'X':'20261008_155934_7f551a25-a6fc-419e-a832-b4a21323cc8a'}}]}}
groups={}
for k,v in S.items():
  p,i=k.split(':')
  if p==part:groups.setdefault(v['o'],[]).append((int(i),k,v))
def line(k,v,idx,o):
  m=MS[v['stem']];ss=max(0,round(m['s']-LEAD,2));end=min(m['dur'],round(m['e']+TAIL,2))
  c={'n':f'{o}.{idx}','t':{v['spk']:v['stem']},'ss':ss,'maxdur':end,'gain':round(LOUD.get(k,TARGET)-m['lufs'],1)}
  c.update(EXTRA.get(k,{}))
  if k in LT:c['lt']=[LT[k]+[0.3,round(min(4.5,end-c['ss']-0.2),2)]]
  return c
out=[];ren={}
for c in OLD:
  if 'card' in c:out.append(c);continue
  o=c['n'];c={k:x for k,x in c.items() if k!='amb'}
  if o in groups:
    new=[line(k,v,j,o) for j,(i,k,v) in enumerate(sorted(groups[o]),1)]
  elif o in NEW_SILENT.get(part,{}):
    new=NEW_SILENT[part][o]
  else:new=[c]
  ren[f'n{o}']=(f"n{new[0]['n']}",f"n{new[-1]['n']}");out+=new
for c in CUES:
  for f,pick in (('from',0),('to',1),('at',0)):
    if c.get(f) in ren:c[f]=ren[c[f]][pick if f!='at' else (1 if c.get('pos')=='end' else 0)]
json.dump(out,open(f'part{part}_edit_list.json','w'),indent=0,ensure_ascii=False)
json.dump(CUES,open(f'part{part}_cues.json','w'),indent=0,ensure_ascii=False)
print(len(out),'clips')
