# DIAMOND ANACONDA — Higgsfield Asset Map

Everything below is already generated in your Higgsfield workspace. IDs are passed
to `generate_video` as `medias[].value` — never as URLs.

---

## 1. Creature — master reference

| Asset | ID |
|---|---|
| **The Mother** — 2,000-year-old anaconda, canonical | `2b2a2920-35d4-4931-9dbe-7d0ee1678510` |

Locked identifying marks, which must appear in every creature shot: **pale diagonal
scar across the LEFT side of the head**, several healed scars along the upper body,
cream-green markings around jaw and throat, wet scale texture, no glowing eyes, no
diamonds attached to the body.

The script now uses that scar as a story beat — in the deep chamber the torchlight
runs down her length and finds it, which is the audience's confirmation that this is
the same animal from every previous glimpse.

---

## 2. Cast

**You have two character sets, and only one of them carries names.** The script is
written against the named set, because the names are what drive the dialogue.

### Named set — `soul_cast` base + weapon edit (use these)

| Character | Role in script | Base ref | With weapon |
|---|---|---|---|
| **Marcus Okoye** — ex-SAS commander | The old soldier. Warns Ryan. Dies covering him. | `5a086372-3750-4f21-a9af-5516b39cffa1` | `03b8ee6d-65cc-49f3-bf7c-3e71a15032ed` |
| **Maya Bennett** — ex-MI6, medic | Conscience. Cracks the egg reveal. The sacrifice. | `690dfe17-95c7-4ac3-a5a5-fcb0b1985f45` | `ba466663-e79e-43ec-ab0f-c3ff54e075f6` |
| **Daniel Mercer** — ex-SF marksman | The skeptic. Found dead with the hidden stone. | `7c60c2d9-e006-48ff-b9b0-efdff074a86b` | `4ec2781a-ae60-41ed-a791-961fe44ec8f1` |
| **Mateo Alvarez** — ex-park ranger | Family man. Carries the charges. Taken first. | `47d02e63-1fec-4975-a59e-c62f4c0460cd` | `4e3c8b35-d58e-4e9e-bbe5-90a3f3e47d9f` |
| **Kofi Mensah** — ex-SAS tracker | Reads the ground. Holds the chokepoint with the LMG. | `242b839e-bb18-469c-9cd2-176ce5f806d0` | `50687d3b-0de8-4353-a50b-5c8feb4be9ae` |
| **Liam O'Rourke** — ex-Navy diver, comms | The lens. Flies the drone. Taken in the canopy. | `25d95898-9fe4-4484-94f4-302a39621a94` | `7d8031ca-f141-4689-8a63-b64bcd56163e` |

### Unnamed set — second casting pass, weapon edits on uploads

| Description | ID | Reads as |
|---|---|---|
| Facial scar, beard, muscular — *"eventual hero of the expedition"* | `664a7145-c7f9-44c9-a2ba-0e97da8fa7ae` | **Ryan** |
| Bald, grey goatee, older | `152eb482-8403-4df9-b2a7-2b08a148c638` | Marcus |
| Woman, long dark hair, tactical | `ec3a91da-da70-47f3-a5bf-c1fcc4acaa63` | Maya |
| Scoped designated-marksman rifle | `fe62d845-c254-4f3f-8ce9-13a1c1af048e` | Daniel |
| Curly hair, beard, jungle specialist | `ca764ab7-2ffe-4603-be92-40612517c1bb` | Mateo |
| Bald, beard, large build, belt-fed LMG | `775128fd-a1b2-43e1-91ee-a6fa7938b03e` | Kofi |
| Assault rifle, generic | `75702710-b898-4aa5-b8e7-d20afe36fe6f` | spare |
| Beard, field operative | `b99a4c74-17f7-4c87-8854-b81b787bb18c` | spare |

**Ryan only exists in the unnamed set** (`664a7145`) — he has no `soul_cast` entry.
So the practical cast is: `664a7145` for Ryan, plus the six named weapon refs above.
Worth confirming that's the combination you want before any batch run, because
mixing the two sets in one shot will produce two different-looking teams.

---

## 3. Locations — the five locked references

These are the only five. Uploaded as media inputs; pass the `media_id`, not a URL.

| # | Location | media_id | Original | Scenes |
|---|---|---|---|---|
| 1 | **The Island** — aerial, mangrove channels cutting inland | `9dfc7dfb-b77a-4990-a0bd-70929d38d06d` | Pulau Bakau | The approach. The reveal of where they're going. |
| 2 | **Totem Creek** — the covered launch, mist, carved totem on the bank | `87fa480b-2558-44ae-ae8d-389dca65ab73` | Igarapé do Totem | Arrival. Engine dies. The shed skins. **The boat here is the film's scale ruler — thirty feet.** |
| 3 | **The Sink Cave** — diamonds seamed in the wall, torches, snakes in the foreground | `145d207e-6e45-43d9-9ac5-749429d3ed0a` | Blackwater Sink Cave | The descent, the diamond walls, the carvings, the deep chamber, the cold-open tunnel. All underground work. |
| 4 | **The Camp** — tarps, rusted crates, overturned boat, snakes lying in the open | `141d6988-80c7-4882-a953-59a5ec4e6fe3` | Pântano do Jacaré | The abandoned settlement, the radio, and the 1974 camp. |
| 5 | **Ceiba Bend** — dawn mist, buttress-rooted tree mid-channel, dark water | `7e64e65b-e7ee-491e-a099-9d0d24db6f07` | Curva da Ceiba | The riverbank where Mateo is taken, and **the flooded crossing**. |

### What the references already give you

Three things are in these frames already, so don't write or generate them twice:

- **The totem** (2). A carved warning marker on the bank. The team motors past it
  without comment on the way in. It costs nothing and it pays when they learn the
  island has been marked by people for centuries.
- **Diamonds already in the wall** (3). The cavern reveal doesn't need a separate
  discovery beat — the lights land and they're simply there.
- **Snakes in the open, in daylight** (4). The camp is already occupied. The team
  doesn't find an empty ruin and then get ambushed; they walk into a place that is
  visibly not theirs. Play it that way.

### One reference, twelve underground scenes — the depth ladder

Reference 3 carries the entire second half. The script now stamps every
underground scene with a bracketed DEPTH note giving its water level, light
source and roof height. Follow them literally and the same reference yields
twelve different places; ignore them and the descent stops reading as a descent.

| Depth | Scene | Water | Light |
|---|---|---|---|
| 2 | First cavern | Dry | Torch, not reaching the far wall |
| 3 | Carving chamber | Dry | Torch close on stone, roof at head height |
| 4 | Side passage | Damp | A seam, not a room |
| 5 | Cavern camp | Flat standing pools | **Chemical lamp** — green-white, unmoving |
| 6 | Passages / hatchlings | Ankle-deep, running | Swinging torch and muzzle flash |
| 7 | Lower passage | Knee-deep and rising | Roof coming down to the water |
| 8 | Sluice gate | Waist-deep, moving fast | Rotted timber. Loudest place in the film |
| 9 | Climbing passage | Climbing clear of it | Running walls, flood dropping away below |
| 10 | **Deep chamber** | Dry | **Lights itself.** Diamond-scatter. Kill the torches |
| 11 | The tunnel (cold open, and its resolve) | Ankle-deep, still | One failing torch. Handprints |

Depth 10 is the only room in the film that is beautiful, and the only one not lit
by the team. That contrast is the whole point of the location.

### Locations still needed — three, not five

Consolidated down from five so you generate less: the boathouse and the dock are
now one **BOATYARD** (day and night), and the dealer's office has been moved into
**RYAN'S ROOM** — the buyer comes to him, which is also better, since Ryan never
has to carry the stones out in public.

1. **Boatyard** — working dock, gear on concrete, day and night
2. **Suburban doorway** — screen door, hot street, a kid's bicycle in the hallway
3. **Ryan's room** — bare rented room, one table (buyer scene by day, final shot at night)

## 4. Already rendered

| Shot | ID | Spec |
|---|---|---|
| Scene 4 — boat approach, engine dies, skins | `9b247dff-d889-45da-892f-a2e414e633fc` | `seedance_2_5`, 16:9, 30s, 720p, audio on |

The screenplay has been **conformed to this clip** so it stays canon: Marcus now says
*"Where did everything go?"* and Ryan answers *"We're not alone."* — the exact lines
in the render. Don't regenerate it.

---

## 5. Generation spec

Match what already worked on Scene 4:

- Model `seedance_2_5`, `aspect_ratio: "16:9"`, `duration: 30`, `generate_audio: true`
- Pass the **location ref** and the **character refs actually in that shot** — not all
  seven. Beyond about three identity references per shot, likeness starts to drift.
- Creature shots: always pass `2b2a2920` and restate the left-side head scar in the
  prompt text. The reference alone doesn't reliably hold it.
- Use `generate_video_batch` (up to 12 jobs) → `jobs_wait` → one `show_generation_by_ids`.

**Reveal schedule — the one rule worth protecting:** no full-body creature shot until
the drone sequence, and that one is degraded, wide, four seconds, never showing her
end. The first clean look at her is the deep chamber. Everything before that is
water displacement, a trough in the mud, a shape passing, and the sound of something
heavy changing direction.

Budget note: 1,042 credits at your current plan. Test 2–3 shots — the sinkhole
descent, one creature glimpse, one dialogue two-hander — and check likeness holds
across a scene cut before committing to a full run.
