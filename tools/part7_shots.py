import json
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field. Every person is an original fictional character who must not resemble any real actor or celebrity. No text, no logos."
GR="the beautiful curvy young Black woman with long box braids worn down, dark brown eyes and a small gold cross necklace, in a plain white T-shirt, light-wash jeans and white sneakers"
GN=GR+" with a soft mustard-yellow cardigan over it"
EW="the very handsome WHITE man, 34, with light skin, short dark-brown hair and a short dark beard, in a gray T-shirt and gray sweatpants"
EN="the very handsome WHITE man, 34, with light skin, short dark-brown hair and a short dark beard, in a gray T-shirt, gray sweatpants and an open navy zip-up hoodie"
DN="the pretty Latina woman, about 38, with a dark ponytail and a warm face, in navy scrubs with a small blank white ID badge (no writing)"
HJ="the heavy-set 62-year-old Black lawyer with a round full face, a short neat salt-and-pepper mustache and no beard, close-cropped salt-and-pepper hair with a side part, thick tortoiseshell glasses, a navy pinstripe suit, white shirt and burgundy bow tie"
R=dict(GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',G6='63cc6fd8-ce19-45b2-ac13-9cff27ba3c5b',E='ada7e801-a781-4694-9800-584fbcf5662a',E6='e5fff3d9-60fe-4ef7-9e92-58b8aaafec42',
 DN='01a5dd9b-85e4-4b2c-8975-88d5fa0e4e2f',DN6='0eb51cdd-470f-4d14-9a31-7c316213bd12',HJ='7d7b513f-a9ea-4ddc-8cf8-4c7ae77cc5bf',HJ6='aeb51b7f-d406-4ebf-96a5-a6873ce2aea0')
ONE=" Only ONE person in the frame, no duplicates."
def OTS(listener,side='left'):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible). Exactly TWO people: the speaker in sharp focus facing the camera, and the blurred listener from behind.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent. Each word is said exactly once."
TALK1=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only this one person speaks. Each word is said exactly once."
SIL=" Realistic natural motion, no dialogue."
P=[]
def s(id,dur,refs,frame,video,spk=None,card=None,master=None,raw=False,sound=None,trim=None):
    P.append(dict(id=id,dur=dur,refs=refs,frame=frame+SUF,video=video,spk=spk,card=card,master=master,lt=None,raw=raw,vo=None,pre=None,reuse=None,sound=sound,trim=trim))
GYM=" in a bright modern rehabilitation gym in daylight (large windows, pale wood floor, exercise mats, long metal parallel bars)"
GB="the young Black woman with long box braids in a white T-shirt"
EB="the white man with short dark-brown hair in a gray T-shirt"
# 66 montage
s(1,5,['E','GD','DN'],f"Wide shot{GYM}: {EW} walks slowly between the long metal parallel bars, gripping them; {DN} walks beside him coaching with one hand near his back; on a bench in the background {GR} sits holding a steel thermos, smiling. Exactly THREE people.",
  "The man takes slow careful steps between the parallel bars; the therapist walks beside him; the young woman on the bench watches, smiling."+SIL,card="THREE WEEKS LATER · CHATTANOOGA",master='A1')
s(2,3,['@A1'],f"Low close-up{GYM}: a man's bare feet in gray sweatpants taking one slow step forward on the pale wood floor between the two metal parallel bars, his hands gripping the bars above. No faces.",
  "One foot slides forward and takes a step, then the other."+SIL)
# 67
s(3,5,['@A1','E'],f"Medium close-up of {EW}{GYM}, between the metal parallel bars, gripping them, gritting his teeth, sweating, facing the camera."+OTS(GB,'left'),
  "Gritting his teeth as he walks, the man says: \"If you tell me one more Titans score, I'm going to fall on purpose.\""+TALK,spk='E',master='A2')
s(4,3,['@A1','GD'],f"Medium close-up of {GR}{GYM}, standing at the end of the parallel bars, a sly smile, facing the camera."+OTS(EB+", between the parallel bars",'right'),
  "The young woman says casually, with a sly smile: \"They won last week.\""+TALK,spk='G',master='A3')
s(5,3,['@A2'],f"Medium close-up of {EW}{GYM}, standing still between the parallel bars, stopping in surprise, eyebrows raised, facing the camera."+OTS(GB,'left'),
  "The man stops walking, surprised, and asks: \"They did?\" Then he waits in silence."+TALK,spk='E')
s(6,5,['@A3'],f"Medium close-up of {GR}{GYM}, standing at the end of the parallel bars, grinning, facing the camera."+OTS(EB+", between the parallel bars",'right'),
  "The young woman grins and says: \"No. But you just walked twelve steps without noticing.\""+TALK,spk='G')
s(7,4,['@A2'],f"Medium shot of {EW}{GYM}, standing between the parallel bars, looking down at his own feet in wonder."+ONE,
  "The man looks down at his feet, then up toward the camera, and bursts out laughing with joy.",spk='E',raw=True,sound='on')
# 68
GDN=" in a quiet rehabilitation center garden at night, warm string lights overhead, a wooden bench, dark hedges"
s(8,4,['E','GD'],f"Wide shot{GDN}: {EN} sits on the wooden bench with a wooden walking cane resting against it; beside him sits {GN}. Both seated side by side, talking quietly. Exactly TWO people.",
  "The two sit side by side on the bench under the string lights; a light breeze moves the hedges."+SIL,card="THAT NIGHT",master='B1')
s(9,8,['@B1','E'],f"Medium close-up of {EN}{GDN}, seated on the bench, turned toward her, tender and serious, facing the camera."+OTS("the young Black woman with long box braids in a mustard-yellow cardigan, seated beside him",'left'),
  "The man says softly: \"That night in the storage room. I think I'm falling in love with you. I don't know which one scares me more.\""+TALK,spk='E',master='B2')
s(10,3,['@B1','GD'],f"Medium close-up of {GN}{GDN}, seated on the bench, frozen in shock, eyes wide, facing the camera."+OTS("the white man with short dark-brown hair in a navy hoodie, seated beside her",'right'),
  "The young woman freezes, then says in a stunned voice: \"You heard that.\""+TALK,spk='G',master='B3')
s(11,7,['@B2'],f"Medium close-up of {EN}{GDN}, seated on the bench, emotional, facing the camera."+OTS("the young Black woman with long box braids in a mustard-yellow cardigan",'left'),
  "The man says gently: \"Grace, I heard every word you said to me for two months. It's the only reason I kept fighting.\""+TALK,spk='E')
s(12,4,['@B3'],f"Medium close-up of {GN}{GDN}, seated on the bench, flustered, looking away, facing the camera."+OTS("the white man with short dark-brown hair in a navy hoodie",'right'),
  "The young woman says quickly, flustered: \"Ethan, I was tired. I didn't mean\" and she breaks off mid-sentence and falls silent."+TALK,spk='G',trim='mean')
s(13,3,['@B2'],f"Medium close-up of {EN}{GDN}, seated on the bench, quiet and direct, facing the camera."+OTS("the young Black woman with long box braids in a mustard-yellow cardigan",'left'),
  "The man asks quietly: \"Did you mean it?\" Then he waits in silence."+TALK,spk='E')
s(14,4,['@B3'],f"Close-up of {GN}{GDN}, seated on the bench, tears in her eyes, facing the camera."+OTS("the white man with short dark-brown hair in a navy hoodie",'right'),
  "The young woman is silent for two seconds, then whispers: \"Yes.\""+TALK,spk='G')
s(15,4,['@B1'],f"Close profile two-shot{GDN}: {EN} and {GN} seated on the bench, leaning toward each other, their faces only a breath apart, eyes half closed; she has just stopped herself. Exactly TWO people.",
  "They lean slowly toward each other; a breath away, she stops and pulls back slightly."+SIL)
s(16,8,['@B3'],f"Medium close-up of {GN}{GDN}, seated on the bench, pulled back, tearful but firm, facing the camera."+OTS("the white man with short dark-brown hair in a navy hoodie",'right'),
  "The young woman says softly but firmly: \"You're still engaged to her. I won't be what she called me in front of that whole street. Not even for you.\""+TALK,spk='G')
s(17,4,['@B2'],f"Medium close-up of {EN}{GDN}, seated on the bench, nodding slowly, resolved, facing the camera."+OTS("the young Black woman with long box braids in a mustard-yellow cardigan",'left'),
  "The man nods slowly and says: \"Then I'd better fix that.\""+TALK,spk='E')
# 69
RM=" in a bright tidy rehabilitation center room in the morning (single bed with white sheets, window with daylight, a wooden walking cane leaning on the bed)"
s(18,8,['E'],f"Medium close-up of {EW}{RM}, sitting on the edge of the bed holding a phone to his ear, determined, facing the camera."+ONE,
  "Holding the phone to his ear, the man says firmly: \"Harold. Call off the engagement. Officially. And find out when the board votes on the Atlas sale.\""+TALK1,spk='E',card="THE NEXT MORNING",master='C1')
s(19,4,['HJ','HJ6'],f"Medium close-up of {HJ} in a small wood-paneled law office with bookshelves, seated at his desk holding a phone to his ear, facing the camera."+ONE,
  "Holding the phone to his ear, the lawyer says: \"Monday, ten a.m. Bradley's presenting.\""+TALK1,spk='HJ')
s(20,3,['@C1'],f"Medium close-up of {EW}{RM}, sitting on the edge of the bed, phone to his ear, a small determined smile, facing the camera."+ONE,
  "The man says with quiet resolve: \"Good. I'll be there.\" Then he lowers the phone."+TALK1,spk='E')
json.dump(dict(shots=P,refs=R),open('p7.json','w'),indent=1)
print(len(P),sum(p['dur'] for p in P))
