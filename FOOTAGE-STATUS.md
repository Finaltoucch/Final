# DIAMOND ANACONDA — FOOTAGE STATUS

What is actually shot, what is approved, and what still needs work.
Approved means Finaltouch watched it and said keep.

---

## ✅ APPROVED — IN THE CUT

### Cold open — 30 seconds, two clips

| Time | Shot | Model | Job ID | Credits |
|---|---|---|---|---|
| 0:00–0:15 | She crosses the flooded passage toward him. Heat POV, camera travelling the whole length, he is a distant ember growing to fill frame. | minimax_h3 | `3f1c7d96-ed8f-454b-9c77-5fa440e7102a` | 30 |
| 0:15–0:30 | Thermal for 5s while she settles behind him, then the grade drops to normal torchlight from the same locked position; he turns into the lens, screams, hard black. | seedance_2_5 | `7f3c51eb-1ae8-4d52-b066-408f23a5545c` | 98 |

Verified by analysis. Clip 2 carries its own audio — breathing, dripping,
the scream, and a sound hit on the cut to black.

Keyframes behind them: far POV `607fb94f-763a-48c8-8469-11e9768e1afd` (heat, distant),
close POV `9ff9a35a-417c-478f-9e5f-25f2739a7ea1` (heat, arrival),
normal `da84031f-e493-4d60-9673-f20d158799c1` (torchlit, carries Ryan's reference).

### Scene 2 — the fishing village, 30 seconds

Armando and Ryan, the business conversation outdoors, late afternoon.
seedance_2_5 · `cee1b944-92f4-458f-9db6-c462f9fe32da`

---

## ✅ APPROVED — BOATYARD COVERAGE

Scene 3's original 45-second wide shot (`3e815f0c`) is **retired** — it was generated
before character references were passed and invented six faces. Replaced by coverage,
one or two named characters per shot, each carrying their Element:

| Shot | Who | Beat | Job ID |
|---|---|---|---|
| Boatyard day 1 | Mateo + Liam | *"My daughter has a house in her mouth."* | `99ca5be8-d1d6-41c5-8889-fd587e2ebb5d` |
| Boatyard day 2 | Daniel + Marcus | *"That's not how sevenths work."* | `13e9cda5-2ae2-40ed-8803-dbb577c56786` |
| Boatyard day 3 | Maya + Ryan + the stone | *"It grew in rings. Like a tree."* | `7624948d-5a9d-4329-a888-20cc35fb2cf7` |
| Boatyard night | Maya + Ryan | *"Say it back to me."* | `0ecdb427-7f82-4711-9431-0ee5663e7af7` |

All four verified by analysis: faces consistent with their locked Elements, every line of
dialogue spoken verbatim, natural ambience. The night shot cuts itself into seven pieces
of proper shot/reverse-shot coverage.

---

## ⚠️ DUPLICATE — RESOLVED

The clip filed as "Scene 4 — the dock" (`8c8a8538-ab00-446b-8d19-e50d1a9407bd`) is **not a
separate scene**. Analysis shows it IS the boatyard night scene: Maya and Ryan, coffee on
the dock, the full *"This is my last one" / "You said that in Kandahar" / "Say it back to
me" / "This is your last one. And I bring you home."*

It runs **30 seconds**, the exact length the spine allots, with correct faces and the
**original Kandahar lines** — the ones seedance's content filter forced out of the later
version.

**Keep `8c8a8538` (30s). Drop the 15s reshoot `0ecdb427`.** The reshoot was generated
without first verifying what this clip contained, and duplicated a scene already in hand.
Lesson: analyse existing footage before shooting anything that might overlap it.

---

## SCENE 5 — RIVER MOUTH (in progress)

| Shot | Who | Beat | Job |
|---|---|---|---|
| Engine dies | Mateo + Marcus | *"It's not anything. It's just off." / "Where'd everything go?"* | `e1aa8e04-f2e4-4480-9c67-f5f7ef32e4b8` ✅ |
| The skins | canopy tilt, no cast | dozens of small skins, then the two enormous ones | `ffa6c9fa-6c2f-4f85-a220-6629590446a4` (minimax) |

**Engine-dies shot verified.** Six shots of coverage, all four lines verbatim, Marcus
correct, and critically the silence lands — "the environment is eerily quiet, with only
very low-volume ambient forest drones and the slight ripple of water against the boat."
No birds, unlike the retired skins take.

One flaw, minor and left in: *"Where'd everything go?"* is spoken by Mateo. It is Marcus's
line in the script — the veteran noticing first. It plays over a rack focus so it does not
read as wrong, but a future reshoot should put the line back on Marcus.

The first skins attempt (`ef6ecd8b`, seedance) is **retired**: dialogue and faces were
right but the two enormous skins never rendered — every skin came out the same size, so
the scale reveal, the entire point of the shot, was missing. It also added bird calls and
a synth drone over a scene whose whole effect is total silence.

The minimax reshoot (`ffa6c9fa-6c2f-4f85-a220-6629590446a4`) **also failed the same way.**
Analysis: "dozens of long, dried snake skins draped over the horizontal branches" — one
uniform group, no large ones, across all three segments. The camera panned right instead
of tilting up.

**Both models fail this shot identically**, from prose and from a keyframe. The problem is
the shot, not the tooling: asking one frame to hold dozens of small skins AND two giant
ones makes the model average everything to a single size. It cannot render the comparison.

**The fix when credits allow:** shoot the big skins as their OWN shot — one enormous skin
filling the frame over a branch, a single small skin beside it for scale, nothing else in
contention. Cut it after the wide of the dozens. Let the edit make the comparison.

**Correction:** minimax_h3 DOES generate audio — this clip came back with wind and "a
subtle, atmospheric musical drone". An earlier note here claimed it produced none and that
the silence would therefore be literal. That was asserted without checking and is wrong.
Both models score their output; the silence in this scene has to be made in the edit.

---

## NOT THIS PROJECT

Eight `kling3_0` clips of a boy on a bicycle sit in the same Higgsfield history.
Unrelated — do not pull them into this film.

---

## RUNTIME ACCOUNTING

Target is **12 minutes = 720 seconds**.

Shot and approved so far: **120 seconds** — 30s cold open, 30s Scene 2 (fishing village),
45s boatyard day coverage, 15s boatyard night.

At the rates established today — 30 credits per 15s on minimax, 98 per 15s on
seedance — the remaining balance decides how much of the film is reachable. Prefer
minimax wherever a shot does not need dialogue audio or a mid-clip grade change.

---

## SCENE 6 — ABANDONED SETTLEMENT / THE RADIO

| Shot | Who | Beat | Job | State |
|---|---|---|---|---|
| 1 | Maya + Ryan | *"Ryan." / "There is charge in it."* | `ee29ed67-ab23-405f-a181-be0aa8a6b2de` | reshoot in flight |
| 2 | Daniel + Maya | *"...sitting in a swamp since Nixon." / "The needle's moving."* | `fcd9a315-8104-4f19-a66b-19dd35f0b6c6` | ✅ keep |
| 3 | Maya + Liam | ***"don't go underground"*** / *"It's not a recording, Liam."* | `26685559-05b5-48e3-9b4e-bf842c722f97` | ✅ keep, with the audio fix below |

Shot 1's first take (`cbc8dfba`) is retired: Maya's second line rendered as **"Hi, Odin"**
instead of "There's charge in it". Retired because it is a lip-synced on-camera line and
cannot be dubbed. The reshoot declares "exactly two spoken lines and nothing else" and
spells out the contraction, which is where the garble occurred.

Shot 2 note: the radio dial in the extreme close-up is stencilled **"GTDERD"** — the usual
AI gibberish-text artifact. Readable, but small. Future prompts push lettering out of frame.

### 🔊 THE CHEAP FIX: dub anything not lip-synced

Shot 3's radio voice came back **male**. The script calls for a woman's, and it matters —
a woman on a 1960s military channel is the thread to whoever tore the notebook pages out.

Because it is a radio voice-over with no mouth on camera, it was fixed for **0.2 credits**
instead of a 98-credit reshoot:

`generate_audio` · model `seed_audio` · voice **Soraya** `5c1d2f7f-cdb4-5b1d-bca9-156439e3275e`
→ `https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_20260903_185312_875ae466-b8c3-41d3-ab0a-0956b964e330.wav`

Lay it over the male line with the static riding on top.

**Apply this everywhere:** any line without a mouth on camera — radio, off-screen, through
a wall, a voice from the dark — is a 0.2-credit audio generation, not a reshoot. Only
lip-synced dialogue needs the video redone. (`speech_rate` must be an integer, not a float.)

---

## SCENE 7 — RIVERBANK, NIGHT / MATEO TAKEN

| Shot | Who | Beat | Job | State |
|---|---|---|---|---|
| 1 | Liam alone | *"He was right here, he was talking, I turned around."* | `0914ab84-560a-45e9-b907-3d767f12de88` | ✅ keep |
| 2 | Maya + Daniel | The rifle in the shallows. *"Mateo!" / "Safety's on."* | `f47d6e3b-3f4e-4c69-98a2-3cff9426a8a4` | ✅ keep |
| 3 | Ryan + Maya | *"There is no blood."* → the trough → *"MATEO!"* | `f94fec33-12b8-4d9f-847d-c129b460feb3` | ✅ keep + dub |
| 4a | water only | the ridge longer than the boat | — | ❌ **CUT** — see below |
| 4b | Marcus + Ryan | *"That boat is thirty feet." / "Out of the water." / "Everybody move. Now."* | `11a17916-c542-49d7-bde7-99f523b83738` | ✅ keep |

**Retired:** `e1542f9d` (shot 3 take 1) — the actor read the stage directions aloud:
"Canal about two feet wide and six inches deep pressed into unbroken mud." `67b29246`
(shot 4 take 1) — the two lines fused into "That boat is thirty feet out of the water",
no ridge of water rendered at all, and Marcus came out light-complexioned.

**Audio dubs for this scene:**
- Shot 3's *"MATEO!"* rendered in a male voice; replaced with Maya's cast voice Maeve
  `64cf4f1a-61c8-5938-9aea-83d12b2e1d13` →
  `https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_20260903_192212_0362c815-b55a-4d11-ba47-1ef78fbab251.wav`

### STAGING PRINCIPLE WORTH USING DELIBERATELY

Wrong-voice and wrong-line problems have now cost 0.2 credits twice and 98 credits twice.
The difference is only whether the mouth is on camera.

**So stage the emotionally critical shouts off-camera or at distance** — a cry from the
treeline, a name shouted while the camera is wide on the water, a warning from behind the
lens. Those become editable for a fifth of a credit. Reserve lips-in-frame for lines whose
delivery you actually want to see performed.

**Shot 4b verified.** Three lines, two speakers, no fusion — the guard plus an action beat
between each line fixed it. Marcus renders correctly as a Black man with a grey goatee once
his skin tone is stated explicitly; leaving it unstated produced a light-complexioned man.
Ends with both men sprinting into the brush.

Two things for a human ear and eye: line two still transcribes with a leading ellipsis, so
it may still sound like a continuation of Marcus's line rather than Ryan's separate order.
And the analyser reads "bloody facial scratches" on Marcus, which is probably his canonical
facial scars under hard torchlight — but if they read as fresh wounds, the audience will
think he has already been attacked.

**Still open:** shot 4a, the ridge of water. Keyframe `ba3b3510-33c2-4b9d-86da-6bd7308cec4f`
awaits approval that the swell out-measures the boat; then 30 credits on minimax to move it.
This is the film's only concrete statement of the creature's size, so the frame is worth
getting right before spending on motion.

### ❌ SHOT 4a IS CUT — A SHOT THE MODELS CANNOT RENDER

Two attempts, 60 credits, two different failures at the same idea:

1. `ed99f11e` — the swell rendered as **bioluminescent**: "a bright phosphorescent wake...
   a glowing, ethereal entity". Caused by asking for a "bright specular highlight".
2. `0ba1e5cb` — with the glow forbidden, the swell was replaced by **a motorboat with a
   spotlight**, engine noise and all. No ridge of water at all.

Given an unfamiliar phenomenon — a long raised bulge of dark water at night — the model
substitutes something familiar. This is the same failure as the shed-skins scale reveal.

**The beat is already covered and covered better.** Shot 4b has Marcus watching something
off-screen, saying "That boat is thirty feet" with no expression, and Ryan ordering
everyone out of the water. The audience never sees it. That is the film's own rule — the
cold open works because she is never shown — so cutting 4a strengthens the scene rather
than weakening it.

**General lesson:** when two attempts fail in two different ways, the shot is wrong, not the
prompt. Check whether existing coverage already carries the beat before spending a third time.


---

# 📼 THE EVERYTHING-REEL — ALL 57 CLIPS, NOTHING WITHHELD

**https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/2e826598-813f-4ed7-9237-ff6e8f3a76fb.mp4**

**14 minutes 44 seconds.** Every clip generated for this film, in the order it was
generated — keepers, retired takes, failed experiments, all of it. This exists because
retirement decisions were being made silently on footage Finaltouch had never seen.
He judges his own film. The reel is the evidence.

The two earlier stitches remain valid as *cuts* — this one is an *archive*:
- Story cut, with cold open, 336s — `d344692c-0620-49f3-b9a8-9e295dc15d4a.mp4`
- Story cut, without cold open, 306s — `6d8e212d-50bc-4cc1-8e02-12b50deeca26.mp4`

## Timecode index

Timecodes confirmed by ffprobe against the normalised masters. Clip UUIDs match the
job IDs recorded elsewhere in this file.

| At | # | Len | What it is | Status |
|---|---|---|---|---|
| 0:00 | 01–02 | 5s ea | earliest tests | — |
| 0:10 | 03–04 | 30s ea | early 30s attempts | superseded |
| 1:10 | 05 | 30s | boatyard wide, six invented faces | ❌ retired |
| 1:40 | 06 | 30s | **dock night — Maya + Ryan, the Kandahar lines** | ✅ **in the cut** |
| 2:10 | 07 | 30s | **Scene 2 — fishing village, Armando + Ryan** | ✅ **in the cut** |
| 2:40 | 08–19 | 5–15s | the cold open, twelve attempts — heat plates, animated-plate errors, static camera, frozen actor | superseded |
| 5:16 | 20 | 15s | **cold open 0:00–0:15 — heat POV travelling toward him** | ✅ **in the cut** |
| 5:31 | 21–23 | 10–15s | further cold-open attempts | superseded |
| 6:06 | 24 | 15s | **cold open 0:15–0:30 — thermal → torchlight, the scream into lens** | ✅ **in the cut** |
| 6:21 | 25–26 | 15s ea | boatyard coverage attempts | superseded |
| 6:51 | 27 | 15s | **boatyard day — Maya + Ryan + the stone** | ✅ **in the cut** |
| 7:06 | 28 | 15s | boatyard night reshoot | ❌ duplicate of 06 |
| 7:21 | 29 | 15s | **boatyard day — Mateo + Liam** | ✅ **in the cut** |
| 7:36 | 30 | 15s | **boatyard day — Daniel + Marcus** | ✅ **in the cut** |
| 7:52 | 31 | 15s | **river mouth — the engine dies** | ✅ **in the cut** |
| 8:07 | 32 | 15s | shed skins, seedance — no scale reveal | ❌ failed |
| 8:22 | 33 | 15s | shed skins, minimax — same failure | ❌ failed |
| 8:37 | 34 | 15s | radio shot 1 — "Hi, Odin" garble | ❌ retired |
| 8:52 | 35 | 15s | **radio — Maya + Liam, "don't go underground"** | ✅ **in the cut** |
| 9:07 | 36 | 15s | **radio — Daniel + Maya, "the needle's moving"** | ✅ **in the cut** |
| 9:22 | 37 | 15s | **radio — Maya + Ryan, "there is charge in it"** | ✅ **in the cut** |
| 9:37 | 38 | 15s | **riverbank — the rifle in the shallows** | ✅ **in the cut** |
| 9:52 | 39 | 15s | **riverbank — Liam alone, "he was right here"** | ✅ **in the cut** |
| 10:07 | 40 | 15s | riverbank shot 4 take 1 — lines fused | ❌ retired |
| 10:22 | 41 | 15s | riverbank shot 3 take 1 — stage directions read aloud | ❌ retired |
| 10:37 | 42 | 15s | **riverbank — "that boat is thirty feet" / "out of the water"** | ✅ **in the cut** |
| 10:52 | 43 | 15s | **riverbank — "there is no blood" → the trough → MATEO!** | ✅ **in the cut** |
| 11:07 | 44 | 15s | ridge of water — rendered bioluminescent | ❌ cut |
| 11:22 | 45–50 | 15s ea | flooded crossing, first attempts — straight-line formation, wrong water level, invented civilians | superseded |
| 12:53 | 51 | 15s | ridge of water take 2 — rendered as a motorboat | ❌ cut |
| 13:08 | 52–56 | 15s ea | flooded crossing / drone reveal, further attempts — creature visible from the surface | superseded |
| 14:23 | 57 | 20s | latest flooded-crossing / drone-reveal take | current best |

**Read that column honestly:** 18 clips carry the film. 39 were spent finding out how.
Roughly two thirds of the credits burned so far went on takes that did not survive.
