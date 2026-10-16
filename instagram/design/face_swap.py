import sys; sys.path.insert(0,'pylib')
import cv2, insightface
from insightface.app import FaceAnalysis
app=FaceAnalysis(name='buffalo_l',providers=['CPUExecutionProvider']); app.prepare(ctx_id=-1,det_size=(640,640))
sw=insightface.model_zoo.get_model('models/inswapper_128.onnx',providers=['CPUExecutionProvider'])
D='/tmp/claude-0/-home-user-Final/cac6646f-95b4-597a-a723-111bc17ef11f/images/'
src=max(app.get(cv2.imread(D+'7.jpg')),key=lambda f:f.det_score)
tgt_img=cv2.imread(D+'19.webp'); fs=app.get(tgt_img)
W=tgt_img.shape[1]
ref=min(fs,key=lambda f:abs((f.bbox[0]+f.bbox[2])/2-W/2))
print('referee bbox',[int(v) for v in ref.bbox])
out=sw.get(tgt_img,ref,src,paste_back=True)
cv2.imwrite('swap/upwork-cover-swapped.png',out)
x0,y0,x1,y1=[int(v) for v in ref.bbox]; p=120
cv2.imwrite('swap/crop-before.png',tgt_img[y0-p:y1+p,x0-p:x1+p]); cv2.imwrite('swap/crop-after.png',out[y0-p:y1+p,x0-p:x1+p])
