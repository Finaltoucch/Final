# Parts 3-4 over-the-shoulder pass: every conversation line re-shot from its own approved frame,
# edited so the listener's back is in the foreground and the speaker looks at them, not at the lens.
# usage: python3 p34ots.py   -> p34ots.json (frame edit + video request per line)
import json,re
GRACE="the young Black woman with long box braids in a navy-and-white maid uniform"
ETHAN_WC="the man with short dark-brown hair in a gray T-shirt, seated in a wheelchair"
ETHAN_BED="the man with short dark-brown hair in a gray T-shirt, in the bed"
VAN="the slim blonde woman with long straight light-blonde hair in a cream silk blouse"
HAYES="the elegant older Black woman with silver hair in a neat bun and a black dress"
MAMA="the warm older Black woman with short graying curly hair"
BRAD="the blond man with short tousled blond hair in a white open-collar shirt"
SAM="the 12-year-old boy lying in the bed beside her"
GRACE_BED="the young Black woman with long box braids lying in the bed"
REF=dict(G='27bbdbf4-09e9-4fae-be3b-ac06852635ed',E='ada7e801-a781-4694-9800-584fbcf5662a',V='54de5d14-a5c7-42e3-b87b-d5aa06618ced',
         H='a06cf4f3-5de6-4941-b406-0aed67147f7e',M='78b978ae-a3e3-4aee-957b-33ccf88aa5d7',B='e59ccf4f-99ae-4084-b9cc-9bd6a543d608')
# (part, shot): (listener description, listener ref key)
L={}
def setl(p,ids,desc,ref):
  for i in ids:L[(p,i)]=(desc,ref)
setl(3,[2,4],GRACE,'G');setl(3,[6],VAN,'V');setl(3,[3,9],ETHAN_WC,'E');setl(3,[5,7],ETHAN_WC,'E')
setl(3,[13,15],GRACE,'G');setl(3,[17],HAYES,'H');setl(3,[14],VAN,'V');setl(3,[16],VAN,'V')
setl(3,[19,21,23,25,28,30],GRACE,'G');setl(3,[20,22,24,29,31,32],ETHAN_WC,'E')
setl(3,[38,40,42,44],GRACE,'G');setl(3,[39,41,43],MAMA,'M')
setl(3,[54,56],VAN,'V');setl(3,[55,57],BRAD,'B')
setl(4,[2,4,5,7,8],GRACE,'G');setl(4,[3,6],ETHAN_BED,'E')
setl(4,[12,14,15],GRACE,'G');setl(4,[13],HAYES,'H')
setl(4,[23,25,27,29],ETHAN_WC,'E');setl(4,[24,28],GRACE,'G')
setl(4,[31,33,35,39,41],ETHAN_WC,'E');setl(4,[32,34,37,38,40],GRACE,'G')
setl(4,[44,46],GRACE,'G');setl(4,[48],ETHAN_WC,'E')
setl(4,[49,51],VAN,'V');setl(4,[50,53],ETHAN_WC,'E')
setl(4,[57,59],GRACE_BED,'G');setl(4,[58,60],SAM,None)
# raw voice (keep Kling's own): emotional shouts / laughs / child
RAW={(3,25),(3,32),(4,27),(4,29),(4,57),(4,59)}
FIXTEXT={(4,38):("And don't say for the money. Vanessa cut your pay in half.","And don't say for the money, because Vanessa cut your pay in half.")}
TALK=(" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue."
      " The speaker looks at the person in the foreground, never into the camera. Only the person facing the camera speaks;"
      " the blurred person in the foreground seen from behind stays still and silent. Each word is said exactly once.")
def frames(p):
  rows={}
  for l in open(f'../part{p}-shotlist-and-jobs.md'):
    m=re.match(r'\| (\d+) \| (\S+) \| \d+ \| ([0-9a-f-]{36}) \|',l)
    if m:rows[int(m.group(1))]=m.group(3)
  return rows
out=[]
for p in (3,4):
  FR=frames(p);d=json.load(open(f'part{p}_shots.json'));S=d['shots'] if isinstance(d,dict) else d
  for s in S:
    k=(p,s['id'])
    if k not in L:continue
    desc,ref=L[k];side='left' if s['id']%2 else 'right'
    v=s['video']
    if k in FIXTEXT:v=v.replace(*FIXTEXT[k])
    v=re.sub(r'\s*Realistic facial acting.*$','',v)+TALK
    fp=(f"Edit the first image into an over-the-shoulder shot. Keep the person facing the camera EXACTLY the same (same face, hair, wardrobe, expression),"
        f" and keep the same room, background and lighting. Recompose slightly wider. Add in the {side} foreground, very close to the camera and softly out of focus,"
        f" the back of the head and one shoulder of {desc}, seen only from behind: no face visible, no jewelry visible from behind."
        f" The person facing the camera now looks at the person in the foreground, not into the lens. Exactly two people in frame."
        f" Cinematic film still, 16:9, photorealistic, shallow depth of field. No text, no logos.")
    out.append(dict(part=p,shot=s['id'],spk=s['spk'],dur=s['dur'],raw=k in RAW,frame_src=FR[s['id']],
      frame_refs=[FR[s['id']]]+([REF[ref]] if ref else []),frame_prompt=fp,video=v))
json.dump(out,open('p34ots.json','w'),indent=1)
print(len(out),'lines',sum(o['dur'] for o in out),'s')
