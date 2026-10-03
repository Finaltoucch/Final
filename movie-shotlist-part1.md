# THE MAID WHO STAYED — Shot List, Part 1: "The New Maid" (0:00–6:09)

Matches screenplay scenes 1–17 in `the-maid-who-stayed-movie-screenplay.md`.

## Locked settings (whole movie)

| Step | Model | Settings | Cost |
|---|---|---|---|
| Character & location images | **Nano Banana Pro** (`nano_banana_pro`) | 2k, 16:9 | 2 per image |
| First frame of each shot | **Nano Banana Pro** + attach character/location refs as `image_references` | 2k, 16:9 | 2 per image |
| Video (dialogue shots 🔊) | **Kling 3.0** (`kling3_0`) | mode **pro** (1920×1080), sound **on**, 16:9, start frame as `start_image` | **2 per second** |
| Video (silent shots 🔇) | **Kling 3.0** | mode **pro**, sound **off** | **1.5 per second** |

**Prices confirmed with Higgsfield's cost check, Oct 3 2026.** Test clip: 8s pro + sound = 16 credits.

**Add this style line to the END of every first-frame prompt:**
`Cinematic film still, shot on 35mm, shallow depth of field, natural skin texture, realistic
lighting, emotional drama, Hollywood movie quality.`

**Add this to the END of every video prompt:**
`Realistic facial acting and lip sync, natural body movement, American accents, no music,
clear dialogue.` (Silent shots: replace with `Realistic natural motion, no dialogue.`)

### Rules that save credits
1. **One speaker per shot where possible.** Kling's lip-sync is best with 1–2 short lines.
2. **Reuse frames.** When a shot continues the same angle, grab the last frame of the previous clip
   in your editor (free), upload it, and use it as the next `start_image`. Marked ♻️ below.
3. **Redo limit: 2 tries per shot.** If it still fails, simplify the prompt (fewer actions).
4. **Budget gate:** Part 1 should cost **~900–1,000 credits**. If it goes over, switch the 🔇 silent
   wide shots in later parts to `mode: std` (1.25 per second). Viewers won't notice on wides.

---

## Already made (from the test, Oct 3)

| Asset | Higgsfield job ID |
|---|---|
| `GRACE_UNIFORM` (character sheet) | `4f16fd7b-fc6b-4021-8eb8-bf24b157700f` |
| `VANESSA` (character sheet) | `60595ef4-874c-426e-a1b5-a9e854f9aad7` |
| `BEDROOM` first frame (Vanessa on bed, Grace standing) | `55cbcd89-012c-49e7-8c7d-34a687ba525d` |
| **Shot 27 video: DONE** ("Change these sheets") | `a386f0f2-bbc1-4aad-b852-396bdf91ce92` |

## Make these first (one-time, ~38 credits)

**Characters** (prompt pattern: `Character reference sheet on a plain light-gray studio background:
[DESCRIPTION]. Three views side by side: front face close-up, three-quarter view, full body
standing. Photorealistic…`)

| ID | Description |
|---|---|
| `GRACE_DRESS` | Attach `GRACE_UNIFORM` as reference. "The SAME young woman from the reference, now wearing a simple yellow sundress, holding an old brown leather handbag" |
| `ETHAN` | handsome white American man, 34, dark brown hair, short neat beard, blue eyes, tall and fit, tailored navy suit, white shirt, no tie |
| `MRS_HAYES` | Black American woman, 60, silver hair in a neat bun, pearl necklace, elegant black dress, strict but kind face |
| `GUARD` | Black American man, 40s, bald, muscular, black security suit, earpiece, friendly eyes |
| `BRADLEY` | white American man, 30, slicked-back dark hair, designer stubble, flashy gold watch, open-collar silk shirt, charming but shifty smile (resembles ETHAN as his brother) |
| `MAMA_RUTH` | Black American woman, 52, reading glasses, floral blouse, warm tired face |

**Locations** (prompt pattern: `Empty location plate, no people: [DESCRIPTION]`)

| ID | Description |
|---|---|
| `GATE` | tall black iron gate of a white-columned Southern mansion, magnolia trees, sunny morning, Belle Meade Nashville |
| `DRIVEWAY` | circular brick driveway lined with a Rolls-Royce, two Bentleys and a red Ferrari, white mansion behind |
| `LIVING_ROOM` | enormous living room, crystal chandelier, double grand staircase, black grand piano, cream sofas, marble floor |
| `KITCHEN` | huge white marble kitchen, island with stools, copper pots, big window, morning light |
| `DINING` | long glass dining table for twelve, flower centerpiece, chandelier |
| `APARTMENT` | tiny East Nashville apartment kitchen at night, small table with textbooks, warm lamp |
| `POOL_HOUSE` | glass-walled pool house at night, blue pool light, string lights |

---

## SHOTS

> Format: **#** · length · 🔊/🔇 · camera · **refs** (attach to first frame) → **FIRST FRAME** prompt → **VIDEO** prompt

### Scene 1: The gate (0:00)

**S1** · 6s · 🔇 · wide, slow push-in · refs `GRACE_DRESS` `GATE`
- **FIRST FRAME:** Wide shot from behind and to the side of the young Black woman in the yellow sundress
  from the reference, standing small in front of a giant iron gate of a white-columned mansion, clutching
  her brown handbag, sunny morning.
- **VIDEO:** Slow dolly push-in. She looks up at the sky, then at the huge house, and grips her handbag
  tighter. A bird flies past.

**S2** · 5s · 🔊 · close-up · ♻️ or refs `GRACE_DRESS` `GATE`
- **FIRST FRAME:** Close-up of her face, eyes glistening, looking up to the sky, gate blurred behind.
- **VIDEO:** She closes her eyes and whispers a prayer: "Lord, please. I need this job. Sam needs this job."

**S3** · 6s · 🔊 · medium two-shot · refs `GRACE_DRESS` `GUARD` `GATE`
- **FIRST FRAME:** The security guard from the reference walks up to the young woman at the open gate.
- **VIDEO:** The guard asks: "You Grace Miller?" She answers nervously: "Yes, sir." He nods: "Follow me."

### Scene 2: The driveway (0:17)

**S4** · 8s · 🔊 · tracking side-on · refs `GRACE_DRESS` `GUARD` `DRIVEWAY`
- **FIRST FRAME:** The young woman and the guard walking up a driveway past a Rolls-Royce, Bentleys and a
  red Ferrari; her eyes wide.
- **VIDEO:** Camera tracks alongside as they walk. She stares at the cars and mutters under her breath:
  "How many cars does one man need?"

**S5** · 8s · 🔊 · medium · ♻️
- **VIDEO:** The guard grins and says: "You're staring at the Ferrari like it owes you money." She laughs
  nervously and covers her mouth.

### Scene 3: The living room (0:33)

**S6** · 8s · 🔊 · extreme wide, high angle · refs `GRACE_DRESS` `GUARD` `LIVING_ROOM`
- **FIRST FRAME:** High wide shot: the young woman stands tiny in the middle of the enormous living room
  under the chandelier, the guard beside her.
- **VIDEO:** The guard says "Wait here," and walks away. She turns slowly in a circle, looking up, and
  whispers to herself: "This living room is bigger than the whole building I grew up in."

### Scene 4: Mrs. Hayes (0:41)

**S7** · 8s · 🔊 · medium two-shot · refs `GRACE_DRESS` `MRS_HAYES` `LIVING_ROOM`
- **FIRST FRAME:** The older woman in the black dress and pearls walks toward the young woman across the
  marble floor, unsmiling.
- **VIDEO:** The older woman says: "You must be Grace." The young woman answers: "Yes, ma'am." The older
  woman: "I'm Mrs. Hayes. I run this house."

**S8** · 10s · 🔊 · over-the-shoulder on Grace · ♻️
- **VIDEO:** Mrs. Hayes asks: "Have you cleaned a house like this before?" Grace answers earnestly: "No,
  ma'am. But I cleaned hospital rooms for two years. Nothing is dirtier than a hospital."

**S9** · 5s · 🔊 · close-up Mrs. Hayes · refs `MRS_HAYES` `LIVING_ROOM`
- **FIRST FRAME:** Close-up of the strict older woman, one eyebrow raised.
- **VIDEO:** A tiny flicker of approval crosses her face. She says dryly: "We'll see."

### Scene 5: The rules (0:59)

**S10** · 10s · 🔊 · walking, front tracking · refs `GRACE_UNIFORM` `MRS_HAYES`
- **FIRST FRAME:** Mrs. Hayes and Grace (now in her maid uniform) walking down an elegant hallway with
  flowers and paintings.
- **VIDEO:** Walking briskly, Mrs. Hayes says: "Never enter Mr. Caldwell's study. Never touch his desk. And
  never, ever argue with Miss Pierce."

**S11** · 6s · 🔊 · ♻️
- **VIDEO:** Grace asks: "Who's Miss Pierce?" Mrs. Hayes, without slowing: "You'll know her when you hear
  her."

### Scene 6: Ethan (1:15)

**S12** · 8s · 🔊 · low angle on stairs · refs `ETHAN` `MRS_HAYES` `GRACE_UNIFORM` `LIVING_ROOM`
- **FIRST FRAME:** The handsome man in the navy suit walks down the grand staircase reading his phone;
  Mrs. Hayes and Grace wait at the bottom.
- **VIDEO:** He looks up and smiles: "Good morning, Mrs. Hayes." She says: "Good morning, Mr. Caldwell.
  This is Grace. New staff."

**S13** · 6s · 🔊 · medium two-shot · refs `ETHAN` `GRACE_UNIFORM`
- **FIRST FRAME:** The man offers his hand to the young maid at the foot of the stairs.
- **VIDEO:** He says warmly: "Ethan. Welcome, Grace." She hesitates, then shakes his hand: "Thank you, sir."

**S14** · 8s · 🔊 · ♻️
- **VIDEO:** He leans toward Grace and whispers playfully: "If Mrs. Hayes gives you a hard time, you're on
  your own." Mrs. Hayes, off to the side, says flatly: "I heard that." He grins.

**S15** · 5s · 🔇 · close-up Grace · refs `GRACE_UNIFORM` `LIVING_ROOM`
- **FIRST FRAME:** Close-up of Grace looking toward the front door, a small surprised smile.
- **VIDEO:** She watches someone leave, her smile lingering, then she catches herself and looks down.

### Scene 7: Work montage (1:42) · upbeat music added in editing

**S16** · 5s · 🔇 · refs `GRACE_UNIFORM` → Grace snapping a white sheet over a big bed, slow motion.
**S17** · 5s · 🔇 · refs `GRACE_UNIFORM` `LIVING_ROOM` → Grace polishing the black grand piano, her reflection in it.
**S18** · 5s · 🔇 · refs `GRACE_UNIFORM` → Grace folding fluffy white towels into a perfect stack, sunlit laundry room.

### Scene 8: The coffee (1:57)

**S19** · 6s · 🔊 · medium · refs `ETHAN` `KITCHEN`
- **FIRST FRAME:** Early morning, the man in shirtsleeves pours black coffee at the marble island.
- **VIDEO:** He sips, flinches, burned: "Ah! Every single morning."

**S20** · 5s · 🔇 · insert close-up · refs `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Extreme close-up: a woman's hand holding one ice cube over a mug of black coffee.
- **VIDEO:** The single ice cube drops into the coffee with a tiny splash, slow motion.

**S21** · 8s · 🔊 · two-shot · refs `ETHAN` `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Grace slides the mug to the man across the island.
- **VIDEO:** She says: "Try it now." He sips and looks up, surprised: "That's… perfect. How did you know?"

**S22** · 10s · 🔊 · close-up Grace · ♻️
- **VIDEO:** She says with a gentle smile: "You've burned your tongue three mornings in a row, sir. A man who
  runs three hundred trucks can wait one minute for coffee."

**S23** · 8s · 🔊 · two-shot · ♻️
- **VIDEO:** He laughs: "Nobody in this house talks to me like that." She panics: "I'm sorry, sir—" He
  shakes his head, smiling: "No. It's refreshing."

### Scene 9: Vanessa arrives (2:34)

**S24** · 6s · 🔇 · wide · refs `VANESSA` `DRIVEWAY`
- **FIRST FRAME:** A white Range Rover in the driveway; the blonde woman in the red dress steps out in
  sunglasses holding many designer shopping bags.
- **VIDEO:** She steps out, flips her hair, lowers her sunglasses and looks around imperiously.

**S25** · 8s · 🔊 · medium · refs `VANESSA` `GRACE_UNIFORM` `DRIVEWAY`
- **FIRST FRAME:** The blonde woman holds out shopping bags toward the maid at the front steps.
- **VIDEO:** She snaps: "You! New girl! Get these upstairs. Carefully. Some of these cost more than you make
  in a year." The maid takes the bags: "Yes, ma'am."

### Scene 10: The sheets (2:48)

**S26** · 8s · 🔊 · ✅ **DONE** (test clip `a386f0f2…`): "Change these sheets." / "I changed them this
morning, ma'am." / "Did I ask for your opinion?"

**S27** · 8s · 🔊 · ♻️ from S26 last frame
- **VIDEO:** The blonde woman says coldly: "Then change them." The maid begins stripping the sheets off the
  bed.

**S28** · 8s · 🔊 · close-up Vanessa · refs `VANESSA` + `BEDROOM`
- **FIRST FRAME:** Close-up of the blonde woman on the bed scrolling her phone, smirking.
- **VIDEO:** Without looking up, she says: "People like you should be grateful to even be inside a house like
  this."

**S29** · 5s · 🔇 · insert · refs `GRACE_UNIFORM`
- **FIRST FRAME:** Close-up of a maid's hands gripping a white bed sheet.
- **VIDEO:** The hands pull the sheet tight, knuckles tense, trembling slightly.

### Scene 11: The table (3:17)

**S30** · 8s · 🔊 · medium · refs `VANESSA` `GRACE_UNIFORM` `DINING`
- **FIRST FRAME:** The maid wiping the long glass table; the blonde woman in red walks up behind her.
- **VIDEO:** The blonde drags one finger along the glass: "This is dirty." The maid: "I cleaned it five minutes
  ago, ma'am."

**S31** · 6s · 🔊 · ♻️
- **VIDEO:** The blonde holds up her finger: "Then what's this?" The maid answers quietly: "That's… your
  fingerprint, ma'am."

**S32** · 8s · 🔊 · close two-shot, push-in · ♻️
- **VIDEO:** The blonde leans in close to the maid's face and hisses: "Clean it again. Harder. And don't you
  ever forget your position in this house."

### Scene 12: Ethan walks in (3:39)

**S33** · 6s · 🔊 · medium · refs `ETHAN` `VANESSA` `GRACE_UNIFORM` `DINING`
- **FIRST FRAME:** The man in a suit enters the dining room loosening his tie; the blonde turns.
- **VIDEO:** He asks: "What's going on?" She instantly turns sweet: "Baby! She just didn't clean the table
  properly."

**S34** · 8s · 🔊 · ♻️
- **VIDEO:** He looks at the spotless table: "It looks clean to me." She grabs his arm: "You men never notice
  anything. Come see the wedding flowers." As she pulls him away, he glances back at the maid.

### Scene 13: "My pride" (3:53)

**S35** · 8s · 🔊 · two-shot · refs `ETHAN` `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Evening; the man approaches the maid alone at the kitchen sink.
- **VIDEO:** He asks gently: "Grace. What really happened in there?" She keeps washing: "It's nothing, sir."

**S36** · 10s · 🔊 · close-up Ethan · ♻️
- **VIDEO:** He says firmly: "You don't have to let anybody disrespect you because you work here. Not even her."

**S37** · 8s · 🔊 · close-up Grace · refs `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Close-up of the maid turning from the sink, eyes wet but steady.
- **VIDEO:** She says: "With respect, sir, I need this job more than I need my pride." She turns back to the sink.

### Scene 14: Mama on the phone (4:19)

**S38** · 10s · 🔊 · medium · refs `MAMA_RUTH`
- **FIRST FRAME:** The older woman in reading glasses at a cluttered kitchen table at night, phone to her ear, an inhaler box in her hand; a boy coughing on a couch behind her.
- **VIDEO:** She says into the phone, worried: "The inhaler went up again, baby. Three hundred and forty dollars."

**S39** · 6s · 🔊 · medium · refs `GRACE_UNIFORM` `APARTMENT`
- **FIRST FRAME:** The young woman, tired, at her tiny kitchen table at night, phone to her ear, textbook open.
- **VIDEO:** She says firmly: "I'll send it Friday, Mama. Every penny."

**S40** · 10s · 🔊 · ♻️
- **VIDEO:** She listens, then smiles a little: "Six months. Then I'm a licensed physical therapist, and nobody
  tells me to clean a clean table ever again."

### Scene 15: 1 a.m. (4:45)

**S41** · 8s · 🔊 · medium · refs `ETHAN` `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Night, dim kitchen; the maid studying a thick textbook at the island; the man in a T-shirt
  appears in the doorway.
- **VIDEO:** He reads the cover aloud, amused: "Neuromuscular rehabilitation. Light reading?" She slams the
  book shut, startled.

**S42** · 8s · 🔊 · two-shot · ♻️
- **VIDEO:** He sits across from her: "Relax. You're studying physical therapy?" She says: "At night. Online."
  He asks: "Why?"

**S43** · 12s · 🔊 · close-up Grace, slow push-in · refs `GRACE_UNIFORM` `KITCHEN`
- **FIRST FRAME:** Close-up of the young woman at night, soft lamp light, emotional.
- **VIDEO:** She says softly: "My daddy had a stroke when I was twelve. Nobody came to help him walk again. So I
  did. He walked me to the bus every day for six years after that."

**S44** · 6s · 🔊 · close-up Ethan · refs `ETHAN` `KITCHEN`
- **FIRST FRAME:** Close-up of the man at night, moved, looking at her.
- **VIDEO:** He says quietly: "That's the best thing anybody's told me in a year."

### Scene 16: The pool house (5:19)

**S45** · 8s · 🔇 · tracking from behind · refs `GRACE_UNIFORM` `POOL_HOUSE`
- **FIRST FRAME:** Night; the maid carries a stack of white towels along the glowing pool toward a glass pool house.
- **VIDEO:** Camera follows her as she walks toward the pool house, then she slows down.

**S46** · 6s · 🔇 · POV through glass · refs `VANESSA` `BRADLEY` `POOL_HOUSE`
- **FIRST FRAME:** Through the glass wall of the pool house at night: the blonde woman in red kissing the
  slick-haired man.
- **VIDEO:** They kiss passionately; blue pool light ripples over them.

**S47** · 5s · 🔇 · close-ups · ♻️ from S46
- **VIDEO:** A white towel falls to the ground. The blonde woman's eyes snap open and look straight at the camera.

### Scene 17: The threat (5:38)

**S48** · 8s · 🔊 · tight two-shot · refs `VANESSA` `GRACE_UNIFORM`
- **FIRST FRAME:** A dim laundry room; the blonde woman corners the maid against a dryer.
- **VIDEO:** The blonde says quietly and dangerously: "You didn't see anything." The maid stammers: "Ma'am, I—"

**S49** · 10s · 🔊 · close-up Vanessa · ♻️
- **VIDEO:** The blonde leans closer: "Your little brother's inhaler. Three hundred and forty dollars. One word to
  Ethan and you'll never work in Nashville again."

**S50** · 5s · 🔊 · close-up Grace · ♻️
- **VIDEO:** The maid nods, shaking. The blonde pats her cheek and says: "Good girl." She walks away; the maid
  exhales, terrified.

**END OF PART 1 — hard cut to black.**

---

## Part 1 cost

| | Seconds | Credits |
|---|---|---|
| 🔊 Dialogue shots (pro, sound on) | ~298s (minus S26 already done) | ~580 |
| 🔇 Silent shots (pro, sound off) | ~63s | ~95 |
| First frames (~35 new; the rest ♻️ reused for free) | | ~70 |
| One-time characters + locations | 13 images | ~26 |
| Redos (~20%) | | ~150 |
| **Part 1 total** | **~6:09** | **≈ 920** |

**Full movie projection at this rate:** ~5,900–6,100 credits, which is right at the 6,000 limit.
To keep a safety margin:
- keep redos to 20% or less, and reuse frames (♻️) everywhere you can
- use `std` (sound off) for silent wide shots in Parts 2–9, which saves ~100–150 credits
- if Part 1 costs more than ~950, buy a small top-up (500 credits) before Part 9, so the proposal
  and wedding aren't rushed
