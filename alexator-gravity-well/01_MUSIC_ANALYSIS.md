# Music Analysis — ALEXATOR, *Rise Again*

Supporting evidence for the fragment selection. Method and measurements are recorded
here so the choice can be defended as a professional edit decision rather than an
arbitrary trim (brief §2).

## Source

| | |
|---|---|
| Title (ID3) | **Rise Again** |
| Artist (ID3) | ALEXATOR |
| Album (ID3) | ALEXATOR.COM |
| Duration | 204.62 s (3:24.62) |
| Encoding | MP3 320 kb/s, 48 kHz, stereo, LAME3.100 |
| Audio content | starts 0.65 s, ends 204.64 s |

## Method

1. Decoded to mono 22.05 kHz float PCM.
2. STFT (N=2048, hop 256) → band energies: low 20–140 Hz (kick), mid 140–2000 Hz,
   high 2–11 kHz (air).
3. Spectral-flux onset envelope → autocorrelation → coarse tempo, then a comb-filter
   refinement pass.
4. Kick-specific onset detection (N=512, hop 64 ≈ 2.9 ms) over the 25–130 Hz band,
   peak-picked at mean + 1.2σ → **925 onsets**.
5. Grid fit by 2-D search over tempo (135.0–137.2 BPM, 0.005 step) and phase, scored
   on onsets landing within ±45 ms.

## Result

```
Tempo            136.060 BPM
Beat             0.44098 s
Bar (4/4)        1.76393 s
8-bar phrase     14.1114 s
First downbeat   0.300 s
Bar n begins at  0.300 + n × 1.76393
```

Confirmed independently: the coarse per-second energy map shows jumps at 171 s, 185 s
and 199 s, which land on the same phrase grid. Two methods agreeing is the check.

## Structure (kick density per bar)

```
bars 28-31   ████████ ███████████ ██████████ █████████    full section
bar  32      ████                                          KICK FALLS AWAY
bars 33-40   ▏ sparse — atmospheric breakdown, kick absent
bar  41      ████████████                                  DROP — kick returns
bars 42-46   ███████████ ██████████ ███████████ ████████ ████████████
bar  47      ██                                            BREATH (1.76 s hole)
bar  48      ███████
bar  49      ████████                                      SECOND WAVE
bars 50-56   ██████████ ████████ █████████ █████████ ████████ █████████ ████████
bar  57      ████                                          breath before re-entry
```

## Candidate windows considered

Scored on RMS energy and escalation ratio (final third ÷ first third):

| Window | Length | Energy | Escalation | Verdict |
|---|---|---|---|---|
| **bar 33 → 57** | **42.33 s** | **0.88** | **×1.67** | **Selected** — strongest escalation, drop at 33%, breath at 58% |
| 71.42 → 113.75 | 42.33 s | 0.99 | ×1.02 | Loudest, but flat — nothing to cut to |
| 156.07 → 204.64 | 48.57 s | 0.95 | ×1.03 | Ends on the track's own ending, but no dynamics |
| 0.88 → 43.21 | 42.33 s | 0.62 | ×2.07 | Best escalation but opens too thin for short-form |
| 113.75 → 170.18 | 56.43 s | 0.84 | ×1.41 | Over the 45 s target, weaker drop |

The 156 s window was the closest rival — ending on the track's natural ending is the
best possible out-point. It was rejected because its energy is flat (×1.03): the brief
requires editing synchronised to "drops, musical accents, transitions, changes in
dynamics," and a flat window offers none. Dynamics beat a convenient ending, and the
fade solves the ending anyway.

## Final cut

```
IN            58.5097 s   (bar 33, downbeat)
Body end     100.8440 s   (bar 57, downbeat) — 24 bars = 3 × 8-bar phrases
OUT          102.2040 s
Duration      43.694 s
Fade in        0.35 s
Fade out       1.36 s     (100.844 → 102.204, entirely after the body)
```

Measured on the rendered cut: **−13.5 LUFS** integrated, **LRA 2.5 LU**,
**true peak −4.6 dBFS**. Fade-in −30.8 → −10.4 dB; fade-out decays to −30.3 dB.
No clipping, no abrupt start or stop.

Both edit points are true downbeats. All 24 bars of the body play at full level —
the fades consume only material outside the body, so no useful music is lost.
