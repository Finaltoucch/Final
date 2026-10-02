# THE HOUSEKEEPER WHO STAYED — Movie Shot List (Part 1 of 5)

**Covers:** Character bible, locations, Cold Open, Act 1 (≈ 0:00–6:15)
**Format:** Full-motion AI movie. Every shot is a video clip with actors moving, acting, and
speaking. A narrator appears only in short voice-over lines over moving shots, never over
still pictures.
**Pipeline per shot:**
1. **START FRAME:** Nano Banana Pro (2 credits), 16:9, 2k, with the listed character and
   location references attached as `image_references`
2. **VIDEO:** Kling 3.0 (`kling3_0`), 16:9, `std`, with the start frame as `start_image`.
   Sound **ON** only for shots with dialogue (marked 🔊). All others are 🔇 (sound off, cheaper).
3. **VOICE-OVER (VO):** generated separately with one locked narrator voice and laid over
   the clip in the editor.

**Part 1 budget:** 38 shots · ~355 seconds of video · ≈ 530 video credits + 76 start-frame
credits + ~150 for redos ≈ **~760 credits**

---

## 1. CHARACTER BIBLE (generate these FIRST, about 80 credits total)

Generate each as a **character sheet**: front face, three-quarter view, and full body, on a
neutral gray background, photoreal cinematic. Then attach it to every shot that character
is in. **Copy the description word for word into every prompt that features them.**

| ID | Character | Locked description (paste exactly) |
|---|---|---|
| `GRACE_2006` | Grace, age 37 | African-American woman, 37, warm brown skin, kind tired eyes, short natural hair under a navy headscarf, slim, faded denim jacket, small gold cross necklace |
| `GRACE` | Grace, age 56 | African-American woman, 56, warm brown skin, kind tired eyes with smile lines, short natural graying hair, small gold cross necklace, faded blue cardigan over a white housekeeper's blouse |
| `THOMAS` | Thomas, age 64 | white American man, 64, silver hair combed back, strong jaw, light stubble, blue eyes, broad shoulders, flannel or navy sweater, plain gold watch |
| `THOMAS_SICK` | Thomas after the stroke | same man as THOMAS, thinner, pale, right side of his face slightly drooping, gray hospital pajamas |
| `MARGARET` | Margaret, age 55 | white American woman, 55, auburn hair in a loose bun, freckles, kind green eyes, linen shirt, gardening gloves |
| `VANESSA` | Vanessa, age 41 | white American woman, 41, platinum blonde blowout, sharp cheekbones, heavy lashes, red lipstick, designer white or black outfits, diamond tennis bracelet |
| `BRADLEY` | Bradley, age 34 | white American man, 34, slicked dark hair, designer stubble, puffy tired eyes, open-collar shirt, flashy watch |
| `HAROLD` | Harold, age 70 | Black American man, 70, white short beard, round gold glasses, gray three-piece suit, leather briefcase |
| `DENISE` | Denise, age 38 | Latina woman, 38, dark hair in a ponytail, navy nurse scrubs, ID badge |
| `LILY` / `SAM` | Lily, 31, and Sam, 7 | Lily: African-American woman, 31, braids, tired eyes, hoodie. Sam: African-American boy, 7, curly hair, dinosaur T-shirt |

> **Casting note:** Grace is written as African-American to give strong visual contrast in
> the thumbnails and scenes. Change any description to whatever fits your audience, but lock
> it before generating anything.

## 2. LOCATIONS (generate once and reuse, about 40 credits)

| ID | Location | Description |
|---|---|---|
| `MANSION_EXT` | Caldwell mansion | white-columned Southern mansion, magnolia trees, circular brick driveway, Belle Meade, Nashville |
| `KITCHEN` | Mansion kitchen | huge white marble kitchen, copper pots, big farmhouse window, warm morning light |
| `STORAGE` | The storage room | cramped storage room by a laundry, rented hospital bed, boxes of Christmas decorations in the corner, one small window |
| `STUDY` | Thomas's study | dark wood study, leather chairs, desk lamp, framed photos of trucks |
| `FOYER` | Foyer | grand white marble foyer, double staircase, chandelier |
| `LAW_OFFICE` | Harold's office | wood-paneled law office, long table, bookshelves, tall windows |
| `HOSPITAL` | Vanderbilt hospital | hospital hallway at night, vending machine glow, empty chairs |
| `APARTMENT` | Grace's apartment | tiny East Nashville apartment, small kitchen table, worn couch, rosary on the wall |
| `REHAB` | Rehab center | bright rehab gym with parallel bars, and a garden with string lights |
| `PORCH` | Grace's new house | small white house, porch with rocking chairs, flower garden |

**Global style line (add to EVERY prompt):**
`cinematic film still, shot on 35mm, shallow depth of field, natural skin texture, realistic
lighting, emotional drama, Hollywood movie quality, 16:9`

**Color grade:** warm golden tones for Grace and Thomas scenes, cold blue-gray for Vanessa and
Bradley scenes.

---

## 3. COLD OPEN — THE WILL READING (0:00–1:20) · 8 shots

**S1** · 10s · 🔇 · Wide establishing, slow push-in
- **Action:** Wide shot of LAW_OFFICE. The Caldwell family sits at a long table in designer
  black. VANESSA checks her nails, BRADLEY bounces his knee. Far back by the door, GRACE stands
  alone clutching her purse.
- **VO:** "Everyone in that room was waiting to hear how many millions they'd get."
- **Start frame:** `[LAW_OFFICE] [VANESSA] [BRADLEY] [GRACE]` wide shot of a wood-paneled law
  office, glamorous blonde woman and slick-haired man seated at a long table in black designer
  clothes, smiling; in the far background by the door an older Black woman in a faded blue
  cardigan stands alone clutching her purse + style line
- **Video prompt:** slow dolly push-in down the length of the table, the blonde woman admires
  her nails, the man nervously bounces his knee, the woman by the door shifts her weight
  uncomfortably, subtle realistic motion

**S2** · 5s · 🔇 · Close-up
- **Action:** VANESSA scrolls Palm Beach mansion listings on her phone, smirking.
- **VO:** "The wife was already picking out a new house in Palm Beach."
- **Video prompt:** close-up of manicured fingers scrolling luxury beach-house photos on a
  phone, red lips curling into a smile

**S3** · 5s · 🔇 · Close-up
- **Action:** BRADLEY's phone lights up: *RICK: FRIDAY. OR ELSE.* He flips it face-down, sweating.
- **VO:** "The son had promised a very dangerous man his money by Friday."
- **Video prompt:** phone screen lights up on a table with a threatening text, a man's hand
  quickly flips it face-down, he wipes sweat from his lip

**S4** · 10s · 🔇 · Slow push-in on Grace
- **Action:** GRACE alone by the door. Nobody offers her a chair. She grips her purse strap.
- **VO:** "And by the door stood Grace Miller, the housekeeper. Five months earlier, this family
  had called the police on her."
- **Video prompt:** slow push-in on an older Black woman by a doorway, eyes lowered, fingers
  tightening on her purse strap, she swallows nervously, soft window light on her face

**S5** · 10s · 🔊 · Medium
- **Action:** HAROLD sits, adjusts his glasses, and unfolds the will.
- **Dialogue:** HAROLD: "Thank you all for coming. Let's begin."
- **Video prompt:** elderly Black lawyer with gold glasses unfolds a document, adjusts his
  glasses, looks up at the table and speaks calmly

**S6** · 5s · 🔇 · Quick cuts on reactions
- **Action:** Vanessa leans forward and Bradley holds his breath.
- **Video prompt:** blonde woman and dark-haired man lean forward eagerly toward the camera,
  hungry anticipation

**S7** · 10s · 🔊 · Close-up on Harold, then whip-pan
- **Dialogue:** HAROLD: "The first beneficiary… Mrs. Grace Miller."
- **Action:** Whip-pan from Harold to Grace's stunned face, then to Vanessa's smile freezing.
- **SFX:** Hard silence, then a single piano note.
- **Video prompt:** lawyer reads a name aloud, camera whip-pans across the room to a stunned
  older woman by the door, then to the blonde woman's smile freezing in shock

**S8** · 10s · 🔇 · Fade to black, then title
- **VO:** "To understand how it came to that, we have to go back. Way back."
- **Action:** Slow push into Grace's eyes, then dissolve to black. Title card:
  **THE HOUSEKEEPER WHO STAYED**
- **Video prompt:** extreme slow push-in on a woman's teary eyes, image slowly dissolves to black

---

## 4. ACT 1 — NINETEEN YEARS (1:20–6:15) · 30 shots

### Scene 1.1: Grace arrives, 2006 (golden, slightly faded "memory" grade)

**S9** · 10s · 🔇 · Wide
- **Action:** A Greyhound bus pulls away. GRACE_2006 stands on the curb in Nashville with two
  battered suitcases, holding a folded newspaper ad.
- **VO:** "Nineteen years ago, Grace Miller got off a bus in Nashville with two suitcases and
  a newspaper ad."
- **Video prompt:** Greyhound bus pulls away revealing a young Black woman on a curb with two
  old suitcases, she unfolds a newspaper, warm faded 2006 film look

**S10** · 10s · 🔇 · Medium, walking
- **Action:** Grace walks up Belle Meade Boulevard and stops at the iron gate of MANSION_EXT,
  staring up at the columns.
- **VO:** "Her husband had died that spring. She had a little girl back in Ohio and a stack
  of bills she couldn't pay."
- **Video prompt:** young woman with suitcases walks to a tall iron gate of a white-columned
  mansion, stops and looks up in awe, magnolia trees swaying

**S11** · 10s · 🔊 · Two-shot
- **Action:** MARGARET opens the gate in gardening gloves and looks at Grace's shaking hands.
- **Dialogue:** MARGARET: "Honey, everybody who answers that ad says they're the best
  housekeeper in Tennessee. You're the first one who looks like she actually needs it."
- **Video prompt:** auburn-haired woman in gardening gloves opens an iron gate, smiles warmly
  at a nervous young woman, speaks kindly

**S12** · 5s · 🔊 · Close two-shot
- **Dialogue:** MARGARET: "Can you make biscuits?" GRACE_2006: "Ma'am, I can make biscuits
  that'll make you cry."
- **Video prompt:** the older woman laughs out loud, the young woman smiles shyly for the first time

**S13** · 10s · 🔇 · Montage, kitchen
- **Action:** Grace and Margaret in KITCHEN, flour everywhere, laughing, dancing to a radio.
- **VO:** "They weren't really boss and employee. They were two women who looked out for each other."
- **Video prompt:** two women laughing in a big kitchen, flour on their faces, one twirls the
  other to radio music, warm golden light

### Scene 1.2: Margaret's deathbed

**S14** · 10s · 🔇 · Slow push
- **Action:** Hospital bed in an upstairs bedroom. MARGARET is thin and pale. GRACE_2006 holds
  her hand. THOMAS (younger, dark-gray hair) stands frozen in the doorway.
- **VO:** "Then Margaret got sick. Four months later, she was gone."
- **Video prompt:** dim bedroom, frail woman in a hospital bed, a younger woman holds her hand,
  a man stands motionless in the doorway, rain on the window

**S15** · 10s · 🔊 · Close-up
- **Dialogue:** MARGARET *(whispering)*: "Tom acts like he's made of iron. He isn't. Promise
  me somebody in this house will love him for who he is."
- **Video prompt:** close-up of a frail woman whispering urgently, squeezing the hand of the
  woman beside her

**S16** · 5s · 🔊 · Close-up
- **Dialogue:** GRACE_2006: "I promise."
- **Video prompt:** young woman's tearful face nodding, whispering a promise

**S17** · 10s · 🔊 · Close two-shot, Margaret smiles
- **Dialogue:** MARGARET: "And Grace… if that somebody turns out to be you one day, don't you
  dare feel guilty about it." GRACE_2006: "Mrs. Caldwell!"
- **Video prompt:** dying woman gives a weak knowing smile, the young woman gasps and blushes,
  both laugh softly through tears

**S18** · 5s · 🔇 · Insert
- **Action:** Their joined hands. Margaret's hand goes slack. Fade.
- **Video prompt:** close-up of two joined hands, one slowly goes still, slow fade to dark

### Scene 1.3: Present day (switch to sharp, modern grade)

**S19** · 10s · 🔇 · Aerial
- **Action:** Drone shot over MANSION_EXT and Nashville, then Caldwell Freight trucks rolling on
  the interstate.
- **VO:** "Thomas Caldwell built Caldwell Freight from one used truck. Forty years later, he had three hundred."
- **Video prompt:** aerial drone shot over a white mansion, transitions to a fleet of semi
  trucks with "CALDWELL FREIGHT" on the side driving on a highway at sunset

**S20** · 10s · 🔇 · Medium
- **Action:** THOMAS at a backyard barbecue, laughing with business partners, but he looks alone
  in the crowd.
- **VO:** "He had all the money in the world, and nobody to come home to."
- **Video prompt:** silver-haired man at an upscale backyard party, forcing a laugh, then his
  smile fades as he looks away alone

**S21** · 10s · 🔇 · Tracking
- **Action:** BRADLEY speeds up in a Porsche, sunglasses on, arguing on the phone.
- **VO:** "His son Bradley was Vice President of something. Nobody could tell you what."
- **Video prompt:** red Porsche screeches into a mansion driveway, slick-haired man in sunglasses
  gets out arguing angrily on his phone

**S22** · 10s · 🔇 · Slow motion
- **Action:** Wedding flashback: VANESSA in white, champagne, kissing Thomas's cheek while
  looking past him at the mansion.
- **VO:** "Then, three years ago, came Vanessa. She married him eight months after they met."
- **Video prompt:** slow-motion garden wedding, blonde bride kisses the older groom's cheek but
  her eyes look past him at the mansion, champagne glasses raised

### Scene 1.4: Vanessa vs. Grace

**S23** · 10s · 🔊 · Two-shot, KITCHEN
- **Action:** VANESSA walks in and looks GRACE up and down.
- **Dialogue:** VANESSA: "I'm going to be honest. I don't like having *help* that's been here
  longer than I have."
- **Video prompt:** glamorous blonde woman strolls into a marble kitchen, looks an older
  housekeeper up and down coldly, speaks with a fake smile

**S24** · 5s · 🔊 · Close-up on Grace
- **Dialogue:** GRACE: "I don't think I own anything, Mrs. Caldwell. I just take care of it."
- **Video prompt:** older housekeeper answers calmly, chin up, dignified

**S25** · 10s · 🔊 · Close-up on Vanessa, moving in close
- **Dialogue:** VANESSA: "Mm. Well, take care of it quietly. And Grace? I see how you look at
  him. Don't."
- **Video prompt:** blonde woman leans in close, eyes narrowing, whispers a threat, then walks
  out; the housekeeper's face falls

### Scene 1.5: The coffee (the love story begins)

**S26** · 10s · 🔇 · Montage, dawn, KITCHEN
- **Action:** GRACE alone before sunrise making biscuits, then dropping one ice cube into black coffee.
- **VO:** "Grace knew everything about him. Black coffee, one ice cube, because he was too
  impatient to let it cool."
- **Video prompt:** before dawn, a woman alone in a big kitchen rolls biscuit dough, then drops
  a single ice cube into a mug of black coffee, soft blue-to-gold morning light

**S27** · 10s · 🔊 · Two-shot
- **Action:** THOMAS shuffles in with a newspaper. Grace hands him the coffee.
- **Dialogue:** THOMAS: "Grace, you're the only one around here who doesn't want anything from
  me." GRACE: "Oh, I want something, Mr. Caldwell. I want you to eat a vegetable once a week."
- **Video prompt:** silver-haired man takes a coffee mug from the housekeeper, they banter,
  he laughs heartily

**S28** · 5s · 🔇 · Insert, slow motion
- **Action:** Their fingers brush on the mug. Grace pulls her hand back a beat too fast.
- **Video prompt:** extreme close-up slow motion, a man's and a woman's fingers brush on a
  coffee mug, her hand pulls away quickly

**S29** · 10s · 🔇 · Close-up on Grace as Thomas walks off
- **VO:** "He never noticed. For twelve years, Grace had loved Thomas Caldwell quietly and kept it
  to herself."
- **Video prompt:** the man walks away laughing reading his paper; the woman watches him go,
  her smile turning wistful and sad, she touches her cross necklace

**S30** · 10s · 🔇 · Through the window
- **Action:** Grace watches through the kitchen window as Vanessa pulls Thomas into a car.
- **VO:** "She put that hope away like a dish on a high shelf."
- **Video prompt:** woman at a kitchen window watches a blonde woman pull a silver-haired man
  into a luxury car, she lowers her eyes and goes back to washing dishes

**S31** · 5s · 🔇 · Freeze frame
- **Action:** Back to Thomas laughing in the kitchen doorway. Freeze frame and desaturate.
- **VO:** "It was the last time anyone heard him laugh for a very long time."
- **Video prompt:** man laughing in a doorway, motion slows to a near stop, color drains out

### Scene 1.6: Bridge to Act 2

**S32** · 10s · 🔇 · Night, wide
- **Action:** The mansion at night. Every window is dark except the kitchen. A storm is coming.
- **Video prompt:** white mansion at night, wind bending magnolia trees, lightning far away,
  one kitchen window glowing warm

**S33** · 10s · 🔇 · Inside KITCHEN, night
- **Action:** GRACE ironing late. Through the doorway, THOMAS pours coffee, rubbing his temple.
- **VO:** "It was a Tuesday night in October."
- **Video prompt:** woman ironing shirts late at night, in the background a silver-haired man
  pours coffee, winces and rubs his temple

**S34** · 5s · 🔇 · Insert
- **Action:** Thomas's hand trembles. The coffee mug slips.
- **Video prompt:** close-up, a man's hand trembles violently, coffee mug slips from his fingers

**S35** · 5s · 🔊 · Slow motion
- **SFX:** The mug shatters on the tile.
- **Video prompt:** slow-motion coffee mug shattering on a tile floor, coffee splashing

**S36** · 5s · 🔇 · Reverse on Grace
- **Action:** Grace's head snaps up and the iron drops.
- **Video prompt:** woman's head snaps up in fear, she drops the iron and runs

**S37** · 5s · 🔊 · Wide
- **SFX:** A heavy thud. Thomas collapses out of frame.
- **Video prompt:** wide kitchen shot, a man collapses to the floor, the woman rushes into frame

**S38** · 5s · 🔊 · Cut to black
- **Dialogue:** GRACE *(off-screen, screaming)*: "TOM!"
- **Video prompt:** smash cut to black

> **END OF PART 1.** Part 2 picks up in the kitchen: Grace on the floor holding Thomas,
> calling 911.

---

## Part 1 cost check

| | Count | Credits |
|---|---|---|
| Character sheets + locations | ~30 images | ~60 (one-time, covers the whole movie) |
| Start frames | 38 | 76 |
| Video seconds | ~315s (≈ 5:15 of screen time) | ~473 |
| Redos (~25%) | | ~140 |
| **Part 1 total** | | **≈ 750** |

At this rate the full 40-minute movie lands around **5,300–5,600 credits**, leaving a little
for narration voice-over.
