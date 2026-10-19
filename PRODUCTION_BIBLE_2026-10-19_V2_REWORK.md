# Videos 26 / 27 / 28 — v2 rework

Date: 2026-10-19. Branch `claude/new-paid-project-34x2t9`.

## Why there is a v2

The client rejected v1 of all three films. Not for craft — for structure:

> "All three videos are too similar in their core storyline. In each one, a woman
> starts listening to the music and then dances to it in different locations...
> This is exactly the kind of 'same creative DNA' that I asked you to avoid."

The three v1 films (THE WINDOW / NIGHT SHIFT / THE CONNECTION) were each
technically clean and each passed every client rule *except* the one that
mattered: they shared a single premise. A different location is not a
different story.

The client asked for each film to have its own **central idea, situation or
character motivation, sequence of events, development or transformation, and
ending or payoff**, and for screenplay work to happen *before* generation.

Okoye then supplied three concept seeds:
1. A young boy driving a scooter in the slums of Africa
2. A boy flying something like a magic broom
3. A science-fiction scene — a half-human, half-machine figure in an AI-vs-humans fight

## The rule this rework is built on

Three different subjects is not enough. v1 had three different subjects too
(three locations). What makes stories different is **the mechanism by which
the audience is made to feel something**. So each film was built on a
different narrative mechanism, and no two share one:

| Film | Title | Mechanism | The thing the audience works out |
|---|---|---|---|
| 26 | THE FUSE | **Dramatic irony** | We know he caused the blackout. Nobody in the film ever does. |
| 27 | LIFT | **Emotional misdirection** | It looks like a story about magic. It is a story about grief. |
| 28 | THE LINE | **Systemic reversal** | The system turns its own logic on the one using it. |

A fourth guard: each film resolves on a different *kind* of beat — a public
one (a street lights up), a private one (a boy at an empty window), and a
physical one (two hands touching).

---

## 26 — THE FUSE

**Track:** 005 — Ever Forward
**Character:** Kwame, 13, a boy in a West African informal settlement.
**Time:** golden hour falling to night.

**Central idea.** A boy breaks the thing his whole street depends on, and
fixes it, and nobody ever learns either half.

**Motivation.** He is riding fast because riding fast is the best thing in
his day. That is all. The fault is carelessness, not malice — which is why
the confession never comes.

**Sequence.** He rides (hook) → he rides harder → something above him gives
way and he hears it → the street goes black and he stands in it alone → a
lineman arrives and starts searching the cables for the fault → the boy rides
across the settlement with a spare fuse hidden against his chest → through
water, through mud → he abandons the scooter and runs → he throws the fuse up
to the lineman, who never asks where a boy got one → every bulb in the lane
comes on and he stands in the light he paid for.

**Development.** Delight → fright → concealment → repair. He does not become
brave; he becomes responsible, quietly.

**Payoff.** The lane lit, him small in it, uncredited. The motif — a single
bare bulb over a doorway, planted lit in shot 1, dead through the middle —
returns as a whole street.

**Why the music fits.** The track drops out almost completely at bar 7
(−18.5 dB against a −11 dB bed). That hole is the blackout. It was found by
measurement, not chosen; the edit was then built around it.

---

## 27 — LIFT

**Track:** 023 — To the Stars
**Character:** Finn, 10, a boy on a British council estate.
**Time:** wet winter dusk.

**Central idea.** A boy tries to make a broom fly. It flies the moment he
gives up. What he actually wanted was never flight.

**Motivation.** Withheld until the last shot. He pulls the broom out of a
skip outside his block. His hands are visibly too small for the worn
finger-grooves in the handle — somebody much larger used this for decades.

**Sequence.** A man clearing a flat tips its contents into a skip → the boy
finds the broom and grips the worn band → he sprints and jumps and lands
badly → he jumps off the skip and drops harder → older children on the
walkway laugh at him → he stays down on the wet tarmac, the broom out of
reach → he carries it back to the skip to give it up, opens both hands — and
it does not fall → his face → he rises, wobbling, barely three metres →
he draws level with one first-floor window and lays a hand on the sill. The
flat beyond is stripped bare. One unlit bulb. One cardboard box.

**Development.** Effort → humiliation → surrender → release. The reversal is
structural, not magical: **it only flies when he lets go.**

**Payoff.** Not altitude — proximity. He is not flying away; he has got back
up to his nan's window one last time. The laughing children below have gone
silent. The film never says the word "nan" and never shows her.

**Why the music fits.** Bar 10 is the quietest in the window (−21.3 dB) and
lands on him face-down on the tarmac. The track then climbs for eleven
straight bars and peaks on the final bar — on the empty window.

---

## 28 — THE LINE

**Track:** 013 — Rise Again
**Character:** Kestrel, a half-human, half-machine soldier. Her left side is
machine; her right side is flesh. This is fixed and never mirrors.
**Time:** night, heavy rain, a ruined city.

**Central idea.** She is a weapon with a targeting system. The system flags
her own living hand as a target. She has to choose which half of herself to
obey.

**Motivation.** She has no doubts at the start. That is the point — the doubt
is installed by the machine, not by conscience.

**Sequence.** A line of machines advances up a flooded street → her human
hand and her steel hand together on one weapon → she walks ahead of the line
→ she comes to a sandbag barricade with people behind it → her optic puts a
reticle on a woman's face → the same reticle snaps onto her own bare human
hand → she crushes her own targeting optic under her palm and the red light
dies → she looks at the dead optic in her fingers → blind to the system now,
she turns and fires on the machines → at the barricade a survivor's hand
closes over her bare human hand.

**Development.** Instrument → glitch → refusal → defection → contact.

**Payoff.** The motif is the human hand, and it runs the whole film in three
states: **on the grip → flagged as a target → held by another person.** The
last shot has no red in it anywhere.

**Why the music fits.** The loudest bar in the window is the last one, and it
sits under the two hands.

---

## Measured music grids

Method unchanged and unchanged on purpose: **fit the bar grid directly over
the exact window the film uses**, then z-test *that same score* against 400
random phases. Fitting beat energy and then testing bar lines is an objective
mismatch and gives unstable z — that mistake is not repeated here.

| Film | Track | Local BPM | Grid z | In point | Bars | Length |
|---|---|---|---|---|---|---|
| 26 THE FUSE | 005 Ever Forward | 134.621 | 3.61 | 135.419 s | 24 | 42.792 s |
| 27 LIFT | 023 To the Stars | 137.860 | 4.59 | 103.363 s | 24 | 40.042 s |
| 28 THE LINE | 013 Rise Again | 136.255 | 4.57 | 119.536 s | 23 | 40.500 s |

All three pass z > 2.5. All three sit >14 BPM clear of both edges of the
118–152 search band, so none is a harmonic artefact. All three lengths are
inside the 30–60 s brief.

**Spoken-tag handling.** Mid/side detection (M=(L+R)/2, S=(L−R)/2, 250–4000 Hz,
flag runs where M/S > 2.2× the track median) located every centred vocal run
in all three masters. The constraint applied is on the **window edges only** —
a run fully inside the window plays complete and is fine; a run straddling an
edge would clip a phrase and is rejected. Both edges of all three windows are
at least 0.30 s clear of any run.

**Masters identified by MD5, never by filename:**
- 005 Ever Forward — `8ab43291510016b05ffa2a541aae3265` — 306.02 s
- 013 Rise Again — `05c7d34fe7d5be359e09a3dc2a428535` — 204.62 s
- 023 To the Stars — `2ba70900c10199b7215594dcb4ed90a9` — 182.47 s

---

## Edit plans (frame-accurate, 24 fps)

**26 THE FUSE** — 1027 frames. Cuts at 128 214 300 342 471 599 685 770 899.

| Shot | Bars | Frames | Content |
|---|---|---|---|
| 101 | 0–2 | 128 | Riding the lane, golden hour, the bulb lit overhead |
| 102 | 3–4 | 86 | Riding past, grinning |
| 103 | 5–6 | 86 | Stopped, looking up at the pole |
| 104 | 7 | 42 | His face in the dark — **the blackout, on the music's hole** |
| 105 | 8–10 | 129 | The lineman up the pole with a flashlight |
| 106 | 11–13 | 128 | Riding, the fuse hidden against his chest |
| 107 | 14–15 | 86 | Through the flooded stretch |
| 108 | 16–17 | 85 | Abandons the scooter, runs |
| 109 | 18–20 | 129 | Throws the fuse up; the lineman catches it |
| 110 | 21–23 | 128 | The lane lights up (start-frame dark → end-frame lit) |

**27 LIFT** — 961 frames. Cuts at 125 209 292 376 418 501 627 710 836.

| Shot | Bars | Frames | Content |
|---|---|---|---|
| 201 | 0–2 | 125 | The skip outside the block, a flat being cleared |
| 202 | 3–4 | 84 | His hands on the worn band — too small for it |
| 203 | 5–6 | 83 | First attempt; bad landing |
| 204 | 7–8 | 84 | Second attempt off the skip; drops hard |
| 205 | 9 | 42 | Older children on the walkway, laughing |
| 206 | 10–11 | 83 | Down on the tarmac — **on the music's hole** |
| 207 | 12–14 | 126 | He lets go. It does not fall. |
| 208 | 15–16 | 83 | His face |
| 209 | 17–19 | 126 | The lift — small, wobbling, three metres |
| 210 | 20–22 | 125 | The emptied window |

**28 THE LINE** — 972 frames. Cuts at 127 211 338 423 507 634 719 803 888.

| Shot | Bars | Frames | Content |
|---|---|---|---|
| 301 | 0–2 | 127 | The machine line advancing up the flooded street |
| 302 | 3–4 | 84 | Human hand and steel hand on one weapon |
| 303 | 5–7 | 127 | Kestrel walks ahead of the line |
| 304 | 8–9 | 85 | The barricade; people behind the sandbags |
| 305 | 10–11 | 84 | A woman's face inside the reticle |
| 306 | 12–14 | 127 | The reticle snaps onto Kestrel's own living hand |
| 307 | 15–16 | 85 | She crushes her own optic; the red dies |
| 308 | 17–18 | 84 | The dead optic in her fingers |
| 309 | 19–20 | 85 | She turns and fires on the machines |
| 310 | 21–22 | 84 | A survivor's hand closes over hers |

---

## Model-behaviour lessons added this session

- **Lock a vehicle with a reference plate in every shot that shows it, and
  name what it is not.** Film A's first pass turned the scooter into a
  bicycle in two shots and a motorcycle in a third. "NOT a bicycle — no
  pedals, no pedal cranks, no chainring; NOT a motorcycle — no fuel tank
  between the knees", plus the plate, fixed all of them in one pass.
- **State the frame orientation as geometry, not as a label.** One keyframe
  came back with correct 9:16 dimensions but the *content* rotated 90°.
  "UPRIGHT PORTRAIT ORIENTATION" was not enough. What worked: "the horizon
  runs horizontally across the frame; the ground is at the bottom and the sky
  at the top; the subject's head is at the top and feet at the bottom; do not
  rotate the composition."
- **Demand a complete body by name.** A shot of a parked scooter returned a
  pair of legs severed at the knee with no body attached. Fix: "his whole
  body is visible from head to feet, complete and unbroken: head, face, neck,
  shoulders, both arms, torso, both legs and both feet", plus an explicit ban
  on "disembodied, severed, floating or partial body parts".
- **Count limbs and count light sources out loud in the prompt.** A shot of a
  one-armed action took four passes. What failed: describing the pose and
  saying where the other arm was. What worked: "THERE IS EXACTLY ONE ARM AND
  EXACTLY ONE HAND ANYWHERE IN THIS FRAME... count the arms before you
  finish." The same shot kept growing a second glowing object until the
  prompt said "THERE IS EXACTLY ONE RED GLOWING OBJECT ANYWHERE IN THIS
  FRAME" and hid it behind a hand so there was nothing to duplicate.
- **If a shot fails three times, change the shot, not the wording.** The
  optic-removal beat was finally solved by replacing "tear it out" (two
  objects: socket and extracted part) with "crush it under your palm" (one
  object, mostly occluded). Reducing the object count is more reliable than
  adding prohibitions.
- **A failure beat must be written as a failure.** Asked for "the first
  attempt", the model produced a boy serenely airborne — which would have
  pre-empted the film's reversal three shots early. Fix: name the physics.
  "He is falling, not flying. He does not rise. He does not hover. One
  trainer is already back on the ground. There is no clear air beneath both
  feet."
- **Wardrobe drifts across re-rolls.** A re-rolled shot came back with a grey
  coat and black trousers where its neighbours had navy and dark green.
  Passing an already-approved neighbouring frame as a reference *and*
  naming the colours ("the coat is NAVY BLUE, not grey; the trousers are
  DARK GREEN, not black") fixed it.
- **`declined_preset_id` belongs inside `params`, not at batch level.** Eight
  video submissions were diverted to a preset recommendation. Passing the
  decline at the top level of the batch call does nothing; inside each
  request's `params` it works. Diverted submissions are not charged.
- **The sandbox does not survive between sessions.** Track masters, analysis
  scripts and build scripts were all gone at the start of this session.
  Masters were recovered from the Higgsfield media library and re-identified
  **by MD5**, not by filename; all three matched the recorded fingerprints
  and durations exactly.

