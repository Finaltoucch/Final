# Never Let Go — Music Analysis

Source: `019-Never-Let-Go.mp3` · media id `72117c80-c651-4b60-b8a8-95447a0284c4`
Full length **218.832 s** (decoded 218.800 s).

## Method

Decoded to mono 22050 Hz f32 PCM, analysed locally at zero credit cost:

- STFT band energies — low 20–140 Hz, mid 140–2000 Hz, high 2–11 kHz
  (N = 2048, hop = 256, ~11.6 ms)
- High-resolution kick envelope — N = 512, hop = 64 (~2.9 ms), 25–130 Hz
- Broadband spectral-flux autocorrelation for tempo
- **Comb filter** on the kick onset envelope: for each candidate tempo across
  128–146 BPM at 0.002 BPM steps, the phase maximising summed onset energy at
  beat positions. This replaced the median-phase fit used on earlier projects.

## Why the method changed

The global onset fit on this track was poor — 116 ms RMS against the beat — and
the two tempo estimates disagreed (autocorrelation 136.97 BPM, onset fit 137.54
BPM). A global fit is being dragged by off-beat elements, so it cannot be
trusted for a film whose entire structure hangs on one frame-accurate hit.

The comb filter, run over three different windows, resolves it:

| Window | Tempo | Bar | Phase anchor | Score |
|---|---|---|---|---|
| Whole track (6–216 s) | 137.466 BPM | 1.745886 s | — | 0.119 |
| Section region (54–104 s) | 136.120 BPM | 1.763150 s | 54.4034 | 0.248 |
| Payoff only (75–130 s) | 135.824 BPM | 1.766993 s | 75.0900 | 0.221 |

The whole-track score (0.119) is half the local scores, confirming the global
grid is unreliable. **The local windows are authoritative**, and the payoff
window independently places a beat at **75.0900 s** — 55 ms from the measured
kick re-entry at 75.035 s.

**Final grid pass still required before clips.** The section and payoff windows
differ by 0.3 BPM, which is 3.8 ms per bar — over a 24-bar film that accumulates
to ~90 ms, or 2 frames. The grid gets re-fitted on the exact chosen span before
any frame counts are set.

## Structure

Kick gaps (low band < −14 dB sustained > 0.35 s) — 30 found. The dense cluster
at 36–54 s is a sparse breakdown section; the film's build sits inside it.

Ranked drop candidates (kick re-entry, by low-band energy jump):

| t (s) | Gap before | Low band | Jump | Verdict |
|---|---|---|---|---|
| 43.433 | 2.57 s | −45.5 → −12.7 dB | +32.8 | returns sparse, not full energy |
| 47.009 | 2.86 s | −41.5 → −11.1 dB | +30.4 | returns sparse |
| 50.573 | 2.74 s | −43.7 → −13.6 dB | +30.0 | returns sparse |
| **75.035** | **2.57 s** | **−29.0 → −5.9 dB** | **+23.1** | **chosen — full energy** |
| 131.657 | 0.51 s | −26.9 → −3.9 dB | +22.9 | full energy, but a shallow hole |
| 208.213 | 0.80 s | −33.8 → −3.9 dB | +29.9 | full energy, too near the end |

## The drop

**t = 75.035 s**, preceded by a **2.57-second hole in the kick**.

This is the structure the film needs and the reason it was chosen over the
larger raw jumps at 43–54 s: those re-enter at −12 dB, still sparse. This one
re-enters at −5.9 dB, near full energy, with a proper silence in front of it.

She is outside in the quiet. The door opens on the kick.

**Shot 07 — the door opening — lands here.** This is the one hard constraint in
the project.

## Provisional section layouts

Anchored on the drop, symmetrical build and payoff:

| Bars | Span | Length | Build / payoff |
|---|---|---|---|
| 24 | 54.31 → 96.19 | 41.88 s | 12 / 12 |
| 28 | 50.82 → 99.68 | 48.86 s | 14 / 14 |
| 32 | 47.33 → 103.17 | 55.84 s | 16 / 16 |

All three sit inside the 30–60 s requirement. The 32-bar layout gives a proper
16-bar build, which is how the track is actually written; final choice follows
the locked grid.
