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

# 🚨 CREATURE SHOTS — HARD RULE

**If the creature appears in a shot, even as two eyes in the dark, the prompt MUST
pass her reference in `medias`:**

```
{"role": "image_references", "value": "2b2a2920-35d4-4931-9dbe-7d0ee1678510"}
```

Element: `223a47e0-bd4c-474c-8c15-1ebc2b2ed43c` · Master image: `2b2a2920-35d4-4931-9dbe-7d0ee1678510`

**This was missed on the Scene 1 render.** Only Ryan and the diamond were passed.
The creature had no reference and no size constraint, so the model invented her scale.
A locked Element does nothing if the generation never references it.

### Banned words in any creature prompt

**enormous · huge · massive · giant · colossal · towering · fills the tunnel ·
titanic · monstrous**

Every one of these invites the model to scale her up. Scene 1 used "enormous" twice.

### Required wording instead

> "A thirty-foot green anaconda, body about thirty centimetres thick at its widest —
> a real animal of believable size, roughly as long as the team's boat. Pale diagonal
> scar on the LEFT side of the head. Never larger than thirty feet."

### Creature shot pre-flight — all four, every time

1. Creature reference `2b2a2920` is in `medias` ✅
2. The words "thirty feet" and "thirty centimetres" appear in the prompt ✅
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
| **THE MOTHER** (30 ft) | `223a47e0-bd4c-474c-8c15-1ebc2b2ed43c` |
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
3. **The creature is 30 feet.** Never "enormous", never fills a tunnel. Scale her
   against the 30-foot boat.
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
