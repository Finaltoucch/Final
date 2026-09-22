# Just Relax — Music Analysis

Source: `020-Just-Relax.mp3` · media id `729f5631-bbcb-4528-9580-2364a3caeeb1`
Full length **284.200 s**.

## Character of the track

Despite the title, this is **not** a downtempo piece. 133 BPM, kick present 68%
of the track (low band above −14 dB), high band averaging −10.4 dB. It is a
groove.

Its defining structural feature is the opening: **no kick at all for the first
36 seconds**, but real music underneath — pads and melody at −8 to −10 dB. That
sparse intro is what the film's first half is built on.

| Block (s) | rms | low | mid | high |
|---|---|---|---|---|
| 0 | −23.4 | −52.9 | −22.0 | −30.9 |
| 10 | −10.0 | −23.5 | −8.7 | −14.0 |
| 20 | −7.6 | −18.3 | −6.1 | −16.9 |
| 30 | −9.8 | −24.1 | −9.4 | −11.3 |
| 40 | −10.2 | −24.9 | −9.1 | −9.4 |
| 50 | −7.3 | −13.7 | −7.7 | −7.9 |
| …240 | −2.7 | −3.5 | −12.3 | −9.1 |

## Tempo — three methods, two rejected

This track did not yield to the usual approach, and the failure is worth
recording.

| Method | Result | Verdict |
|---|---|---|
| Comb filter over kick onset envelope | 131.506 BPM, score **0.14** | **rejected** — score is half what the same method scores on a cleanly gridded track (0.24 on *Never Let Go*) |
| Structural-event spacing (kick-gap boundaries) | inconclusive | **rejected** — every candidate bar length mispredicted events by 300–600 ms; this track's gaps are soft, not hard |
| **Direct interval measurement** | **133.703 BPM** | **accepted** |
| Broadband spectral-flux autocorrelation | 133.478 BPM | corroborates (0.17% apart) |

The accepted figure comes from **154 consecutive kick intervals spanning
69.108 s** in the clean region 40–120 s: 69.108 / 154 = 0.448756 s per beat.

Two independent methods agreeing to 0.17% beats one method with a weak score.

| Quantity | Value |
|---|---|
| Tempo | **133.703 BPM** |
| Beat | 0.448756 s |
| Bar | 1.795024 s |

## The drop

A fine attack scan at hop = 16 (0.73 ms resolution) over 36.020 → 36.110 s:

| t (s) | kick envelope |
|---|---|
| 36.0448 | 0.089 |
| 36.0483 | 0.227 |
| 36.0490 | 0.460 |
| 36.0504 | 1.117 |
| **36.0620** | **7.347** |
| 36.0765 | 14.120 |
| 36.0824 | 33.586 |
| 36.1010 | 36.372 |

Baseline 0.071, plateau 35.520. Taking the 20% crossing:

**DROP = 36.06204 s** — the track goes from silence in the low band to full kick
energy in roughly 40 milliseconds.

### A trap worth recording

An earlier pass took "the strongest transient in the window" and returned
**36.2376 s** — 176 ms late. That sample sat in the middle of the sustained loud
plateau, where frame-to-frame variation happens to be largest. The strongest
*difference* is not the attack when the signal is already loud and oscillating.
**Find the attack by threshold crossing from baseline, not by maximum delta.**

## Chosen section

**24 bars · 14.52175 s → 57.60233 s · 43.083 s**, laid out as a symmetrical
12-bar build and 12-bar payoff with the drop on the bar line between them.

Fades: natural fade-in 0.35 s, smooth fade-out 0.30 s, both inside the cut.

## Cut accuracy achieved

Scene-change detection at threshold 0.03 on the finished master. All ten
internal boundaries present, max error **0.137 frame**:

| Target (s) | Detected (s) | Error (frames) |
|---|---|---|
| 3.5833 | 3.58398 | 0.016 |
| 7.1667 | 7.16797 | 0.030 |
| 10.7500 | 10.75200 | 0.048 |
| 14.3750 | 14.37700 | 0.048 |
| 17.9583 | 17.96100 | 0.065 |
| **21.5417** | **21.54500** | **0.079** ← the drop |
| 25.1250 | 25.12900 | 0.096 |
| 28.7083 | 28.71300 | 0.113 |
| 34.1250 | 34.13000 | 0.120 |
| 37.7083 | 37.71400 | 0.137 |

**Drop alignment: shot 07 begins at absolute 36.06342 s against a measured drop
of 36.06204 s — +1.4 ms, or 0.03 of one frame.**

Cut-accuracy progression: FORGE ±0.48 → LAST TRAIN ±0.13 → SAND ±0.10 →
WHERE THE SOUND IS ±0.055 → **SATURDAY ±0.137**.
