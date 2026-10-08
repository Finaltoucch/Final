# For every screenplay part, list screenplay sentences that no shot in that part speaks.
# Spoken text = quoted text in the shot prompts (part3..9 _shots.json) + remade lines (part1r/2r/1fix).
import json,re,sys
sp=open('the-maid-who-stayed-movie-screenplay.md').read()
parts=re.split(r'\n## PART (\d+)',sp)
sec={parts[i]:parts[i+1] for i in range(1,len(parts)-1,2)}
def lines_of(t):
    out=[];cur=None
    for l in t.split('\n'):
        m=re.match(r"\*\*([A-Z][A-Z .'’-]+?)(?::\*\*|\*\*\s*(?:\*\([^)]*\)\*)?\s*:)\s*(.*)",l)
        if m: cur=[m.group(1),m.group(2)];out.append(cur);continue
        if cur and l.strip() and not l.startswith(('*','#','---','|')): cur[1]+=' '+l.strip()
        else: cur=None
    return [(a,' '.join(re.sub(r'\*[^*]*\*','',b).split())) for a,b in out]
N=lambda s:' '.join(re.sub(r"[^a-z0-9' ]",' ',s.lower().replace('’',"'").replace('$340','three hundred and forty dollars')).split())
def spoken(p):
    d=json.load(open(f'tools/part{p}_shots.json'));shots=d['shots'] if isinstance(d,dict) else d
    q=[]
    for s in shots:
        for v in s.values():
            if isinstance(v,str): q+=re.findall(r'"([^"]+)"',v)
    return q
for p in sys.argv[1:]:
    F=' | '.join(N(x) for x in spoken(p))
    print(f'===== PART {p}')
    for who,t in lines_of(sec[p]):
        miss=[s for s in re.split(r'(?<=[.!?…—])\s+',t) if N(s) and N(s) not in F]
        if miss: print(f'  {who}: {t}\n      MISSING: {miss}')
