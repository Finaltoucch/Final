# READY-TO-FIRE SHOT PLAN

Exact payloads. Paste and go — no improvising at generation time, which is where
both earlier errors came from (a missing creature reference, and six missing faces).

> ## ⚠️ ELEMENT IDs DO NOT GO IN `medias`
>
> `medias` takes **image job ids / media ids only**. Passing an Element id returns
> `404 Media input not found` and the job is rejected. Elements are a library concept;
> generations take the underlying image.
>
> | Asset | Element id (library) | **media id — USE THIS in `medias`** |
> |---|---|---|
> | Ryan armed | `066aa34a…` | **`61201a14-4c4a-49aa-bbce-78e6753b4ad8`** |
> | The Mother 50ft | `88a74648…` | **`2b2a2920-35d4-4931-9dbe-7d0ee1678510`** |
> | Snake-vision POV | `9490f7c0…` | ****[REMOVED — two-figure look study, do not use]**** |
> | The Diamond | `e0762233…` | **`0836207e-6716-4e1c-a898-6cecdfc544b1`** |

**Model spec for every video shot:** `seedance_2_5` · `mode: omni_reference` ·
`16:9` · `720p` · `generate_audio: true` · `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`

**Cost:** 6.5 credits/second. 15 s = 98 · 30 s = 195.

---

## PRIORITY 1 — THE COLD OPEN, AS TWO 15-SECOND CLIPS

Split deliberately. The rewritten cold open contains the collapse, the handprints, two
POV cuts, the stone, her arrival and the run. That is far too much for one 30-second
generation to hold together, and a failure costs the whole 195. Two halves cost the
same in total, and each half has its own chance of landing.

### 1A — "The Collapse" · 15 s · 98 credits

`medias`:
```
{"role":"image_references","value":"61201a14-4c4a-49aa-bbce-78e6753b4ad8"}   Ryan, armed
```

> Extreme photorealistic live-action cinema, 35mm, handheld, fine film grain. Underground, night. No dialogue, no speech.
>
> THE MAN: the man from the first reference, identity exact — Black, fifties, short greying afro, grey-flecked beard, scar across the bridge of the nose. Olive-green combat shirt, olive tactical trousers with knee pads, belt rig, black fingerless gloves. His AR-pattern rifle with suppressor is SLUNG ACROSS HIS BACK the entire shot, never in his hands. Filthy, soaked, blood down the left side of his face. Heavy pack on one shoulder.
>
> He is at the absolute end of himself — not running like an action hero, running like a man who has been running a very long time and has nothing left. Chest heaving, mouth open, dragging air in and not getting enough back.
>
> A tight limestone tunnel, roof low enough to touch, ankle-deep black water, constant dripping. The only light is his own handheld torch.
>
> Beat 1: he comes down the tunnel toward camera at a broken, stumbling run, torch beam jittering because his hand cannot hold still.
> Beat 2: he goes down HARD into the shallow water. Lies there. The torch rolls away and keeps burning, throwing hard light sideways across the surface.
> Beat 3: he gets a hand under himself and forces himself up. It visibly costs him everything.
> Beat 4: he reaches the wall and the beam finds HUMAN HANDPRINTS — dozens, dried black blood, smeared along the rock, all travelling one direction deeper into the mountain. He puts his forehead against the stone for one second.
> Beat 5: he lifts his head and tries to listen, and cannot hold his breathing quiet enough to hear.
> Beat 6: HARD CUT to the infrared point of view from the second reference — extremely low resolution, heavily blurred, no sharp edges, no detail, no interface of any kind. The rock is dead black and formless. He is a single blooming orange-and-white mass of heat. On his back is a hard mass of ABSOLUTE BLACK COLD, backpack sized, punched into the middle of the heat. The view does not track his face. It watches the cold. Hold three seconds.
>
> Sound: ragged panting, boots through water, dripping. Under the infrared shot, only slow heavy breathing, no score. Natural darkness, deep blacks, no fill light, no glowing eyes, no text on screen.

### 1B — "The Stone" · 15 s · 98 credits

`medias`:
```
{"role":"image_references","value":"61201a14-4c4a-49aa-bbce-78e6753b4ad8"}   Ryan, armed
{"role":"image_references","value":"0836207e-6716-4e1c-a898-6cecdfc544b1"}   The diamond, 8cm
{"role":"image_references","value":"2b2a2920-35d4-4931-9dbe-7d0ee1678510"}   The Mother, 50ft
```

> Extreme photorealistic live-action cinema, 35mm, handheld, fine film grain. Underground, night. Same tunnel, same man as before. No dialogue except one whispered line at the end.
>
> THE MAN: from the first reference, identity exact. Rifle SLUNG ACROSS HIS BACK, never in his hands. Exhausted, soaked, bleeding, hands shaking.
>
> THE STONE: from the second reference exactly — an irregular, lumpy, chipped rough diamond about eight centimetres across, filling most of his palm. NOT fist-sized, NOT a neat crystal, NOT faceted.
>
> THE ANIMAL: from the third reference exactly — pale diagonal scar on the LEFT side of the head, healed body scars, olive-green and charcoal patterning, wet scales. FIFTY FEET long, SIXTY CENTIMETRES thick at the widest, about as thick through as a grown man's chest. Real snake anatomy and correct proportions. She does not fill the tunnel.
>
> Beat 1: he turns his back on a faint distant grey smudge of daylight far down the tunnel behind him.
> Beat 2: hands shaking badly, he works the pack buckle and lifts out the rough stone. It throws hard white points of light across the tunnel; the walls are seamed with thousands of much smaller ones.
> Beat 3: he crouches and sets it down on the wet stone, carefully, almost gently, and backs away from it watching it.
> Beat 4: hold on the abandoned stone in the shallow water, glittering.
> Beat 5: from the darkness behind him, two eyes rise slowly and catch the light. They fix on the STONE ON THE GROUND, not on the man. The head and the front of the body come forward — wet olive-green and charcoal scales, sixty centimetres thick, partly lit.
> Beat 6: he whispers, almost no air left: "We were never supposed to find them." He turns and runs deeper into the mountain, away from the daylight, torch beam swinging.
>
> Sound: dripping, ragged panting, boots through water, one deep wet hiss, heavy body moving through shallow water. Natural darkness, deep blacks, no fill light, no glowing eyes, no text on screen.

---

## PRIORITY 2 — SCENE 3, THE BOATYARD, AS FOUR SHOTS

Never as one clip. The earlier single-clip attempt invented six faces.

| Shot | Sec | Cost | `medias` |
|---|---|---|---|
| **3A** wide establisher, no readable faces | 10 | 65 | `997cf577` |
| **3B** Marcus cleans his rifle, Daniel counts the split | 15 | 98 | `152eb482` + `fe62d845` + `997cf577` |
| **3C** Kofi feeds the belt, Maya packs clotting agent | 15 | 98 | `775128fd` + `ec3a91da` + `997cf577` |
| **3D** Ryan: "We go in, we find them, we get out." | 10 | 65 | `61201a14` + `997cf577` |

**Total 326 credits** — cheaper than two 30-second clips, and every face is locked.

---

## PRIORITY 3 — THE FLOODED CROSSING

The sequence that sells the film. Three clips.

| Shot | Sec | Cost | `medias` |
|---|---|---|---|
| **4A** six wading waist-deep in file, weapons up, Kofi stops | 15 | 98 | `61201a14` + `775128fd` + `7e64e65b` |
| **4B** camera lifts to straight-down aerial; she crosses their line four feet under | 20 | 130 | `2b2a2920` + `7e64e65b` |
| **4C** POV: six burning shapes, four with cold masses on their backs | 10 | 65 | `6b42ede5` |

**Total 293 credits.**

---

## BUDGET LADDER

| Package | Credits |
|---|---|
| Cold open only (1A + 1B) | **196** |
| Cold open + Scene 3 coverage | **522** |
| Cold open + Scene 3 + flooded crossing | **815** |
| Whole 12-minute film, no retakes | **~4,680** |
| Whole film, realistic 1.6× retakes | **~7,500** |

Current balance ~30. The cold open is the first 196 to spend: it is the hook, it now
carries the POV device, and nothing else in the film matters if it doesn't land.

---

## PRE-FLIGHT — RUN THIS EVERY TIME

1. Every character visible in the shot has their media id in `medias`. No one described in words.
2. Creature in frame → **`2b2a2920`** in `medias` (the IMAGE, not the element), and the words "fifty feet" and "sixty centimetres" in the prompt.
3. No banned word: enormous, huge, massive, giant, colossal, towering, titanic, monstrous.
4. POV shot → **`6b42ede5`** in `medias` (the IMAGE, not the element).
5. Hero id starts `066aa34a` / media `61201a14`. **Never `e788b2c7`.**
6. Ryan's rifle slung across his back in every tunnel shot.
7. Diamond is 8 cm and irregular.
8. `declined_preset_id` included, or the job bounces.
