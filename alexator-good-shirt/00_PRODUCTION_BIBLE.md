# THE GOOD SHIRT
ALEXATOR **010 — New Horizon** · vertical 9:16 AI music video · 10 shots

## CONCEPT
A man was laid off six weeks ago and has not told his wife. Every morning he
puts on a good shirt, kisses her goodbye and goes nowhere. On the drop she sits
down next to him on the park bench with a cup of tea, because she has known for
weeks. Register: **shame → being loved anyway.**

## WHY THIS SHAPE
Two adults, a doorway, a bus, a bench and a library. No crowds pressing on the
subject, no vehicle ever near a body, no fast motion. Every error in the last
three films came from human or animal animation under speed; this film is built
to have almost none of it.

## SUBJECTS — PASTE VERBATIM INTO EVERY PROMPT

**TOM — the man, 44.** A white British man of forty-four, pale weathered skin,
short mid-brown hair greying clearly at both temples, close-trimmed greying
stubble, heavy tired eyelids, a narrow face with high cheekbones, and a small
vertical scar through the outer end of his left eyebrow. Build: tall and
slightly stooped at the shoulders. WARDROBE, UNCHANGING: a pale blue cotton
dress shirt worn thin and slightly frayed at the collar, a plain navy tie, dark
grey trousers, black shoes, and a brown leather briefcase with one scuffed
corner. A plain gold wedding band on the fourth finger of his left hand.

**CLAIRE — his wife, 42.** A white British woman of forty-two, fair skin, dark
blonde hair to the shoulders tied back loosely, a round face, calm steady eyes,
small gold hoop earrings. WARDROBE, UNCHANGING: a mustard-yellow wrap cardigan
over a cream top. A plain gold wedding band on the fourth finger of her left
hand.

**WORLD.** A rainy northern European city in late autumn. Overcast daylight,
wet pavement, low warm interior lamps. Photoreal, 35 mm, shallow depth of field.

## SHOT PLAN — 10 shots
| # | Shot | Beat |
|---|---|---|
| 01 | EXTREME CLOSE: his hands knotting the navy tie at his throat, gold wedding band sharp, edge of a cheap mirror | **HOOK** |
| 02 | The briefcase open on the bed — inside only a folded letter and a foil-wrapped sandwich. His hand closes it | the lie |
| 03 | At the front door: she straightens his collar and puts the sandwich in his hand. Both in frame, no kiss | the leaving |
| 04 | He walks to the bus stop in the rain among commuters, indistinguishable from them | the performance |
| 05 | On the bus: the glass office building he used to work in slides across his reflection | the wound |
| 06 | The park bench. He sits, sets the briefcase down, pulls the tie off and pockets it | the truth |
| 07 | Library computer, his face lit by the screen, a column of rejections | the work |
| 08 | He eats the sandwich alone on the bench, cold hands, pigeons | the long middle |
| 09 | **DROP** — she sits down beside him and puts a paper cup of tea into his hands. He goes completely still | **the drop** |
| 10 | Wide from the side: the two of them on the bench, shoulders touching, city moving past. His shoulders come down | release |

## RULES CARRIED IN
- No kissing anywhere (client standing rule).
- No grid, no collage, anywhere.
- Locked-off camera on every insert shot (01, 02, 07) — a push makes the model
  re-draw and delete objects.
- Every shot must contain a living, breathing subject or a moving element, or
  freezedetect fires at d=0.3.
- Inspect every keyframe at NATIVE RESOLUTION before any clip is ordered.

## CASTING — client direction, 13 October 2026
All characters in this round are **white**. The client's note: Black characters
have been used a lot across the engagement and they want this set different.
Four reference plates generated before that direction arrived (the man, the
wife and both schoolgirls) were discarded and re-rolled; 4.00 credits were lost
on the two already inspected. Henry and Elsie were specified white from the
start and were not affected, and no location plate was affected.

## KEYFRAMES — generated and verified 14 October 2026
All ten inspected at native resolution 1536 × 2752.

| # | Job id | Shot |
|---|---|---|
| 01 | `282e1637-f32d-440a-acad-9892e2a7b203` | hands knotting the tie — HOOK |
| 02 | `1e50a72e-e5f4-4fa5-95f7-1a9afba06606` | the briefcase: a letter and a sandwich |
| 03 | `cc9a021c-dbfb-4820-9e9d-a928a7ec0f1a` | the doorway, she straightens his tie |
| 04 | `4b3169d9-b97c-4339-9b96-1ed3743a9930` | the commute, one of the crowd |
| 05 | `2ba90cb5-a0ea-4813-8fc7-b856d2ca3726` | the old office reflected over his face |
| 06 | `c014f905-4a1c-4294-91ea-0f4d5a29a1f6` | the bench, the tie comes off |
| 07 | `74a6c20e-2624-41bf-b83d-b2a22b50f67d` | the library screen |
| 08 | `fbed6413-649c-4557-9fac-eaa378890a81` | eating alone, bench half empty |
| 09 | `58f96310-98f7-457d-9a4e-a41b72b1030b` | **DROP** — she sits down with the tea *(v2)* |
| 10 | `aa316c44-bf16-44bd-b6d7-609395c0e8ed` | the closing wide, shoulders touching |

### SHOT 09 FAILED FIRST TIME — THE FLOATING-SUBJECT FAULT, AGAIN
The client spotted it immediately: both figures were **floating in front of the
bench**, not sitting on it. No seat surface under them, feet too far forward,
bench slats passing behind with no contact anywhere.

This is the same mechanism as the floating ring box on THE LONGEST DINNER.
**It was the camera angle, not the wording.** Shot 09 was specified as a
straight-on front two-shot, which hides the seat plane completely, so the model
had no visible surface to rest them on. Shots 06, 08 and 10 were specified as
three-quarter views, the seat plane is visible in all three, and all three
rendered correct seating first time.

The fix was to copy the geometry that already worked:
- three-quarter view from the front-left, from standing height looking slightly
  down, so **the horizontal seat slats read as a flat surface** running under
  both figures and continuing past them;
- explicit contact described — thighs flat along the slats, weight pressing on
  the wood, backs against the backrest, lower legs hanging from the front edge,
  shoes on the tarmac directly below it.

**Rule, now twice earned: a subject will float wherever the camera angle hides
the surface it is meant to rest on. Show the supporting plane, do not describe
it.** Adding the word "sitting" a second time would have changed nothing.

**Cost:** 10 keyframes + 1 re-roll = 11 × 2.00 = 22.00.
