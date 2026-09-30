# 002 *Awakening* — music analysis

First use of this release. Verified against the repo, not from memory: prior
projects used 003, 008, 013 (×2), 014, 016, 017, 018, 019 (×2), 020 and
*Through the Fire*. 002 was free.

`media_id` in Higgsfield storage: `3e4f2fe4-f0c2-4b8f-849b-e0d86d05f5b6`
MD5: `6706a6ec2d17b0a836a3d63f8b269335`

**The mp3 carries an attached-picture video stream**, so every ffmpeg call that
touches it must use `-map 0:a:0`. Without it the cover art is muxed as a video
stream and the build silently produces a still image.

---

## Analysis ran locally

`pip install imageio-ffmpeg` provides a static ffmpeg 7.0.2 binary inside the
agent container. That removes the sandbox round-trip entirely for analysis —
only the client's file still has to arrive through `media_upload_widget`,
because `upload.higgsfield.ai` and both CloudFront hosts return
`403 CONNECT tunnel failed` from this container.

Decode: mono, 22050 Hz, f32 raw PCM.
STFT bands: low 20–140 Hz · mid 140–2000 Hz · high 2–11 kHz.

## Tempo — three independent methods must agree

1. **Spectral-flux autocorrelation**, harmonic-summed
2. **Comb-filter template match** — trusted only at correlation ≥ 0.40
3. **Phase-locked beat-grid search** over the full track — this is the value
   used, because it accumulates the least drift across 46 s

```
BPM   133.60100
beat    0.4490984 s
bar     1.7963937 s
```

## The bar-phase trap

Hit on this track and on *Never Let Go* in the same session, so it is not a
one-off — treat it as the default failure mode.

Maximising flux at the **beat** level fixes the grid only *modulo one beat*. Both
times the bar phase came out one beat early, which placed the drop at bar N.25 —
audibly a quarter-bar late on screen, and invisible in the beat-level score
because that score is identical for all four phases.

Fix: re-derive the phase from the **beat envelope** rather than the flux peak.

```
corrected phase   0.61686
lift              133.55000 s  =  bar 74.0000 exactly
```

Under the uncorrected phase the lift sat at bar 73.75.

## Attack detection doctrine

Threshold-crossing-from-baseline is correct only when there **is** a clean
baseline. Hardest-transient search fails when energy is still climbing through
the scan window — it lands at the window edge every time, which looks like a
confident answer and is not one.

## Selection

```
IN    108.400488 s
OUT   155.106725 s
       26 bars
fade in   0.600 s
fade out  0.546667 s, starting 46.1616663 s
```

Shot 08 — the look — starts at 133.550 s = **frame 604**, on the lift.
