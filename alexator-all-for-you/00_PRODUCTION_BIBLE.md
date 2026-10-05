# ALL FOR YOU — THE KITE
ALEXATOR "017 All for You". Fourth paid deliverable. Vertical 9:16 AI music video.

## CONCEPT
A rooftop kite festival at dusk in a dense Indian old city. A girl of nineteen
flies a saffron paper kite from a packed roof and goes after the big black kite
nobody has brought down all week. On the drop she snaps her line taut; her kite
climbs; the two lines cross; the black kite falls across the roofline and the
roofs erupt. The last beats are her grandfather down in the street, looking
straight up — he taught her and can no longer climb. That is the "for you".

Deliberately unlike the three before it: not a machine, not underwater, not a
period romance. First film with a crowd, first set in a contemporary real
place, first that ends in joy rather than loss.

## MUSIC GRID — measured, not guessed
```
BPM  134.080505      beat 0.4474923 s      bar 1.7899694 s
IN    136.243732 s
DROP  150.563487 s   = IN + 8 bars   = FRAME 344
OUT   193.522752 s   = DROP + 24 bars
32 bars = 57.279021 s -> 1374 frames @24fps = 57.250000 s
(lands 0.029 s BEFORE the bar line, so the phrase resolves and we stop on it)
MD5 95fe0bbd8f3691b762e32b8b31ec020d   full length 251.30 s
mp3 carries an attached-picture stream -> `-map 0:a:0` MANDATORY
```
Three independent methods agreed: kick inter-onset histogram 134.23 BPM, global
phase-locked comb fit 134.22, least-squares fit of nine measured section
boundaries 134.08 (6 of 9 inliers, 71 ms rms). An onset-grid fit returning
135.00 was the outlier and was discarded.

Section map that produced the cut: breakdown at bars 76-83 (low band falls to
0.17, mids rise to 0.95), the biggest late energy step at bar 84, a comedown at
bar 104, and a new section starting at bar 108. IN sits at the top of the
breakdown, OUT on the bar line where the post-drop 24-bar phrase resolves.

## FRAME PLAN — must sum to exactly 1374
| # | frames | n | beat |
|---|---|---|---|
| 01 |    0– 85 |  86 | HER FINGERS RELEASE THE KITE (hook) |
| 02 |   86–171 |  86 | THE ROOFLINE |
| 03 |  172–257 |  86 | HER FACE, TRACKING IT UP |
| 04 |  258–343 |  86 | THE BLACK KITE CROSSES ABOVE |
| 05 |  344–472 | 129 | **THE LINE SNAPS TAUT — ON THE DROP** |
| 06 |  473–601 | 129 | HER KITE ROCKETS UP |
| 07 |  602–730 | 129 | THE TWO LINES CROSS |
| 08 |  731–859 | 129 | THE ROOFS ERUPT |
| 09 |  860–988 | 129 | THE BLACK KITE FALLS |
| 10 |  989–1117 | 129 | HER FACE, WON |
| 11 | 1118–1245 | 128 | THE GRANDFATHER IN THE STREET |
| 12 | 1246–1373 | 128 | HER SILHOUETTE, ONE KITE HIGH |

Expected scene cuts: `86 172 258 344 473 602 731 860 989 1118 1246`
Clips: 01–04 → 5 s (7.50). 05–12 → 6 s (9.00).

## REFERENCE PLATES
| Plate | Job ID |
|---|---|
| The girl | `42a3b965-f16f-493e-a963-3dd11b5275ff` |
| The grandfather | `ec5d66b7-73df-44ba-90f2-cd568a992f17` |
| The rooftop quarter | `4bf5d43b-044b-4981-88c8-03c7118f7e55` |
| The sky of kites | `5df9df62-4433-435f-9ae3-a7e12ff10354` |
| Her kite and spool | `ac685173-11c5-4cfd-a632-dd3a2f149b5a` |
| The black kite | `c3b13a1c-246f-43a2-95ec-169e43fc0859` |

The first grandfather attempt (`18279c69-75f6-456a-a537-8469a58b6ad7`) was a
backend failure, not charged. The replacement plate put him in a European
cobbled street; rather than spend 2.00 regenerating it, shot 11's prompt
specified the Indian lane explicitly and carried the rooftop plate as a second
reference. That fixed it completely.

## KEYFRAMES
| # | Job ID |
|---|---|
| 01 | `186039b2-2617-40a0-8ba9-f0592776f973` |
| 02 | `ab60ad8b-4cca-4a13-b482-2144723a5a8f` |
| 03 | `7286363a-d5c4-48c2-ac44-736fcc1f6a26` |
| 04 | `d2c6d675-a5aa-40ab-ae65-849b3496cb7d` |
| 05 | `7c19280e-14f9-4418-96a1-3f250b2a5ca4` |
| 06 | `d8caec3e-92e8-4c88-958f-3b18510c07fb` |
| 07 | `b87ee39e-212c-4f46-9c67-03c0c1bdcda3` |
| 08 | `69bf7a28-abce-4869-92e6-21205aac8fab` |
| 09 | `b6c451e6-7e7b-4e4a-b6b4-1210f5ac069b` |
| 10 | `920e6d65-a777-4bcb-acb2-2fa39d2290c9` |
| 11 | `f35324cd-16f4-4741-b135-49a698375baa` |
| 12 | `6136885e-e613-491d-b946-70eb46123359` |
All twelve passed visual review first time. No keyframe redos.

## LOCKED SPECS — paste VERBATIM into every prompt showing that subject

**THE GIRL** — 19 years old, South Asian, North Indian features, AN INVENTED
FICTIONAL CHARACTER, NOT any real person. Warm medium-brown skin with visible
pores. Dark brown almond eyes, thick straight black eyebrows, a straight nose,
a wide mouth, high cheekbones. Long black hair in ONE THICK BRAID pulled over
her right shoulder, loose strands at the temples, NO fringe. A faded TURQUOISE
COTTON KURTA, long sleeves pushed up above the elbows, hem to mid-thigh, worn
soft with a small mend at one shoulder. Loose OFF-WHITE COTTON TROUSERS
gathered at the ankle. BAREFOOT. A thin plain BRASS BANGLE on each wrist. The
first two fingers of BOTH hands wrapped in narrow strips of slightly grubby
WHITE COTTON TAPE. NO neck jewellery, NO earrings, NO makeup, NO nail polish.

**THE GRANDFATHER** — about 70, South Asian, North Indian features, AN INVENTED
FICTIONAL CHARACTER, NOT any real person. Warm deep brown skin with laugh lines
at the eyes and across the forehead. Neat SHORT WHITE HAIR combed back, a
trimmed WHITE MOUSTACHE and short white stubble, a broad forehead, friendly
dark eyes. Upright, square shoulders, big capable hands. A clean PLAIN WHITE
COTTON KURTA to the knee, long sleeves. Loose WHITE COTTON TROUSERS. Brown
LEATHER SANDALS. A folded GREY WOOL SHAWL over his left shoulder. HEAVY
BLACK-FRAMED GLASSES. NO jewellery, NO hat, NO stick.

**THE ROOFTOP QUARTER** — flat concrete rooftops of a dense Indian old city at
MANY DIFFERENT HEIGHTS. Parapet walls of brick and lime plaster painted FADED
TURQUOISE, OCHRE YELLOW and DUSTY PINK, chalky and patchy, plaster chipped
through to the brick, water stains under the copings. Black plastic WATER TANKS
on steel frames, iron stair-heads, short BAMBOO POLES, LOOPS OF SMALL
WARM-WHITE BULBS strung along the parapets and lit, washing lines with white
sheets, clay pots with dry plants, coiled wire. Real dust in the air. Sky deep
MAGENTA at the top shading through violet to BURNT ORANGE at the horizon, the
sun already gone.

**HER KITE** — a DIAMOND PAPER KITE about 60 cm across, thin SAFFRON ORANGE
tissue paper with a TURQUOISE BAND across the middle and a narrow white edge,
split BAMBOO SPINE and bowed cross-spar showing through the translucent paper,
a short twisted paper tail, one corner repaired with brown gummed tape.

**THE SPOOL** — a WOODEN SPOOL the length of a forearm, pale turned wood, two
round end discs, wound with THICK TWISTED OFF-WHITE COTTON LINE about 2 mm
thick with the twist clearly visible, scuffed and hand-worn.

**THE BLACK KITE** — a DIAMOND PAPER KITE about 1 metre across, MATTE BLACK
paper with a single thin WHITE BORDER line, visible bamboo spars, and a LONG
WHITE CLOTH TAIL about two metres long streaming from its lower point.

## NEW RULES EARNED ON THIS PROJECT
1. `generate_video_batch` can return `submission_failed` with a preset
   recommendation instead of a job — nine of twelve did here. Nothing is
   charged. Resubmit with
   `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`.
2. For a track whose tempo estimates disagree, fit a grid to MEASURED section
   boundaries over a long baseline. A 200 s baseline makes a 0.2 s onset error
   worth only 0.0018 s per bar. Single autocorrelation peaks were 0.6% apart
   here, which is 0.33 s of drift over 32 bars.
3. Crowds: keep every figure fifteen metres back, silhouetted, seen from behind,
   with motion blur on two of them. No readable face anywhere, no uncanny faces.
4. A character plate with the wrong background is still usable. Specify the
   environment in the shot prompt and pass the location plate as a second
   reference instead of paying to regenerate the character.

## SPEND
| Item | Credits |
|---|---|
| 6 reference plates (1 backend failure not charged) | 12.00 |
| 12 keyframes, no redos | 24.00 |
| 4 clips @ 7.50 | 30.00 |
| 8 clips @ 9.00 | 72.00 |
| **projected total** | **138.00** |
Balance at start 443.58.
