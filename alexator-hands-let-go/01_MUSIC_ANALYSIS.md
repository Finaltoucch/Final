# WHAT THE HANDS LET GO — Music Analysis
**Track:** ALEXATOR — *Brighter Days* (release 008)
**Source media id:** `50efb7c4-7d99-40de-a237-f51f9ceb3a13`
**Full duration:** 236.680 s (decoded, mono 22050 Hz f32)

## Tempo

Three independent methods were run. Doctrine: take the method with the
highest **measured** confidence, and never accept a figure on one method alone.

| Method | Result | Confidence | Verdict |
|---|---|---|---|
| Comb filter, kick onset envelope, whole track | 135.0000 BPM | score **0.1152** | rejected |
| Comb filter, broadband flux, whole track | 137.0200 BPM | score **0.2586** | rejected |
| Comb filter, kick, 20–110 s | 135.0000 BPM | score 0.2097 | rejected |
| Comb filter, kick, 120–230 s | 136.6800 BPM | score 0.1787 | rejected |
| Direct interval measurement | 123–253 BPM | unstable | rejected |
| **Broadband flux autocorrelation** | **136.3980 BPM** | **peak 0.4671** | **accepted** |

The comb filter fails on this track because *Brighter Days* has a soft,
non-percussive kick — there is no kick at all for the first 13.7 s, and the
high band is the brightest of any track in the engagement (mean −6.3 dB).
Interval measurement was worse: with a loose gate it caught eighth-note
percussion (246 BPM); with a strict gate it dropped beats the kick does not
play (123 BPM). It has no stable operating point here, so it is not a
competing answer — it is a failing method.

Autocorrelation is the only method that scored above the 0.4 trust line, and
it reproduced an earlier independent run (136.3913 BPM) to within **0.005%**.

**Accepted: 136.3980 BPM — beat 0.439889 s, bar 1.759557 s.**

Caveat, recorded honestly: disjoint halves give 135.245 BPM (14–125 s) and
137.157 BPM (127–236 s), and the autocorrelation harmonics drift (3× peak
lands 4 frames early, 4× peak 6 frames late). This is a soft, human tempo,
not a hard metronomic grid. The grid is therefore **anchored to the drop**
and used over a 26-bar span, not extrapolated across the whole track.

## The drop

Earlier coarse analysis put the drop at 126.874 s. A fine scan (N=256,
hop=16, 0.73 ms) on the raw low band shows what is actually there:

| t (s) | low band |
|---|---|
| 126.680 | −31.71 dB |
| 126.760 | −48.61 dB |
| 126.800 | −56.86 dB |
| 126.840 | **−59.06 dB** |
| 126.880 | −45.75 dB |
| **126.887** | **impact** |
| 126.920 | −5.70 dB |

The producer cut a **~200 ms hole of near-silence** immediately before the
hit. The low band falls to −59 dB, then climbs 40 dB in 40 ms.

Threshold-crossing-from-baseline — correct on *Just Relax* — is the **wrong
tool here**, because the breakdown is not quiet and there is no clean
baseline to measure a rise from. Run anyway it fired at 126.432 s, 455 ms
early, on riser texture inside the breakdown. The hard-transient method is
correct on this track.

**Drop anchor: 126.88689 s.**

### Structural corroboration
`126.88689 − 6 bars = 116.32955 s`, which is the musical start of the
kick-free stretch. The earlier reading of 117.10 s was **0.77 s late** — that
figure was kick reverb decaying past an energy threshold, not the boundary
itself. Two independent measurements now agree, and the kick hole is
**exactly 6 bars**.

Verification that the hole is real and not merely quiet:

| Window | low mean | low max |
|---|---|---|
| 110–118 s (pre) | −14.21 dB | −1.18 dB |
| **116.3–126.9 s (hole)** | **−27.69 dB** | **−10.37 dB** |
| 127–136 s (post) | −6.95 dB | −0.80 dB |
| 40–60 s (ordinary body) | −25.05 dB | −1.61 dB |

The ordinary body of the track has a similar *mean* but peaks at −1.61 dB.
Nothing in the hole exceeds −10.37 dB. There are no kick transients in it.

## The cut

- **In:** 102.25310 s
- **Out:** 148.00157 s
- **Length:** 45.750 s (26 bars)
- Fade in 0.60 s, fade out 0.55 s starting at 45.20 s

Measured on the rendered cut:

| Check | Value |
|---|---|
| Integrated loudness | −13.5 LUFS |
| Loudness range | 1.7 LU |
| True peak | −2.12 dBFS |
| Clipped samples | 0 |
| First 10 ms | −50.78 dBFS |
| Full level by | 0.6 s |
| Last 10 ms | −43.60 dBFS |

Natural fade-in, smooth fade-out, no clipping.
