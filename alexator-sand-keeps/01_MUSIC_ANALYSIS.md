# Endless Sands — Music Analysis

Source: `018-Endless-Sands.mp3` · media id `decb7898-794f-4c3d-a4da-237049af2f93`
Full length **329.400 s**.

## Method

Decoded to mono 22050 Hz f32 raw PCM via ffmpeg, then analysed locally at zero
credit cost:

- STFT band energies — low 20–140 Hz (kick), mid 140–2000 Hz, high 2–11 kHz
- Kick-band onset detection — N = 512, hop = 64 (~2.9 ms), 25–130 Hz,
  peak-picked at mean + 1.2σ
- Broadband spectral-flux autocorrelation for tempo

**Doctrine:** raw on-grid counts are biased toward faster grids; the
autocorrelation peak is authoritative. The bar grid is then anchored on
*measured structural events* (kick drop-outs), not extrapolated from a single
tempo estimate across the whole track.

## Grid

| Quantity | Value |
|---|---|
| Tempo | **135.3960 BPM** |
| Beat | 0.443145 s |
| Bar | 1.772578 s |
| 8-bar phrase | 14.18063 s |
| Phase vs track zero | +0.0064 s |

### Validation

Three measured structural points land on bar lines within 7 ms:

| Event (s) | Error |
|---|---|
| 0.000 | −6.4 ms |
| 23.043 | −7.0 ms |
| 322.612 | −3.4 ms |

Independent cross-check: (322.612 − 23.043) / 169 bars = 1.77260 s/bar →
**135.394 BPM**, agreeing with the autocorrelation peak to 0.002 BPM.

## Structure

Largest breakdown: **268.176 → 272.631 s** (4.46 s), low band falling to
−39.4 dB at 269.6 s. Kick-gap mapping used a threshold of low band < −14 dB
sustained for > 0.35 s.

## Chosen section

**Bars 136–160 → 241.077 s → 283.619 s · 24 bars · 42.542 s**

Begins on a downbeat at the head of a phrase and ends on a downbeat, so the
fragment reads as a complete musical statement rather than a slice.

The breakdown falls at **t+27.1 → t+31.6** inside the cut. That was chosen
deliberately and mapped onto **shot 08 — the fossil turning in her palm**: the
music hollows out as the shell is revealed and the kick returns as the
grandfather settles beside her.

Fades: natural fade-in 0.35 s, smooth fade-out 0.30 s, both inside the cut.

## Cut accuracy achieved

Scene-change detection at threshold 0.03 on the finished master. All ten
internal boundaries present, max error **0.10 frame**:

| Target (s) | Detected (s) | Error (frames) |
|---|---|---|
| 3.5417 | 3.54199 | 0.007 |
| 7.0833 | 7.08398 | 0.016 |
| 10.6250 | 10.62600 | 0.024 |
| 14.1667 | 14.16800 | 0.031 |
| 17.7083 | 17.71000 | 0.040 |
| 21.2917 | 21.29400 | 0.055 |
| 26.5833 | 26.58600 | 0.064 |
| 31.9167 | 31.92000 | 0.080 |
| 35.4583 | 35.46200 | 0.090 |
| 39.0000 | 39.00400 | 0.096 |

Progression across the engagement: FORGE ±0.48 frame → LAST TRAIN ±0.13 →
**WHAT THE SAND KEEPS ±0.10**.
