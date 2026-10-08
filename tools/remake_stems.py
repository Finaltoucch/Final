# Picks the final stem for every remade Part 1/2 line: the voice-changed take unless it was
# flagged as garbled (then the raw Kling take). Guard, doctor and shouts stay raw.
# usage: python3 remake_stems.py <scratch dir>  -> remake_stems.json
import json,sys,os
D=sys.argv[1]
def rd(f):
  r={}
  for l in open(os.path.join(D,f)):
    k,v=l.split()[:2]
    if k.isdigit():r[int(k)]=v
  return r
raw={**rd('r1r.txt'),**rd('r2r.txt')}
vc={}
for l in open(os.path.join(D,'vcres.txt')):
  k,v=l.split()
  if v.startswith('20261008_15'):vc[int(k)]=v
bad={int(l.split()[0]) for l in open(os.path.join(D,'vcbad.txt')) if l.split()[1:2]==['raw']}
RAW_ALWAYS={206}
P1=json.load(open('part1r_shots.json'))['lines'];P2=json.load(open('part2r_shots.json'))['lines']
out={}
for part,L,off in (('1',P1,0),('2',P2,200)):
  for p in L:
    s=off+p['id']
    if part=='1' and p['id'] in (9,11,13):s=100+p['id']
    if p['spk']=='U' or s in bad or s in RAW_ALWAYS or s not in vc:src='raw';stem=raw[s]
    else:src='vc';stem=vc[s]
    out[f"{part}:{p['id']}"]=dict(stem=stem,src=src,spk=p['spk'],o=p['o'],text=p['text'])
json.dump(out,open('remake_stems.json','w'),indent=0)
miss=[k for k,v in out.items() if v['src']=='raw' and v['spk'] not in 'U']
print(len(out),'stems; raw:',miss)
