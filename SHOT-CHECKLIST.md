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
3. If that means more than three faces — **split the shot**, do not describe anyone.
4. Creature in frame → `2b2a2920` is in `medias` too.


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
