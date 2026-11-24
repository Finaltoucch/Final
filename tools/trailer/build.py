import json,subprocess as sp,numpy as np,os
from PIL import Image,ImageDraw,ImageFont
W='/home/user/tr/w'; SR=48000
OFF=[('hook',0.0),('p1b',48.084),('p2b',254.434),('p3b',439.483),('p4b',609.542)]
def src(T):
  name,o=[x for x in OFF if x[1]<=T][-1]
  if name=='hook': return '/home/user/hb2/hook_v4.mp4','/home/user/hb2/dlg.wav',T-o
  return '/home/user/%s/vid.mp4'%name,'/home/user/%s/dlg.wav'%name,T-o
TL={k['key']:k for k in json.load(open('/home/user/p4b/timeline.json'))}
def key(k,ln,frac=0.5):  # final-time start of a montage shot
  t=TL[k]; return 609.542+t['start']+t['dur']*frac-ln/2
# (type, final_time or text, length, dialogue?)
EDL=[('card','KHARUNE STUDIOS\nPRESENTS',2.5),
 ('shot',48.084+1.5,1.5,False),
 ('shot',182.35,4.15,True),
 ('shot',227.35,3.6,True),
 ('shot',290.75,6.4,True),
 ('card','TWO BOYS.',1.5),
 ('shot',23.55,3.2,True),
 ('shot',456.35,3.0,True),
 ('card','ONE CHOICE.',2.1),
 ('shot',485.65,3.85,True),
 ('shot',522.25,1.65,True),
 ('shot',533.4,2.5,True),
 ('shot',571.65,3.5,True),
 ('shot',650.8,3.3,True),
 ('shot',key('nX32',1.3),1.3,False),
 ('shot',key('n1604',1.3),1.3,False),
 ('shot',key('n1606',1.3),1.3,False),
 ('shot',key('n1607',1.3,0.35),1.3,False),
 ('shot',key('n16081',1.3,0.6),1.3,False),
 ('shot',842.25,2.75,True),
 ('shot',key('n1703',1.5,0.7),1.5,False),
 ('shot',key('n1704',2.5,0.5),2.5,False),
 ('black',721.8,2.0,True),   # "I don't know, Grandma." over black
 ('title','TWO BOYS, ONE HEART',3.8),
 ('shot',801.1,5.0,True),
 ('end','THE FULL MOVIE\nWATCH NOW',3.0)]
F='/home/user/tr/fonts/Cinzel.ttf'
def card(text,path,size=92,sub=None):
  im=Image.new('RGB',(1920,1080),'black'); d=ImageDraw.Draw(im)
  f=ImageFont.truetype(F,size); 
  try: f.set_variation_by_axes([500])
  except Exception: pass
  lines=text.split('\n')
  while max(d.textbbox((0,0),' '.join(l),font=f)[2] for l in lines)>1500: size-=4; f=ImageFont.truetype(F,size)
  hs=[]; ws=[]
  for l in lines:
    l2=' '.join(l)  # letter spacing
    b=d.textbbox((0,0),l2,font=f); ws.append(b[2]-b[0]); hs.append(b[3]-b[1])
  y=540-(sum(hs)+30*(len(lines)-1))/2
  for l,w,h in zip(lines,ws,hs):
    d.text((960-w/2,y),' '.join(l),font=f,fill=(236,236,236)); y+=h+30
  im.save(path)
VF="crop=1920:804:0:138,eq=contrast=1.06:saturation=0.92:brightness=-0.01,vignette=PI/5,noise=alls=5:allf=t,pad=1920:1080:0:138:black,format=yuv420p"
segs=[];T=0.0;dlg=[];marks=[]
for i,e in enumerate(EDL):
  o='%s/s%02d.mp4'%(W,i); typ=e[0]
  if typ=='shot':
    v,a,t=src(e[1]); ln=e[2]
    sp.run(['ffmpeg','-v','error','-y','-ss','%.3f'%t,'-i',v,'-t','%.3f'%ln,'-an','-vf',VF,'-r','24','-c:v','libx264','-preset','veryfast','-crf','17',o],check=True)
    if e[3]: dlg.append((T,a,t,ln))
  elif typ=='black':
    v,a,t=src(e[1]); ln=e[2]
    sp.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=black:s=1920x1080:r=24:d=%.3f'%ln,'-pix_fmt','yuv420p','-c:v','libx264','-crf','17',o],check=True)
    dlg.append((T,a,t,ln))
  else:
    text=e[1]; ln=e[2]; png='%s/c%02d.png'%(W,i)
    card(text,png,size=120 if typ=='title' else 84)
    zoom="zoompan=z='1+0.00045*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=%d:s=1920x1080:fps=24"%int(ln*24)
    fi=0.35 if typ!='title' else 0.12
    sp.run(['ffmpeg','-v','error','-y','-loop','1','-i',png,'-t','%.3f'%ln,'-vf',zoom+',fade=in:st=0:d=%.2f,fade=out:st=%.2f:d=0.35,format=yuv420p'%(fi,ln-0.4),'-r','24','-c:v','libx264','-crf','17',o],check=True)
  marks.append((typ,T,ln,e[1] if typ!='shot' else '')); segs.append(o); T+=e[2]
open(W+'/list.txt','w').write(''.join("file '%s'\n"%s for s in segs))
sp.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+'/list.txt','-c','copy',W+'/video.mp4'],check=True)
json.dump({'marks':marks,'dlg':dlg,'T':T},open(W+'/plan.json','w'))
print('video',T); [print(m) for m in marks]
