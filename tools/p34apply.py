# Swap the Parts 3-4 OTS takes into the edit list: python3 p34apply.py <part> meas.json
# meas.json: {stem: [first_word_start, last_word_end, duration, lufs]}. Each line is trimmed to its speech
# (0.4 s lead, 0.55 s tail) and level-matched to -25 LUFS; old crops/trims belonged to the old frames and are dropped.
import json,sys
p=int(sys.argv[1]);MS=json.load(open(sys.argv[2]));S=json.load(open('p34state.json'))
O={o['part']*1000+o['shot']:o for o in json.load(open('p34ots.json'))}
LEAD,TAIL,TARGET=0.4,0.55,-25;LOUD={'raw':-22}
M=json.load(open(f'part{p}_edit_list.json'));n=0
for i,c in enumerate(M):
  k=str(p*1000+c.get('n',-1)) if isinstance(c.get('n'),int) else None
  if not k or k not in S or 'final' not in S[k]:continue
  o=O[int(k)];stem=S[k]['final'];s,e,d,l=MS[stem]
  ss=float(S[k].get('ss',max(0,round(s-LEAD,2))))
  new={'n':c['n'],'t':{o['spk']:stem},'ss':ss,'maxdur':min(d,round(e+TAIL,2)),'gain':round((LOUD['raw'] if o['raw'] else TARGET)-l,1)}
  if 'lt' in c:new['lt']=c['lt']
  M[i]=new;n+=1
json.dump(M,open(f'part{p}_edit_list.json','w'),indent=0,ensure_ascii=False)
print('replaced',n)
