# Music analysis — ALEXATOR, "Never Let Go" (release 019)

Source file: 9,270,776 bytes, MP3 339 kb/s, 48 kHz joint stereo, 218.832 s
MD5: `34a58330f147d5487693e731ba938a59`

The file analysed locally and the file uploaded for the mux were verified to be
byte-identical by MD5 before the cut was made.

## Tempo

Three independent methods, required to agree before the grid was fixed.

| Method | Result | Confidence |
|---|---|---|
| Spectral-flux autocorrelation, harmonic-summed (N=1024, hop=256, 86.13 fps) | lag 75.22 -> 68.708 BPM, x2 = **137.416** | peak 1.216 |
| Comb-filter template, 4 harmonics, 0.05 BPM grid | **137.40 – 137.70** | 0.594 (trust threshold 0.40) |
| Phase-locked beat-grid search, full 218.8 s, 0.0005 BPM grid | **137.52650** | mean on-beat flux 0.695 |

Spread across all three: 0.15 BPM. The phase-locked figure is used — it is fitted
across the whole track and so carries the least accumulated drift over 26 bars.

```
BPM   137.52650
beat    0.4362727 s
bar     1.7451182 s   (4/4)
```

## Bar phase — a correction worth recording

The beat-grid search returned a beat phase of 0.33146 s. Numbering bars from that
phase put the drop at bar 75.25 — a quarter-bar offset, which is impossible for a
drop. The beat phase was right; the *bar* phase was one beat early, because
beat-level flux maximisation fixes the beat grid only modulo one beat.

Re-deriving from the beat envelope (see below), the true downbeat sits one beat
later: **bar lines at 0.76776 + n x 1.7451182 s**. Under the corrected phase the
emptied bar is exactly bar 74 and the drop is exactly bar 75, both landing on
integers, and the distances between all five major drops in the track (bars 31, 43,
75, 103, 119) become divisible by 4.

## Structure

Per-bar low-band (20–140 Hz) energy, normalised to the track maximum:

```
bars 61-70   55 48 71 88 83 87 78 79 83 83   driving section
bars 71-74   67 44 40 18                     the arrangement empties out
bar  75      69                              KICK RETURNS
bars 76-86   92 93 93 76 88 90 89 86 81 75 74  full arrangement
bar  87      57                              dips
```

The beat envelope through the hole (N=512, hop=64, low band), showing why bar 75 is
unambiguous:

```
beat 297  129.907  59.95
beat 298  130.343  57.58
beat 299  130.779  24.47   <- floor
beat 300  131.215  35.56
beat 301  131.652 146.24   <- the drop
beat 302  132.088 147.78
beat 303  132.524 161.43
```

## Drop position

Fine scan of the 20–140 Hz band at N=256, hop=16 (0.7256 ms resolution).

| Method | Result |
|---|---|
| Bar-grid prediction | **131.65160 s** |
| Threshold crossing from baseline (2.14 vs 27.92 peak — a clean 13:1) | 131.69755 s |

46 ms apart, which is inside the physical rise time of a sub-bass kick. The grid
value is used, so every cut in the film lands on a bar line rather than only the one
at the drop.

**Note on method choice.** Threshold-crossing-from-baseline is only correct when there
*is* a clean baseline. On *Brighter Days* the breakdown was noisy with riser texture
and threshold fired 455 ms early; hardest-transient was correct there. Here the
breakdown floor is near-silent in the low band, so threshold is reliable and it
corroborates the grid. Hardest-transient was tried first and gave 131.935 s — wrong,
because the low-band energy is still climbing through the whole scan window and the
largest first difference lands late. It was discarded on that reasoning, not on
preference.

## The cut

```
IN    107.219945 s   (drop - 14 bars)
OUT   152.593019 s
DUR    45.373074 s   (26 bars) -> 1089 frames at 24 fps = 45.375 s
fade in  0.600 s
fade out 0.547 s from 44.828 s
```

## Frame plan

```
FR=(84 84 83 84 84 84 83 126 126 125 126)   total 1089
```

| Shot | Bars | Frames | Duration | Track position |
|---|---|---|---|---|
| 01 | 2 | 84 | 3.500 s | 107.220 |
| 02 | 2 | 84 | 3.500 s | 110.710 |
| 03 | 2 | 83 | 3.458 s | 114.200 |
| 04 | 2 | 84 | 3.500 s | 117.691 |
| 05 | 2 | 84 | 3.500 s | 121.181 |
| 06 | 2 | 84 | 3.500 s | 124.671 |
| 07 | 2 | 83 | 3.458 s | 128.161 |
| **08** | 3 | 126 | 5.250 s | **131.652 — the drop** |
| 09 | 3 | 126 | 5.250 s | 136.887 |
| 10 | 3 | 125 | 5.208 s | 142.122 |
| 11 | 3 | 126 | 5.250 s | 147.358 |

Frame counts are cumulative-rounded, never per-shot-rounded, so the 26-bar total is
exact and drift cannot accumulate across eleven cuts.
