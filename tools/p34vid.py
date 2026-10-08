# Print Kling requests for Parts 3-4 OTS lines whose frame is approved: python3 p34vid.py 4002 4003 ...
import json,sys
O={o['part']*1000+o['shot']:o for o in json.load(open('p34ots.json'))};S=json.load(open('p34state.json'))
R=[]
for k in sys.argv[1:]:
  o=O[int(k)];f=S[k]['frame']
  R.append(dict(index=int(k),params=dict(model='kling3_0',mode='pro',duration=o['dur'],aspect_ratio='16:9',
    declined_preset_id='24bae836-2c4a-48e0-89b6-49fcc0b21612',medias=[dict(value=f,role='start_image')],prompt=o['video'])))
print(json.dumps(R))
