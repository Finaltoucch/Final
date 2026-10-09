# GENESIS — THE RESTORER
ALEXATOR "001 Genesis". Vertical 9:16 AI music video.

## CONCEPT
A conservator alone on scaffolding in a half-ruined chapel, cleaning a painted
face that has been black with soot and overpaint for four hundred years. Swab
by swab a face comes back out of the dark. On the drop the work lamps strike
and the whole wall blazes into view.

MEANING: creation as recovery. Genesis is not only making something new — it
is bringing back what was almost lost, by hand, one square centimetre at a
time. The title earns the concept: a face returns to existence.

Unlike anything before it: first interior film, first about craft and patience,
first where the "character" the camera falls in love with is a painting.

## MUSIC GRID — locked
```
BPM 109.0528   beat 0.5502000 s   bar 2.2008000 s
IN    151.9157 s
DROP  158.5181 s   = IN + 3 bars   = FRAME 158
OUT   211.3373 s   = DROP + 24 bars, on the measured section end at 211.2727 s
27 bars = 59.4216 s -> 1426 frames @24fps = 59.4167 s
MD5 88f180f2eef605da9b88aa7d127a048e   full length 215.920 s
mp3 carries an attached-picture stream -> `-map 0:a:0` MANDATORY
```
LOWEST-CONFIDENCE TEMPO OF THE THREE. Methods spread 108.6-109.8. The locked
value comes from an 88-bar baseline between two strong measured onsets
(17.6020 -> 211.2727), which also made all fourteen boundary candidates land on
4-bar multiples. If a tempo re-check is ever needed, it is this film.

## FRAME PLAN — must sum to exactly 1426
| # | frames | n | beat |
|---|---|---|---|
| 01 |    0-  78 |  79 | THE SWAB (hook) |
| 02 |   79- 157 |  79 | HER EYE BEHIND THE VISOR |
| 03 |  158- 284 | 127 | **THE LAMPS STRIKE — ON THE DROP** |
| 04 |  285- 411 | 127 | THE PAINTED EYE EMERGES |
| 05 |  412- 538 | 127 | MIXING THE SOLVENT |
| 06 |  539- 665 | 127 | THE CRACK, AND THE FILL |
| 07 |  666- 792 | 127 | SHE STEPS BACK ON THE SCAFFOLD |
| 08 |  793- 919 | 127 | THE DIVIDE — HALF CLEAN, HALF BLACK |
| 09 |  920-1046 | 127 | DUST IN THE LAMP BEAM |
| 10 | 1047-1173 | 127 | HER FACE AND THE PAINTED FACE |
| 11 | 1174-1299 | 126 | THE LAST STROKE |
| 12 | 1300-1425 | 126 | LAMPS OFF — THE FACE IN DAYLIGHT |
Expected cuts: `79 158 285 412 539 666 793 920 1047 1174 1300`
Clips: shots 01-02 -> 5 s (7.50). Shots 03-12 -> 6 s (9.00).

## LOCKED SPECS — paste VERBATIM into every prompt showing that subject

**THE CONSERVATOR** — 34, Southern European, AN INVENTED FICTIONAL CHARACTER,
NOT any real person. Olive skin with visible pores and no makeup, faint
freckles across the nose, dark grey-brown eyes, straight dark brows, a long
straight nose, a wide thin mouth held closed in concentration. Dark brown hair
pulled back in a low flat bun, a few strands loose at the temple. A
PALE GREY COTTON LAB COAT, worn soft, sleeves rolled to the elbow, one chest
pocket holding three brushes. A charcoal long-sleeved shirt underneath. Dark
work trousers. Scuffed brown leather boots. On her head a BLACK MAGNIFYING
HEAD-VISOR pushed up onto her forehead when not in use, with two small round
lenses on a hinged bar. Pale blue nitrile gloves, thin, slightly stained. A
plain steel watch on the left wrist. NO jewellery, NO nail polish, NO rings.

**THE CHAPEL** — a small half-ruined stone chapel interior, cold and bare. Walls
of rough lime plaster over stone, large areas fallen away to the masonry, water
staining down from the vault, old iron tie-rods. A broken arched window high on
one side with no glass, throwing one hard shaft of pale daylight. Scaffolding
of dull aluminium poles and scuffed timber boards against the painted wall,
with a hanging work lamp on a yellow cable. On the boards: glass dishes, cotton
wool, bamboo skewers, a small jar of pigment, a sponge, a water bottle. Grit and
plaster dust underfoot. Cold blue daylight against warm tungsten lamplight. The
air is full of fine dust.

**THE FRESCO** — AN INVENTED PAINTING, NOT a copy of any existing artwork and
NOT attributable to any real artist. A larger-than-life painted face on the
plaster, seen from the chest up, androgynous and calm, eyes open and looking
slightly off to one side. Painted in earth reds, ochre, bone white and a deep
LAPIS BLUE robe. The paint surface is matt, cracked in a fine net of craquelure,
with small losses down to the plaster. MOST OF IT IS COVERED in a thick
blackish-brown layer of soot and discoloured varnish, so only the cleaned areas
show colour. The boundary between cleaned and uncleaned is a hard irregular
edge. NO lettering, NO inscription, NO halo, NO symbol of any kind.

**THE SWAB** — a small ball of white cotton wool wound onto the end of a thin
bamboo skewer, damp, rolling across the paint surface and coming away stained
dark brown. Beside it a shallow GLASS DISH of clear solvent and a row of three
used swabs, each dirtier than the last.

## REFERENCE PLATES TO GENERATE (6 x 2.00 = 12.00)
1. The conservator, full-length standing, photoreal
2. The chapel interior, empty, scaffolding in place, shaft of daylight
3. The fresco wall — half cleaned, half black
4. The swab, dish and tools on the scaffold board, macro still life
5. The work lamp on its yellow cable against the plaster (lighting reference)
6. The broken arched window with daylight (lighting reference)

## RULES CARRIED FORWARD
1. Full locked specs verbatim in every prompt. Never shorten on a rebuild.
2. Ask for A REAL PHOTOGRAPH — "shot on 35mm film, real skin texture, NOT a 3D
   render, NOT CGI, NOT ArchViz".
3. State blocking against the FRAME, not just the world.
4. `generate_image_batch` MUST carry `aspect_ratio:"9:16"`.
5. `generate_video_batch` may return `submission_failed` with a preset
   recommendation; resubmit with
   `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`.
6. CHECK BOTH SIDES OF EVERY CUT before delivering, not just end frames.
7. A light source asked for "just out of frame" gets put IN frame floating —
   say "WE DO NOT SEE THE LAMP".

## REFERENCE PLATES — GENERATED 9 Oct 2026
| Plate | Job ID |
|---|---|
| The conservator | `799e3a17-f679-4a4c-8fec-1fac91faa110` |
| The chapel, empty, scaffolding | `929b96ae-09fd-4799-84be-fa7484c07e6e` |
| The fresco, half cleaned (v2 FINAL) | `0ef264c5-2638-4916-9a71-2d9979a54095` |
| The swab, dish and tools | `7caeffc3-4136-4145-8bef-2b1f8020cbf6` |

SUPERSEDED: fresco v1 `34b7387f-2045-43ee-8d05-c6e054685f6b` came back as a
Byzantine Christ icon with a halo and a blessing gesture, despite the prompt
banning both. That is a recognisable existing artwork type and would breach the
brief's no-third-party-visual-material clause. Rebuilt as an invented secular
portrait of a young woman, cropped at the shoulders so no hands appear.

SPEC AMENDMENT: THE FRESCO is now a painted portrait of a YOUNG WOMAN -- dark
curling hair gathered back, large dark almond eyes looking slightly off to one
side, a deep LAPIS BLUE cloth over one shoulder, flat deep red-brown background.
NO halo, NO gold, NO hands, NO arms, NO symbol, NO lettering. Cropped at the
shoulders. Every later prompt must carry this wording.
