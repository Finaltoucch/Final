> # ⛔ DO NOT USE — RETIRED ELEMENT
>
> **`e788b2c7-0476-443f-bfdb-dd8832f85644` — "Ryan-Cole" (unarmed)**
>
> This element is **retired**. Using it puts the team leader on screen **with no
> rifle**, which is what happened on the first render of Scene 1.
>
> **The only approved hero element is:**
> ## `066aa34a-37fa-411b-8dcf-d356fb5bf083` — Ryan-Cole-Armed
>
> Check the ID before every single shot. If it starts `e788b2c7`, stop.

---

# DIAMOND ANACONDA — Character & Creature Bible

Single source of truth for identity and scale. If a prompt disagrees with this
file, this file wins.

---

## THE HERO

**RYAN COLE** — team lead. The only survivor. He is the man in the cold open and
the man in the last shot.

| | |
|---|---|
| **Element** | **`066aa34a-37fa-411b-8dcf-d356fb5bf083`** — Ryan-Cole-Armed. Use this one. |
| **Reference** | Armed three-panel turnaround (front / back / close-up) supplied by the director, media `61201a14-4c4a-49aa-bbce-78e6753b4ad8`. Supersedes both the broken `664a7145` and the unarmed element. |
| **Source upload it was built from** | `28eafc20-97e2-45ef-9478-6b3494765754` |
| **Look** | Black, 50s. Short greying afro, grey-flecked beard, deep-lined face. **Scar across the bridge of the nose toward the left cheek.** Olive long-sleeve combat shirt, olive tactical trousers, knee pads, belt rig, fingerless gloves, thigh holster, worn boots. |
| **Weapon** | **AR-pattern assault rifle with suppressor and optic on a shoulder sling** — now in the reference itself. Pistol in a thigh holster on the left leg. In the tunnel scenes the rifle is slung across his back, never in his hands. |
| **Why this is the hero** | It is the only asset in your entire workspace whose prompt names him: *"He is a veteran special-operations team member and **the eventual hero of the expedition**."* Nothing else carries that tag. |

Ryan now has a dedicated turnaround rather than a job ID pulled from the cast
passes. It is the strongest identity asset in the project — front, back and
close-up on a neutral field is exactly what holds a face steady across shots.

**Age note:** he reads 50s on the plate, so the script now says 50s. Marcus stays
58 and stays bald with a grey goatee, which keeps the two of them clearly apart.

---

## THE COMBINATION — answered

You have two overlapping cast sets. Use **Set B**, the second pass:

**Set A** — six `soul_cast` characters that carry real names (Marcus Okoye, Maya
Bennett, Daniel Mercer, Mateo Alvarez, Kofi Mensah, Liam O'Rourke), each with a
weapon edit. **No Ryan.**

**Set B** — eight weapon edits built on uploaded photographs. **Contains Ryan.**
Covers every role. Generated later (17:20 vs 16:46 the same day), so it is your
more recent decision.

**Use Set B for all seven on-screen roles, and carry the Set A names across onto
those faces.** That is "the combination": *Set B faces + Set A names.*

Never mix a Set A image and a Set B image inside one shot — they are different
photographic sources and will read as two different teams standing next to each other.

---

## LOCKED ELEMENTS — the whole cast

Every character is now a saved Higgsfield Element with an enforcing description,
the same protection the creature had. Reference the Element, not a loose job ID.

| Character | Element ID |
|---|---|
| **RYAN COLE** — hero, 50s, greying afro, nose scar, **armed** | `066aa34a-37fa-411b-8dcf-d356fb5bf083` |
| ~~Ryan-Cole (unarmed, retired)~~ | ~~`e788b2c7-0476-443f-bfdb-dd8832f85644`~~ — **do not use** |
| **MARCUS OKOYE** — 58, bald, grey goatee, assault rifle | `2a32ebca-35a7-4e6c-8653-a318517d8482` |
| **MAYA BENNETT** — 30s, medic, long dark hair | `f44248b6-531b-4889-946c-b4a8b166477a` |
| **DANIEL MERCER** — 40s, the only scoped rifle | `422c12d2-5a8b-497c-a08b-97c6e54066e6` |
| **MATEO ALVAREZ** — 30s, curly hair, beard, the charges | `36e42750-f538-4e2f-aec7-7ae9c9f7c960` |
| **KOFI MENSAH** — 40s, bald, bearded, the only machine gun | `44880f6f-1994-40a3-b6b2-590c4fa18baa` |
| **LIAM O'ROURKE** — 26, youngest, the drone | `195d7dd6-010f-4799-b56e-4c10421f4a73` |
| **ARMANDO** — 75, the old man by the fire | `c471596e-2ca8-4662-b3bb-27a604605691` |
| **THE BUYER** — 60, gemstone dealer | `63965603-83e0-48df-a591-716d0f919c37` |
| **ELENA ALVAREZ** — 30s, Mateo's wife | `53497a77-1208-4f26-aa53-3cfabbc7d686` |
| **THE MOTHER** — **50 ft, 60 cm thick**, left-side head scar | `88a74648-e818-438f-ab04-5ba44a56cabf` |
| ~~The Mother (30 ft, retired)~~ | ~~`223a47e0-bd4c-474c-8c15-1ebc2b2ed43c`~~ — **do not use** |
| **THE DIAMOND** (prop) — 8 cm, irregular, brilliant | `e0762233-1eaa-43ab-a8d6-5c99fa8e0a0b` |

Two pairs are deliberately disambiguated inside their own descriptions, because
they are the confusion risk: **Marcus and Kofi are both bald and bearded** — Marcus
is older, slighter and grey-goateed with an assault rifle; Kofi is younger, much
bigger, and the only man with a belt-fed machine gun. Weapon is the fastest way an
audience tells them apart, so the weapon is written into both Elements.

Ryan's Element uses the director-supplied three-panel turnaround, and nothing else.
Media id `5edc5c76-1a09-4067-9949-af1c38ba856b`. This is the only approved image of
the hero. Do not generate replacements or variants of him.

## VOICE CASTING

Ten speaking parts, ten distinct voices, gender-matched. All Higgsfield presets —
pass `voice_id` with `voice_type: "preset"`.

| Character | Voice | voice_id | Why |
|---|---|---|---|
| **RYAN COLE** ♂ 50s | **Barrett** | `d603a8cd-3fe1-55e0-9245-617a2589131e` | Lead. Needs weight and tiredness, not heroism. He mostly gives orders and stops talking. |
| **MARCUS OKOYE** ♂ 58 | **Arthur** | `30fc8796-ceb6-4a66-b3a7-4a145ef7f346` | The oldest. Dry, unhurried, says little. |
| **KOFI MENSAH** ♂ 40s | **Knox** | `195e386a-cb61-5c1b-a53b-0e2f0669c408` | Biggest man, fewest words. Low and quiet. |
| **DANIEL MERCER** ♂ 40s | **Dylan** | `b847bc29-f184-583a-8ad9-d1f1e16d1a60` | The sceptic — talks most, and fastest. Needs to sit clearly above the older three. |
| **MATEO ALVAREZ** ♂ 30s | **Evan** | `f7a46aa0-183a-5327-b554-e71d8c0071bb` | Warm, open, talks about his kid. Dies first — the warmth has to land in one scene. |
| **LIAM O'ROURKE** ♂ 26 | **Benji** | `e6f9b893-51b1-51d3-afe9-9e0482cb7ac1` | Must read audibly youngest. |
| **ARMANDO** ♂ 75 | **Desmond** | `563f728c-e249-5a85-97ab-8461e8c09da6` | Weathered, patient, unbothered. Carries the legend. |
| **THE BUYER** ♂ 60 | **Cillian** | `d8ba9f14-8a24-44db-932b-99e16c45bd32` | Cool, precise, professional. |
| **MAYA BENNETT** ♀ 30s | **Maeve** | `64cf4f1a-61c8-5938-9aea-83d12b2e1d13` | Conscience of the film, and the sacrifice. Warm but hard-edged. |
| **ELENA ALVAREZ** ♀ 30s | **Soraya** | `5c1d2f7f-cdb4-5b1d-bca9-156439e3275e` | One scene. Must not sound like Maya — different register entirely. |

### The separation problem

Ryan, Marcus and Kofi are three older men who share scenes constantly, often in the
dark where the audience cannot see who is speaking. If those three blur, the film
becomes incomprehensible in exactly the stretch that matters most. They are cast
deliberately apart — Barrett with weight, Arthur older and drier, Knox lower and
sparser — and Dylan sits above all three so Daniel cuts through. **Audition those
four together before anything else.**

### I have not heard these

The audio CDN is blocked from my session, so these are cast on character fit, not
on sound. Every voice has a `preview_url` from `list_voices` — audition them and
swap freely. The assignments are a starting point, not a verdict.

### Voices CAN be locked — two ways

**Presets.** `generate_audio` accepts `voice_id` plus `voice_type: "preset"`. Same
id, same voice, every line, deterministic. That is what the ten above are.

**Voice Elements.** `create_voice` clones a voice from recorded or uploaded audio
and stores it as `voice_type: "element"` — the exact parallel of the character
Elements. One already exists in this workspace: `Finaltouch-`,
`f20af7a3-2416-4cb8-b394-688e71bcc43d`. Use this route to give Ryan a specific real
voice rather than a preset.

### The actual limitation

`generate_video` has **no voice parameter**. So when `seedance_2_5` runs with
`generate_audio: true` — as the existing Scene 4 render did — it improvises a voice
for that shot and there is no handle on it. The constraint is not the voice system;
it is that the video model will not accept a voice id.

**Therefore the pipeline is:** generate picture with the video model, generate every
line of dialogue separately through `generate_audio` with the locked voice ids, and
lay them together. Voices then hold across all thirty scenes as firmly as the faces
do. Decide this before the first shot, because it changes how every clip is
generated — a clip made with the model speaking cannot be re-voiced later.

## THE SEVEN

| # | Name | Role | Weapon | Set B ref (USE THIS) | Set A ref (name source) |
|---|---|---|---|---|---|
| 1 | **RYAN COLE** | Team lead. Survives. | Assault rifle | `664a7145-c7f9-44c9-a2ba-0e97da8fa7ae` | — none — |
| 2 | **MARCUS OKOYE**, 58 | Ex-SAS commander. The old soldier. Dies covering Ryan in the deep chamber. | Assault rifle | `152eb482-8403-4df9-b2a7-2b08a148c638` (bald, grey goatee) | `03b8ee6d-65cc-49f3-bf7c-3e71a15032ed` |
| 3 | **MAYA BENNETT**, 30s | Ex-MI6, medic. Conscience. Cracks the reveal. **The sacrifice.** | Assault rifle | `ec3a91da-da70-47f3-a5bf-c1fcc4acaa63` (woman, long dark hair) | `ba466663-e79e-43ec-ab0f-c3ff54e075f6` |
| 4 | **DANIEL MERCER**, 40s | Marksman. The skeptic. Found dead with the hidden stone. | Scoped DMR | `fe62d845-c254-4f3f-8ce9-13a1c1af048e` | `4ec2781a-ae60-41ed-a791-961fe44ec8f1` |
| 5 | **MATEO ALVAREZ**, 30s | Jungle specialist. Carries the charges. Family man. Taken first. | Assault rifle | `ca764ab7-2ffe-4603-be92-40612517c1bb` (curly hair, beard) | `4e3c8b35-d58e-4e9e-bbe5-90a3f3e47d9f` |
| 6 | **KOFI MENSAH**, 40s | Tracker and support gunner. Holds the chokepoint. | **Belt-fed LMG** | `775128fd-a1b2-43e1-91ee-a6fa7938b03e` (bald, beard, large build) | `50687d3b-0de8-4353-a50b-5c8feb4be9ae` |
| 7 | **LIAM O'ROURKE**, 26 | Comms and surveillance. Flies the drone. Taken in the canopy. | Compact carbine | `75702710-b898-4aa5-b8e7-d20afe36fe6f` | `7d8031ca-f141-4689-8a63-b64bcd56163e` |

**Spare / unassigned:** `b99a4c74-17f7-4c87-8854-b81b787bb18c` (beard, field operative).
Use for the 1974 expedition photographs, or drop it.

**Non-team speaking parts with no reference yet:** ARMANDO (70s, the old man by the
fire), the BUYER (60s), and MATEO'S WIFE. Three refs still to generate.

---

## THE CREATURE — locked

**Saved Element:** `Diamond-Anaconda-50ft` — **`88a74648-e818-438f-ab04-5ba44a56cabf`**
**Retired:** ~~`223a47e0-bd4c-474c-8c15-1ebc2b2ed43c`~~ (30 ft) — do not use
**Approved scale still:** `ffe555d4-91fd-4a70-b9ca-7e6a6224a578`
**Master image:** `2b2a2920-35d4-4931-9dbe-7d0ee1678510`

| Spec | Value — FIXED |
|---|---|
| Total length | **50 feet (15.2 m)** |
| Max body diameter | **60 cm** — a grown man's chest |
| Implied weight | well over a ton |
| Head scar | **Pale diagonal scar, LEFT side of head** |
| Body | Healed scars on upper body |
| Colour | Olive-green / dark emerald / charcoal; cream-green jaw and throat |
| Never | Glowing eyes. Diamonds on the body. Any size change between scenes. |

**All other snakes are different, smaller animals** — 8 to 10 feet, thick as a
forearm — and must never read as her.

### Scale ruler

The film measures her against **the team's 18-foot boat**, twice, deliberately:

- **Riverbank, night one.** A ridge of water draws level with the bow, keeps going,
  and is still going when the far end clears the stern. Marcus: *"That boat is
  eighteen feet."*
- **The drone.** Liam measures her on his screen against the bank they tied up at
  that morning: *"It's longer than the boat."*

That is the entire reveal strategy. At 30 feet you cannot sell her with spectacle —
you sell her by giving the audience something they already know the length of.

### What changed in the script because of this

The draft had her as a kaiju and that was wrong against your locked Element. Fixed
throughout: no "twenty tons," no "size of a train," no "it never shows its end."
The trough in the mud is now **a foot wide and four inches deep** — heavy, not huge.
The canopy snake is **nine feet**. In the tunnel, **a quarter of a ton** passes
Ryan at eighteen inches, and it takes a very long time.

One deliberate story addition, because real anacondas do not lay eggs — they bear
live young. Kofi says so out loud, and Maya answers:

> **KOFI:** My uncle kept them. They carry them. They give birth to them alive, in
> the water. Every one of them.
> **MAYA:** I know.
> **MAYA:** So whatever's down here with us — it isn't an anaconda.

That turns the one piece of biology that could read as a mistake into the deepest
question in the film.


---

## THE STONE — locked prop

Size and shape were drifting between fist, orange and plum. Now one spec everywhere.

| Stone | Size | Reference |
|---|---|---|
| **The eggs** — every diamond in the cave, in the packs, in Ryan's hand | **~8 cm at its widest.** Fills most of a palm, fingers still visible around it. Never fist-sized. | in hand `0836207e-6716-4e1c-a898-6cecdfc544b1` · on wet rock `0326e392-aa2d-4c16-b60d-adb0cf41cb2c` |
| **Armando's stone** | **~1 cm, a pea.** Visibly tiny on the crate. | `c8da5536-47d9-4269-8de7-5dec3fde2f3f` |

**Shape — irregular, not crystalline.** Asymmetric, knobbly, unbalanced. Broken and
chipped edges, one side sheared off blunt, shallow pits and gouges. It sits at an
awkward angle because no face is flat. Never a symmetrical octahedron, never a cut or
faceted jewellery gemstone. With the shine covered it would look like an ordinary
broken rock.

**Finish — brilliant.** Patches of naturally glassy material throw hard white
speculars and deep internal reflections, prismatic fire flashes blue and gold through
the body, and caustic light spills onto whatever it is resting on, so the stone lights
its surroundings. Frosted greasy matte areas between the glassy patches.

The ugly shape fighting the brilliance is the effect. A neat crystal reads as a prop;
a lumpy rock that throws light like that reads as something nobody carved.

**Faint concentric layering sits deep beneath the surface in all of them.** That is the
egg seeded in plain sight, so when Maya says *"It grew in rings, like a tree"* she is
pointing at something the audience has been looking at since the opening scene.

**Why this size.** A rough diamond the size of a fist is a once-in-a-century object and
reads as fantasy. Eight centimetres is still extraordinary and still believed. And the
gap between Armando's pea and what is underground is what makes *"That is the smallest
one"* land.

## RYAN'S RIFLE — standing rule

**Resolved.** The armed turnaround now carries the rifle, so the Element enforces it
rather than each prompt having to remember. The unarmed element is retired — using it
is what sent the team leader into the cave with no weapon on the first render of Scene 1.

He carries it **slung across his back, never in his hands.** Through the cold open, and
again when the film returns to that tunnel at the end. He has carried that weapon
through everything and it has never once been any use to him.

This is deliberate, not a costume note. Marcus dies firing at her. Ryan survives by
putting a stone down. The weapon being visibly useless is the argument the film makes.


---

## CREATURE SCALE — WHAT WENT WRONG ON SCENE 1

The Element fixes her at 30 feet. The Scene 1 render still produced an oversized
creature. The cause was not the Element and not the model:

**The generation never referenced her.** `medias` carried Ryan's turnaround and the
diamond only. Her master image `2b2a2920` was not passed, so nothing tied the shot to
the locked spec — and the prompt text said "two enormous reptilian eyes", which is the
one word the scale rules forbid.

**A locked Element constrains nothing unless the generation passes it.** That is the
whole lesson. From here, every shot in which she appears — including shots where only
her eyes are visible — must pass `2b2a2920-35d4-4931-9dbe-7d0ee1678510` in `medias`
and must state "thirty feet" and "thirty centimetres thick" in the prompt text.

See SHOT-CHECKLIST.md for the pre-flight.

---

## SNAKE VISION — her POV

### The biology it's built on

Boids sense infrared through **labial pit organs**. Unlike an eye, a pit organ has
**no lens** — heat blooms through a bare aperture onto a membrane. The resolution is
genuinely terrible. She does not see a picture. She senses a smear of warmth with no
edges and no detail.

**So this is NOT Predator.** Predator's POV is crisp, high-resolution false colour with
targeting graphics. Hers is the opposite, and it should be more disturbing for it:
blurred, formless, no outlines, no readout, no interface. It looks like being seen by
something that does not have eyes.

### Locked look

| | |
|---|---|
| Resolution | **Very low.** Heavy blur. No sharp edges anywhere. No fine detail. |
| Warm bodies | Blooming **orange → white** at the core, falling off to red at the margins. Soft-edged masses, not silhouettes. Faces do not read. |
| Cold rock, water, air | **Dead black.** Formless. The cave has no geometry in her view. |
| Interface | **None.** No crosshairs, no text, no scan lines, no HUD. |
| Movement | Slow, heavy, low to the ground. She does not dart. |
| Sound | Her breathing only. No score. All the world's sound drops away. |

### THE RULE THAT MAKES IT MEAN SOMETHING

**The diamonds are cold. She cannot see them as objects — she sees the hole they make.**

A man carrying eggs reads as a burning orange body with a **dead-black cold mass on
his back**. That is how she picks her targets out of a group. It is also why she goes
past men who are not carrying, and why Maya survives long enough to say so.

In the cold open, when Ryan sets the stone down, her POV shows the cold mass **separate
from the man, alone on the floor.** The shot explains why her eyes go to the stone
instead of to him — before the audience has consciously worked it out.

### Where it fires — and where it must not

Use it **four times in the whole film.** It stops working the moment it is decoration.

| Scene | Length | What it shows |
|---|---|---|
| **Cold open** | 2 × ~3 s | The cold mass on Ryan's back; then the same mass alone on the floor after he sets it down. |
| **Flooded crossing** | ~3 s | Six burning shapes wading in file. Four have cold masses on their backs. She passes between them anyway — she is not hunting yet. |
| **The chokepoint** | ~2 s | Kofi burning white-hot from the machine gun barrel, muzzle flash blowing the whole frame out. The only time her view is overwhelmed. |
| **Deep chamber** | ~3 s | The clutch on the floor as a field of cold. Ryan's pack the same cold. **She cannot tell the difference** — which is exactly why she comes for him. |

**Never** use it for a jump scare, never during dialogue, and never when she is merely
present. It fires only when she has already decided to move, so the cut itself becomes
the threat signal.

### Prompt wording for generation

> "Extreme low-resolution infrared thermal point-of-view, as seen through a snake's pit
> organ — heavily blurred, no sharp edges, no fine detail, no outlines. Warm human bodies
> bloom orange and white against dead black cold rock and water. No interface, no
> crosshairs, no text, no scan lines, no HUD. Slow, heavy, low to the ground."

Add for shots with eggs in frame:

> "The stone the man carries is COLD — it appears as an absolute black void against his
> burning body."
