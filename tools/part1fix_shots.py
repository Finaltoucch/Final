# Part 1 screenplay-accuracy fixes: lines re-shot word-for-word from the screenplay on the approved OTS frames.
# 'at' = the part1r line id this clip replaces ('+N' = inserted after line N).
import json,math
FR=json.load(open('part1r_frames.json'));FR['C1']='8a111d32-bb75-409f-a978-757a568ef004'
TALK=(" Realistic facial acting and precise lip sync, natural conversational American accent, no music, clear dialogue."
      " Only the person facing the camera speaks; the blurred person in the foreground seen from behind stays still and silent. Each word is said exactly once.")
P=[]
def S(i,at,k,who,t,m="says",d=None):
    w=len(t.split());P.append(dict(id=i,at=at,frame=k,frame_id=FR[k],spk=who,text=t,dur=d or max(3,min(15,math.ceil(w/2.7+1.2))),
      video=f"The person facing the camera {m}: \"{t}\""+TALK))
S(401,'2','A2','G',"I'm so sorry, ma'am, I—",'says quickly, flustered, and is cut off mid-sentence')
S(402,'+7','C2','U',"Is it that obvious you're new?",'smiles and says')
S(403,'+7','C1','G',"Is it that obvious?",'laughs nervously and says')
S(404,'12','D2','G',"No, ma'am. But I cleaned hospital rooms for two years while I was in school. Nothing is dirtier than a hospital.")
S(405,'14','E1','H',"Laundry, upstairs bedrooms, kitchen when the cook is off. Three rules. Never enter Mr. Caldwell's study. Never touch anything on his desk. And never, ever argue with Miss Pierce.",'says firmly, counting on her fingers')
S(406,'23','G1','E',"If anybody gives you a hard time, you tell Mrs. Hayes. And if Mrs. Hayes gives you a hard time... you're on your own.",'grins and says, whispering the last words')
S(407,'27','H1','G',"You've burned your tongue three mornings in a row, sir. A man who runs three hundred trucks should be able to wait one minute for coffee.")
S(408,'29','H1','G',"I'm sorry, sir, I—",'starts to apologise and is cut off mid-sentence')
S(409,'30','H2','E',"No. Don't be sorry. It's refreshing.",'smiles warmly and says')
S(410,'35','J1','V',"You again. The girl from the gate. Get these upstairs. Carefully. Some of those cost more than you make in a year.",'says coldly')
S(411,'49','M2','V',"Baby! You're home early. Nothing, she just didn't clean the table properly.",'switches to a sweet smile and says')
S(412,'51','M2','V',"You men never notice anything. Come on, I want to show you the wedding flowers.",'laughs lightly and says')
S(413,'66','Q1','V',"Your little brother. The inhaler. Three hundred and forty dollars, isn't it? I hear everything in this house. One word to Ethan and you'll never work in Nashville again. Understood?",'whispers menacingly')
S(414,'56','O1','E',"Neuromuscular rehabilitation. Light reading?",'reads the book title aloud with a teasing smile')
S(415,'+56','O2','G',"I'm sorry, sir, I'm on my break, I—",'closes the book fast, flustered, and is cut off mid-sentence')
S(416,'+56','O1','E',"Grace. Relax. You're studying physical therapy?",'says gently')
S(417,'+57','O1','E',"Why?",'asks softly',3)
S(418,'58','O2','G',"Because my daddy had a stroke when I was twelve. Nobody came to help him walk again. So I did. He walked me to the bus every day for six years after that.",'says softly, pausing before the last sentence')
json.dump(P,open('part1fix_shots.json','w'),indent=1)
print(len(P),'lines',sum(p['dur'] for p in P),'s')
