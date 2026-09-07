# CLOSING THE HOLES — NARRATION, FILLER, AND ACTION

Finaltouch's note: *"this movie makes no sense so far, a lot of loop holes… the actions
are little to none… I told you to add narration to the dialogue you didn't."*

All three are correct. This document is the fix.

---

## THE DIAGNOSIS

The 42-minute screenplay works. **The 12-minute cut kept every payoff and deleted every
setup.** Compare against the setup-and-payoff ledger in the structure document: eleven of
the thirteen payoffs still fire in the 12-minute version, but seven of their setups were
cut. That is the definition of a plot hole.

| The hole | What was cut that used to fill it |
|---|---|
| Why do they go at all? | There was never a decision scene, even at 42 minutes |
| Who are these seven people? | The boatyard gives one action each — too thin at this length |
| Mateo just disappears | The taking is off-screen by design; at 12 min it reads as missing |
| Liam is a stranger when he dies | **My error** — his face was cut to fit a 3-element cap |
| The island has no history | The 1974 camp, the bones, the torn-out notebook pages |
| Why don't they turn back after Mateo? | Nothing. This is the largest hole in the film |
| Why is Daniel dead with no wound? | Explained in dialogue, never set up |
| How does Ryan get out? | The escape is not shot |

---

## THE FIX THAT COSTS ALMOST NOTHING: RYAN NARRATES

Ryan is the only survivor. He is telling this afterwards. That frame closes **every hole
above except the escape**, and it costs about **0.2 credits per line** as generated audio
— roughly **3 credits for the whole film** instead of 195 per missing scene.

It also gives the film the thing it currently lacks entirely: a reason to care about six
people we barely meet.

### THE NARRATION SCRIPT

Timecodes are against the current 11:52 assembly.

**0:30 — over the fishing village**
> Six people went to that island because I asked them to. I want that said first, before
> anything else.

**0:45 — over Armando**
> An old man told me a story I did not believe. Then he put something on the table.

**1:00 — over the boatyard, the team packing** *(this single line introduces all seven)*
> Marcus had thirty years and a bad knee. Kofi had not spoken in two days, which is how he
> thinks. Mateo had a daughter and a dentist's bill. Daniel could count. Liam filmed
> everything, because he was twenty-six and nothing had happened to him yet. And Maya
> packed four times the blood-clotting agent she needed, because she was the only one of us
> taking it seriously.

**1:30 — still over the boatyard** *(the plan, and the greed)*
> Three days in, three days out, no contact. Seven ways. Every one of us had run harder
> jobs than that for less.

**2:15 — over the river mouth**
> The engine died a mile short of the creek. There were no insects. I have worked in six
> jungles. I have never been anywhere with no insects.

**3:00 — over the radio scene** *(closes the entire 1974 hole)*
> The settlement had been empty since nineteen seventy-four. Somebody had torn the pages
> out of the log book before they left. The radio still had charge in it, which should not
> have been possible, and we stood there and listened to a woman fifty years dead tell us
> not to go underground.

**3:45 — over the riverbank, before the aftermath**
> Mateo was talking. And then he was not there. No blood. No shot. Nobody heard anything.
> Thirty seconds, and we were six.

**4:45 — over the crossing** *(closes the largest hole in the film)*
> We should have turned around. I have had two years to work out why we did not, and the
> honest answer is that I had already decided, and nobody wanted to be the man who said it
> out loud.

**5:51 — over the far bank**
> Liam went on the far bank, climbing out of the water behind us. His camera was still
> running when we found it.

**6:51 — over the side passage**
> Daniel had no wound on him anywhere. Maya said his heart simply stopped. He had one in
> his sock that he had not told any of us about.

**7:21 — over the cavern camp**
> Maya worked it out by the lamp, with a loupe, at four in the morning. They were not
> diamonds. They had never once been diamonds.

**8:51 — over the sluice gate**
> Maya took the winch handle out of my hand. I want to be clear that she did not ask me.

**9:21 — over the deep chamber**
> Marcus walked out in front of me and fired at something a rifle was never going to stop,
> so that I would have four seconds. I used them.

**10:51 — over the doorway**
> I went to see his wife. I had an envelope and no words. She did not take the envelope.

**11:21 — over the final shot**
> I came out with three. I have spent every day since trying to decide whether I stole
> them, or whether she let me carry them out.
>
> *(beat, over the line moving inside the stone)*
>
> Last night, one of them moved.

**Voice:** Ryan's cast voice, dry and flat. Not dramatic. A man giving a statement.
**Cost:** ~15 lines of `generate_audio` at ~0.2 credits each = **≈3 credits.**

---

## FILLER SCENES STILL WORTH SHOOTING

Narration cannot do everything. Three gaps need picture.

| | Scene | Why it cannot be narrated | Credits |
|---|---|---|---|
| 1 | **THE DECISION** — Ryan puts the photograph and the diamond on a table in front of Marcus. Names the split. Marcus says the thing that makes him right later, and comes anyway | The audience must watch him choose this, or he is not the protagonist | 195 |
| 2 | **MATEO TAKEN** — his face, alone at the water's edge, mid-sentence. A beat. Empty water. His rifle turning on its sling | The first death is the turn of the film. Narration over a gap is still a gap | 195 |
| 3 | **THE ESCAPE** — Ryan through the crawl, the wire, the roof coming down, water | The film currently cuts from Marcus dying to Ryan in a boat. He teleports | 195 |

---

## THE ACTION PROBLEM

Finaltouch is right: **there are two action beats in twelve minutes** — Kofi's corridor and
Marcus firing. For a creature film that is far too thin, and it is a structural consequence
of the never-show-her rule being applied everywhere instead of selectively.

**She stays off-screen. The violence does not have to.** Four beats, none of which require
her to be rendered:

| | Beat | What is on screen | Credits |
|---|---|---|---|
| A | **The stern goes** — night, the boat, something takes the outboard and a man goes over the side. Torches, shouting, water | Water, men, a broken transom | 195 |
| B | **Mateo taken** (also fills a story hole) | A face, then no face | 195 |
| C | **The hatchlings, extended** — the run through the passages before Kofi stops. Muzzle flash, water, young snakes at forearm thickness | Small snakes, which render fine | 195 |
| D | **The escape** (also fills a story hole) | Rock, water, dust, one man running | 195 |

B and D do double duty — story hole and action beat in the same clip.

---

## PRIORITY AND COST

| Tier | What | Credits |
|---|---|---|
| **0** | **The full narration pass** — closes seven holes | **≈3** |
| 1 | Mateo taken (hole + action) | 195 |
| 2 | The escape (hole + action) | 195 |
| 3 | The decision scene | 195 |
| 4 | The stern goes (action) | 195 |
| 5 | Extended hatchlings (action) | 195 |
| 6 | Far bank rebuilt with Liam's face | 195 |

**Tier 0 alone changes the film more than any single clip, and costs three credits.**
Tiers 0–3 = **≈590** and fix every structural complaint.
All of it = **≈1,173.**

---

## THE RULE THAT WAS MISSED

**Whoever the film is about to take must be recognisable in the shot immediately before it
takes them.** The creature stays hidden. The person never does. Liam was made faceless to
satisfy a rendering constraint, and the loss went with the face.
