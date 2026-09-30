# THE WINDING — ALEXATOR, *Awakening* (002)

**Concept.** Before dawn in a snowbound old stone town, the tower clock has stopped.
An old clock-keeper climbs the spiral stair with a lantern and winds the mechanism by
hand until the great gears catch. On the drop the bell swings, pigeons burst off the
roofs, windows light up and the sun clears the hills. The clock wakes the town.

Note: *Awakening* was also used on Project 14 (THE PASS). Re-used at client's explicit
instruction this project. Concept shares nothing with any previous film.

## Music (locked)

| Item | Value |
|---|---|
| File | `002-Awakening.mp3`, MD5 `6706a6ec2d17b0a836a3d63f8b269335`, 238.39 s, 48 kHz stereo, 320 kb/s, has attached-picture stream → `-map 0:a:0` |
| BPM, whole track | autocorr 16-beat lag 133.517 · autocorr 32-beat lag 133.480 · comb (kick, 32 multiples) 133.655 · phase-locked grid 133.599 — spread 0.13% |
| **BPM, section fit (95–150 s, kick flux, phase-locked)** | **133.420** · beat 0.449708 s · **bar 1.798831 s** |
| Bar phase | structural low-band entries at 104.77 / 119.18 / 133.53 s land on the fitted grid at 104.804 / 119.195 / 133.585 (exactly 8 and 16 bars apart) |
| **IN** | **104.804 s** (bar line, start of breakdown pads) |
| Length | 24 bars = **1036 frames @ 24 fps = 43.1667 s** |
| Structure | bars 0–8 breakdown (climb) · bar 8 kick returns (119.195) · bar 16 full drop (133.585) |
| Fades | in 0.60 s from 0 · out 0.547 s from 42.6197 s |

Audio command:
`ffmpeg -ss 104.804 -t 43.1667 -i track.mp3 -map 0:a:0 -af "afade=t=in:st=0:d=0.60,afade=t=out:st=42.6197:d=0.547" -ar 48000 -ac 2 -c:a pcm_s24le cut.wav`

## Shot list — cuts on bar lines

Cumulative cut frames: 0 86 173 259 345 432 518 604 691 777 907 1036

| # | Bars | Frames | Clip | Camera position | Shot |
|---|---|---|---|---|---|
| 01 | 0–2 | 86 | 5 s | Locked, 30 cm from the clock face, low, looking up and across it | **HOOK:** giant frosted black iron minute hand frozen on a snow-crusted stone clock face, snow blowing across it, deep blue pre-dawn |
| 02 | 2–4 | 86+1 | 5 s | High, from the tower top looking straight down its outside wall into the square | The snowbound empty square far below; one small figure with a lantern crosses toward the tower door |
| 03 | 4–6 | 86 | 5 s | Inside, at the foot of the stair, looking straight up the stone spiral | Lantern light climbing the spiral; the keeper's hand on the rope rail |
| 04 | 6–8 | 86 | 5 s | Stair above him, looking down at his face as he climbs toward camera | The keeper's face, breath fogging, lantern under his chin |
| 05 | 8–10 | 87 | 5 s | Clock room, camera at chest height beside the frame, facing the mechanism | **Kick returns.** He hangs the lantern on a hook and fits the iron crank into the winding square |
| 06 | 10–12 | 86 | 5 s | Locked to the crank, tight on his two gloved hands | Hands on the crank handle, pushing the first heavy turn |
| 07 | 12–14 | 86 | 5 s | Macro, camera locked, facing the gear train straight on | The large brass gears begin to turn slowly, ratchet pawl clicking |
| 08 | 14–16 | 87 | 5 s | Behind the translucent clock face from inside, looking out, keeper silhouetted at left | The minute hand shadow on the glass jumps forward one minute |
| 09 | 16–18 | 86 | 5 s | Belfry, below the bell, looking straight up into its mouth | **DROP.** The great bronze bell swings and strikes |
| 10 | 18–21 | 130 | 6 s | From a rooftop, looking up at the tower against the dawn | Pigeons burst off every roof and wheel round the tower; windows light up |
| 11 | 21–24 | 129 | 6 s | Outside the belfry arch, level with him, sun behind the camera | The keeper at the belfry arch, sun full on his face, the town awake below |

Cost: 4 refs 8.00 + 11 keyframes 22.00 + 9 × 7.50 + 2 × 9.00 = **115.50**.

## Locked specifications — paste VERBATIM into every prompt that shows the subject

**KEEPER:** An old man, about 70, white European, lean, slightly stooped. Short cropped
white hair, a short neat white beard, weathered ruddy cheeks, pale grey-blue eyes, deep
lines around the eyes. Long charcoal-grey heavy wool overcoat, buttoned, collar turned
up. Dark bottle-green knitted scarf wound twice around the neck. Brown leather
fingerless gloves. Dark grey flat wool cap. Dark brown leather boots. He is NOT young,
NOT bald, NOT clean-shaven, NOT wearing glasses, NOT a woman, NOT wearing a hood.

**LANTERN:** A plain black iron hurricane lantern with a clear glass chimney and a
warm orange flame, carried by a wire bail handle.

**MECHANISM:** An antique tower-clock movement in a flat-bed black-painted cast-iron
frame, with large brass spur gears, a brass escapement, a steel ratchet wheel with a
pawl, and a square iron winding arbor at waist height taking a plain black iron
crank handle. Dust on the frame, cold blue light from a slit window.

**TOWN & TOWER:** A small old European town of pale limestone buildings with
steep dark slate roofs under fresh snow, around a cobbled square. The clock tower
is square, pale limestone, with a large round white clock face with black Roman
numerals and black iron hands, and an open belfry above with one large bronze bell.
Time: deep blue pre-dawn until the drop, then warm gold sunrise.

## Prompt rules applied
- First line of every prompt = the camera position from the table.
- The man faces/moves in frame-stated directions; the crank is always turned with
  both hands, so no handedness mirror problem.
- Shot 06/07: "THE CAMERA IS LOCKED TO THE CRANK/GEAR AND STAYS STILL IN THE FRAME."
- No "strike/hit/impact" wording for the bell: use "the bell swings and rings".
  (Shot 09 description above is for humans only.)
- Every prompt ends: *no watermark, no logo, no text, no split screen, no grid, no
  collage, no borders.* Clock face numerals are the only permitted markings.
- All image calls: `aspect_ratio:"9:16"`, nano_banana_pro. All video: kling3_0,
  `mode:"pro"`, `sound:"off"`, `medias` role `start_image`.

## Status
- [x] Concept + track
- [x] Music analysed, grid locked
- [x] Shot list with camera positions
- [ ] Reference sheets (4) — **blocked: Higgsfield MCP timing out, balance unread**
- [ ] Keyframes (11) — look at each
- [ ] Clips (11) — look at each
- [ ] Build / verify / deliver
