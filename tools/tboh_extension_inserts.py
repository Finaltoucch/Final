# Two Boys, One Heart: 15-minute extension.
# Inserts 37 silent montage/beat shots (X01-X38) into the Part 1-4 edit lists.
# All inserted clips have their Kling audio muted; the score carries them.
# Usage (sandbox): python3 tboh_extension_inserts.py 123   |   python3 tboh_extension_inserts.py 4
import json,sys
def X(stem,name,**k):
  d={"n":name,"t":{"X":"20261122_"+stem},"mute":[[0,30]]};d.update(k);return d
def apply(path,out,ins):
  L=json.load(open(path));R=[]
  key=lambda c:c.get('n',('card',c.get('card')))
  for c in L:
    k=key(c)
    R+= ins.get(('before',k),[])
    R.append(c)
    R+= ins.get(('after',k),[])
  used=set(x for x in ins); found=set()
  for c in L:
    for p in ('before','after'):
      if (p,key(c)) in ins: found.add((p,key(c)))
  miss=used-found
  json.dump(R,open(out,'w'));print(out,len(L),'->',len(R),'missing',miss)
P="colortemperature=temperature=8600,eq=saturation=0.9"
# Part 1: skyline, walk/bike/drive to school, tests handed back, library montage, walking out, Trey alone in rain
p1={('before',101):[X("191902_e4362796-1b00-4790-a9d6-c2ad7e5df5ff","X01")],
 ('after',101):[X("191542_32575061-3d0e-48ce-82ba-ce045f64d3f6","X02"),X("191542_0f09900a-23cf-421b-bdaf-d4ef34b5a7d6","X03"),X("191542_388f1837-e1c0-4b4c-8718-a60a74f23d75","X04")],
 ('before',106):[X("191542_bb658532-bceb-4eba-a2bd-d896383ab789","X05")],
 ('before',201):[X("191542_2f121e6c-7b88-4e33-8d45-db66f09f97f6","X06")],
 ('after',202):[X("191902_2c8ac3bd-48f6-4d00-a1b7-f527b007c189","X07"),X("191902_6580b060-ab65-4e87-94d7-40cc170672fc","X08")],
 ('after',210):[X("191542_f1c117fe-ae2a-4b0d-8825-d0bd3373d745","X09")],
 ('after',315):[X("191542_a283ff19-adfa-4064-a884-83913de471c4","X10",maxdur=3.5)]}
# Part 2: Zara awake at night, Malik cycling at dawn, Zara looks back, scoreboard, Trey alone in car, hallway, card finished
p2={('after',405):[X("191542_d5ece9ba-2c34-49cc-b391-5a3489475294","X11")],
 ('before','e2'):[X("191902_5bc069a2-ed39-494d-b8ef-eca7a982c530","X12")],
 ('after',504):[X("191902_19ca7054-b710-4a1e-a674-27f3c1cf89d3","X13")],
 ('before',601):[X("191902_f87e1a2b-83c9-4642-8996-bb174bd2d935","X14")],
 ('after',605):[X("191902_a56d69d4-6e2b-4085-a0b2-0ee993f4c88f","X15")],
 ('after','e3'):[X("191903_2fc7514b-b138-4a9b-a94b-ac5ab0bbc5a0","X16")],
 ('after',802):[X("192229_d83482a7-307b-4501-96a7-fe520c73bd6b","X17")]}
# Part 3: Zara searching hallway, Malik on bed with notice, Angela at window, Trey in car with notice, Malik rides away, Zara alone in hallway
p3={('after',903):[X("192231_276375b5-da58-4d3f-ac05-cde4416ae498","X19")],
 ('after',1003):[X("192230_8b4c1d35-f388-4daf-bf2e-93d95410d247","X20",maxdur=5.5),X("192229_57a272e6-2b29-499e-b1dd-19ba381cc22c","X21")],
 ('after',1106):[X("192229_b99811e0-e3ae-4841-a533-afcbbb1d781c","X22")],
 ('after',12013):[X("192229_d49b5216-502f-4b97-9449-1f4437d79163","X23")],
 ('after',1203):[X("192229_bffc4ebf-d0fd-4d3b-b4ea-43da1599fb27","X24")]}
# Part 4: Trey walks off without car, father with old photo, morning building, Malik cycling, prom prep x2,
# Zara leaves porch, prom crane, slow dance, Trey looks back, father+son walk, car drives off, night aerial, studio card
p4={('after',1304):[X("192405_681a63d0-44a4-4956-b0d8-03aa82614300","X26"),X("192528_f8e64da3-a27f-496a-89b7-486d0660eaa1","X27")],
 ('after',('card','THE NEXT MORNING')):[X("192529_56968f17-4840-4c83-b3df-93ad6da18acb","X28")],
 ('after',1402):[X("192528_e4c7c8ec-2b89-4206-917a-d544cdca1be7","X29")],
 ('after',('card','PROM NIGHT')):[X("192528_ab452b27-ccba-4234-a544-64c305b3750f","X30"),X("192528_7f920bc4-375b-4526-b978-8cd68caa9bde","X31")],
 ('after',1501):[X("192528_6bc1f5a1-731e-4364-a43b-6c57bdc861ac","X32",maxdur=3.5)],
 ('after','e7'):[X("192528_319d0fb5-2d33-4e7a-be00-b0676c1b5d6e","X33",pre=P)],
 ('after',1612):[X("192807_23ac2edd-7d03-4c0c-a50e-26b142b3d263","X34",pre=P)],
 ('before',1701):[X("192807_10edf73b-2b21-49fa-aa57-fa6bcde11b0f","X35",pre=P)],
 ('after',1704):[X("192919_9044d892-3ea1-48da-bc42-ea348d92f707","X36"),X("192918_3ceeec1b-ea28-4748-b675-5ce373f391bd","X37"),X("192919_853f7e62-380d-4a26-8423-2e6fa48394c0","X38")],
 ('after',('card','THE END')):[{"card":"A KHARUNE STUDIOS FILM","sec":3.0}]}
which=sys.argv[1]
if which=='123':
  apply('/home/user/p1b/el.json','/home/user/p1b/elx.json',p1)
  apply('/home/user/p2b/el2.json','/home/user/p2b/elx.json',p2)
  apply('/home/user/p3b/el3.json','/home/user/p3b/elx.json',p3)
if which=='4':
  apply('/home/user/p4b/el4.json','/home/user/p4b/elx.json',p4)
