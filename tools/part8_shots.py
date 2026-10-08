import json
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field. Every person is an original fictional character who must not resemble any real actor or celebrity. No readable text, no logos."
ES="the very handsome WHITE man, 34, with light skin, full short dark-brown hair and a short full dark beard, in a tailored navy suit, white shirt and no tie, holding a dark wooden walking cane"
GB="the beautiful curvy young Black woman with long box braids worn down, dark brown eyes and a small gold cross necklace, in a simple knee-length royal-blue dress with short sleeves and a modest neckline"
HJ="the heavy-set 62-year-old Black lawyer with a round full face, a short neat salt-and-pepper mustache and no beard, close-cropped salt-and-pepper hair with a side part, thick tortoiseshell glasses, a navy pinstripe suit, white shirt and burgundy bow tie"
B="the handsome BLOND man, 30, with short tousled blond hair, light stubble and a gold watch, in a navy blazer over an open-collar white shirt"
V="the stunning woman with long light buttery-blonde hair and red lipstick, in a fitted long-sleeved red sheath dress with a modest high neckline and small gold earrings"
BC="the silver-haired white board chairman in his 60s with a lined face, in a charcoal three-piece suit and red tie"
DT="the female police detective, 45, white, with a square jaw, short straight ash-brown hair in a low ponytail, light freckles and a small scar through her left eyebrow, in a navy blazer and white shirt with a gold badge on her belt"
RY="the Latino police officer, about 35, with short black hair, in a dark navy police uniform with a silver badge"
R=dict(E6='e5fff3d9-60fe-4ef7-9e92-58b8aaafec42',GB='1f059989-0208-46dd-a350-e957a60af65b',GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',HJ='7d7b513f-a9ea-4ddc-8cf8-4c7ae77cc5bf',
 B3='e59ccf4f-99ae-4084-b9cc-9bd6a543d608',V5='ace27837-384e-4fde-96b7-400c71c758f5',VG='6977815a-009f-4da0-9799-8a1c8daf4026',BC='7cee2784-1c67-4ee8-9d7b-fdb71398ad79',
 DT='9d7a04cc-bbfd-49a6-ad6e-59077f966591',RY='ac5e0c43-ef4f-4228-920f-0bbcce106433',RY5='84e70d95-f0b7-43bd-9376-84ebb5d0fbb7')
ONE=" Only ONE person in the frame, no duplicates."
def OTS(listener,side='left'):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible). The speaker is in sharp focus facing the camera.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; everyone else stays silent. Each word is said exactly once."
TALK1=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only this one person speaks. Each word is said exactly once."
SIL=" Realistic natural motion, no dialogue."
P=[]
def s(id,dur,refs,frame,video,spk=None,card=None,master=None,raw=False,sound=None,vo=None,trim=None):
    P.append(dict(id=id,dur=dur,refs=refs,frame=frame+SUF,video=video,spk=spk,card=card,master=master,lt=None,raw=raw,vo=vo,pre=None,reuse=None,sound=sound,trim=trim))
LOB=" in the bright modern lobby of a freight company headquarters (glass walls, polished pale stone floor, a long white reception desk, potted plants, no logos or signs)"
EB="the white man with short dark-brown hair in a navy suit"
GBB="the young Black woman with long box braids in a royal-blue dress"
# 70 lobby
s(1,5,['E6','GB','HJ'],f"Wide shot{LOB}: {ES} walks in through the glass doors, slowly but upright, leaning on the cane; beside him walks {GB}; one step behind follows {HJ}, carrying a leather briefcase. In the background several office employees (a young Black woman at the reception desk with a headset, a middle-aged white man with glasses holding a coffee cup, an Asian woman with a tablet) stop and stare. Exactly SIX people.",
  "The three walk slowly across the lobby; the employees in the background stop what they are doing and stare."+SIL,card="MONDAY · 9:55 A.M.",master='A1')
s(2,3,['@A1'],f"Medium close-up{LOB}: a young Black woman, about 25, with short natural curly hair and a phone headset, standing behind the white reception desk, astonished, facing the camera, pointing slightly."+ONE,
  "The receptionist gasps and says excitedly: \"That's Mr. Caldwell!\""+TALK1,spk='X1',raw=True)
s(3,3,['@A1'],f"Medium close-up{LOB}: a middle-aged white office worker with thinning hair and wire glasses, in a light blue shirt and tie, holding a paper coffee cup, amazed, facing the camera."+ONE,
  "The office worker says in amazement: \"He's walking!\""+TALK1,spk='X2',raw=True)
s(4,3,['@A1','GB'],f"Medium close-up of {GB}{LOB}, walking slowly beside him, glancing around, a little nervous, facing the camera."+OTS(EB,'right'),
  "Walking slowly, the young woman says quietly: \"Everyone's watching.\""+TALK,spk='G',master='A2')
s(5,7,['@A1','E6'],f"Medium close-up of {ES}{LOB}, walking slowly with the cane, calm and certain, facing the camera."+OTS(GBB,'left'),
  "Walking slowly, the man says calmly: \"Let them. I already lost everything I was afraid to lose. Except you.\""+TALK,spk='E',master='A3')
# 71 boardroom
BR=" in a modern glass-walled boardroom on a high floor (long dark walnut table, black leather chairs, a city skyline beyond the windows, no logos or signs)"
s(6,5,['B3','V5','BC'],f"Wide shot{BR}: at the head of the table sits {B}; beside him sits {V}; along the table sit {BC}, two Atlas executives (a bald Black man in his 50s in a gray suit, and an East Asian woman in her 40s with a short bob and a black suit) with contracts in front of them, and two more board members (a white woman in her 50s with short gray hair, and a Latino man in his 40s with a mustache). Exactly SEVEN people.",
  "The blond man at the head of the table smiles and slides a contract toward the executives; everyone leans in."+SIL,card="THE BOARDROOM",master='B1')
s(7,4,['@B1','E6','GB','HJ'],f"Wide shot{BR}, from inside the room toward the double doors: the glass double doors swing open and {ES} stands in the doorway, with {GB} at his side and {HJ} behind them. Exactly THREE people.",
  "The double doors open; the man with the cane stands in the doorway and looks into the room."+SIL)
s(8,4,['@B1','B3'],f"Medium close-up of {B}{BR}, seated at the head of the table, his face draining of color, shocked, facing the camera."+OTS(EB+", standing near the doors",'left'),
  "The blond man stammers in shock: \"Ethan. You should be resting.\""+TALK,spk='B',master='B2')
s(9,5,['@7','E6'],f"Medium close-up of {ES}{BR}, standing just inside the doorway, cold and calm, facing the camera."+OTS("the blond man in a navy blazer, seated at the head of the table",'right'),
  "The man with the cane says calmly: \"I've rested enough. I believe you're in my chair.\""+TALK,spk='E',master='B3')
s(10,5,['@B1','E6','B3'],f"Medium wide shot{BR}: {B} slowly standing up from the chair at the head of the table and stepping aside, while {ES} walks to the head of the table. Exactly TWO people in focus; others blurred at the table.",
  "The blond man slowly rises and steps aside; the man with the cane walks to the head of the table and sits down in the chair."+SIL)
# 72
s(11,5,['@B3','E6'],f"Medium close-up of {ES}{BR}, now seated at the head of the table, hands folded, facing the camera."+OTS("the blond man in a navy blazer, seated at the side of the table",'right'),
  "The seated man says evenly: \"I understand decisions have been made without me.\""+TALK,spk='E',master='B4')
s(12,4,['@B2','B3'],f"Medium close-up of {B}{BR}, now seated at the side of the table next to the blonde woman in red, defensive, forced smile, facing the camera."+OTS(EB+", seated at the head of the table",'left'),
  "The blond man says defensively: \"We were protecting the company.\""+TALK,spk='B',master='B5')
s(13,5,['@B4'],f"Medium close-up of {ES}{BR}, seated at the head of the table, cold, facing the camera."+OTS("the blond man in a navy blazer",'right'),
  "The seated man asks coldly: \"From me?\" Then he turns his head to the side and says: \"Play it.\""+TALK,spk='E')
s(14,3,['@B1','HJ'],f"Close-up{BR}: the hand of the lawyer in a navy pinstripe sleeve with a white cuff setting a small black digital voice recorder on the dark walnut table and pressing play; a tiny red light comes on. No faces.",
  "The hand sets down the small recorder and presses the button; the red light turns on."+SIL)
s(15,10,['@B1'],f"Medium wide shot{BR}: the board members and the two executives around the table slowly turning their heads to stare at {B} and {V}, who sit frozen. Exactly SIX people.",
  "One by one, the people around the table turn to stare at the blond man and the blonde woman, who sit frozen. Slow push-in.",vo='V6')
s(16,8,['@B1','B3','V5'],f"Medium shot{BR}: {B} sweating and swallowing, and {V} beside him going pale, both frozen. Exactly TWO people in focus.",
  "The blond man sweats and swallows; the blonde woman beside him stares, frozen, her lips parted. Slow push-in.",vo='B6')
# 73
s(17,5,['@B1','V5'],f"Medium close-up of {V}{BR}, seated at the table, panicked, pleading sweetly, facing the camera."+OTS(EB+", seated at the head of the table",'left'),
  "The blonde woman says in a panicked, pleading voice: \"Ethan, baby, that was taken out of context. Bradley forced me.\""+TALK,spk='V',master='B6')
s(18,4,['@B2','B3'],f"Medium close-up of {B}{BR}, turning furiously toward the woman beside him, shouting, facing the camera."+OTS("the blonde woman in a red dress",'right'),
  "The blond man turns on her and shouts angrily: \"I forced you? It was your idea!\""+TALK,spk='B',raw=True)
s(19,9,['@B4'],f"Medium close-up of {ES}{BR}, seated at the head of the table, raising one hand for silence, commanding, facing the camera; the board members are softly blurred in the background."+ONE,
  "The seated man raises a hand and says firmly: \"Enough.\" Then he turns to the table and says: \"I move to cancel the Atlas sale and remove Bradley Caldwell as acting CEO.\""+TALK1,spk='E')
s(20,3,['@B1','BC'],f"Medium close-up of {BC}{BR}, seated at the table, raising his hand, firm, facing the camera."+ONE,
  "The silver-haired man raises his hand and says firmly: \"Seconded.\""+TALK1,spk='X3',raw=True)
s(21,3,['@B4'],f"Medium close-up of {ES}{BR}, seated at the head of the table, looking around the table, facing the camera."+ONE,
  "The seated man looks around the table and asks: \"All in favor?\" Then he waits in silence."+TALK1,spk='E')
s(22,4,['@15'],f"Wide shot{BR}, same seating as the reference image (the man with dark-brown hair and beard in a navy suit at the head of the table): around the long table, the board members and the two executives all raise their hands; only {B} and {V}, seated side by side, keep their hands down. No hands are raised by anyone else.",
  "One after another, every hand around the table goes up; the blond man and the blonde woman do not move."+SIL)
# 74
s(23,4,['@7','DT','RY5'],f"Wide shot{BR}, toward the double doors: the doors open and in walk {RY}, {DT}, and a second detective (a tall Black man, 40s, with a shaved head in a gray suit). Exactly THREE people.",
  "The doors open and the officer and the two detectives walk briskly into the boardroom."+SIL)
s(24,9,['@23','DT'],f"Medium close-up of {DT}{BR}, standing beside the table holding up her badge, stern, facing the camera."+OTS("the blond man in a navy blazer",'left'),
  "The detective says firmly and clearly: \"Bradley Caldwell, Vanessa Pierce, you're under arrest for attempted murder, fraud, and filing a false police report.\""+TALK,spk='DT',raw=True)
s(25,3,['@B1','B3'],f"Close-up{BR}: metal handcuffs closing around the wrists of a man wearing a navy blazer and a gold watch, held by hands in a dark navy police uniform sleeve. No faces.",
  "The handcuffs click shut around the wrists."+SIL)
s(26,4,['@B6','V5'],f"Medium close-up of {V}{BR}, standing, her hands cuffed in front of her, being led out, turning back, tearful, facing the camera."+OTS(EB+", seated at the head of the table",'left'),
  "The blonde woman turns back and says tearfully: \"Ethan, please. I loved you.\""+TALK,spk='V')
s(27,7,['@B4'],f"Medium close-up of {ES}{BR}, seated at the head of the table, quiet and final, facing the camera."+OTS("the blonde woman in a red dress, standing",'right'),
  "The seated man says quietly and firmly: \"No. You loved my life. She loved me when I didn't have one.\""+TALK,spk='E')
s(28,3,['@B6'],f"Close-up of {V}{BR}, standing, glancing to the side toward someone, bitter and humiliated."+ONE,
  "The blonde woman turns her eyes to the side and stares coldly."+SIL)
s(29,3,['@A2','GB'],f"Close-up of {GB}{BR}, standing near the wall, chin up, calmly meeting someone's gaze, unafraid."+ONE,
  "The young woman holds the gaze steadily, chin up, unafraid."+SIL)
# 75
s(30,5,['@A1'],f"Wide shot{LOB}: {ES} walks out across the lobby with the cane; {GB} takes his free arm; {HJ} follows; around them office employees stand and applaud. Exactly SIX people.",
  "The employees stand and applaud as the man with the cane walks across the lobby; the young woman takes his arm.",sound='on',spk='X4',raw=True,card="MOMENTS LATER")
s(31,3,['@A2'],f"Medium close-up of {GB}{LOB}, walking arm in arm with him, smiling, facing the camera."+OTS(EB,'right'),
  "Walking arm in arm, the young woman smiles and asks: \"How did it go?\""+TALK,spk='G')
s(32,4,['@A3'],f"Medium close-up of {ES}{LOB}, walking arm in arm with her, a warm small smile, facing the camera."+OTS(GBB,'left'),
  "Walking arm in arm, the man smiles and says: \"I think you already know.\""+TALK,spk='E')
json.dump(dict(shots=P,refs=R),open('p8.json','w'),indent=1)
print(len(P),sum(p['dur'] for p in P))
