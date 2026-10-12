# THE LONGEST DINNER
Vertical 9:16 AI music video. Client concept 1: *"a love date dinner between
just two people."*

## CONCEPT
A proposal that almost doesn't happen. A ring turns between his fingers in the
dark. Across the table she is laughing; he is not really listening, he is
rehearsing. His hand goes toward his jacket and stops. On the drop the box
lands on the white linen and the candle flame jumps. She freezes, understands,
cries; he finally steadies; the lid comes up; her hand closes over his. The
last shot pulls back out through the rain on the window.

Legibility test: a viewer who knows nothing reaches the whole story from the
shots alone — object, hesitation, decision, answer. Nothing depends on a note
written in this file.

Built insert-heavy on purpose: the two faces are almost never in frame
together, which is what produced the body-swap complaint on an earlier film.
They share a frame only once, at the very end, seen through rain-streaked
glass with their faces deliberately soft.

Client rule respected by structure, not by avoidance: **no kissing** — the
film resolves on hands.

## TRACK
```
media_id  af3c1bb9-3da2-48c9-87e8-5ee5e9f58fa3
MD5       20a0f894b782c9311a9d6bb0196fc438
length    243.960 s · 48 kHz stereo · 336,970 bps · attached-picture stream
```
TITLE NOT YET KNOWN. This is an ALEXATOR master that had never been used in
any project. It carries no ID3 title tag and the cover art is the generic
ALEXATOR.COM artwork, so the release name must come from the client.
`-map 0:a:0` is MANDATORY (attached picture stream).

## MUSIC GRID — measured, confirmed by two independent methods
```
BPM  137.3779      beat 0.4367516 s      bar 1.7470064 s
IN    164.1319 s
DROP  178.1080 s   = IN + 8 bars   (MEASURED low-band onset, not a grid phase)
OUT   220.0362 s   = DROP + 24 bars
32 bars = 55.9042 s -> 1342 frames @24fps = 55.9167 s
Drop lands on FRAME 335.
```
Local grid fit over the window the film actually uses (160–225 s): 137.3429 /
137.3779 / 137.5108 BPM at three tolerances, spread 0.168 BPM, best 106
inliers at 16.9 ms rms. Fourier comb over the same window peaked at 137.61,
over the whole track at 137.29. Two independent methods inside 0.25 BPM.

Rejected along the way, and why:
- A fit over 100–230 s returned 137.75 at **all four** tolerances while sitting
  0.24 BPM from the edge of its search range. Edge-pinned, discarded.
- Narrowing the search to 134.5–137.0 produced a tight-looking 135.13–135.18.
  That basin only exists because the range excluded the true one. Range-forced,
  discarded. The comb, which has no search range and no inlier threshold,
  settled the question.

**OUT point confirmed structurally.** The RMS envelope dips to −15.2 and
−19.5 dB at 219.50 and 219.75 s and snaps back to −11.3 dB at 220.00 s. The
24-bar phrase resolves and the next one begins exactly where the cut lands —
derived from the grid, then confirmed by the audio independently.

## FRAME PLAN — sums to exactly 1342
| # | frames | n | beat |
|---|---|---|---|
| 01 |    0– 83 |  84 | THE RING TURNING IN THE DARK (hook) |
| 02 |   84–167 |  84 | HER, LAUGHING |
| 03 |  168–251 |  84 | HIM, REHEARSING |
| 04 |  252–334 |  83 | THE HAND THAT STOPS |
| 05 |  335–478 | 144 | **THE BOX LANDS — ON THE DROP** |
| 06 |  479–622 | 144 | HER HAND REACHES AND PULLS BACK |
| 07 |  623–766 | 144 | HER FACE, UNDERSTANDING |
| 08 |  767–910 | 144 | HIS FACE, STEADY AT LAST |
| 09 |  911–1054 | 144 | THE LID COMES UP |
| 10 | 1055–1198 | 144 | HER HAND OVER HIS |
| 11 | 1199–1341 | 143 | OUT THROUGH THE RAIN |

Measured scene cuts: `84 168 252 335 479 623 767 911 1055 1199` — 10/10 exact,
no false positives.

## ASSET IDS
Plates (nano_banana_pro, 2.00 each)
| Plate | Job ID |
|---|---|
| The woman | `e6b0e541-75fd-4192-acfe-2df7b5d802d5` |
| The man | `3a37a562-f535-45fa-821b-7ae0d1c6a6f8` |
| The restaurant | `ccecddfb-a0f8-4a33-9c6e-8ee1c897d95b` |
| The ring and box | `016bdf39-37d4-4550-b3ec-bdf4aca25a72` |

Keyframes / clips — THE TABLE THE GENESIS BIBLE FAILED TO WRITE
| # | keyframe | clip |
|---|---|---|
| 01 | `7be8f0f8-170a-4f94-b88b-a32cfbf7ffb7` | `d8c8e039-5fa8-4f99-a802-46a4b119a944` |
| 02 | `e6c72872-2b58-450f-bc9f-8371242511d4` | `87bf22ce-c2ac-4563-beb6-114ba7fec0b3` |
| 03 | `d29902d4-121a-42b0-9b5e-50e107404b01` | `86228429-7d5f-4313-8160-f96e96865603` |
| 04 | `0088a79f-da6d-42be-abfc-37c701439077` | `74526214-02ce-4ef3-97ec-35f72ca250fe` |
| 05 | `cfcd680a-9b81-4b91-9606-7a8689dde9f3` | `4dd5823f-48e1-4ec6-9dab-41b2f27039ae` |
| 06 | `a1bc2511-5dc8-4c44-93e8-6dbad9e63155` | `7724fec7-3deb-4114-826f-d2a9d60694e3` |
| 07 | `f4ed3d88-5135-4624-8ed8-3bf4f14ecab5` | `95508d85-2f88-44a4-a0ce-a9c9d40a309a` |
| 08 | `be6d92ba-83cc-43ce-bc52-6f9d3446e082` | `9931a07a-8070-4c02-b2bf-64947b9ee316` |
| 09 | `0788b72a-906f-464c-a81b-5be20b841cf5` | `44d401bc-187b-4455-b64f-774e0c5470af` |
| 10 | `63465fc0-1544-427e-a0c5-6eb73eab5682` | `05998202-410c-4915-941c-b7bad706dd0c` |
| 11 | `1f3dc01b-8fcc-41be-afac-471ee145c2e4` | `e82448ce-6039-4cd7-8ac9-249b046183f3` |

Superseded, kept for the record:
- keyframe 01 first attempt `1ad2df2e-4c33-4e0b-86ae-d2078a846a18` — returned
  `nsfw`, not charged. Cause was the phrase "below the table" next to a hand
  and a trouser leg. Rewritten as macro-in-darkness; passed.
- clip 06 first attempt `0eca83e8-d6f1-45b1-86ac-05ca0c737dee` — froze for its
  last 10 frames (freeze_start 25.5423, duration 0.4167). Re-rolled, 9.00.

## LOCKED SPECS — paste VERBATIM into every prompt showing that subject

**THE WOMAN** — 29, AN INVENTED FICTIONAL CHARACTER, NOT any real person.
Mediterranean Southern European features, warm olive skin with visible pores
and a few small freckles across the nose. Dark hazel eyes, thick dark eyebrows
with a natural arch, a straight nose, a full mouth, a small mole below the left
corner of her mouth. Dark brown wavy shoulder-length hair worn loose, tucked
behind the right ear ONLY. A deep FOREST-GREEN SILK BLOUSE, long sleeves,
buttoned to the second button. Small plain GOLD STUD earrings. NO necklace,
NO rings on any finger, NO bracelet, NO watch, NO lipstick, short unpainted
nails.

**THE MAN** — 32, AN INVENTED FICTIONAL CHARACTER, NOT any real person.
Northern European features, fair skin with a visible stubble shadow along the
jaw. Grey-blue eyes, straight dark-blond eyebrows, a slightly broad nose, thin
lips. Short dark-blond hair, side-parted, a little untidy at the crown. A
CHARCOAL-GREY WOOL SUIT JACKET over a WHITE COTTON SHIRT open at the collar,
NO TIE. A plain brown LEATHER-STRAP WATCH on his LEFT wrist. NO rings on any
finger, NO necklace, NO glasses. Large hands, short clean nails, one small
white scar across the back of the RIGHT hand.

**THE ROOM** — a small quiet restaurant at night with only these two people in
it. A round table for two under a HEAVY WHITE LINEN CLOTH falling to the floor.
ONE short white DINNER CANDLE in a plain brass holder with a tall steady flame,
two long-stemmed glasses of DEEP RED WINE, a small white bread plate, a folded
white napkin. Dark panelled walls, deep shadow beyond, one warm amber wall lamp
far behind. A large window at frame left with RAIN RUNNING DOWN THE GLASS and
soft out-of-focus amber street lights beyond. NO other diners, NO staff, NO
flowers, NO menus, NO phones.

**THE RING AND BOX** — a small SQUARE RING BOX about 5 cm across covered in
WORN DARK-NAVY VELVET with a slightly rubbed lid, and inside on OFF-WHITE SILK
a PLAIN SLIM YELLOW-GOLD BAND set with ONE small round clear DIAMOND in a
simple four-claw setting. NO engraving, NO brand marks.

## DELIVERY — verified
```
1342 frames · 55.917 s · 1080x1920 · 9:16 · 24 fps · AAC 48k stereo 320k
76,575,161 B   MD5 ac2bfe07df49fda706fcd8fb534dc598
black 0 · freeze 0 at d=0.5, 0.4 AND 0.3 · cropdetect 1080:1920:0:0
-14.4 LUFS · LRA 1.8 LU · peak -5.1 dBFS
cuts 84 168 252 335 479 623 767 911 1055 1199 — 10/10 exact
served file byte-identical to the local build
```
media_id `ca77777d-8fa7-40f2-962b-b6e7f45fd7df`

Conform: Kling renders 9:16 at 1076x1928. Every clip is scaled to 1080 wide
(1080x1936) and centre-cropped to 1080x1920, which removes 8 px top and 8 px
bottom — 0.83% of height. This is inherent to hitting the 1080x1920 spec and
is applied identically to all eleven shots.

## SPEND
| Item | Credits |
|---|---|
| 4 reference plates | 8.00 |
| 11 keyframes (1 nsfw rejection, not charged) | 22.00 |
| 4 clips @ 7.50 | 30.00 |
| 7 clips @ 9.00 | 63.00 |
| 1 clip re-roll (freeze) @ 9.00 | 9.00 |
| **total** | **132.00** |

---

# CORRECTION ROUND — client rejected shots 04, 05 and 10

The client flagged three frames. All three were real defects, and **two of them
originated in keyframes I approved** — reviewed at 290 px wide, where the fault
was invisible. At full resolution it is obvious in both. This is the same
failure that shipped the blinking painting on GENESIS: **a keyframe is not
approved until it has been looked at at native resolution.**

| Shot | Defect | Where it came from |
|---|---|---|
| 04 | A malformed second hand merged under the first | the KEYFRAME |
| 05 | The box tips and balances on an edge; both background figures rendered as men, the woman absent | the KEYFRAME (background) + the clip (tipping) |
| 10 | Hands deformed, ring box floating unsupported at frame top | the clip |

A fourth fault was found during the fix and corrected before delivery: the
first replacement clip for shot 04 LOST THE CANDLE — it vanished from its brass
holder between frames 60 and 118, and the wine emptied from the glass. Cause
was the slow camera push forcing the model to re-draw the background. Same
mechanism as the GENESIS painting. Fixed by locking the camera off completely
and stating object permanence explicitly.

That in turn caused shot 05 to go static in its last 9 frames once its camera
was locked too (freeze_start 19.584, duration 0.375 at d=0.3). Rather than
spend another 9.00 re-rolling, a 2% post zoompan push was applied to shot 05
alone. **This crops shot 05 by 2% and the client was told.**

## REPLACEMENT ASSET IDS
| # | keyframe | clip |
|---|---|---|
| 04 | `d52eb0fc-8f23-470c-a10a-9b6ec02fdb59` | `12856bc5-5588-4e49-b0fe-c24177ce7cbf` |
| 05 | `c12b36ad-f28f-4faf-9401-7903a629c936` | `f903de3b-80ff-4b8e-8f32-86a4eae67385` |
| 10 | (unchanged `63465fc0-…`) | `9cacf101-6b97-42b3-a647-feffb79aa189` |

Discarded: clip `1f18c784-abdf-4a93-81cb-f7d66eaa2d2e` (lost the candle) and
clip `ddfaf329-dc22-48a6-8c2f-8b036ce284f6` (rolled from the faulty keyframe
background before the background fault was found — 9.00 wasted, my error).

## WHAT ACTUALLY WORKED
1. **Look at every keyframe at NATIVE RESOLUTION before approving it.** Crop
   the region that carries the story — the hands, the face, the object — and
   view that crop. Contact sheets and 290 px thumbnails hide deformed hands,
   wrong-sex background figures and wrong-scale limbs.
2. **For an insert shot, lock the camera off.** Every object-permanence failure
   in this engagement — the GENESIS painting, this film's candle — happened
   under a camera push. A push forces the model to re-draw, and what it
   re-draws it can lose.
3. **A locked camera then needs motion from somewhere else** or freezedetect
   fires. Candle flame and rain on glass were not enough at d=0.3 on shot 05.
4. **Do not describe a background person you cannot afford to have redrawn.**
   Shot 05's new keyframe gives the model a green sleeve and a charcoal
   shoulder cropped at the frame edges, with no head and no face anywhere. A
   face that does not exist cannot be rendered as the wrong person.

## CORRECTED DELIVERY — verified
```
1342 frames · 55.917 s · 1080x1920 · 9:16 · 24 fps · AAC 48k stereo 320k
73,513,733 B   MD5 e111e87df7bbb9ef5ae07bb42ddd8265
black 0 · freeze 0 at d=0.5, 0.4 AND 0.3 · cropdetect 1080:1920:0:0
-14.4 LUFS · LRA 1.8 LU · peak -5.1 dBFS
cuts 84 168 252 335 479 623 767 911 1055 1199 — 10/10 exact
served file byte-identical to the local build
```
media_id `cb98a540-d138-4cd3-a1ba-3a1338998e4a`

Correction spend: 3 keyframes 6.00 + 5 clips 42.00 = 48.00
(of which 9.00 was wasted on a clip rolled from a keyframe whose background
fault I had not yet found).
