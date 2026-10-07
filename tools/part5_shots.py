import json
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field."
G="the beautiful curvy young Black woman with long box braids, dark brown eyes and a small gold cross necklace, in a modest navy-and-white maid uniform"
GD="the beautiful curvy young Black woman with long box braids, dark brown eyes and a small gold cross necklace, in a simple fitted yellow sundress"
GPJ="the beautiful young Black woman with dark brown eyes, a patterned head wrap over her braids, a loose gray T-shirt and red plaid pajama pants"
EW="the very handsome WHITE man, 34, with light skin, short dark-brown hair and a short dark beard, in a gray T-shirt"
EB=EW+", LYING in a narrow metal hospital-style bed under a gray blanket, head on the pillow (he cannot walk)"
EC=EW+", SEATED IN HIS BLACK WHEELCHAIR (he cannot walk)"
H="the elegant 60-year-old Black woman Mrs. Hayes with silver hair in a neat bun and a pearl necklace"
V="the stunning blonde woman with red lipstick, in an elegant high-neck cream silk blouse buttoned to the collar and tailored dark trousers (modest, covered neckline)"
B="the handsome man, 30, with slick dark hair, designer stubble and a gold watch, in a black silk shirt"
RY="the Latino police officer, about 35, with short black hair, in a dark navy police uniform with a silver badge"
M="the beautiful 52-year-old Black woman with short natural hair and reading glasses"
S="the 11-year-old Black boy with short curly black hair, in a navy Tennessee Titans jersey"
CL="a tired middle-aged white hospital billing clerk with short gray hair, in a burgundy cardigan with an ID lanyard"
AG="a professional middle-aged white woman with a neat brown bob, in a gray blazer, wearing a slim office headset"
R=dict(G='27bbdbf4-09e9-4fae-be3b-ac06852635ed',GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',GPJ='d78e965c-93b4-41ce-837b-915e658e64a0',E='ada7e801-a781-4694-9800-584fbcf5662a',
 H='a06cf4f3-5de6-4941-b406-0aed67147f7e',V='60595ef4-874c-426e-a1b5-a9e854f9aad7',B='8f021d31-5f5f-4c9d-8d87-a2a0cc59dd47',RY='ac5e0c43-ef4f-4228-920f-0bbcce106433',
 M='78b978ae-a3e3-4aee-957b-33ccf88aa5d7',S='7f4a3e65-b525-43d5-890c-880817be583d',
 MB='b5f8e290-9436-4d25-b111-2c86f55f10f7',LA='ffad441f-6279-4b09-89a8-bb04da3b4b65',FO='8527312d-488b-4051-af76-08efe3ac7655',DW='7dd3b00d-aa14-4991-8b26-cf0b1b2627d8',
 AP='547cc763-25e8-4f82-9936-3ead4ac5b666',ER='f326efcf-a4fe-405e-b423-abab98df56af',GRN='b30fb6ea-53f4-4603-8416-3de86dd71177')
ONE=" Only ONE person in the frame, no duplicates."
# Over-the-shoulder: speaker sharp facing camera, listener as soft blurred back-of-head + shoulder in the foreground
def OTS(listener,side='left'):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible). Exactly TWO people: the speaker in sharp focus facing the camera, and the blurred listener from behind.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent."
TALK1=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only this one person speaks."
SIL=" Realistic natural motion, no dialogue."
STAY_B=" The man stays lying in the bed the whole time; he never gets up."
STAY_W=" The man stays seated in his wheelchair the whole time; he never stands."
P=[]
def s(id,dur,refs,frame,video,spk=None,card=None,master=None,raw=False,vo=None,reuse=None):
    P.append(dict(id=id,dur=dur,refs=refs,frame=frame+SUF,video=video,spk=spk,card=card,master=master,lt=None,raw=raw,vo=vo,reuse=reuse))
MBD=" in the luxurious master bedroom in soft morning light (arched windows, cream walls, dark wood)"
LAD=" in the dark-paneled laundry room in morning light (white washer and dryer, shelves of folded white towels, a window)"
s(1,4,['MB','V'],f"Medium close-up of {V}{MBD}, standing at a vanity, unclasping a sparkling diamond tennis bracelet from her wrist, a sly look."+ONE,
  "The woman unclasps the diamond bracelet from her wrist and closes her hand around it, a sly look in her eyes."+SIL,card="THE NEXT MORNING")
s(2,5,['LA','V'],f"Wide shot{LAD}: {V} walks toward an old worn brown leather handbag hanging on a hook by the doorway, glancing back over her shoulder."+ONE,
  "The woman walks to the old brown handbag on the hook, glances over her shoulder, and quietly slips something into it."+SIL,master='A1')
s(3,3,['@A1'],"Extreme close-up in the same laundry room: a woman's manicured hand with red nails dropping a sparkling diamond tennis bracelet into an open, old, worn brown leather handbag hanging on a hook. No faces.",
  "The manicured hand lets the diamond bracelet slide down into the worn handbag and pulls away."+SIL)
s(4,3,['@A1','V'],f"Close-up of {V}{LAD}, a small cold satisfied smile."+ONE,"The woman smiles coldly to herself and walks out of frame."+SIL)
FOY=" in the grand white marble foyer of the mansion (crystal chandelier, curved staircase, round table with flowers, tall dark wood front doors)"
s(5,5,['FO','V'],f"Medium shot of {V}{FOY}, standing in the middle of the foyer, shouting up toward the staircase, holding her bare wrist, furious."+ONE,
  "The woman shouts furiously: \"My bracelet! My Cartier! Forty-two thousand dollars! Someone in this house STOLE it!\""+TALK1,spk='V',raw=True,master='B0')
s(6,5,['FO','V','RY','G'],f"Wide shot{FOY}, morning: {RY} stands in the center taking notes; {V} on the left dabbing her eyes with a tissue, fake-crying; {G} on the right with an old worn brown leather handbag over her shoulder, worried. Through the open front doors, neighbors watch from the distant gate. Exactly THREE people in the foyer.",
  "The officer writes in his notebook while the blonde woman dabs her eyes and the maid stands anxiously holding her handbag strap. Nobody speaks."+SIL,card="20 MINUTES LATER",master='B1')
s(7,8,['@B1','V'],f"Medium close-up of {V}{FOY}, tearful, sorrowful, facing the camera."+OTS("the police officer in a dark navy uniform with short black hair",'right'),
  "The blonde woman says sadly, dabbing her eyes: \"I hate to say it, Officer. Her brother's sick. Medicine is expensive. I think she got desperate.\""+TALK,spk='V')
s(8,4,['@B1','RY'],f"Medium close-up of {RY}{FOY}, polite and serious, facing the camera."+OTS("the young Black woman with long box braids in a navy-and-white maid uniform",'left'),
  "The officer says politely: \"Ma'am, may I check your bag?\""+TALK,spk='RY')
s(9,4,['@B1','G'],f"Medium close-up of {G}{FOY}, chin up, calm and dignified, facing the camera, the old brown handbag on her shoulder."+OTS("the police officer in a dark navy uniform with short black hair",'right'),
  "The maid hands over her bag and says calmly: \"Go ahead. I have nothing to hide.\""+TALK,spk='G')
s(10,5,['@B1'],"Slow-motion close-up on the white marble floor of the foyer: an old worn brown leather handbag being turned upside down by a man's hand in a navy uniform sleeve; keys, a wooden rosary, a small blue asthma inhaler and a sparkling diamond tennis bracelet tumble out onto the marble. No faces.",
  "Slow motion: the bag is upended and the keys, rosary, blue inhaler and the glittering diamond bracelet spill and bounce onto the marble floor."+SIL)
s(11,4,['@B1'],"Low close-up at floor level on white marble: a small blue asthma inhaler rolling slowly away across the polished floor, a sparkling diamond bracelet lying just behind it. No people.",
  "The blue inhaler rolls slowly across the marble and comes to rest near the baseboard while the bracelet glitters behind it."+SIL)
s(12,3,['@9'],f"Close-up of {G}{FOY}, staring down at the floor in shock, color draining from her face."+ONE,"The maid stares down, frozen in shock, her lips parting."+SIL)
s(13,6,['@9'],f"Close-up of {G}{FOY}, panicked, pleading, facing the camera, eyes wet."+OTS("the police officer in a dark navy uniform with short black hair",'right'),
  "The maid pleads desperately: \"No... no, I didn't... Officer, she put that there! I would never...\""+TALK,spk='G')
s(14,5,['@7'],f"Medium close-up of {V}{FOY}, cold, wiping her eyes, facing the camera."+OTS("the police officer in a dark navy uniform with short black hair",'right'),
  "The blonde woman says coldly: \"I won't press charges. I just want her OUT.\""+TALK,spk='V')
s(15,6,['@B1','V'],f"Medium shot of {V}{FOY}, turning toward the open front doors, raising her voice so the neighbors at the far gate can hear, theatrical disgust."+ONE,
  "The blonde woman turns to the open doors and says loudly: \"Everybody knows she's been throwing herself at my fiance. It's disgusting.\""+TALK1,spk='V')
s(16,5,['@B1','E'],f"Wide shot{FOY}: {EC} wheeling himself fast out of a side hallway into the foyer, arms straining on the wheels, jaw clenched."+ONE,
  "The man pushes the wheels of his wheelchair hard with both arms, rolling fast into the foyer."+STAY_W+SIL)
s(17,4,['@16','E'],f"Medium close-up of {EC}{FOY}, furious, straining to speak, facing the camera."+OTS("the stunning blonde woman in a cream silk blouse",'left'),
  "The man in the wheelchair forces the words out slowly, hard and furious: \"She... didn't... do it!\""+STAY_W+TALK,spk='E')
s(18,6,['@7'],f"Medium close-up of {V}{FOY}, sweetly pitying, facing the camera."+OTS("the police officer in a dark navy uniform with short black hair",'right'),
  "The blonde woman says with fake sadness: \"He's confused, Officer. The stroke. He doesn't know what's real anymore.\""+TALK,spk='V')
s(19,4,['@17'],f"Medium close-up of {EC}{FOY}, shouting with all his strength, veins in his neck, facing the camera."+OTS("the stunning blonde woman in a cream silk blouse",'left'),
  "The man in the wheelchair shouts with all his strength: \"I know... EXACTLY... what's real!\""+STAY_W+TALK,spk='E',raw=True)
s(20,3,['@8'],f"Medium close-up of {RY}{FOY}, raising a calming hand, facing the camera."+OTS("the dark-haired man seated in a black wheelchair (the back of his head and the wheelchair push handles)",'left'),
  "The officer raises a hand and says firmly: \"Sir, please calm down.\""+TALK,spk='RY')
s(21,5,['@B1','B'],f"Low-angle medium shot of {B} leaning on the banister halfway down the curved staircase of the marble foyer, smirking down at the people below."+OTS("the young Black woman with long box braids in a navy-and-white maid uniform, looking up",'left'),
  "The man on the stairs smirks and says mockingly: \"Six months, and this is how you repay us. Wow.\""+TALK,spk='B')
DWR=" on the long brick driveway of the white-columned mansion in pouring rain, gray sky"
s(22,6,['DW','GD'],f"Wide shot{DWR}: {GD} walking away down the driveway toward the gate, soaked, carrying one small cardboard box; neighbors under umbrellas whisper at the distant gate."+ONE.replace('ONE person','ONE person in the foreground'),
  "The young woman walks slowly down the driveway in the pouring rain carrying the box, head down."+SIL,card="THAT AFTERNOON",master='C1')
s(23,4,['C1','H'] if False else ['@C1','H'],f"Medium shot of {H}, in a long-sleeved black dress, standing in the open front doorway of the mansion, rain falling in front of her, hand over her mouth, helpless."+ONE,
  "The older woman watches from the doorway, her hand slowly covering her mouth, eyes full of sorrow."+SIL)
s(24,4,['@C1','GD'],f"Medium close-up of {GD}{DWR}, soaked, stopping and turning back to look at the house, rain on her face."+ONE,
  "The young woman stops in the rain and slowly turns around to look back at the house."+SIL)
s(25,5,['@C1','E'],f"Exterior close-up of a small ground-floor window of the mansion in pouring rain, rain streaming down the glass: behind the glass, {EW} kneeling on the floor inside, one hand pressed flat against the window, looking out desperately."+ONE,
  "Rain streams down the window as the man inside keeps his hand pressed flat against the glass, staring out."+SIL)
s(26,4,['@24'],f"Close-up of {GD}{DWR}, tears mixing with rain, pressing her hand to her heart."+ONE,
  "The young woman presses her hand to her heart, crying in the rain, then turns and walks away out of frame."+SIL)
APD=" in a small cramped apartment in daylight (worn sofa, small kitchen table, family photos on the wall)"
s(27,4,['AP','GD'],f"Medium shot of {GD}{APD}, sitting at the small kitchen table holding a phone to her ear, listening, hopeful but tense."+ONE,
  "The young woman listens to the phone, hopeful, then her face slowly falls."+SIL,card="THE NEXT DAY")
s(28,7,[],f"Medium close-up of {AG} sitting at an office desk with a computer, speaking into her headset, uncomfortable, apologetic."+ONE,
  "The woman with the headset says, uncomfortable and apologetic: \"I'm sorry, Miss Miller. Mrs. Pierce has called every agency in Nashville. Nobody will hire you.\""+TALK1,spk='AG')
s(29,4,['@27'],f"Close-up of {GD}{APD}, slowly lowering the phone from her ear, staring at nothing, devastated."+ONE,
  "The young woman slowly lowers the phone, staring blankly, her eyes filling with tears."+SIL)
APN=" in a small cramped apartment bedroom at night, dim streetlight through thin curtains"
s(30,5,['AP','GPJ','S'],f"Wide shot{APN}: {S} sitting up in the double bed clutching his chest, struggling to breathe, mouth open; {GPJ} bolting upright beside him, terrified. Exactly TWO people.",
  "The boy sits up gasping for air and clutching his chest; the young woman jolts awake and grabs his shoulders."+SIL,card="2 A.M.",master='D1')
s(31,4,['@D1','S'],f"Close-up of {S}{APN}, sitting up in bed, gasping for air, lips grayish, terrified, facing the camera."+OTS("the young woman in a patterned head wrap",'left'),
  "The boy gasps, barely able to speak: \"Gracie... can't... breathe...\""+TALK,spk='S',raw=True)
s(32,3,['@D1','GPJ'],f"Close-up of {GPJ}{APN}, panicking, facing the camera."+OTS("the 11-year-old boy with short curly black hair in a navy jersey",'right'),
  "The young woman shouts in panic: \"Inhaler! Where's your inhaler?\""+TALK,spk='G',raw=True)
s(33,4,['@D1'],"Top-down close-up on a rumpled bed at night: a woman's hands dumping an old brown handbag onto the sheets; keys, a wooden rosary and a wallet fall out. No inhaler. No faces.",
  "The hands shake the bag upside down; keys, rosary and wallet tumble onto the sheet, the hands search frantically through them."+SIL)
s(34,3,[],"",'',reuse=11)
s(35,3,['@32'],f"Close-up of {GPJ}{APN}, screaming toward the bedroom door, desperate."+ONE,
  "The young woman screams toward the door: \"MAMA! Call 911!\""+TALK1,spk='G',raw=True)
s(36,3,['@D1','M'],f"Medium shot of {M}, in a floral robe, rushing into the bedroom doorway at night with a phone in her hand, frightened."+ONE,
  "The older woman rushes into the doorway, already dialing the phone with shaking hands."+SIL)
s(37,8,['@D1','GPJ'],f"Close-up of {GPJ}{APN}, holding the boy's face in both hands, forcing calm into her voice, facing the camera."+OTS("the 11-year-old boy with short curly black hair",'right'),
  "The young woman says slowly and steadily: \"Look at me. Look at me, baby. Breathe with me. In... two, three. Out... two, three.\""+TALK,spk='G')
s(38,5,['@37'],f"Close-up of {GPJ}{APN}, tears on her face but steady, facing the camera."+OTS("the 11-year-old boy with short curly black hair",'right'),
  "The young woman says firmly through tears: \"You stay with me. You hear me? You stay with me.\""+TALK,spk='G')
ERN=" in a hospital emergency room cubicle at night (curtain, monitors, cool fluorescent light)"
s(39,5,['ER','S','GPJ'],f"Wide shot{ERN}: {S} asleep on the hospital bed with a clear oxygen mask over his face; {GPJ} slumped exhausted in a blue plastic chair beside the bed. Exactly TWO people.",
  "The boy sleeps peacefully with the oxygen mask fogging softly; the young woman sits slumped in the chair, exhausted."+SIL,card="THE ER",master='E1')
s(40,6,['@E1'],f"Medium close-up of {CL}{ERN}, standing, holding out a clipboard, flat and tired, facing the camera."+OTS("the young woman in a patterned head wrap, seated",'left'),
  "The clerk says flatly, holding out the clipboard: \"Emergency visit, nebulizer, overnight observation. Payment or insurance?\""+TALK,spk='CL')
s(41,3,['@E1'],"Close-up of a phone screen in a woman's hand in dim light showing a simple banking app with the balance '$612.40' in large numbers. No faces.",
  "The thumb holds still on the screen showing the balance."+SIL)
s(42,4,['@E1','GPJ'],f"Close-up of {GPJ}{ERN}, closing her eyes, barely holding together, facing the camera."+OTS("the hospital clerk with short gray hair in a burgundy cardigan",'right'),
  "The young woman whispers, barely audible: \"I'll figure it out.\""+TALK,spk='G')
s(43,4,['@E1','H'],f"Medium shot of {H}, in a beige raincoat over her black dress, standing in the ER cubicle opening at night, holding a small blue asthma inhaler."+ONE,
  "The older woman stands in the opening, holding up the small blue inhaler."+SIL)
s(44,9,['@43'],f"Medium close-up of {H}, in a beige raincoat over her black dress,{ERN}, gentle, holding the blue inhaler, facing the camera."+OTS("the young woman in a patterned head wrap, seated",'left'),
  "The older woman says gently: \"You left this on Miss Pierce's floor. I picked it up when nobody was looking. Your mother told me where to find you.\""+TALK,spk='H')
s(45,5,['@E1','H','GPJ'],f"Medium shot{ERN}: {H}, in a beige raincoat, sitting beside {GPJ} and holding her tightly as she breaks down crying on her shoulder. Exactly TWO people.",
  "The young woman breaks down sobbing; the older woman holds her close and strokes her back."+SIL)
s(46,8,['@44'],f"Close-up of {H}, in a beige raincoat,{ERN}, seated, eyes glistening, facing the camera."+OTS("the young woman in a patterned head wrap leaning against her",'right'),
  "The older woman says softly: \"Thirty years I've watched that family. I have never seen anybody love that boy upstairs the way you do.\""+TALK,spk='H')
s(47,5,['@46'],f"Close-up of {H}, in a beige raincoat,{ERN}, seated, bitter sorrow, facing the camera."+OTS("the young woman in a patterned head wrap leaning against her",'right'),
  "The older woman says quietly: \"And I have never seen anybody get paid back so cruelly for it.\""+TALK,spk='H')
s(48,5,['@E1','GPJ'],f"Close-up of {GPJ}{ERN}, seated, crying, facing the camera."+OTS("the elegant older Black woman with silver hair in a bun and a beige raincoat",'left'),
  "The young woman says through tears: \"He's alone with them, Mrs. Hayes. With those pills.\""+TALK,spk='G')
s(49,7,['@46'],f"Close-up of {H}, in a beige raincoat,{ERN}, seated, firm and reassuring, facing the camera."+OTS("the young woman in a patterned head wrap",'right'),
  "The older woman says firmly: \"Not for long. Mr. Jennings is coming to see you tomorrow. Get some sleep, child.\""+TALK,spk='H')
NIGHT_GR=" in the same shabby storage room at night (peeling cream walls, stacked cardboard boxes labeled XMAS DECOR, a small lamp glowing dimly)"
s(50,5,['GRN','V','E'],f"Wide shot{NIGHT_GR}: {V} stands over {EB}, holding a small white paper pill cup and a glass of water. Exactly TWO people.",
  "The blonde woman holds out the pill cup and the glass of water to the man in the bed."+STAY_B+SIL,card="THE MANSION · THAT NIGHT",master='F1')
s(51,3,['@F1','V'],f"Close-up of {V}{NIGHT_GR}, sweet fake smile, holding out a paper pill cup, facing the camera."+OTS("the dark-haired man lying in the bed",'left'),
  "The blonde woman says sweetly: \"Take your medicine, babe.\""+TALK,spk='V')
s(52,5,['@F1','E'],f"Close-up of {EB}{NIGHT_GR}, looking at the pills in the paper cup, then up at the woman, expressionless."+ONE,
  "The man looks at the pills, then at her, tips them into his mouth and sips water from the glass."+STAY_B+SIL)
s(53,9,['@52'],f"Close-up of {EB}{NIGHT_GR}, alone, turning his head, spitting pills into his palm, then pushing them deep down between the mattress and the bed frame."+ONE,
  "The man, alone now, spits the pills into his palm and quietly pushes them deep into the mattress edge. His lips do not move afterwards."+STAY_B+SIL,vo=153)
s(153,9,['@52'],f"Close-up of {EB}{NIGHT_GR}, alone, eyes on the door, quiet."+ONE,
  "The man lying in bed says softly to himself: \"Grace taught me that. Hold the pills under the tongue. Count to ten.\""+STAY_B+TALK1,spk='E')
s(54,4,['@F1','E'],f"Close-up of {EB}{NIGHT_GR}, eyes closed, pretending to sleep."+ONE,"The man lies still with his eyes closed, breathing slowly, pretending to sleep."+STAY_B+SIL)
s(55,9,['GRN','B'],f"Medium close-up of {B}{NIGHT_GR}, standing by the door, speaking low, facing the camera."+OTS("the stunning blonde woman with long hair in a cream silk blouse",'left'),
  "The man by the door says quietly: \"The transfer to Ridgeview is set for Thursday, seven a.m. The hearing's Friday. By Monday, Atlas wires the money.\""+TALK,spk='B',master='G1')
s(56,5,['@G1','V'],f"Medium close-up of {V}{NIGHT_GR}, standing by the door, cold smile, facing the camera."+OTS("the man with slick dark hair in a black silk shirt",'right'),
  "The blonde woman says with a cold smile: \"And by Christmas, nobody will remember Ethan Caldwell existed.\""+TALK,spk='V')
s(57,4,['@54'],f"Close-up of {EB}{NIGHT_GR}, eyes opening slowly in the dark, staring at the ceiling, determined."+ONE,
  "The man slowly opens his eyes in the dark, staring upward, jaw tightening."+STAY_B+SIL)
s(58,6,['@F1'],"Slow push-in in the dark storage room at night between stacked cardboard boxes labeled XMAS DECOR: a small black digital voice recorder hidden in a gap between the boxes, its tiny red recording light glowing. No people.",
  "Slow push-in toward the hidden recorder as its tiny red light keeps glowing in the dark."+SIL)
json.dump(dict(shots=P,refs=R),open('p5.json','w'),indent=1)
print(len(P),sum(p['dur'] for p in P if p['id']<150))
