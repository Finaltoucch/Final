# RIDE THE STORM — Music Analysis
**Track:** ALEXATOR — *Ride the Storm* (release 014)
**Source media id:** `41fddf73-ab0d-48e5-84d3-d9f1bffb306a`
**Full duration:** 254.440 s

## Tempo

| Method | Result | Confidence | Verdict |
|---|---|---|---|
| Comb filter, kick envelope | 137.6600 BPM | score **0.1399** | rejected |
| Comb filter, broadband flux | 137.3600 BPM | score **0.2930** | rejected |
| Autocorrelation, low band | 138.2099 BPM | peak 0.2049 | corroborator |
| **Autocorrelation, broadband flux** | **138.2158 BPM** | **peak 0.4955** | **accepted** |

Both comb scores fall below the 0.4 trust line, so they are rejected on the
same doctrine used on *Brighter Days*: take the method with the highest
measured confidence and never accept a figure on one method alone. The low
band corroborates the broadband figure to **0.004%** (138.2099 vs 138.2158),
which is the cross-check.

**Accepted: 138.2158 BPM — beat 0.434104 s, bar 1.736415 s.**

Recorded honestly: disjoint halves give 137.2894 and 138.9645 BPM, a 1.2%
spread. The autocorrelation harmonics fall away cleanly (1x 0.496, 2x 0.292,
3x 0.147, 4x 0.082), which confirms the fundamental but also shows a soft
rather than metronomic grid. The grid is therefore **anchored to the drop**
and used across 26 bars only, never extrapolated over the whole track.

## Structure

| Window | Low band | Kick |
|---|---|---|
| 0–8 s | −43.4 dB | no |
| 8–32 s | −22 to −26 dB | yes, sparse |
| 40–80 s | −7.7 to −10.0 dB | full |
| **80–88 s** | **−20.0 dB** | **breakdown** |
| 88–144 s | −7.4 to −10.6 dB | full |
| 248–256 s | −29.7 dB | outro |

**Kick-free stretch: 84.428 → 87.679 s (3.251 s).**

Top energy rises measured over a 1 s window:

| t (s) | Rise |
|---|---|
| **18.945** | **+13.2 dB** (−22.6 → −9.4) |
| 149.357 | +8.4 dB |
| **87.142** | **+8.4 dB** (−27.4 → −19.0) |
| 164.888 | +8.3 dB |

## The two pivots

Fine scan at N=256, hop=16 (0.73 ms resolution) on the raw low band:

| Event | Threshold crossing | Hardest transient | Taken |
|---|---|---|---|
| First drop | 18.85016 s | 19.09469 s | 19.09469 |
| Re-entry after breakdown | 87.00385 s | **87.17583 s** | **87.17583** |

The two pivots are 68.0811 s apart = 39.208 bars — not an integer, which is
the same soft-tempo signature the disjoint halves showed. The grid is
therefore anchored locally to **87.17583 s**, not fitted globally.

**Anchor: 87.17583 s** — the re-entry after the breakdown.

## The cut

- **In:** 66.33885 s (drop − 12 bars)
- **Out:** 111.50552 s
- **Length:** 45.1667 s (26 bars)
- Fade in 0.60 s, fade out 0.547 s from 44.62 s

Measured on the rendered cut:

| Check | Value |
|---|---|
| Integrated loudness | −12.7 LUFS |
| Loudness range | 1.8 LU |
| True peak | −1.50 dBFS |
| Clipped samples | 0 |

The breakdown at 84.428 s falls inside shot 06, which runs 83.703 → 87.176 s.
The stalled moment plays through the kick-free stretch and cuts to the launch
on the re-entry.
