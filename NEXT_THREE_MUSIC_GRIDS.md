# NEXT THREE FILMS — MUSIC GRIDS (locked 9 Oct 2026)
Analysis done locally at zero credit cost. No generation has started:
the Higgsfield balance is 4.83 after an unexplained ~3,880-credit drain.

Method per track: broadband + low-band autocorrelation, kick inter-onset
histogram, a global phase-locked comb fit, a least-squares grid fitted to
measured section boundaries, and a high-count beat-grid fit over every strong
low-band onset. A value is only locked when two independent methods agree.

All three mp3s carry an attached-picture stream -> `-map 0:a:0` is MANDATORY.

---------------------------------------------------------------------------
## 001 GENESIS   ->  THE RESTORER
MD5 88f180f2eef605da9b88aa7d127a048e   length 215.920 s
BPM 109.0528   beat 0.5502000 s   BAR 2.2008000 s
  derived from an 88-bar baseline between two strong measured onsets
  (17.6020 s -> 211.2727 s), which also made all 14 boundary candidates
  land on 4-bar multiples. High-count onset fit gave 109.836 (55 inliers);
  the long baseline is preferred. LOWEST CONFIDENCE OF THE THREE.
IN    151.9157 s
DROP  158.5181 s   = IN + 3 bars   (measured onset, post-breakdown lift)
OUT   211.3373 s   = DROP + 24 bars, landing on the measured section end
                     at 211.2727 s -> the 24-bar phrase resolves in full
27 bars = 59.4216 s -> 1426 frames @24fps = 59.4167 s (0.005 s inside the line)
Drop lands on FRAME 158.

---------------------------------------------------------------------------
## 025 PAIN AND LOVE   ->  THE AVALANCHE DOG
MD5 f21408ae0fd5319f56036797af0a71ab   length 232.743 s
BPM 139.1062   beat 0.4313253 s   BAR 1.7253011 s
  high-count onset fit: 82 inliers, 12.6 ms rms. Agrees with both
  autocorrelations (139.34 / 139.24) and the kick histogram (139.67).
  An earlier section-boundary fit returned 136.23 — it had hit the edge of
  its search range and was discarded.
IN    116.4719 s   (measured breakdown start 116.3299 s)
DROP  130.2743 s   = IN + 8 bars  (strongest onset in the track)
OUT   171.6815 s   = DROP + 24 bars
32 bars = 55.2096 s -> 1325 frames @24fps = 55.2083 s
Drop lands on FRAME 331.

---------------------------------------------------------------------------
## 021 ADRENALINE   ->  THE SMOKEJUMPER
MD5 7997e3c355a43f41ffdd554903b70ffe   length 189.161 s
BPM 133.9960   beat 0.4477746 s   BAR 1.7910983 s
  high-count onset fit: 73 inliers, 5.3 ms rms — the cleanest of the three.
  Section-boundary fit independently gave 134.094 (9/10 inliers). The
  broadband autocorrelation returned 89.27, a metrical-level error
  (89.27 x 1.5 = 133.9), and was discarded.
IN    114.5324 s
DROP  121.6968 s   = IN + 4 bars  (measured; low band jumps 0.30 -> 0.81)
OUT   171.8475 s   = DROP + 28 bars, on the measured collapse at 171.7321 s
                     where the track drops to near silence
32 bars = 57.3151 s -> 1375 frames @24fps = 57.2917 s
Drop lands on FRAME 172.

---------------------------------------------------------------------------
## FRAME PLANS (each must sum exactly)
GENESIS        1426 = 79,79 | 127 x8, 126 x2          cuts at 79,158,285,412,539,666,793,920,1047,1174,1300
PAIN AND LOVE  1325 = 83,83,83,82 | 125 x2, 124 x6    cuts at 83,166,249,331,456,581,705,829,953,1077,1201
ADRENALINE     1375 = 86,86 | 121 x3, 120 x7          cuts at 86,172,293,414,535,655,775,895,1015,1135,1255

## BUDGET (per film)
6 reference plates 12.00 + 12 keyframes 24.00 + redo allowance 12.00
+ clips (2-4 at 7.50, 8-10 at 9.00) 102.00-105.00  =  150.00-153.00
Three films: 450-460, plus ~45 headroom for clip re-rolls = ~500.
