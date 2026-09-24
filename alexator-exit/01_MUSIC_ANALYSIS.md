# Open Skies — Music Analysis

Source: `003-Open-Skies.mp3` · media id `c5282618-e2c9-434a-b69e-058c95df86d8`
Full length **268.840 s**.

First track selected under the new rotation guideline — release **003**, against
the previous five which ran 016, 017, 018, 019, 020 consecutively.

## Structure

| Block (s) | rms | low | mid | high |
|---|---|---|---|---|
| 0 | −18.1 | −32.7 | −18.1 | −15.6 |
| 20 | −11.8 | −19.7 | −13.0 | −6.5 |
| 40 | −8.5 | −12.6 | −11.4 | −6.0 |
| 50 | −9.1 | −15.0 | −11.0 | −6.3 |
| **60** | **−5.1** | **−6.3** | −13.2 | −7.9 |
| 100 | −6.4 | −9.2 | −11.3 | −4.8 |
| 160 | −8.3 | −32.6 | −9.0 | −3.9 |
| 230 | −4.3 | −5.6 | −12.1 | −6.0 |

Sparse for ~37 s, builds through the forties and fifties, **opens into full
energy at 58 s**. A second large breakdown sits at 158.9–168.6.

## Tempo

| Window | BPM | Comb score |
|---|---|---|
| 60–105 s | 135.196 | **0.4461** |
| 105–150 s | 135.413 | **0.4237** |
| 60–150 s | **135.2870** | 0.3013 |
| 170–255 s | 136.362 | 0.2520 *(rejected — low score)* |

**135.2870 BPM · beat 0.443502 s · bar 1.774008 s.**

The two independent 45-second windows agree to **0.16%**, and the 90-second
window spanning both returns a figure sitting between them. Comb scores of
0.42–0.45 are roughly three times what the same method produced on *Just Relax*
(0.14), where it had to be rejected — this track has a genuinely clean kick grid
and the comb is trustworthy here.

A direct interval measurement over 60–150 s returned 134.9095 BPM, 0.63% away.
That method divides span by `round(span/median)`, so a single missed or spurious
onset shifts the interval count by one; at 203 intervals instead of 202 it gives
135.58. With the comb scoring this high, the comb wins.

## The drop

Fine attack scan at hop = 16 (0.73 ms) over 58.00–58.45 s.
Baseline 4.2282, plateau 9.1406, 20% threshold 5.2106.

**DROP = 57.99982 s.**

## Chosen section

**24 bars · 36.71172 s → 79.28791 s · 42.583 s**, symmetrical 12-bar build and
12-bar payoff.

The six aircraft shots play over the track's rising section; the five shots of
the fall play over the full-energy section that opens at 58. Fades 0.35 s in,
0.30 s out, both inside the cut.

## Picture-to-arrangement mapping

**The drop falls on the cut to shot 07 — the exit.** Frame 511, absolute
58.00339 s, against a measured drop at 57.99982 s.

**Error +3.6 ms, or 0.09 of one frame.**

The most literal mapping available: the beat drops and so does he.

## Cut accuracy achieved

All ten internal boundaries present at scene-detect threshold 0.03, max error
**0.096 frame**:

| Target (s) | Detected (s) | Error (frames) |
|---|---|---|
| 3.5417 | 3.54199 | 0.007 |
| 7.0833 | 7.08398 | 0.016 |
| 10.6250 | 10.62600 | 0.024 |
| 14.2083 | 14.21000 | 0.040 |
| 17.7500 | 17.75200 | 0.048 |
| **21.2917** | **21.29400** | **0.055** ← the exit |
| 24.8333 | 24.83600 | 0.064 |
| 28.3750 | 28.37800 | 0.072 |
| 33.7083 | 33.71200 | 0.089 |
| 37.2500 | 37.25400 | 0.096 |

Progression: FORGE ±0.48 → LAST TRAIN ±0.13 → SAND ±0.10 → SOUND ±0.055 →
SATURDAY ±0.137 → **EXIT ±0.096**.
