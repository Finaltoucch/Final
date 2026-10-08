# Compare every remade line with the closest screenplay line; print the ones that differ.
# usage: python3 script_check.py  (run from repo root)
import json,re,difflib
sp=open('the-maid-who-stayed-movie-screenplay.md').read()
sp=sp[:sp.find('## PART 3')]
lines=[];cur=None
for l in sp.split('\n'):
    m=re.match(r"\*\*([A-Z][A-Z .'’-]+?)(?::\*\*|\*\*\s*(?:\*\([^)]*\)\*)?\s*:)\s*(.*)",l)
    if m: cur=[m.group(1),m.group(2)];lines.append(cur);continue
    if cur and l.strip() and not l.startswith(('*','#','---')): cur[1]+=' '+l.strip()
    else: cur=None
def clean(s): s=re.sub(r'\*\([^)]*\)\*','',s);s=re.sub(r'\*[^*]*\*','',s);return ' '.join(s.split())
lines=[(a,clean(b)) for a,b in lines]
N=lambda s:' '.join(re.sub(r"[^a-z0-9' ]",' ',s.lower().replace('’',"'").replace('three hundred and forty dollars','340').replace('$340','340')).split())
print(len(lines),'script lines')
for part,f in (('1','tools/part1r_shots.json'),('2','tools/part2r_shots.json')):
  for p in json.load(open(f))['lines']:
    w=N(p['text'])
    best=max(lines,key=lambda l:max(difflib.SequenceMatcher(None,N(l[1]),w).ratio(),1.0 if w and w in N(l[1]) else 0))
    if w!=N(best[1]):
      print(f"{part}:{p['id']} {p['spk']} OURS:   {p['text']}\n      SCRIPT {best[0]}: {best[1]}")
