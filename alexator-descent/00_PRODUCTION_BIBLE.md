# DESCENT — Production Bible
ALEXATOR **007 — Full Throttle** · working title **DESCENT**

## Concept
A diver gears up on a small boat alone at sea, rolls backward into deep blue
water, descends until blue turns black, switches on a torch, and finds a
sunken treasure chest half-buried in the sand. The lid opens and gold light
floods up out of the dark. No dialogue. The camera only ever travels DOWN.

Chosen because none of the 13 previous projects is aquatic, dark, or a
treasure-hunt; and because there is no vehicle, so none of the left/right
mirror geometry traps that damaged the previous project apply here.

## Music (locked — see 01_MUSIC_ANALYSIS.md)
```
BPM 138.77937     beat 0.4323409 s     bar 1.7293637 s
IN   28.469849 s        drop 38.846032 s  (= IN + 6 bars)
26 bars = 1079 frames @24fps = 44.958333 s      OUT 73.428182 s
fade in 0.600 s   ·   fade out 0.547 s from 44.411 s
MD5 9287cd6a250c823110d7d38f612ffb23
mp3 carries an attached-picture stream -> `-map 0:a:0` is MANDATORY
```
The track has a full kick drop-out immediately before the drop. That silence
is bars 4-6 and is where he takes the last breath. **The entry lands on the
drop at frame 249.**

| bars | music | film |
|---|---|---|
| 1-3  | kick running  | mask, boat, gear |
| 4-6  | kick drops out| he looks down, breathes |
| 7    | **THE DROP**  | **he hits the water** |
| 7-26 | full energy   | descent -> the chest opens |

## REFERENCE SHEETS (generated 2026-10-04, 2.00 each)
| Sheet | Job ID |
|---|---|
| Diver | `6e9b716f-66db-46a9-8626-a54df8965b82` |
| Boat  | `eba110dd-c198-497e-ac3a-c31dc8241ca6` |
| Chest | `ea2a553f-b614-467b-9271-a21ae38b6f17` |
All three 1536x2752 (9:16). nano_banana_pro.

## LOCKED SPECS — paste VERBATIM into every prompt showing that subject
Reference sheets do NOT carry these properties between shots. Only the prompt
text does. Shortening a spec on a rebuild is what caused drift on two
previous projects.

**THE DIVER** — a 32-year-old man, lean and athletically built, broad
shoulders, 1.85 m. Short dark brown hair cropped close at the sides, damp and
pushed back. Short dark stubble. Strong straight nose, defined jaw, deep-set
dark brown eyes, weathered sun-tanned skin. He wears a one-piece MATT BLACK
neoprene wetsuit, full length, completely plain — no stripes, no coloured
panels, no logos, no lettering, no numbers. Over it a MATT BLACK buoyancy
jacket with plain black webbing and dull-silver buckles. A single SILVER-GREY
ALUMINIUM CYLINDER on his back, plain bare brushed metal, no markings, black
valve. A BLACK REGULATOR with a BRUSHED CHROME mouthpiece housing, black
rubber hoses over his right shoulder and under his left arm. A LOW-VOLUME
DIVE MASK, black silicone skirt, slim brushed-chrome frame, clear glass. A
BLACK DIVE COMPUTER with a plain dark face on his LEFT wrist. A compact BLACK
DIVE TORCH with a brushed-chrome bezel. Long BLACK FINS. Plain black neoprene
gloves. He is NOT blonde, NOT fair-haired, NOT long-haired, NOT a woman, and
wears NO hood covering his face.

**THE BOAT** — a small open fishing skiff about 5 metres long, weathered and
workmanlike. The hull is WHITE, sun-faded and lightly scuffed along the
waterline. A narrow VARNISHED WOODEN GUNWALE runs along the top edge of both
sides. Plain wooden bench seats across the middle and the stern, bare pale
wooden deck, open empty interior. A small PLAIN BLACK OUTBOARD MOTOR on the
transom. A coil of pale rope in the bow. A short stainless rail at the bow.
No name on the hull, no registration numbers, no letters, no digits, no
flags, no logos, no decals anywhere on the boat or the motor.

**THE CHEST** — a heavy antique wooden sea chest about 90 cm wide with a
DOMED CURVED LID. DARK WATERLOGGED OAK, deeply grained, blackened and
softened by immersion. Four broad bands of CORRODED WROUGHT IRON wrap over
the lid and down the sides, rust-orange and pitted. A heavy IRON LOCK PLATE
at the front centre with a keyhole. Iron ring handles on both ends. The lower
third is sunk into fine PALE GREY-GOLD SAND. Crusts of WHITE BARNACLES and
knots of PALE PINK AND ORANGE CORAL over the lid and the iron bands. No
carved letters, no painted words, no numbers, no symbols, no insignia.

**THE WATER** — deep saturated blue falling off to blue-black at depth. Fine
suspended marine snow catching the light. Shafts of surface sunlight in the
upper section, a single hard torch beam in the lower section.

## Rules carried forward
1. Full specs verbatim in every prompt. Never shorten on a rebuild.
2. Never contradict yourself inside one prompt.
3. State direction against the WORLD and against the FRAME.
4. State a PATH, not just a position.
5. Two references beat three — fewer references means more weight each.
6. Camera-locked motion kills bodywork/large-object distortion.
7. Avoid collision / impact / near miss / hit — they trip the safety filter.
8. Every prompt ends with: no watermark, no logo, no text, no split screen,
   no grid, no collage, no borders.
9. NEVER assemble or deliver until every shot has been LOOKED AT as a still.
   `sandbox_exec` now returns images natively via `image_paths` — use it.
10. `generate_image_batch` MUST carry `aspect_ratio:"9:16"`.

## Spend
| Item | Credits |
|---|---|
| 3 reference sheets | 6.00 |
| **Spent so far** | **6.00** |
Balance before 31.58 -> after ~25.58.
Remaining estimate: 8-shot minimum ~92, 12-shot version ~123.
