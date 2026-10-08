import json
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field. Every person is an original fictional character who must not resemble any real actor or celebrity. No readable text, no logos."
GC="the beautiful curvy young Black woman with long box braids worn down, dark brown eyes and a small gold cross necklace, in a soft lavender T-shirt and light-wash jeans"
EC="the very handsome WHITE man, 34, with light skin, very dark brown short hair and a short full dark beard, in a light blue button-down shirt with the sleeves rolled up and dark chinos"
MR="Mama Ruth, a warm 52-year-old Black woman with short natural graying curly hair and tortoiseshell glasses, in a floral blouse and a cream cardigan"
SAM="Sam, a 10-year-old Black boy with short curly hair, in a navy blue number 22 football jersey and jeans"
GG="the beautiful curvy young Black woman with long box braids swept over one shoulder, dark brown eyes and a small gold cross necklace, in an elegant emerald-green dress with a modest neckline"
EN="the very handsome WHITE man, 34, with light skin, very dark brown short hair and a short full dark beard, in a charcoal suit with a white open-collar shirt"
GB="the beautiful young Black bride with her box braids in an elegant updo with small white flowers, a small gold cross necklace, in a white wedding gown with lace sleeves and a modest neckline"
ET="the very handsome WHITE groom, 34, with very dark brown short hair and a short full dark beard, in a black tuxedo with a black bow tie"
HW="the elegant 60-year-old Black woman Mrs. Hayes with silver hair in a neat bun and pearls, in an elegant lavender dress"
HJ="the heavy-set 62-year-old Black lawyer with a round full face, a short neat salt-and-pepper mustache, tortoiseshell glasses and a burgundy bow tie, in a navy suit"
DN="the pretty Latina woman, about 38, with a dark ponytail and a warm face, in a coral dress"
RY="the Latino man, about 35, with short black hair, in a dark gray suit"
R=dict(GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',G8='620fa36b-52c5-419a-ba93-50b4d9431fc0',GGR='8acbb01c-2eb0-4566-a911-1bf987d6e215',GBR='29fb2456-2395-4a78-b262-24dfc597814b',
 E6='e5fff3d9-60fe-4ef7-9e92-58b8aaafec42',E8='62f761f1-c1a4-422f-9550-bf59d87965a4',ETX='b680952e-0b27-4645-9afb-ccfafc24447c',
 MR='78b978ae-a3e3-4aee-957b-33ccf88aa5d7',SAM='7f4a3e65-b525-43d5-890c-880817be583d',H='a06cf4f3-5de6-4941-b406-0aed67147f7e',H5='971f8a3f-3fcb-4776-b903-ff2cbc58f240',
 HJ='7d7b513f-a9ea-4ddc-8cf8-4c7ae77cc5bf',DN='5ca5c94d-b88b-4e9d-bd10-20e744935c07',RY='84e70d95-f0b7-43bd-9376-84ebb5d0fbb7',
 AP='547cc763-25e8-4f82-9936-3ead4ac5b666',AP6='6f981b0d-2c17-4b98-8e8b-6529bd57690c',PORCH='d5ec9247-02a1-45c1-b373-cf34fb7bcefc',DW='7dd3b00d-aa14-4991-8b26-cf0b1b2627d8')
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
APD=" in Grace's small cozy apartment in daylight (worn floral sofa, small wooden kitchen table with a laptop, family photos on the wall, peeling paint, front door)"
GBK="the young Black woman with long box braids in a lavender T-shirt"
EBK="the white man with very dark brown hair in a light blue shirt"
# 76 apartment
s(1,3,['AP6','G8'],f"Close-up of {GC}{APD}, seated at the kitchen table reading an email on a silver laptop, her hand rising to her mouth, eyes widening."+ONE,
  "She reads the screen, freezes, and her eyes go wide with disbelief."+SIL,card="SIX WEEKS LATER",master='A1')
s(2,5,['@A1','G8'],f"Medium shot of {GC}{APD}, jumping up from the kitchen table, overjoyed, shouting toward the next room, facing the camera."+ONE,
  "The young woman jumps up and shouts joyfully: \"Mama! Sam! I passed! I'm a licensed physical therapist!\""+TALK1,spk='G',raw=True)
s(3,4,['@A1','MR','SAM'],f"Medium wide shot{APD}: {MR} and {SAM} rush in and pile onto {GC} in a big joyful three-way hug, laughing. Exactly THREE people.",
  "The mother and the boy rush in and wrap the young woman in a big laughing hug.",sound='on',raw=True,spk='X1')
s(4,3,['@A1','E8'],f"Medium shot of {EC}{APD}, leaning in the open front doorway holding a bouquet of sunflowers, grinning warmly."+ONE,
  "The man in the doorway grins, holding the sunflowers, watching them."+SIL,master='A2')
s(5,3,['@A2'],f"Medium close-up of {EC}{APD}, in the doorway holding sunflowers, proud smile, facing the camera."+OTS(GBK,'left'),
  "The man smiles and says warmly: \"I'm proud of you.\""+TALK,spk='E',master='A3')
s(6,3,['@A1','G8'],f"Medium close-up of {GC}{APD}, standing, surprised and delighted, facing the camera."+OTS(EBK+", in the doorway",'right'),
  "The young woman asks, surprised: \"You knew?\""+TALK,spk='G',master='A4')
s(7,8,['@A3'],f"Medium close-up of {EC}{APD}, in the doorway with the sunflowers, playful, facing the camera."+OTS(GBK,'left'),
  "The man says with a straight face: \"Harold has friends at the licensing board.\" He pauses one second, then grins and says: \"Kidding. I just refreshed the website forty times.\""+TALK,spk='E')
s(8,9,['@A1','SAM'],f"Medium shot of {SAM}{APD}, bursting in excitedly waving a sheet of paper, facing the camera."+ONE,
  "The boy waves the paper and says excitedly: \"Gracie! Gracie! The hospital called. Somebody paid my whole bill. And there's a fund for my inhalers. Until I'm eighteen!\""+TALK1,spk='X2',raw=True)
s(9,3,['@A4'],f"Close-up of {GC}{APD}, slowly turning her head toward someone, realization dawning, eyes narrowing with a smile."+ONE,
  "The young woman slowly turns her head, realization dawning on her face."+SIL)
s(10,4,['@A3'],f"Medium close-up of {EC}{APD}, in the doorway, shrugging innocently and looking up at the ceiling, facing the camera."+OTS(GBK,'left'),
  "The man shrugs, looks up at the ceiling and says innocently: \"Mrs. Hayes might have mentioned something.\""+TALK,spk='E')
s(11,3,['@A4'],f"Close-up of {GC}{APD}, eyes filling with tears, moved, facing the camera."+OTS(EBK,'right'),
  "Her eyes fill with tears and she says softly: \"Ethan.\" Then she is silent."+TALK,spk='G')
s(12,7,['@A3'],f"Medium close-up of {EC}{APD}, tender and sincere, facing the camera."+OTS(GBK,'left'),
  "The man says gently: \"You held my hand on a garden floor, Grace. Let somebody hold yours for once.\""+TALK,spk='E')
# 77 porch
PD=" on the white-columned porch of a Southern mansion at night, dozens of candles, warm string lights, a small table for two with a white tablecloth"
GBG="the young Black woman with box braids in an emerald-green dress"
EBN="the white man with very dark brown hair in a charcoal suit"
s(13,5,['PORCH','E8','GGR'],f"Wide shot{PD}: {EN} stands by the table for two, without a cane, as {GG} steps onto the porch, delighted by the candles. Exactly TWO people.",
  "The young woman steps onto the candlelit porch, taking in the lights; the man waits by the table, smiling."+SIL,card="ONE MONTH LATER",master='B1')
s(14,3,['@B1'],f"Medium shot{PD}: {EN} handing {GG} a small gift wrapped in brown paper and tied with string. Exactly TWO people.",
  "He hands her the small brown-paper gift; she takes it, curious."+SIL)
s(15,3,['@B1','GGR'],f"Medium close-up of {GG}{PD}, holding a small brown-paper gift, curious smile, facing the camera."+OTS(EBN,'right'),
  "The young woman asks with a curious smile: \"What's this?\""+TALK,spk='G',master='B2')
s(16,9,['@B1','E8'],f"Medium close-up of {EN}{PD}, warm and a little nervous, facing the camera."+OTS(GBG,'left'),
  "The man says softly: \"My mother's gardening gloves. Harold kept something in his safe for ten years, and told me to give it to the woman I wanted to marry.\""+TALK,spk='E',master='B3')
s(17,4,['@B1'],f"Close-up{PD}: a woman's hand sliding into an old worn tan leather gardening glove; a small gold ring and a folded yellowed note fall out of the glove into her open palm. Only hands visible, no faces.",
  "Her hand slides into the glove; a gold ring and a folded yellowed note drop out into her palm."+SIL)
s(18,12,['@B2'],f"Medium close-up of {GG}{PD}, holding an unfolded yellowed note in trembling hands, reading it, tears in her eyes, facing the camera."+OTS(EBN,'right'),
  "Reading the note aloud, her voice shaking with emotion, the young woman says: \"Ethan. If you're reading this, Harold says you finally found a woman who loves you and not your money. Took you long enough. Marry her. Love, Mom.\""+TALK,spk='G')
s(19,3,['@B2'],f"Close-up of {GG}{PD}, looking up from the note, tears on her cheeks."+ONE,
  "She slowly lowers the note and looks up."+SIL)
s(20,4,['@B1'],f"Medium wide shot{PD}: {EN} slowly getting down on one knee on the porch floor without a cane, in front of {GG}, who covers her mouth. Exactly TWO people.",
  "The man slowly and steadily lowers himself onto one knee; she covers her mouth with her hand."+SIL)
s(21,12,['@B3'],f"Medium close-up of {EN}{PD}, down on one knee, looking up at her, holding up a small gold ring, emotional, facing the camera."+OTS(GBG+", standing",'left'),
  "Kneeling, the man says with emotion: \"When I had everything, I thought I knew what love looked like. Then I lost everything, and you stayed. Grace Miller, will you stay for good?\""+TALK,spk='E')
s(22,4,['@B2'],f"Medium close-up of {GG}{PD}, crying and laughing at the same time, facing the camera."+OTS(EBN+", kneeling",'right'),
  "Crying and laughing, the young woman says: \"Ethan Caldwell. Yes. Yes!\""+TALK,spk='G')
s(23,3,['@B1'],f"Close-up{PD}: a man's hand sliding a small gold ring onto a woman's ring finger, candlelight. Only hands visible.",
  "He slides the gold ring onto her finger."+SIL)
s(24,5,['@B1'],f"Medium shot{PD}: {EN} standing and {GG} sharing their first gentle kiss under the string lights, her hand on his cheek. Exactly TWO people.",
  "They kiss tenderly under the string lights, then rest their foreheads together, smiling."+SIL)
# 79 wedding
WD=" in the sunny garden of a white-columned Southern mansion on a wedding day (rows of white chairs, a white flower arch, roses, green lawn)"
s(25,6,['DW','GBR','ETX'],f"Wide shot{WD}: under the flower arch stand {ET} and {GB}; beside the bride stands {HW} as maid of honor; at the front {HJ} and {DN}; in the front row {MR} wearing a giant purple church hat and a purple dress; a small boy ring bearer in a tiny black tuxedo; guests in the rows including {RY}.",
  "A gentle breeze moves the flowers; the guests smile; the bride and groom face each other under the arch."+SIL,card="THE WEDDING",master='C1')
s(26,3,['@C1','MR'],f"Close-up of {MR.replace('in a floral blouse and a cream cardigan','in a purple dress and a giant purple church hat')}{WD}, seated in the front row, crying happy tears into a handkerchief."+ONE,
  "She dabs her happy tears with a handkerchief, beaming."+SIL)
s(27,3,['@C1','SAM'],f"Medium close-up of Sam, a 10-year-old Black boy with short curly hair, in a tiny black tuxedo with a bow tie, proudly holding a small white ring pillow{WD}."+ONE,
  "The boy holds up the ring pillow proudly and grins."+SIL)
s(28,3,['@C1','H'],f"Medium close-up of {HW}{WD}, the maid of honor, holding a small bouquet, smiling and wiping a tear."+ONE,
  "She smiles warmly and wipes a single tear."+SIL)
DF=" on a wooden dance floor in the mansion garden at dusk, warm string lights overhead, guests watching from round tables"
s(29,10,['@C1','GBR','ETX'],f"Wide shot{DF}: {ET} and {GB} share their first dance; he spins her gracefully. Exactly TWO people dancing; guests softly blurred around the edges.",
  "The groom spins the bride gracefully and steadily; they dance slowly, smiling; the guests watch."+SIL,vo='GVO',master='D1')
s(30,4,['@D1'],f"Close two-shot{DF}: {ET} and {GB} dancing slowly, foreheads touching, eyes closed, smiling. Exactly TWO people.",
  "They sway slowly with their foreheads together, smiling."+SIL)
# 80
s(31,5,['PORCH'],"Close-up of two white coffee cups side by side on a white wooden porch rail in soft morning light, garden blurred behind; one cup holds black coffee with a single ice cube floating in it. No people.",
  "Morning light; the single ice cube slowly melts in the black coffee; a gentle breeze."+SIL,master='E1')
# Grace voice-over source (audio only, not shown)
s(99,9,['@C1','GBR'],f"Close-up of {GB}{WD}, soft and reflective, facing the camera."+ONE,
  "The bride says softly and warmly: \"My mama told me to be careful with my heart. I was. I gave it to the one man who knew what it cost.\""+TALK1,spk='G')
json.dump(dict(shots=P,refs=R),open('p9.json','w'),indent=1)
print(len(P),sum(p['dur'] for p in P))
