# Part 1 dialogue remake: every line as an over-the-shoulder shot (speaker sharp, listener blurred from behind).
import json,math
SUF=" Cinematic film still, 16:9, photorealistic, 35mm film look, shallow depth of field. Every person is an original fictional character who must not resemble any real actor or celebrity. No text, no logos."
def OTS(listener,side):
    return (f" Over-the-shoulder shot: in the {side} foreground, very close to the camera and softly out of focus, the back of the head and one shoulder of {listener},"
            f" seen only from behind (no face visible). Exactly TWO people: the speaker in sharp focus facing the camera, and the blurred listener from behind.")
TALK=" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue. Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent. Each word is said exactly once."
L=dict(  # library refs
 GU='27bbdbf4-09e9-4fae-be3b-ac06852635ed',GD='152a6fd3-1ac7-4225-9b1e-8e63a654012c',ES='63eb90a2-08c5-40a4-ae59-110eefe298e3',
 EW='ada7e801-a781-4694-9800-584fbcf5662a',H='a06cf4f3-5de6-4941-b406-0aed67147f7e',M='78b978ae-a3e3-4aee-957b-33ccf88aa5d7',
 U='0f150821-525c-43fe-bc8d-ee35831260da',B='e59ccf4f-99ae-4084-b9cc-9bd6a543d608',B2='9bf308d3-8577-40d1-a9d9-88a305a544f3',
 S2b='6b122033-434a-4324-924d-14f0c72b0b06',S3='3c73337d-ec5b-4b00-9171-27e7200e8778',S4='22ed1e7a-78a0-4328-aa3d-9d91fdd2c0ce',
 S7='8b979946-5e7e-4bfc-af5c-2cf517ca1254',S9='d04282c2-db84-4b6d-8232-01d8838a1203',S10='c4b650b0-9bbf-4407-9804-175c41d344a4',
 S12='e8e861b4-0a9c-455a-8928-5f53ab9ac9e2',S13='9bc782d8-f753-437b-af9b-8c7734a47070',S21='cfbafc75-8383-49d1-a8cb-2da94589a85b',
 PAN='333c21b0-6cdf-4021-ba50-447924a9481f',S24='c2506e6a-9bd4-4116-b5f8-fa2c4d523189',S25='634abb0f-8e07-46cf-a0e8-c5c88367533a',
 S26='b92673ca-928d-4ec0-892e-52359e556f5e',S28='f652109f-1800-4ab0-9ab7-c7565b93adb3',S30='63e8c7f0-8d58-40e0-88cc-6586697ef7b9',
 S33='c997b236-c345-4683-82b8-0e8e2578a02f',S35='a8cfb6b7-9d84-494c-9234-058010c792a1',S37='229a35ae-bdd8-47f7-8958-fe9087600475',
 S41='10dae71e-3193-4854-965a-574bd2ce35c8',S43='0eda3a3e-7a53-4ed0-b1f0-83e450dcadef',S44='f287b753-2350-44fe-8fb5-fb235ec82f67',
 S38='b510f20b-fe0b-48ad-8742-d705f4198c07',APT='547cc763-25e8-4f82-9936-3ead4ac5b666',S48='3c8546ee-2439-478a-95e0-eed925987517')
GDR="the beautiful young Black woman with long box braids, a small gold cross necklace, in a fitted yellow sundress, carrying an old brown handbag"
GUN="the beautiful young Black woman with long box braids and a small gold cross necklace, in a knee-length navy-and-white maid uniform with a white apron"
VAN="the glamorous slim blonde woman with long straight light-blonde hair, red lipstick and a fitted red dress"
ETS="the very handsome white man, 34, with short dark-brown hair and a neat short beard, in a tailored navy suit"
ETW="the very handsome white man, 34, with short dark-brown hair and a neat short beard, in a crisp white shirt with rolled sleeves"
ETT="the very handsome white man, 34, with short dark-brown hair and a neat short beard, in a plain gray T-shirt"
HAY="the elegant 60-year-old Black woman with silver hair in a neat bun, a pearl necklace and a black dress"
GRD="the tall Black security guard in a black suit with an earpiece"
BRD="the handsome blond man, 30, with short tousled blond hair, light stubble, a gold watch and a light-blue shirt"
MAM="the warm 52-year-old Black woman with short graying curly hair and reading glasses, in a cream cardigan"
F={};P=[]
def fr(k,refs,place,spk,lis,side,extra=""):
    F[k]=dict(refs=[L[r] for r in refs],prompt=f"Medium close-up of {spk} {place}, facing the camera{extra}."+OTS(lis,side)+SUF)
def ln(k,who,text,mood="says"):
    w=len(text.split());d=max(3,min(15,math.ceil(w/2.7+1.2)))
    P.append(dict(id=len(P)+1,frame=k,spk=who,text=text,dur=d,
      video=f"The person facing the camera {mood}: \"{text}\""+TALK))
GATE="at the open iron gates of a white-columned Southern mansion in bright morning sun"
fr('A1',['S2b','S24','GD'],GATE+", standing beside a white Range Rover",VAN,GDR,'left',", sunglasses pushed up, irritated")
fr('A2',['S2b','GD','S24'],GATE,GDR,VAN+" standing by a white Range Rover",'right',", flustered and apologetic")
fr('B1',['S3','U','GD'],GATE,GRD,GDR,'left',", polite but unsmiling")
fr('B2',['S3','GD','U'],GATE,GDR,GRD,'right',", nervous and hopeful")
DRV="on a long brick driveway lined with luxury cars, a white mansion behind, bright sun"
fr('C1',['S4','GD','U'],DRV,GDR,GRD,'right',", glancing at the cars in disbelief")
fr('C2',['S4','U','GD'],DRV,GRD,GDR,'left',", amused, half smiling")
LIV="in a grand white mansion living room with a curved staircase, a crystal chandelier and a black grand piano"
fr('D1',['S7','S9','H'],LIV,HAY,GDR,'left',", composed and strict, assessing")
fr('D2',['S7','GD','H'],LIV,GDR,HAY,'right',", respectful and earnest")
HALL="in an elegant mansion hallway with tall windows"
fr('E1',['S10','H','GU'],HALL,HAY,GUN,'left',", strict and serious")
fr('E2',['S10','GU','H'],HALL,GUN,HAY,'right',", attentive")
STR="at the foot of a grand curved staircase with gold railings in a white marble foyer"
fr('F1',['S12','H','ES'],STR,HAY,ETS,'left',", polite and formal")
fr('F2',['S12','ES','H'],STR,ETS,HAY,'right',", warm and friendly")
fr('G1',['S13','ES','GU'],STR,ETS,GUN,'left',", offering his hand with a kind smile")
fr('G2',['S13','GU','ES'],STR,GUN,ETS,'right',", shy and polite")
fr('G3',['S13','H','ES'],STR,HAY,ETS,'left',", dry and amused")
KIT="in a bright luxury mansion kitchen with a white marble island and copper pans, morning light"
fr('H1',['S21','GU','EW'],KIT,GUN,ETW+" standing across the marble island",'right',", calm with a small smile")
fr('H2',['S21','EW','GU'],KIT,ETW,GUN+" across the marble island",'left',", holding a coffee mug, surprised and amused")
PANTRY="in a dim mansion pantry with an open medicine cabinet"
fr('I1',['PAN','B','B2'],PANTRY,BRD,GUN,'left',", holding a phone to his ear and a small pill bottle, a charming but nervous smile")
fr('I2',['PAN','GU','B'],PANTRY,GUN,BRD,'right',", wary, holding a stack of folded towels")
BAGS="on the sunny brick driveway in front of the mansion beside parked luxury cars"
fr('J1',['S25','S24'],BAGS,VAN+" with sunglasses",GUN+" holding many designer shopping bags",'left',", haughty and cold")
fr('J2',['S25','GU'],BAGS,GUN+" holding many designer shopping bags",VAN,'right',", calm and polite")
BED="in a luxurious master bedroom with a big white bed and tall windows, daylight"
fr('K1',['S28','S26'],BED+", lounging on the bed",VAN,GUN+" standing at the foot of the bed",'left',", smug and dismissive")
fr('K2',['S26','GU'],BED,GUN+" standing at the foot of the bed",VAN+" lounging on the bed",'right',", holding her temper, polite")
DIN="in an elegant mansion dining room with a long glass dining table, a crystal chandelier and tall windows"
fr('L1',['S30','S24'],DIN,VAN,GUN,'left',", cold and contemptuous, pointing at the table")
fr('L2',['S30','GU'],DIN,GUN+" holding a cleaning cloth",VAN,'right',", calm and firm")
fr('M1',['S33','ES'],DIN,ETS,VAN,'left',", puzzled, looking between the women")
fr('M2',['S33','S24'],DIN,VAN,ETS,'right',", suddenly sweet and smiling")
fr('N1',['S35','ES','GU'],KIT,ETS+" with his tie loosened",GUN+" at the sink",'left',", concerned and gentle")
fr('N2',['S37','GU','ES'],KIT+", at the sink",GUN,ETS,'right',", composed but hurt")
NIGHT="in the dark mansion kitchen at 1 a.m., lit only by a warm pendant lamp over the marble island"
fr('O1',['S44','EW','S41'],NIGHT,ETT,GUN+" sitting at the island with an open textbook",'left',", curious and warm")
fr('O2',['S43','GU','EW'],NIGHT+", sitting at the island with an open textbook",GUN,ETT,'right',", soft and sincere")
APTS="in a small, worn but tidy Nashville apartment living room at night, warm lamp light"
fr('P1',['S38','M','APT'],APTS+", sitting in an armchair holding a pharmacy receipt",MAM,GUN,'left',", worried and loving")
fr('P2',['S38','GU','M'],APTS,GUN,MAM,'right',", tired but determined")
LAU="in a dim mansion laundry room at night with washing machines and dryers"
fr('Q1',['S48','S24'],LAU,VAN+" in a red dress",GUN+" backed against a dryer",'left',", quiet, cold and threatening, leaning close")
fr('Q2',['S48','GU'],LAU+", backed against a dryer",GUN,VAN+" in a red dress",'right',", frightened")
# lines (in film order); old clip number noted as o
def S(o,k,who,t,m="says"):ln(k,who,t,m);P[-1]['o']=o
S(3,'A1','V','Move! Are you blind?','snaps angrily');S(3,'A2','G',"I'm so sorry, ma'am.",'says quickly');S(3,'A1','V','Ugh. Let me guess. The new help.','says with contempt, looking her up and down')
S(4,'B1','U','You Grace Miller?','asks');S(4,'B2','G','Yes, sir.');S(4,'B1','U','Follow me.')
S(5,'C1','G','How many cars does one man need?','murmurs under her breath');S(5,'C2','U',"You're staring at the Ferrari like it owes you money.",'says with a smile')
S(7,'D1','H','You must be Grace.');S(7,'D2','G',"Yes, ma'am.");S(7,'D1','H',"I'm Mrs. Hayes. I run this house. Have you cleaned a house like this before?")
S(7,'D2','G',"No, ma'am. But I cleaned hospital rooms for two years. Nothing is dirtier than a hospital.")
S(8,'D1','H',"We'll see. Your uniform is in the laundry room. You start today.",'says with a flicker of approval')
S(9,'E1','H',"Never enter Mr. Caldwell's study. Never touch his desk. And never, ever argue with Miss Pierce.",'says firmly');S(9,'E2','G',"Who's Miss Pierce?",'asks')
S(9,'E1','H',"You'll know her when you hear her.");S(9,'E2','G','I think I already met her.','says quietly')
S(12,'F1','H','Good morning, Mr. Caldwell.');S(12,'F2','E','Good morning, Mrs. Hayes.');S(12,'F1','H','This is Grace. New staff.')
S(13,'G1','E','Ethan. Welcome, Grace.');S(13,'G2','G','Thank you, sir.');S(13,'G1','E',"If Mrs. Hayes gives you a hard time, you're on your own.",'says with a grin')
S(13,'G3','H','I heard that.','says dryly')
S(20,'H1','G','Try it now.');S(20,'H2','E',"That's perfect. How did you know?",'sips the coffee and says in surprise')
S(20,'H1','G',"You've burned your tongue three mornings in a row, sir. A man who runs three hundred trucks can wait one minute for coffee.")
S(21,'H2','E','Nobody in this house talks to me like that.','laughs and says');S(21,'H1','G',"I'm sorry, sir.");S(21,'H2','E',"No. It's refreshing.",'says warmly')
S(10,'I1','B',"End of the month, Rick. You'll have every dollar.",'says quietly into the phone');S(10,'I1','B',"Vitamins. For my brother. And you didn't hear any of that, sweetheart. Did you?",'lowers the phone and says with a charming smile')
S(10,'I2','G','Hear what, sir?','says carefully');S(10,'I1','B','Smart girl.','smiles and says')
S(23,'J1','V','You again. The girl from the gate. Get these upstairs. Carefully. Some of these cost more than you make in a year.','says coldly');S(23,'J2','G',"Yes, ma'am.")
S(24,'K1','V','Change these sheets.');S(24,'K2','G',"I changed them this morning, ma'am.");S(24,'K1','V','Did I ask for your opinion?','says without looking up')
S(24,'K2','G',"No, ma'am.");S(24,'K1','V','Then change them.')
S(25,'K1','V','People like you should be grateful to even be inside a house like this.','says with a cruel smile')
S(27,'L1','V','This is dirty.');S(27,'L2','G',"I cleaned it five minutes ago, ma'am.");S(27,'L1','V',"Then what's this?",'points and asks')
S(27,'L2','G',"That's your fingerprint, ma'am.",'says calmly')
S(28,'L1','V',"Clean it again. Harder. And don't you ever forget your position in this house.",'hisses')
S(29,'M1','E',"What's going on?",'asks');S(29,'M2','V',"Baby! She just didn't clean the table properly.",'says sweetly');S(29,'M1','E','It looks clean to me.')
S(29,'M2','V','You men never notice anything. Come see the wedding flowers.','laughs lightly and says')
S(30,'N1','E','Grace. What really happened in there?','asks gently');S(30,'N2','G',"It's nothing, sir.")
S(30,'N1','E',"You don't have to let anybody disrespect you because you work here. Not even her.",'says firmly but kindly')
S(31,'N2','G','With respect, sir, I need this job more than I need my pride.','says quietly')
S(34,'O1','E',"Neuromuscular rehabilitation. Light reading? You're studying physical therapy?",'reads the book title and asks with a smile');S(34,'O2','G','At night. Online.')
S(35,'O2','G',"My daddy had a stroke when I was twelve. Nobody came to help him walk again. So I did. He walked me to the bus every day for six years after that.",'says softly')
S(36,'O1','E',"That's the best thing anybody's told me in a year.",'says, moved')
S(32,'P1','M','The inhaler went up again, baby. Three hundred and forty dollars.','says worriedly');S(32,'P2','G',"I'll have it Friday, Mama. Every penny.")
S(33,'P1','M','And your exam?','asks');S(33,'P2','G',"Six months. Then I'm a licensed physical therapist, and nobody tells me to clean a clean table ever again.",'says with quiet determination')
S(39,'Q1','V',"You didn't see anything.",'says quietly and coldly');S(39,'Q2','G',"Ma'am, I",'starts to say, then stops');S(39,'Q1','V',"Your little brother's inhaler. Three hundred and forty dollars. One word to Ethan and you'll never work in Nashville again.",'whispers menacingly')
S(40,'Q1','V','Good girl.','smiles coldly and says')
json.dump(dict(frames=F,lines=P),open('part1r_shots.json','w'),indent=1)
print(len(F),'frames',len(P),'lines',sum(p['dur'] for p in P),'s')
