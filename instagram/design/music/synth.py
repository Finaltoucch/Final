"""Royalty-free music beds for Final Touch videos, composed in code (no samples, no licences needed).
usage: synth.py STYLE SECONDS OUT.wav   STYLE = afro | luxury | cinematic | nineties
"""
import sys, numpy as np, wave
SR = 48000
rng = np.random.default_rng(7)

def env(n, a=0.002, d=0.2, shape=4.0):
    t = np.arange(n) / SR
    att = np.clip(t / a, 0, 1)
    return att * np.exp(-shape * t / d)

def sine(f, n, ph=0): return np.sin(2*np.pi*np.cumsum(np.full(n, f) if np.isscalar(f) else f)/SR + ph)
def note(m): return 440 * 2 ** ((m - 69) / 12)

def kick(n=int(.45*SR), f0=120, f1=42, d=.35):
    t = np.arange(n)/SR; f = f1 + (f0-f1)*np.exp(-t*28)
    return sine(f, n) * env(n, .001, d, 3.2)
def snare(n=int(.3*SR), tone=190, d=.16):
    return (0.55*rng.standard_normal(n)*env(n,.001,d,4) + 0.45*sine(tone,n)*env(n,.001,d*.6,5))
def hat(n=int(.06*SR), d=.04):
    x = rng.standard_normal(n); x = np.diff(np.concatenate([[0], x]))  # crude high-pass
    return 0.35*x*env(n,.0005,d,5)
def shaker(n=int(.09*SR)):
    x = rng.standard_normal(n); x = np.diff(np.concatenate([[0], x]))
    return 0.22*x*env(n,.012,.07,4)
def log_drum(f, n=int(.42*SR)):  # amapiano log drum: pitched, pitch-dropping, slightly overdriven
    t=np.arange(n)/SR; fr = f*(1+0.6*np.exp(-t*30))
    x = sine(fr, n)+0.3*sine(fr*2.01, n)
    return np.tanh(2.2*x)*env(n,.002,.33,3)*0.6
def keys(freqs, n, bright=1.0):  # Rhodes-ish chord
    out = np.zeros(n)
    for f in freqs:
        out += sine(f,n)+0.25*bright*sine(2*f,n)+0.08*bright*sine(3*f,n)
    return out/len(freqs)*env(n,.004,.9,2.2)
def pad(freqs, n):
    out=np.zeros(n); t=np.arange(n)/SR
    for f in freqs:
        for det in (-0.12, 0, 0.12):
            out += sine(f*2**(det/12), n, rng.uniform(0,6))
    a = np.minimum(1, t/0.8) * np.minimum(1, (n/SR - t)/0.6)
    return out/(3*len(freqs))*np.clip(a,0,1)
def lowpass(x, cutoff):
    a = np.exp(-2*np.pi*cutoff/SR); y=np.zeros_like(x); acc=0.0
    for i,v in enumerate(x): acc = (1-a)*v + a*acc; y[i]=acc
    return y

def place(buf, snd, t, g=1.0):
    i = int(t*SR); j = min(len(buf), i+len(snd))
    if i < len(buf): buf[i:j] += g*snd[:j-i]

def chords(prog):
    return [[note(m) for m in c] for c in prog]

def build(style, secs):
    n = int(secs*SR); mix = np.zeros(n)
    if style in ('afro','luxury'):
        bpm = 112 if style=='afro' else 120; beat=60/bpm; bar=4*beat
        prog = chords([[57,60,64,67],[53,57,60,64],[55,59,62,65],[52,55,59,62]])  # Am7 Fmaj7 G7 Em7
        roots = [45,41,43,40]
        b=0; t=0
        while t < secs:
            c = prog[b%4]; r = note(roots[b%4]+12 if style=='afro' else roots[b%4])
            for k in range(4): place(mix, kick(), t+k*beat, 0.9)
            for k in range(16): place(mix, shaker() if style=='afro' else hat(), t+k*beat/4, 0.9 if k%2 else 0.55)
            if style=='afro':
                place(mix, snare(tone=330,d=.08), t+1*beat, .35); place(mix, snare(tone=330,d=.08), t+3*beat, .35)
                for pos in (0, 1.5, 2.75, 3.5): place(mix, log_drum(r), t+pos*beat, 1.0)
                for pos in (0.5, 2.5): place(mix, keys(c, int(beat*1.2*SR)), t+pos*beat, .55)
            else:
                for k in range(4): place(mix, hat(int(.09*SR),.07), t+k*beat+beat/2, 1.1)
                place(mix, snare(tone=220,d=.12), t+1*beat, .3); place(mix, snare(tone=220,d=.12), t+3*beat, .3)
                bass = sine(r, int(bar*SR))*0.5*np.minimum(1, np.arange(int(bar*SR))/(0.01*SR))
                place(mix, np.tanh(1.5*bass)*0.7, t)
                place(mix, keys(c, int(bar*SR), .6), t, .55)
            b+=1; t+=bar
    elif style=='cinematic':
        bpm=90; beat=60/bpm; bar=4*beat
        prog = chords([[38,45,50,53],[34,41,46,50],[36,43,48,52],[33,40,45,49]])  # Dm Bb C A
        b=0;t=0
        while t<secs:
            c=prog[b%4]; place(mix, pad([f*2 for f in c], int(bar*SR)), t, 1.3)
            place(mix, kick(int(1.2*SR),90,32,1.0)*1.3, t, 1.0)
            for k in range(8): place(mix, hat(int(.05*SR),.03), t+k*beat/2, .8)  # ticking pulse
            place(mix, snare(int(.6*SR),150,.4), t+2*beat, .45)
            if b%2: 
                for k in (2.5, 3.0, 3.5): place(mix, kick(int(.5*SR),140,50,.3), t+k*beat, .7)
            b+=1; t+=bar
        # riser into the last 2 seconds
        rn=int(2.0*SR); tt=np.arange(rn)/SR
        riser = rng.standard_normal(rn)*(tt/2.0)**2*0.25 + 0.2*sine(200+tt*500, rn)*(tt/2.0)
        place(mix, riser, max(0, secs-2.2))
    elif style=='nineties':
        bpm=90; beat=60/bpm; bar=4*beat
        prog = chords([[50,53,57,60],[55,59,62,65],[48,52,55,59],[57,60,64,67]])  # Dm7 G7 Cmaj7 Am7
        b=0;t=0
        while t<secs:
            for pos in (0, 1.75, 2.5): place(mix, kick(d=.28), t+pos*beat, 1.0)
            for pos in (1, 3): place(mix, snare(tone=200,d=.2), t+pos*beat, .7)
            for k in range(8): place(mix, hat(), t+k*beat/2, .7)
            place(mix, keys(prog[b%4], int(bar*SR), .5), t, .6)
            place(mix, sine(note(prog[b%4][0]-12), int(bar*SR))*np.exp(-np.arange(int(bar*SR))/SR*1.5)*.5, t)
            b+=1; t+=bar
        mix = lowpass(mix, 3800)
        crackle = (rng.random(n) > 0.9993)*rng.standard_normal(n)*0.3 + rng.standard_normal(n)*0.004
        mix += crackle
    mix = np.tanh(mix*0.8)
    fade=int(0.8*SR); mix[:int(.05*SR)] *= np.linspace(0,1,int(.05*SR)); mix[-fade:] *= np.linspace(1,0,fade)
    mix /= np.max(np.abs(mix))+1e-9
    st = np.stack([mix, np.roll(mix, int(0.012*SR))*0.92], 1)  # slight stereo width
    return (st*0.9*32767).astype(np.int16)

if __name__=='__main__':
    style, secs, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    data = build(style, secs)
    with wave.open(out,'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())
    print(out, style, secs)
