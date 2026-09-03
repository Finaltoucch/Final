> ## ⛔ DELETE IN THE HIGGSFIELD UI
>
> **Element `Snake-Vision-POV`** and its image — the infrared study containing **two
> figures**. It cannot be deleted through the tools here. Remove it in Higgsfield
> (Elements → Snake-Vision-POV → delete) so it can never be selected again.
>
> It put a second man into a one-man scene. It is not a generation input under any
> circumstances. The thermal look is described in words only.
>
> Also still pending deletion: **`Ryan-Cole`** (unarmed, `e788b2c7…`) and
> **`Diamond-Anaconda`** (30 ft, `223a47e0…`).

---

# ⛔ CHECK THIS BEFORE EVERY SINGLE SHOT

## The one that will bite you

| | |
|---|---|
| ❌ **NEVER** | `e788b2c7-0476-443f-bfdb-dd8832f85644` — Ryan-Cole (retired, **UNARMED**) |
| ✅ **ALWAYS** | `066aa34a-37fa-411b-8dcf-d356fb5bf083` — **Ryan-Cole-Armed** |

If the hero ID starts **`e788b2c7`** — STOP. Ryan will render with no rifle.
If it starts **`066aa34a`** — correct.

Delete the retired one in the Higgsfield UI when you get a moment
(Elements → Ryan-Cole → delete). It cannot be deleted from here.

---


---


---


---


---

# 🔴 SNAKE CAM — LOCKED LOOK ELEMENT

**`60de5c28-4ef2-4f54-8a60-6d06ec61ccfa` — Snake-Cam-View**

Pass it for the **treatment only** — colour mapping and camera. It is NOT a frame to
reproduce; the content changes every scene.

**Colour maps to temperature.** Cold = the world (blue, indigo, violet, cold blue-green,
to black). Hot = living bodies only (white-yellow core → orange → red edge). **An empty
shot has almost no warm colour in it.** A pack of eggs reads COLDER than its carrier —
a dark void in the middle of their burning silhouette.

**Camera:** low at the waterline · ultra-wide, slight fisheye · horizon rolled ·
swings side to side with each undulation while driving slowly forward · **nothing of
the creature ever visible** · real location, real depth · no interface, ever.

**People come from character references, never from the look element.** State the
headcount explicitly in every POV prompt.

### MODEL CHOICE, AND SEEDANCE'S CONTENT FILTER

| | seedance_2_5 | minimax_h3 |
|---|---|---|
| Camera move off a start frame | Fails — coerces `start_image` to `image_references`, goes static | Works |
| Two colour grades in one clip | **Works** when both references share the same composition | Untested |
| Generated audio | Yes, incl. dialogue | Yes — ambient and score, no dialogue |
| Max duration | 30s | 15s |
| Cost | 6.5/sec (98 for 15s) | 2/sec (30 for 15s) |

Use **minimax_h3** for travelling POV moves off a keyframe. Use **seedance_2_5** for
dialogue and for shots needing generated audio or a mid-clip grade change.

**Two grades in one seedance clip works** if you pass the same shot twice, once graded
each way, and say which governs which section. Confirmed on the cold open's second half:
thermal for 0-5s, then "the camera remains static, transitioning to natural lighting",
then the turn into the lens and the scream. It failed earlier only because the two
references disagreed about composition.

**Seedance's content filter is stricter than MiniMax's** and rejects with status `nsfw`
(credits are refunded — verify on `balance`). A shot that passes on MiniMax can bounce on
seedance purely on wording. Rejected: "blood down the left side of his face", "bloody
handprints", "absolute terror", "SCREAMS, raw and full-throated". Passed: "cave mud",
"dark handprints", "his expression changes completely", "a single shout of alarm".
The rendered picture was unchanged — blood and red handprints still appear on screen.
Describe the shot plainly; the filter reads the prompt, not the result.

### THE SNAKE-VIEW CUT — THE WORKING PATTERN

**The camera IS the creature, and the audience is looking out through her.** That single
idea governs every snake-view sequence. A shot standing off to one side watching a shadow
on the wall is a different shot entirely and breaks the effect.

The cut runs in three pieces, each its own clip:

1. **THE APPROACH — heat vision, camera travelling.** She starts far down the passage with
   the whole length between her and him, and crosses all of it. Keyframe puts him small and
   distant. 15s on minimax_h3, 30 credits.
2. **THE ARRIVAL — heat vision, camera settling.** She closes the last step and comes to
   rest right behind him.
3. **THE SWITCH — normal colour, camera LOCKED.** The viewpoint does not move; only the
   grade changes, from her heat sight to ordinary torchlight. Because the lens is still her
   face, when he turns he looks straight down it and screams INTO CAMERA. Whatever he sees
   is behind the lens and therefore never in frame. 10s on minimax_h3, 20 credits.

Confirmed working on the cold open: "Static camera... same man jerks head toward camera,
eyes wide, screaming in terror. Body recoils from wall."

**Normal-colour shots must carry the character reference** (`61201a14` for Ryan). Identity
is unreadable in heat vision and forgiving there, but in ordinary light a text-only keyframe
produces the wrong actor.

### WHAT ACTUALLY MOVES A CAMERA — LEARNED THE HARD WAY

**Prohibitions render as stillness.** Prompts built from DOES NOT move / DOES NOT walk /
NOTHING is visible / ZERO colour / NO interface produce a frozen actor AND a locked-off
camera. Three takes died this way. Every time a shot went wrong the instinct was to add
another ban, and every ban made the shot deader.

Write the shot as **action**: what the camera does, what the body does. Keep restrictions
to one short line at the end, in plain sentences, not a capitalised wall.

- Dead: "THE MAN DOES NOT MOVE. HE DOES NOT STAND. HE DOES NOT WALK. HE DOES NOT TURN."
- Alive: "His back and shoulders heave violently with every gasp. His ribs pump. His head
  sags against the rock. One hand slips on the wet stone. He kneels facing the wall,
  unaware of anything behind him."

**Model choice for POV moves.** `seedance_2_5` will not move the camera off a supplied
frame — it coerces `start_image` into `image_references` and reproduces the still. Use
**`minimax_h3`**: genuine start-frame image-to-video, 2K, and cheaper (10 credits for 5s,
30 for 15s, versus seedance's 6.5/second). Confirmed working: "the camera performs a slow,
continuous zoom-in down a dark, jagged rocky cave tunnel."

**Give the move room.** A creeping approach needs distance and time. Put the character
FAR down the passage in the keyframe — a small hot ember in the depth of the shot, with
the whole passage between — and run 15 seconds so she genuinely crosses it. A close start
has nothing to close.

**Keep identity in the keyframe.** A text-only keyframe loses the character: the 15s POV
came back with a fair-skinned man in his twenties instead of Ryan. If the face matters at
that distance, pass the character reference when generating the keyframe.

### VERIFY EVERY CLIP BEFORE SHOWING IT

The CDN is blocked from this environment, so generated media cannot be opened directly.
It can still be checked:

1. `media_import_url` the result URL back into Higgsfield — returns a `media_id`.
2. `video_analysis_create` with that `video_input_id`, then poll `video_analysis_status`.

It reports camera movement, what the subject is doing, colour and location, per scene.
This is how the static camera, the walking-away framing, the concrete tunnel and the wrong
actor were all caught. Never hand over a clip without running it.

### HOW TO SHOOT ANY SNAKE-VIEW SHOT — THE ONLY APPROVED METHOD

**Never describe a POV composition in prose and hope. Build the frame, then move the camera on it.**

1. **Generate the POV keyframe as a still image.** Text-only — pass NO heat plate as a
   reference. Describe the character's exact pose, exactly as the preceding beat left
   them, seen from whatever angle she is approaching, plus the heat colour rules.
   ~2 credits. Approve it visually before going further.
2. **Run the POV clip with that still as `start_image`.** The video is then forced to
   begin on that frame, so the composition is locked by a picture, not by wording.
   The prompt supplies ONLY the camera move: low at the waterline, weaving left-right,
   driving slowly forward, never stopping.
3. **Keep the normal-colour section as a separate clip.** Never bundle a normal
   section and a POV section into one generation — the heat reference bleeds backwards
   and the colour switch is unreliable. Cut them together in the edit.

**Why this rule exists.** Passing the heat plate as an `image_references` input makes
the model reproduce that plate's composition, and no amount of "colour sample only,
do not copy its action" in the prompt overrides it. Proven twice on cold open 1A:
the plate showed a man walking away up a tunnel, so both takes rendered Ryan walking
away — with a **static camera** — when the scene had him collapsed on his knees at the
wall. The second take said "DO NOT copy its composition, DO NOT copy its camera
position, DO NOT copy what the man in it is doing" in capitals and did it anyway.
Words lose to reference images. So supply the right image.

### THE POV IS THE SAME MOMENT, NOT A NEW SHOT

**The heat plate is a COLOUR SAMPLE. It is never content to animate.**

Whatever the man in the plate is doing is irrelevant. Say so explicitly in every POV
prompt: take the colour treatment only, ignore its composition, its camera position
and its action.

**She sees people in the exact position they are already in, at that exact moment.**
A POV shot is a cut to a different *lens on the same instant* — never a new action.
So before writing a POV prompt, answer: where is the character standing/kneeling/lying
right now, and which way are they facing? The POV must show them in that pose, from
whatever angle she is approaching, unmoved.

What went wrong on 1A: the plate showed a man walking away up a tunnel, so the POV
rendered Ryan running away — when the scene had just put him **down on his knees at
the wall with the handprints**. The plate's content overwrote the scene's staging.

**Write both of these into every POV prompt:**
1. "REFERENCE 2 is a COLOUR SAMPLE ONLY — do not copy its composition, camera or the
   action of anyone in it."
2. The character's exact pose and facing, carried over verbatim from the beat before,
   plus "he/she has not moved" and what they do NOT do (run, stand, turn around).

### WHICH PLATE TO PASS — READ THIS BEFORE EVERY POV SHOT

**Match the plate to the headcount of the shot. This is the rule that got broken.**

| The shot has… | Pass this plate | Job ID |
|---|---|---|
| **a person in it** | the WITH-FIGURE heat plate — **APPROVED** | `72546de2-2676-4c4d-8ec8-424e0bf5d825` |
| **nobody in it** | an EMPTY heat plate | `f460487a-023a-4632-ad43-ef344f371be4` · `e32ea560-9c40-4f1d-84ea-abdbae50c040` |

**WHY.** Both empty plates are cold blue tunnels with **nothing hot anywhere in them**.
Passing an empty plate on a shot that has a man in it tells the model, in pictures,
that nothing in this frame is warm — so it renders the man **cold**. That is exactly
what happened on cold open 1A: the prompt said "blazing white and yellow" and the
reference said "everything here is cold." **The reference won.**

The earlier note that said the plates are "empty of people on purpose" was written to
stop a *second* figure appearing. It over-corrected into the opposite failure. The
correct rule is the table above: **the plate must show the same number of hot bodies
the shot has** — and the identity of those bodies still comes from the character
references, with the headcount stated explicitly in the prompt.

Passing the with-figure plate **plus** Ryan's character reference **plus** "EXACTLY ONE
PERSON APPEARS IN THIS VIDEO" in the prompt is the correct payload for a one-man POV.

---

# ⛔ RETIRED — NEVER USE

**[REMOVED — two-figure look study, do not use]** is the POV **look study**. It contains **TWO
FIGURES**, because it was made to show how she views two people.

Passing it into a shot **puts those two figures into that shot.** It did exactly that
on the cold open, which has only Ryan in it — a second man appeared in the tunnel.
The prompt said "the same man" in the singular. **The reference overrode the words.
References always beat prose.**

It is a look guide for humans reading this document. It is NOT a generation input.

## How to shoot a POV shot instead

**`medias` contains ONLY the characters actually present in that scene.** Nothing else.
Cold open POV = Ryan `61201a14` and nothing more.

**Describe the thermal look in words:**

> "The entire shot is graded as thermal infrared laid over the live action: his body and
> limbs glow hot in white, orange and red; the stone, water and air read cold in deep
> blue-black. Soft and low in contrast, like heat rather than light, but the scene stays
> fully legible with real depth and real perspective. Anything cold he carries reads as a
> dark void against his heat. No interface — no crosshairs, no text, no scan lines, no HUD."

**And state the headcount explicitly:**

> "EXACTLY ONE PERSON IS VISIBLE IN THIS SHOT. No second figure. No other people anywhere
> in frame."


# 🔴 SNAKE CAM SHOTS

**It is a CAMERA MOVE, not a colour effect.** A camera rigged to the animal, so the
audience rides her. The thermal look is DESCRIBED IN WORDS in the prompt. There is no
reference image for it — the old study contained two figures and has been withdrawn.

**The move — non-negotiable:** waterline height · continuous LEFT-RIGHT SWING with each
body undulation so the horizon rocks · slow relentless forward drive that never stops or
jerks · water lapping the bottom of the lens · snout and tongue entering frame · ultra-wide
with slight fisheye. Humans get closer without ever appearing to be chased.

**The colour is ALWAYS infrared — laid OVER THE REAL SCENE.** She is looking at the
actual characters in the actual location. Ryan is recognisably Ryan; the tunnel is the
real tunnel. **Pass every character reference on a POV shot exactly as on a normal
shot.** Bodies read hot white/orange/red, stone and water cold blue-black, soft and
low-contrast, no interface. NOT abstract blobs in a void — that was a misread of the
colour study.

**Needs all three:** the weave (or it's a still picture) · the grade (or it isn't her) ·
the real people (or the audience doesn't know who she's closing on).

Four uses: cold open, flooded crossing, chokepoint, deep chamber. Full spec in the bible.

# ⚠️ ELEMENT IDs DO NOT GO IN `medias`

`medias` takes **image job ids / media ids only**. An Element id returns
`404 Media input not found`. Elements are a library concept; the generation needs the
underlying image.

| Asset | Element id | **media id — use in `medias`** |
|---|---|---|
| Ryan armed | `066aa34a…` | **`61201a14-4c4a-49aa-bbce-78e6753b4ad8`** |
| The Mother 50 ft | `88a74648…` | **`2b2a2920-35d4-4931-9dbe-7d0ee1678510`** |
| The Diamond | `e0762233…` | **`0836207e-6716-4e1c-a898-6cecdfc544b1`** |

---

# 🚨 CAST IN SHOT — HARD RULE

**Never describe a character in prompt text. If they have an Element, pass it.**

Writing "an older bald man with a grey goatee" instead of passing Marcus's reference
produces a stranger who happens to be bald. **This happened on the Scene 3 render:**
only Ryan and the location were passed, so six of the seven team members were invented
by the model.

### Ensemble scenes must be broken into coverage

A seven-hander cannot be one clip. Reference fidelity degrades as you stack faces, so
split the scene into shots of **one or two named characters each**, and pass their
actual references in every one.

**Scene 3 — the boatyard — should be shot as four clips, not one:**

| Shot | Who | References to pass |
|---|---|---|
| A — wide establisher | No faces readable. Gear on concrete, boat, shed. | boatyard plate only |
| B — Marcus & Daniel | Marcus cleans his rifle; Daniel counts the split | `152eb482` + `fe62d845` + plate |
| C — Kofi & Maya | Kofi feeds the belt; Maya packs clotting agent | `775128fd` + `ec3a91da` + plate |
| D — Ryan | "We go in, we find them, we get out." | `61201a14` + plate |

Same scene, same lines, four clips. Every face is a locked face.

### Reference media ids for prompts (NOT the element ids)

| Character | media/job id for `medias` |
|---|---|
| Ryan (armed) | `61201a14-4c4a-49aa-bbce-78e6753b4ad8` |
| Marcus Okoye | `152eb482-8403-4df9-b2a7-2b08a148c638` |
| Maya Bennett | `ec3a91da-da70-47f3-a5bf-c1fcc4acaa63` |
| Daniel Mercer | `fe62d845-c254-4f3f-8ce9-13a1c1af048e` |
| Mateo Alvarez | `ca764ab7-2ffe-4603-be92-40612517c1bb` |
| Kofi Mensah | `775128fd-a1b2-43e1-91ee-a6fa7938b03e` |
| Liam O'Rourke | `75702710-b898-4aa5-b8e7-d20afe36fe6f` |
| Armando | `e31ad326-ca34-4789-88be-6cf88571f53c` |
| The Buyer | `a09bed23-6102-48fd-aec4-fffd87663be2` |
| Elena Alvarez | `ac93b0c7-3408-4256-afe8-a5e32cdeb07d` |
| **The Mother** | `2b2a2920-35d4-4931-9dbe-7d0ee1678510` |
| The Diamond | `0836207e-6716-4e1c-a898-6cecdfc544b1` |

### Pre-flight, every shot

1. List every character visible in the shot.
2. Every one of them has their media id in `medias`. No exceptions.
3. **Also name each one's identity-critical features in the prompt** — see below.
4. If that means more than three faces — **split the shot** into coverage.
5. Creature in frame → `2b2a2920` is in `medias` too.

### 🚨 DECLARE THE LINE COUNT, OR THE PROMPT GETS SPOKEN

**Every dialogue prompt must state exactly how many lines are spoken and that nothing else
is.** Without it, two things go wrong, both proven on the riverbank scene:

1. **Stage directions get read aloud.** The trough shot's description — "a trough about two
   feet wide and six inches deep, pressed into unbroken mud" — came out of the actor's
   mouth as dialogue.
2. **Consecutive short lines by different characters merge into one.** Marcus's *"That boat
   is thirty feet."* and Ryan's *"Out of the water."* fused into *"That boat is thirty feet
   out of the water"* — which means nothing, and destroys the film's key scale beat.

The guard that works, added verbatim near the top of the prompt:

> THE SHOT CONTAINS EXACTLY TWO SPOKEN LINES AND NOTHING ELSE. Speak both slowly and
> clearly, with a pause between them. Do not add any other words.

Then give each line on its own, in quotes, attributed by name.

**Also:** spell out contractions in spoken lines. "There's charge in it" rendered as
"Hi, Odin"; "There is charge in it" rendered correctly.

**And:** when two short lines belong to different speakers, separate them with an action
beat or split them across two shots. Adjacent short lines fuse.

### 🚨 THE REFERENCE IMAGE ALWAYS WINS

**A character renders as whatever their reference image actually shows. Prompt wording
cannot override it.** Tested directly on the boatyard: the same shot was generated twice,
the second time with explicit contradicting descriptions, and the faces came back
identical both times.

| Character | Second take asked for | Rendered, both takes |
|---|---|---|
| Mateo | "warm mid-brown skin, thick dark curly hair, full dark beard" | fair skin, short reddish-brown hair, light beard |
| Daniel | "in his FORTIES, a lined weathered adult face" | late 20s |
| Marcus | "bald head, grey goatee" | bald head, grey goatee, scar near the left eye ✅ |
| Ryan | "greying afro, grey-flecked beard, nose scar" | dark skin, short beard, muscular ✅ |

Marcus and Ryan match because their reference images match their bible entries. Mateo,
Liam and Daniel do not — and getting the same face twice from two contradicting prompts
is the model obeying the picture, not ignoring the instruction.

**So the bible is the wrong source of truth for a face. The reference image is.** Before
writing a character into a shot, check what their reference actually shows; if the bible
disagrees, the bible is what needs fixing — or the character Element needs regenerating.

An earlier version of this note claimed "pass the reference AND describe the features"
was the fix. That was inferred from three clips and is disproven: description changed
nothing. Identity comes from the reference alone.

Describing a character is still worth doing in a multi-character shot — it tells the
model which reference belongs to which name and which person speaks which line — but it
will not change how anyone looks.

# 🚨 CREATURE SHOTS — HARD RULE

**If the creature appears in a shot, even as two eyes in the dark, the prompt MUST
pass her reference in `medias`:**

```
{"role": "image_references", "value": "2b2a2920-35d4-4931-9dbe-7d0ee1678510"}
```

Element: **`88a74648-e818-438f-ab04-5ba44a56cabf`** (Diamond-Anaconda-50ft) · Master image: `2b2a2920-35d4-4931-9dbe-7d0ee1678510` · Approved scale still: `ffe555d4-91fd-4a70-b9ca-7e6a6224a578`

❌ **RETIRED — do not use:** `223a47e0-bd4c-474c-8c15-1ebc2b2ed43c` (the old 30-foot element)

**This was missed on the Scene 1 render.** Only Ryan and the diamond were passed.
The creature had no reference and no size constraint, so the model invented her scale.
A locked Element does nothing if the generation never references it.

### Banned words in any creature prompt

**enormous · huge · massive · giant · colossal · towering · fills the tunnel ·
titanic · monstrous**

Every one of these invites the model to scale her up. Scene 1 used "enormous" twice.

### Required wording instead

> "A fifty-foot green anaconda, body about sixty centimetres thick at its widest —
> as thick through as a grown man's chest, half as long again as the team's thirty-foot
> boat. Pale diagonal scar on the LEFT side of the head. Never larger than fifty feet."

### Creature shot pre-flight — all four, every time

1. Creature reference `2b2a2920` is in `medias` ✅
2. The words "fifty feet" and "sixty centimetres" appear in the prompt ✅
3. No banned word anywhere in the prompt ✅
4. A known-scale object in frame — the 30-foot boat, a man, the rock walls ✅


## Approved element IDs

| Asset | ID |
|---|---|
| **RYAN COLE** (armed) | `066aa34a-37fa-411b-8dcf-d356fb5bf083` |
| MARCUS OKOYE | `2a32ebca-35a7-4e6c-8653-a318517d8482` |
| MAYA BENNETT | `f44248b6-531b-4889-946c-b4a8b166477a` |
| DANIEL MERCER | `422c12d2-5a8b-497c-a08b-97c6e54066e6` |
| MATEO ALVAREZ | `36e42750-f538-4e2f-aec7-7ae9c9f7c960` |
| KOFI MENSAH | `44880f6f-1994-40a3-b6b2-590c4fa18baa` |
| LIAM O'ROURKE | `195d7dd6-010f-4799-b56e-4c10421f4a73` |
| ARMANDO | `c471596e-2ca8-4662-b3bb-27a604605691` |
| THE BUYER | `63965603-83e0-48df-a591-716d0f919c37` |
| ELENA ALVAREZ | `53497a77-1208-4f26-aa53-3cfabbc7d686` |
| **THE MOTHER** (50 ft, 60 cm) | `88a74648-e818-438f-ab04-5ba44a56cabf` |
| ~~The Mother (30 ft, retired)~~ | ~~`223a47e0-bd4c-474c-8c15-1ebc2b2ed43c`~~ — **do not use** |
| **THE DIAMOND** (8 cm) | `e0762233-1eaa-43ab-a8d6-5c99fa8e0a0b` |

## Locations

| Location | media_id |
|---|---|
| The Island (aerial) | `9dfc7dfb-b77a-4990-a0bd-70929d38d06d` |
| Totem Creek (boat, totem) | `87fa480b-2558-44ae-ae8d-389dca65ab73` |
| The Sink Cave (all underground) | `145d207e-6e45-43d9-9ac5-749429d3ed0a` |
| The Camp | `141d6988-80c7-4882-a953-59a5ec4e6fe3` |
| Ceiba Bend (riverbank, crossing) | `7e64e65b-e7ee-491e-a099-9d0d24db6f07` |

| Generated (job ids) | |
|---|---|
| Fishing settlement, dusk | `51ece402-29dd-4ec4-86ce-c4d6344563b3` |
| Boatyard, day | `997cf577-19fe-45e1-bde5-ae94970904ba` |
| Boatyard, night | `9f76af82-f434-4a14-ad67-65aca77d1f40` |
| Suburban doorway | `7c3edeac-699e-4508-9a45-ec0d9115bbbb` |
| Ryan's room | `365d92ba-e6cf-4017-a4ae-e99157f8503f` |

---

## Five checks before you submit

1. **Hero ID is `066aa34a`**, not `e788b2c7`.
2. **Ryan's rifle is slung across his back** in every tunnel scene — never in his hands.
3. **The creature is 50 feet, 60 cm thick.** Never "enormous", never fills a tunnel.
   She is half as long again as the 30-foot boat.
4. **The diamond is 8 cm and irregular.** Never fist-sized, never a neat crystal.
5. **`generate_audio` OFF for any shot with dialogue** — otherwise the model invents a
   voice you cannot change, and the clip cannot be re-voiced later.

## Voice IDs (dialogue generated separately)

Ryan **Barrett** `d603a8cd-3fe1-55e0-9245-617a2589131e` · Marcus **Arthur**
`30fc8796-ceb6-4a66-b3a7-4a145ef7f346` · Kofi **Knox** `195e386a-cb61-5c1b-a53b-0e2f0669c408` ·
Daniel **Dylan** `b847bc29-f184-583a-8ad9-d1f1e16d1a60` · Mateo **Evan**
`f7a46aa0-183a-5327-b554-e71d8c0071bb` · Liam **Benji** `e6f9b893-51b1-51d3-afe9-9e0482cb7ac1` ·
Armando **Desmond** `563f728c-e249-5a85-97ab-8461e8c09da6` · Buyer **Cillian**
`d8ba9f14-8a24-44db-932b-99e16c45bd32` · Maya **Maeve** `64cf4f1a-61c8-5938-9aea-83d12b2e1d13` ·
Elena **Soraya** `5c1d2f7f-cdb4-5b1d-bca9-156439e3275e`
