# PAIN AND LOVE — THE AVALANCHE DOG
ALEXATOR "025 Pain and Love". Vertical 9:16 AI music video.

## CONCEPT
First light over an avalanche debris field. A handler and her search dog work
the broken snow. The dog quarters, catches scent, and on the drop drives its
head down and digs. They find someone buried — a red glove, then a bare hand
that closes around hers.

MEANING: the title, exactly. The pain is the field itself and what it means
that anyone is under it. The love is the animal that will not stop looking and
the woman who follows it. Hope is earned in the last five seconds, not given.

First film with an animal, first in snow, first rescue story.

## MUSIC GRID — locked
```
BPM 139.1062   beat 0.4313253 s   bar 1.7253011 s
IN    116.4719 s   (measured breakdown start 116.3299 s)
DROP  130.2743 s   = IN + 8 bars  = FRAME 331   (strongest onset in the track)
OUT   171.6815 s   = DROP + 24 bars
32 bars = 55.2096 s -> 1325 frames @24fps = 55.2083 s
MD5 f21408ae0fd5319f56036797af0a71ab   full length 232.743 s
mp3 carries an attached-picture stream -> `-map 0:a:0` MANDATORY
```
Tempo from a high-count onset fit: 82 inliers, 12.6 ms rms. Confirmed by both
autocorrelations (139.34 / 139.24) and the kick histogram (139.67). An earlier
section-boundary fit returned 136.23 — it had hit the edge of its own search
range and was discarded.

## FRAME PLAN — must sum to exactly 1325
| # | frames | n | beat |
|---|---|---|---|
| 01 |    0-  82 |  83 | THE NOSE IN THE SNOW (hook) |
| 02 |   83- 165 |  83 | THE DEBRIS FIELD AT FIRST LIGHT |
| 03 |  166- 248 |  83 | HER FACE, SCANNING |
| 04 |  249- 330 |  82 | THE DOG QUARTERING |
| 05 |  331- 455 | 125 | **THE DOG DIGS — ON THE DROP** |
| 06 |  456- 580 | 125 | SHE RUNS |
| 07 |  581- 704 | 124 | GLOVED HANDS CLAWING SNOW |
| 08 |  705- 828 | 124 | THE RED GLOVE EMERGES |
| 09 |  829- 952 | 124 | THE DOG'S FACE, LOCKED ON THE HOLE |
| 10 |  953-1076 | 124 | SHE REACHES DOWN |
| 11 | 1077-1200 | 124 | A HAND CLOSES AROUND HERS |
| 12 | 1201-1324 | 124 | FIRST SUN ON THE RIDGE |
Expected cuts: `83 166 249 331 456 581 705 829 953 1077 1201`
Clips: shots 01-04 -> 5 s (7.50). Shots 05-12 -> 6 s (9.00).

## LOCKED SPECS — paste VERBATIM into every prompt showing that subject

**THE HANDLER** — 31, Northern European, AN INVENTED FICTIONAL CHARACTER, NOT
any real person. Fair skin wind-burned red across the cheekbones and nose, pale
grey-blue eyes, straight light brows, a short straight nose, a firm mouth.
Dark blonde hair pulled back, mostly hidden. She wears a HIGH-VISIBILITY ORANGE
MOUNTAIN RESCUE SHELL JACKET, slightly faded, with a dark grey chest harness
over it and a coiled radio cable to one shoulder. Black softshell trousers,
black gaiters, heavy mountaineering boots. BLACK SKI GOGGLES with an amber
lens, worn pushed up on her forehead. A thin black neck gaiter pulled down
under her chin. Black gloves with worn leather palms. NO logos, NO brand marks,
NO text of any kind on any garment.

**THE DOG** — a BELGIAN MALINOIS, 4 years old, lean and muscular, short dense
coat in FAWN with a BLACK MASK across the muzzle and black-tipped guard hairs
along the back. Large upright triangular ears, dark almond eyes, a long clean
muzzle. He wears a SIMPLE ORANGE WORKING HARNESS with a padded chest plate and
a short handle loop on the back, nothing else — NO tags, NO text, NO patches.
His muzzle and chest are crusted with snow; his breath steams.

**THE DEBRIS FIELD** — the runout of a fresh avalanche at first light. Broken
blocks of hard snow the size of furniture, tumbled and tilted, with deep blue
shadow between them. Churned white debris over a wide fan, streaked grey with
dirt and shattered timber. Dark splintered conifers at the edges, some snapped
off at head height. Above and behind, a steep mountain face with the fracture
crown visible as a clean horizontal line across the white. The sky is pale
cold blue at the horizon shading to deep blue overhead, the sun not yet on the
field. Spindrift blowing low across the surface.

**THE RED GLOVE** — a single heavy ski glove in SATURATED RED with a black
reinforced palm and a short cuff, half buried, snow packed into its seams. The
only strong warm colour in the film apart from the rescue orange.

## REFERENCE PLATES TO GENERATE (6 x 2.00 = 12.00)
1. The handler, full-length standing, photoreal
2. The dog, standing in profile on snow, full body
3. The dog's head, close, with the orange harness (continuity plate)
4. The debris field, empty, first light, wide
5. The fracture crown on the face above (location plate)
6. The red glove half buried in snow, macro still life

## RISK NOTE
Animals are the hardest subject for Kling. Budget ONE extra clip re-roll here
(9.00). Shots 04, 05 and 09 are the dog-heavy ones. If a wide of the dog keeps
failing, convert it to an INSERT — nose, paws, a shoulder driving down — which
is the technique that rescued shot 05 on THE LAST GOODBYE.

## RULES CARRIED FORWARD
Same seven as the Genesis bible. In particular: check BOTH SIDES OF EVERY CUT
before delivering, and no shot may introduce a character into a space the
previous shot established as empty.

## REFERENCE PLATES — GENERATED 9 Oct 2026
| Plate | Job ID |
|---|---|
| The handler | `1d658ee2-99c3-45e7-8f9c-b6b701150560` |
| The dog, full body in profile | `1e6efb64-8524-481a-8260-1e5d9a70c3d7` |
| The dog, head close | `2defe8c9-5722-4392-b047-f6390850f947` |
| The debris field at first light | `4d77ea79-2e48-499b-b99f-f69a23eeb72a` |
| The red glove | `8653e49e-1232-480c-9c70-c57cb8bcd36b` |

SPEC AMENDMENT — THE DOG'S KIT. The two dog plates disagree: the full-body plate
gave an ORANGE WEBBING HARNESS across the chest and shoulders, the head plate
gave an ORANGE COLLAR. The HARNESS is canonical. Every keyframe prompt must say:
"a SIMPLE ORANGE WEBBING HARNESS across the chest and over the shoulders, and NO
COLLAR". The head plate stays usable as a face and fur reference only.

## KEYFRAMES — GENERATED 9 Oct 2026
| # | Job ID |
|---|---|
| 01 THE NOSE IN THE SNOW | `da53de66-ec7e-4f97-9c9b-2b289b7c87c1` |
| 02 THE DEBRIS FIELD | `8c8a00b8-5ab2-4098-a6ab-08e6a5680e12` |
| 03 HER FACE, SCANNING | `13ab3da3-cd4b-41d6-a5ea-a54aa3e57abb` |
| 04 THE DOG QUARTERING | `dd5ee46d-cf8e-4be4-8088-8c936bebbaf7` |
| 05 THE DOG DIGS (DROP) | `3e76760b-3ac2-4f28-94b8-bc4c70ae8af0` |
| 06 SHE RUNS | `146edcef-55ab-44a0-b0b3-2a7e9928a65a` |
| 07 CLAWING SNOW | `449f1def-1db4-464f-9b38-723d8c097f4c` |
| 08 THE RED GLOVE EMERGES | `8d604f3b-e4a2-4615-8c35-ced9636b59d2` |
| 09 THE DOG LOCKED ON (v2 FINAL) | `f5215224-2d8f-4b98-84e1-134747646266` |
| 10 SHE REACHES DOWN (v2 FINAL) | `7e58a324-2e4b-4c45-9aca-919ec4097ed8` |
| 11 A HAND CLOSES AROUND HERS | `a0f75b6c-12c7-4d24-a8c9-8e939acedc68` |
| 12 FIRST SUN ON THE RIDGE | `ab9f53c7-678d-42c7-9758-39996f5fd59c` |
SUPERSEDED: 09 v1 `2f33752a-a584-4073-83f0-b15fa6351ce9` put an ORANGE COLLAR on
the dog instead of the harness -- the collar leaked in from the head reference
plate. 10 v1 `766fbed5-642d-422f-8ae7-5e7b4fbe2077` had her crouching and
looking into the lens with an almost cheerful expression instead of lying prone
with her face turned down into the hole.
