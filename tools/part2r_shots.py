# Part 2 conversation remake: over-the-shoulder shots (speaker sharp, listener blurred from behind).
import json,math
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field. Every person is an original fictional character who must not resemble any real actor or celebrity. No text, no logos."
def OTS(listener,side):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible, no jewelry visible from behind). Exactly TWO people: the speaker in sharp focus facing the camera, and the blurred listener from behind.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent. Each word is said exactly once."
L=dict(PARTY='7be55d14-f2b0-4b7c-b87f-e39ec46177ac',ETUX='b680952e-0b27-4645-9afb-ccfafc24447c',B='e59ccf4f-99ae-4084-b9cc-9bd6a543d608',
 WAIT='a8a54c4a-b8fe-433c-950d-eb086cd6ab37',H='a06cf4f3-5de6-4941-b406-0aed67147f7e',GU='27bbdbf4-09e9-4fae-be3b-ac06852635ed',GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',
 PATDAY='9266e229-d068-4e36-b7bf-f9c3cf93e47d',E29='2f1d3fe4-6dcd-4c55-a78e-c08c6ea69252',EVE='47b37329-42cb-4f36-ae28-2670b5ca256a',ROOM='46491f74-5a09-4954-b489-353d86673049')
F={};P=[]
def fr(k,refs,prompt):F[k]=dict(refs=[L[r] for r in refs],prompt=prompt+SUF)
def S(o,k,who,t,m="says",d=None):
    w=len(t.split());P.append(dict(id=len(P)+1,o=o,frame=k,spk=who,text=t,dur=d or max(3,min(15,math.ceil(w/2.7+1.2))),
      video=f"The person facing the camera {m}: \"{t}\""+TALK))
ETX="the very handsome white man, 34, with short dark-brown hair and a neat short beard, in a black tuxedo with a black bow tie"
BRW="the handsome blond man, 30, with short tousled blond hair in a white dinner jacket and black bow tie"
fr('P1',['PARTY','ETUX','B'],f"Medium close-up of {ETX} at a glamorous night garden party under warm string lights, holding two small pills in his palm and a glass of water, facing the camera, smiling gratefully."+OTS(BRW,'left'))
HAY="the elegant 60-year-old Black woman with silver hair in a neat bun, a pearl necklace and a black dress with a coat"
GUC="the young Black woman with long box braids in a navy maid uniform with a dark coat over her shoulders"
fr('W1',['WAIT','H','GU'],f"Medium close-up of {HAY}, sitting in a hospital waiting room at 3 a.m. under cool fluorescent light, rows of blue chairs, facing the camera, worried."+OTS(GUC+", sitting beside her",'left'))
fr('W2',['WAIT','GU','H'],f"Medium close-up of {GUC}, exhausted, sitting in a hospital waiting room at 3 a.m. under cool fluorescent light, rows of blue chairs, facing the camera."+OTS(HAY+", sitting beside her",'right'))
ETH="the very handsome white man, 34, with short dark-brown hair and a neat short beard, in a light-blue hospital gown, lying propped up in a hospital bed"
PAT="the female doctor with glasses and shoulder-length dark wavy hair in a white coat"
fr('D1',['PATDAY','E29'],f"Same room and same people as the first reference image, reverse angle: medium close-up of {ETH}, in a bright hospital room in daytime with a city skyline window, facing the camera, confused and frightened."+OTS(PAT+", standing beside the bed",'left'))
GDR="the beautiful young Black woman with long box braids and a small gold cross necklace, in a casual yellow sundress, her day off"
fr('V1',['EVE','GD','E29'],f"Medium close-up of {GDR}, standing at the side of a hospital bed in the evening, warm lamp light and city lights in the window, holding a covered soup container, facing the camera, warm and determined."+OTS(ETH,'right'))
fr('V2',['EVE','E29','GD'],f"Medium close-up of {ETH}, in a hospital room in the evening, warm lamp light and city lights in the window, facing the camera, tired and bitter, holding his phone."+OTS("the young Black woman with long box braids in a yellow sundress, standing beside the bed",'left'))
S(7,'P1','E','Thanks, Brad.','smiles and says',3)
S(24,'W1','H',"Where's Miss Pierce?",'asks quietly')
S(25,'W2','G',"She said she'd come in the morning. She was tired.",'answers softly')
S(27,'D1','E','Where... am I?','mumbles, slightly slurred')
S(29,'D1','E',"I'm thirty-four.",'says in disbelief')
S(31,'D1','E',"My legs. Why can't I... Why can't I move my legs?!",'tries to move, panics and shouts',5)
S(33,'D1','E','Doctor. Tell me the truth. Will I walk again?','swallows hard and says')
S(39,'V1','G','Mrs. Hayes sent soup. Real food. The hospital stuff could kill a healthy man.','smiles and says')
S(40,'V2','E',"I'm not hungry.",'says flatly')
S(41,'V1','G',"I didn't ask if you were hungry.",'says firmly with a small smile')
S(43,'V2','E',"You know what's funny? When I had everything, I couldn't get a minute alone. Now nobody picks up.",'looks at his phone and says bitterly')
S(44,'V1','G','I picked up.','says softly')
S(45,'V2','E','You work for me.','says')
S(46,'V1','G',"Not today, sir. Today's my day off.",'smiles warmly and says')
json.dump(dict(frames=F,lines=P),open('part2r_shots.json','w'),indent=1)
print(len(F),'frames',len(P),'lines',sum(p['dur'] for p in P),'s')
