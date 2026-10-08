# Voice-change requests for QA-passed Parts 3-4 OTS clips: python3 p34vc.py 4005 ...
import json,sys
V=dict(G='caeba733-3c17-43db-863e-69c7025512cd',E='e6f9b893-51b1-51d3-afe9-9e0482cb7ac1',V='57ccb351-84d7-54ba-afd4-26b566ca6023',
       H='3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd',M='66f35c82-2088-55eb-a0aa-7bf715dc03b7',B='66469f5a-10db-586a-bab1-72f6ee66ba69')
O={o['part']*1000+o['shot']:o for o in json.load(open('p34ots.json'))};S=json.load(open('p34state.json'))
print(json.dumps([dict(index=int(k),params=dict(model='voice_change',voice_id=V[O[int(k)]['spk']],voice_type='preset',
  medias=[dict(value=S[k]['clip'],role='input_video')])) for k in sys.argv[1:] if not O[int(k)]['raw'] and O[int(k)]['spk'] in V]))
