import json
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field."
GD="the beautiful curvy young Black woman with long box braids, dark brown eyes and a small gold cross necklace, in a simple fitted yellow sundress"
GJ=GD+" with a light denim jacket over it"
EW="the very handsome WHITE man, 34, with light skin, short dark-brown hair and a short dark beard, in a gray T-shirt and gray sweatpants"
HJ="the distinguished 65-year-old Black lawyer with a white beard, short white hair, round wire-rimmed glasses and a charcoal three-piece suit"
H="the elegant 60-year-old Black woman Mrs. Hayes with silver hair in a neat bun, a pearl necklace and a long-sleeved black dress"
VR="the stunning blonde woman with red lipstick, in a long ivory silk robe tied closed at the waist (modest, covered neckline), holding a white coffee cup"
B="the handsome BLOND man, 30, with short tousled blond hair, light stubble and a gold watch, in an open-collar white shirt"
RY="the Latino police officer, about 35, with short black hair, in a dark navy police uniform with a silver badge and a navy police cap"
DN="the pretty Latina woman, about 38, with a dark ponytail and a warm face, in navy scrubs"
AT="two male medical transport attendants in light blue uniforms"
R=dict(GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',G5='ae581a1c-6746-400c-bd17-7351b0fa46a3',E='ada7e801-a781-4694-9800-584fbcf5662a',HJ='9d1044f9-8821-4731-86ab-264ff93a4d2e',
 HJ4='bac74591-d9cc-4447-8a59-5588435941b1',H='a06cf4f3-5de6-4941-b406-0aed67147f7e',H5='971f8a3f-3fcb-4776-b903-ff2cbc58f240',V5='ace27837-384e-4fde-96b7-400c71c758f5',
 ROBE='8cf325d1-074a-4949-b292-4932345a1ac3',B3='e59ccf4f-99ae-4084-b9cc-9bd6a543d608',B3W='9bf308d3-8577-40d1-a9d9-88a305a544f3',RY='ac5e0c43-ef4f-4228-920f-0bbcce106433',
 RY5='84e70d95-f0b7-43bd-9376-84ebb5d0fbb7',DN='01a5dd9b-85e4-4b2c-8975-88d5fa0e4e2f',AP='547cc763-25e8-4f82-9936-3ead4ac5b666',AP5='f07b45a2-53cb-4810-9743-520cabb74a46',
 CAR='1327d542-efa3-4256-adbf-f2796a8390e4',DW='7dd3b00d-aa14-4991-8b26-cf0b1b2627d8',FO='2547b718-1527-4247-b3b2-0d7b23f237df',HALL='87e665f3-1bf5-4ed7-988f-e88e42b3818f',
 V56='d55d9b8c-d7b4-4f74-ba19-1bc01f91906d',B55='31d83565-b6ab-4f4a-8cfb-e07d750c3289')
ONE=" Only ONE person in the frame, no duplicates."
def OTS(listener,side='left'):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible). Exactly TWO people: the speaker in sharp focus facing the camera, and the blurred listener from behind.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent."
TALK1=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only this one person speaks."
SIL=" Realistic natural motion, no dialogue."
STAY_W=" The man stays seated in his wheelchair the whole time; he never stands."
P=[]
def s(id,dur,refs,frame,video,spk=None,card=None,master=None,raw=False,vo=None,pre=None):
    P.append(dict(id=id,dur=dur,refs=refs,frame=frame+SUF,video=video,spk=spk,card=card,master=master,lt=None,raw=raw,vo=vo,pre=pre,reuse=None))
APD=" in Grace's small cramped apartment in daylight (worn sofa, small kitchen table, family photos on the wall, peeling paint)"
GB="the young Black woman with long box braids in a yellow sundress"
HB="the older Black man with short white hair and a charcoal suit"
s(1,5,['AP5','GD','HJ4'],f"Medium wide shot{APD}: {GD} has just opened the front door; standing in the doorway is {HJ}, holding a silver laptop under his arm, solemn. Exactly TWO people.",
  "The young woman opens the door wider, surprised; the old lawyer nods politely and steps inside holding the laptop."+SIL,card="THE NEXT DAY",master='A1')
s(2,6,['@A1','HJ4'],f"Medium close-up of {HJ}{APD}, just inside the door, serious and gentle, facing the camera."+OTS(GB,'left'),
  "The lawyer says gently: \"Miss Miller. I'm sorry it took this long. I had to be sure.\""+TALK,spk='HJ')
s(3,4,['@A1'],f"Medium shot{APD}: {HJ} sets a silver laptop on the small kitchen table and presses a key; {GD} leans in beside him, tense. Exactly TWO people.",
  "The lawyer opens the laptop and presses play; the young woman leans in to listen."+SIL)
s(4,3,['@A1'],"Close-up of a silver laptop screen on a kitchen table showing a simple audio player with a moving green waveform and the file name 'storage_room_rec_04.wav'. No people.",
  "The audio waveform on the screen moves as the recording plays."+SIL)
s(5,10,['V56'],"Same as the reference image: the blonde woman in the cream silk blouse in the shabby storage room at night, cold smile, facing the camera, the blond man's back blurred in the foreground.",
  "The blonde woman says coldly and casually: \"Put the bracelet in her bag, call the cops, cry a little, mention the brother. She's gone by the weekend, and nobody's left to tell the judge he's improving.\""+TALK,spk='V',pre='hue=s=0.25,eq=contrast=1.05')
s(6,8,['B55'],"Same as the reference image: the blond man in the white shirt by the door of the shabby storage room at night, facing the camera, the blonde woman's back blurred in the foreground.",
  "The blond man says quietly, annoyed: \"And the pills. If he'd taken the whole bottle at the party like I planned, we wouldn't need any of this.\""+TALK,spk='B',pre='hue=s=0.25,eq=contrast=1.05')
s(7,3,['@A1','GD'],f"Close-up of {GD}{APD}, both hands over her mouth in horror, eyes wide and wet."+ONE,"The young woman slowly covers her mouth with both hands, horrified."+SIL)
s(8,8,['@2'],f"Medium close-up of {HJ}{APD}, seated at the kitchen table beside the laptop, grave, facing the camera."+OTS(GB,'left'),
  "The lawyer says gravely: \"Attempted murder, fraud, a false police report. But here's the problem. They move him to Memphis Thursday morning.\""+TALK,spk='HJ')
s(9,10,['@8'],f"Medium close-up of {HJ}{APD}, seated at the kitchen table, urgent, facing the camera."+OTS(GB,'left'),
  "The lawyer says urgently: \"Once he's in Ridgeview, they control his doctors, his medicine, and his visitors. I've filed for an emergency order, but the judge can't sign it before six a.m.\""+TALK,spk='HJ')
s(10,3,['@A1','GD'],f"Close-up of {GD}{APD}, seated at the kitchen table, jaw set, determined, facing the camera."+OTS(HB,'right'),
  "The young woman says firmly: \"Then we stop that van.\""+TALK,spk='G')
s(11,4,['@8'],f"Medium close-up of {HJ}{APD}, seated, a slow proud smile spreading, facing the camera."+OTS(GB,'left'),
  "The lawyer smiles slowly and says: \"Ethan said you'd say that.\""+TALK,spk='HJ')
FOGST=" on a quiet, wide, tree-lined residential boulevard of big Southern mansions at dawn, thick morning fog, soft blue light"
s(12,5,['CAR'],f"Wide shot{FOGST}: an old silver sedan parked at the curb in the foreground; far down the street in the fog, a plain white medical transport van idles with its headlights on. No people visible.",
  "Fog drifts; the white van idles far down the street with its lights on; the parked silver car stays still."+SIL,card="THURSDAY · 6:30 A.M.",master='B1')
CARI=" inside an old silver sedan at dawn, fog outside the windshield, soft blue light"
s(13,6,['CAR','DN'],f"Medium close-up of {DN}{CARI}, in the driver's seat, hands on the steering wheel, looking toward the passenger, facing the camera."+OTS(GB+" and a denim jacket, in the passenger seat",'left'),
  "The woman at the wheel says warmly: \"When you called, I didn't even ask. I just said, what time.\""+TALK,spk='DN',master='B2')
s(14,5,['@B2','GD'],f"Medium close-up of {GJ}{CARI}, in the passenger seat, looking up from her phone, facing the camera."+OTS("the Latina woman with a dark ponytail in navy scrubs, in the driver's seat",'right'),
  "The young woman checks her phone and says: \"Judge signed at six fifteen. Harold's ten minutes out.\""+TALK,spk='G')
s(15,3,['@13'],f"Medium close-up of {DN}{CARI}, eyes on the road ahead, worried, facing the camera."+OTS(GB+" and a denim jacket, in the passenger seat",'left'),
  "The woman at the wheel says tensely: \"That van isn't waiting ten minutes.\""+TALK,spk='DN')
DWD=" on the long brick driveway of the white-columned Southern mansion at dawn, light fog, soft blue morning light"
s(16,6,['DW','ROBE','V5'],f"Wide shot{DWD}: a plain white medical transport van has stopped near the front steps; {AT} lift a folded stretcher out of the back; at the open front door stands {VR}. Exactly THREE people.",
  "The two attendants pull the stretcher from the van; the blonde woman watches from the doorway sipping her coffee."+SIL,card="6:41 A.M.",master='C1')
s(17,4,['@C1','GD'],f"Wide shot{DWD}, from the house looking toward the gate: {GJ} running fast up the driveway toward the house, determined."+ONE,
  "The young woman runs up the driveway toward the house."+SIL)
s(18,6,['@C1','ROBE','V5'],f"Medium shot of {VR} standing at the open front door of the mansion at dawn, furious, facing the camera."+OTS(GB+" and a denim jacket, at the foot of the steps",'left'),
  "The blonde woman in the robe says angrily: \"Oh, you have GOT to be kidding me. Get off my property or I'm calling the police.\""+TALK,spk='V')
s(19,4,['@C1','GD'],f"Medium close-up of {GJ} at the foot of the mansion steps at dawn, chin up, calm and defiant, facing the camera."+OTS("the blonde woman in a long ivory silk robe",'right'),
  "The young woman says calmly: \"Please do. I'd love them here for this.\""+TALK,spk='G')
s(20,4,['@18'],f"Medium shot of {VR} at the open front door at dawn, turning to the side and pointing into the house, commanding."+ONE,
  "The blonde woman turns aside and says sharply: \"Ignore her. She's a thief. Go get him.\""+TALK1,spk='V')
s(21,4,['@C1','H'],f"Medium shot of {H} stepping into the open front doorway of the mansion and blocking it with her body, arms at her sides, steady, facing the camera."+OTS("one of the male transport attendants in a light blue uniform",'right'),
  "The older woman steps into the doorway and says firmly: \"Nobody goes through this door.\""+TALK,spk='H')
s(22,3,['@18'],f"Medium close-up of {VR} in the front hall at dawn, enraged, shouting, facing the camera."+OTS("the elegant older Black woman with silver hair in a bun and a black dress",'right'),
  "The blonde woman shouts: \"You're FIRED!\""+TALK,spk='V',raw=True)
s(23,4,['@21'],f"Medium close-up of {H} in the doorway, a small unbothered smile, facing the camera."+OTS("the blonde woman in a long ivory silk robe",'left'),
  "The older woman says calmly with a small smile: \"Honey, I quit thirty seconds ago.\""+TALK,spk='H')
FOY=" in the grand white marble foyer of the mansion at dawn (crystal chandelier, curved staircase)"
s(24,8,['FO','GD'],f"Medium shot of {GJ}{FOY}, facing the camera, speaking firmly and clearly."+OTS("a male transport attendant in a light blue uniform",'right'),
  "The young woman says firmly: \"That man is not incompetent. He can talk, he can think, and he does not want to go with you.\""+TALK,spk='G',master='D1')
s(25,3,['@D1','ROBE','V5'],f"Medium close-up of {VR}{FOY}, scornful, facing the camera."+OTS(GB+" and a denim jacket",'left'),
  "The blonde woman snaps scornfully: \"He can't even stand up!\""+TALK,spk='V')
s(26,3,['@24'],f"Medium shot{FOY}: {GJ} turning her head sharply toward a hallway on the right, startled."+ONE,
  "The young woman turns her head sharply toward a sound from the hallway."+SIL)
HAL=" in a long elegant mansion hallway (cream paneled walls, gilt-framed oil paintings, polished wood floor, arched window at the end)"
s(27,5,['HALL','E'],f"Wide shot{HAL}: {EW} STANDING in a doorway, gripping the doorframe with both hands, legs shaking, an empty black wheelchair tipped over on its side behind him."+ONE,
  "The man clings to the doorframe, his legs trembling violently, but he stays standing."+SIL,master='E1')
s(28,8,['@E1','E'],f"Medium close-up of {EW}{HAL}, standing, gripping the doorframe, sweating, fierce, facing the camera."+ONE,
  "The man says slowly and with fierce effort: \"My name... is Ethan... Caldwell. And I'm... not going... anywhere!\""+TALK1,spk='E')
s(29,3,['@D1'],"Slow-motion close-up on the white marble foyer floor: a white coffee cup hitting the floor and shattering, coffee splashing. The hem of a long ivory silk robe and bare feet in the background. No faces.",
  "Slow motion: the coffee cup hits the marble and shatters, coffee splashing outward."+SIL)
s(30,3,['@24'],f"Close-up of {GJ}{FOY}, tears in her eyes, a proud trembling smile."+ONE,"The young woman's eyes fill with tears as a proud smile breaks through."+SIL)
s(31,5,['@C1'],f"Wide shot{DWD}: a black sedan followed by a police cruiser with lights flashing drive up through the fog toward the house. No people visible.",
  "The black sedan and the police cruiser roll up the driveway through the fog and stop."+SIL)
s(32,7,['@C1','HJ4'],f"Medium close-up of {HJ}{DWD}, handing a folded legal document forward, firm, facing the camera."+OTS("the police officer in a dark navy uniform and police cap",'right'),
  "The lawyer hands over the papers and says firmly: \"Emergency protective order. Mr. Caldwell goes to a facility of HIS choosing.\""+TALK,spk='HJ',master='F1')
s(33,5,['@F1'],f"Medium close-up of {HJ}{DWD}, holding up his phone, facing the camera."+OTS("the police officer in a dark navy uniform and police cap",'right'),
  "The lawyer says pointedly: \"And Officer, you'll want to hear a recording about a certain bracelet.\""+TALK,spk='HJ')
s(34,4,['@C1','RY5'],f"Medium close-up of {RY}{DWD}, holding a phone to his ear, listening, his face slowly changing to shock and shame."+ONE,
  "The officer listens to the phone, his expression turning from doubt to shame."+SIL)
s(35,4,['@34'],f"Medium shot of {RY}{DWD}, taking off his police cap and walking toward the camera."+ONE,
  "The officer slowly takes off his cap and walks forward."+SIL)
s(36,4,['@34','GD'],f"Medium close-up of {RY}{DWD}, bareheaded, holding his cap against his chest, humble, facing the camera."+OTS(GB+" and a denim jacket",'left'),
  "The officer says humbly: \"Ma'am... I owe you an apology.\""+TALK,spk='RY')
s(37,3,['@19'],f"Close-up of {GJ}{DWD}, giving a small gracious nod."+ONE,"The young woman gives a small, gracious nod."+SIL)
s(38,5,['@C1','GD','DN','E'],f"Medium shot{DWD}: {GJ} and {DN} help {EW} from his wheelchair into the back seat of an old silver sedan, one on each side supporting him. Exactly THREE people.",
  "The two women support the man under his arms and help him slide into the back seat of the car."+SIL,card="MOMENTS LATER")
CARB=" in the back seat of an old silver sedan, foggy dawn light through the windows"
s(39,6,['CAR','GD','E'],f"Medium shot{CARB}: {GJ} sits beside {EW}; both facing forward, the car moving. Exactly TWO people.",
  "As the car pulls away, the man slowly reaches over and laces his fingers through hers; she looks at him and squeezes his hand."+SIL,master='G1')
s(40,3,['@G1'],"Extreme close-up on a car seat: a man's light-skinned hand slowly lacing its fingers through a young Black woman's hand. Exactly two hands, natural anatomy, five fingers each.",
  "The fingers slowly interlace and hold tight."+SIL)
s(41,5,['@C1','ROBE','V5','B3W'],f"Medium shot of {VR} frozen in the open front doorway of the mansion at dawn, cold fury, and just behind her {B}, pale and frightened. Exactly TWO people.",
  "The blonde woman stares out, frozen; the blond man behind her swallows nervously."+SIL)
s(42,5,['@C1'],f"Wide shot{DWD}, from the house: an old silver sedan driving away down the long brick driveway into the fog toward the gate. No people visible.",
  "The silver sedan drives away down the driveway and disappears into the fog."+SIL)
json.dump(dict(shots=P,refs=R),open('p6.json','w'),indent=1)
print(len(P),sum(p['dur'] for p in P))
