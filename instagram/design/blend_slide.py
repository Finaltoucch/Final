from PIL import Image, ImageFilter
import numpy as np, sys
def blend(src,out,start=520,end=1135,vseam=None,seam=1000):
    im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(np.float32); H,W,_=a.shape
    if vseam:
        blur=np.asarray(im.filter(ImageFilter.GaussianBlur(45))).astype(np.float32)
        x=np.arange(W); wx=np.clip(1-np.abs(x-vseam)/170,0,1); wx=wx*wx*(3-2*wx)
        a[:seam]=a[:seam]*(1-wx[None,:,None])+blur[:seam]*wx[None,:,None]
    # melt the hard horizontal edge: heavy vertical blur band centred on the seam
    vb=np.asarray(Image.fromarray(a.clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(60))).astype(np.float32)
    y=np.arange(H); wy=np.clip(1-np.abs(y-seam)/170,0,1); wy=(wy*wy*(3-2*wy))[:,None,None]
    a=a*(1-wy)+vb*wy
    tgt=a[end:end+4].mean(axis=0)
    tgt=np.asarray(Image.fromarray(tgt[None].clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(80)))[0].astype(np.float32)
    yy=np.arange(start,end); t=(yy-start)/(end-start); t=t*t*(3-2*t)
    a[start:end]=a[start:end]*(1-t[:,None,None])+tgt[None]*t[:,None,None]
    Image.fromarray(a.clip(0,255).astype(np.uint8)).save(out,quality=95)
D='/tmp/claude-0/-home-user-Final/cac6646f-95b4-597a-a723-111bc17ef11f/images/'
blend(D+'17.webp','blend/slide-02-blended.jpg',vseam=805)
blend(D+'18.webp','blend/slide-03-blended.jpg')
