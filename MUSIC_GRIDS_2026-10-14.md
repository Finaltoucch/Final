# MUSIC GRIDS — the three new films
Measured 14 October 2026, entirely in the local container at **zero credits**.
The three masters are client chat attachments: they are not on the Higgsfield
account (all 60 audio items swept by exact byte size, no match), and this
container is blocked by the organisation egress policy from Higgsfield's upload
host. Decoding and analysis were therefore done locally with ffmpeg + numpy.

| Film | Track | BPM | bar (s) | IN (s) | DROP (s) | OUT (s) | duration | frames |
|---|---|---|---|---|---|---|---|---|
| THE GOOD SHIRT | 010 New Horizon | 133.9200 | 1.7921147 | 53.4937 | 92.9202 | 103.6729 | 50.179 | 1204 |
| THE LUNCH TABLE | 022 Kindred Soul | 135.9900 | 1.7648356 | 76.3445 | 115.1709 | 125.7599 | 49.415 | 1186 |
| THE SONG SHE STILL KNOWS | 024 Words Unsaid | 135.3500 | 1.7731806 | 196.1153 | 235.1252 | 245.7643 | 49.649 | 1192 |

28 bars each. The drop lands on bar 22, which is the cut into shot 09 — the
beat the whole film is built towards in all three.

## THE TEMPO METHODS, AND WHICH ONES LIE
**ACF returned exactly 135.999 BPM for all three tracks.** That is not a
measurement, it is the integer-lag quantisation: at hop 512 the envelope runs at
43.066 Hz, and lag 19 frames *is* 135.999 BPM. Anything from roughly 134 to 138
collapses into that one bucket.

**The IOI histogram returned exactly 135.977 for all three** — 0.44125 s, which
is 19 frames again. It shares ACF's quantisation, so **it is not an independent
method** and must never be used to confirm ACF.

**A 60 s windowed comb drifted monotonically upward on every track** (New
Horizon 131.6 → 136.1). That is not accelerando: a 60 s observation resolves
only about ±1 BPM at this frequency, so the apparent drift is sidelobe wander
dressed up as precision by a 0.01 BPM search step.

**What actually settles it** is a local grid fit over the exact window the film
uses — tempo and phase together, wide-open 118–152 range, rejected if the answer
lands within 1.5 BPM of either edge — and then an empirical check.

## THE GRID CHECK THAT CAUGHT MY OWN ERROR
For each candidate grid, score the onset envelope at the 28 bar lines and
compare against 400 random phases:

| Film | bar-line energy | random phase | z |
|---|---|---|---|
| THE LUNCH TABLE | 62.77 | 3.76 | **+4.93** |
| THE SONG SHE STILL KNOWS | 26.49 | 4.46 | **+5.08** |
| THE GOOD SHIRT *(first attempt)* | 2.84 | 3.61 | **−0.51** |
| THE GOOD SHIRT *(corrected)* | 20.86 | 3.44 | **+5.69** |

A negative z means the bar lines were landing in the **gaps between** onsets —
the grid was not just imprecise, it was anti-phase.

**The cause was mine.** I fitted New Horizon over 100–156 s, but the film window
works out at 53–104 s, so I extrapolated the grid roughly 40 s *backwards,
outside the fitted region* — the exact local-fit rule I had written down and then
broke. Re-fitting over the real window gave 133.9200 BPM and z = +5.69.

**Rule, now earned the hard way: fit the grid over the window the film uses, and
then prove it by scoring bar lines against random phase. A grid that cannot beat
random phase is not a grid.** Every tempo in this engagement should carry that z.

## SHOT LENGTHS (24 fps)
Bars per shot `3 3 3 3 2 3 2 3 3 3` — 28 bars, with the cut into shot 09 landing
exactly on the drop. Shots come out at **127–129 frames**, except shots 05 and
07 at **85–86 frames**.

Kling returns 121 frames for a 5 s job and 145 for a 6 s job, so:
- eight shots per film need the 6 s job (9.00)
- shots 05 and 07 need only the 5 s job (7.50)

**Clip cost: 8 × 9.00 + 2 × 7.50 = 87.00 per film, 261.00 for all three.**
My earlier estimate of ~790 was wrong and too high — it assumed every shot
needed a 6 s clip at a longer film length.

## OUTSTANDING — CLIENT ACTION NEEDED
Assembly needs the three mp3s inside the Higgsfield build sandbox. They are not
on the account and this container cannot upload them. They must be uploaded
through the Higgsfield upload widget. Until then the clips can be generated but
the films cannot be cut.
