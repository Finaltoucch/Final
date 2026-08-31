# GRAVITY WELL
### ALEXATOR — AI Short Video · Creative Bible & Production Spec

**Track:** ALEXATOR — *Rise Again* (album: ALEXATOR.COM)
**Fragment:** 00:58.510 → 01:42.204 of the original master
**Duration:** 43.694 s · **Format:** vertical 9:16, 1080×1920, 30 fps, MP4, stereo

---

## 1. The idea

A woman stands on a wet rooftop at night. The rain stops falling — and begins
falling **upward**. As the track builds, every body of water in the city peels off
the ground and rises: puddles, gutters, fountains, the river. On the drop she steps
off the roof edge and does not fall down. She falls **up**, accelerating into a
suspended ocean hanging above the skyline. The final image reveals her weightless
inside that ocean, and far below her, through clear water, the city glittering like
a galaxy.

**Why this and not a visualiser.** The brief rejects "a random collection of
attractive AI shots." This is a single physical premise — *gravity has inverted for
water, and then for her* — carried through four escalating stages with one character,
one continuous location, and an emotional arc from unease to surrender to peace.
Every shot is a consequence of the shot before it.

**Why it is built for 9:16.** The concept's only axis is vertical. Water rises up the
frame; the character rises up the frame; the reveal is a vertical stack — ocean above,
woman centre, city below. The format is not a crop applied to the idea; the format
*is* the idea. A 16:9 version of this video would be materially worse, which is the
test of a genuinely vertical concept.

**Title resonance.** The track is called *Rise Again*. The video is about rising.
The relationship between the two is legible without a single word on screen — which
matters, because on-screen text is prohibited.

---

## 2. Why this fragment

Analysis of the full 3:24.62 master (see `01_MUSIC_ANALYSIS.md` for method and data):

- **Tempo:** 136.060 BPM · beat 0.44098 s · bar 1.76393 s · first downbeat 0.300 s
- The fragment is **bar 33 → bar 57**, exactly **24 bars = three 8-bar phrases**, plus
  a 1.36 s decay tail. Both edit points sit on true downbeats, not arbitrary timestamps.

It was selected because its internal shape matches the story beat for beat:

| Musical event | Bar | Video time | Story beat |
|---|---|---|---|
| Kick falls away, breakdown | 33 | `0.000` | Rain reverses |
| **Kick slams back — the drop** | **41** | **`14.111`** | **She steps off the edge** |
| 1.76 s breath, kick drops out | 47 | `24.695` | She breaks the ocean surface |
| Second wave, sustained | 49 | `28.223` | Weightless inside the water |
| Breath before re-entry | 57 | `42.334` | The reveal — fade begins |

The bar-47 breath is the reason this fragment beats every other candidate window: the
track opens a natural 1.8-second hole in the drums exactly where the story needs a
transition. That silence carries the breach into the ocean. It cannot be manufactured
in the edit — it is in the music, and the visual was written to it.

**Fades.** Fade-in 0.35 s; fade-out 1.36 s. Critically, the fade-out lives **entirely
in the material after bar 57** — all 24 bars of the body play at full level. The brief
warns that a fade "should not unnecessarily remove several seconds of useful music";
here it removes none. This is only possible because the cut was made from the full
master rather than a pre-trimmed clip.

**Measured:** 43.694 s · −13.5 LUFS integrated · LRA 2.5 LU · true peak −4.6 dBFS.

---

## 3. Character lock

One character. Fictional, AI-generated, unmistakably an adult. No real-person
reference of any kind.

| Attribute | Locked value |
|---|---|
| Age read | Late 20s to early 30s |
| Build | Slim, average height |
| Hair | **Long, dark, wet** — non-negotiable: it is the visual tell for the gravity flip |
| Skin | Pale-olive, cool highlights from above, warm bounce from below |
| Wardrobe | Unstructured charcoal-grey long coat, no buttons, no hardware, no logo |
| Under | Plain pale-grey top, dark trousers, simple dark ankle boots |
| Accessories | **None.** No jewellery, no watch, no bag, no phone |
| Emotional arc | Unease (01–03) → wonder (04) → surrender (05–07) → peace (08–11) |

The coat and the long hair do the storytelling work: both hang normally in shot 01
and both rise for the rest of the film. That single continuity detail is what makes
the inverted gravity readable without narration.

---

## 4. Palette & lighting continuity

- **Sky / ground:** deep teal-black, `#0B1418`
- **City glow (from below):** warm sodium amber, `#D9915A`
- **Water / air (from above):** cyan-silver, `#BFE9F2`
- **Water** always reads luminous cyan-silver, never muddy or grey-brown

**The lighting rule, applied to every shot without exception:** cool light from
above, warm light from below. It is the continuity anchor across eleven separately
generated clips and the fastest way to make independent generations feel like one
photographed piece. Any shot that violates it gets regenerated.

---

## 5. Shot list

Cuts fall on bar lines. `Δ` is shot duration; `Gen` is what to request from the model
(always longer than needed, so the edit has handles).

### Act I — THE ANOMALY · bars 33–41 · `0.000–14.111` · breakdown, kick absent

| # | Bars | In | Δ | Gen | Shot |
|---|---|---|---|---|---|
| 01 | 33–35 | `0.000` | 3.528 | 5 s | **HOOK.** Macro on wet rooftop concrete. Raindrops strike, stop, and lift back off the surface, rising out of frame. Rack focus to her boots behind them. |
| 02 | 35–37 | `3.528` | 3.528 | 5 s | Low angle on her face, upturned. Rain streams upward past her cheeks. Her hair begins to lift at the ends. |
| 03 | 37–39 | `7.056` | 3.528 | 5 s | Wide. She is small in a vast rooftop. Columns of water rise from every puddle around her like slow reversed fountains. |
| 04 | 39–41 | `10.584` | 3.528 | 5 s | From the roof edge, city beyond. Ribbons of water peel off a hundred rooftops and a distant river, all climbing. Slow push in as the riser builds. |

### Act II — THE FALL UPWARD · bars 41–47 · `14.111–24.695` · the drop

| # | Bars | In | Δ | Gen | Shot |
|---|---|---|---|---|---|
| 05 | 41–43 | `14.111` | 3.528 | 5 s | **ON THE DROP.** She steps off the edge — and falls **up**. Coat and hair snap upward. Camera falls with her; the roof recedes below at speed. |
| 06 | 43–45 | `17.639` | 3.528 | 5 s | Acceleration. Rushing upward through the rising water columns, city light smearing into vertical streaks. |
| 07 | 45–47 | `21.167` | 3.528 | 5 s | From far below: her silhouette shrinking against the underside of a vast silver ceiling of water that fills the sky. |

### Act III — THE BREACH · bars 47–49 · `24.695–28.223` · the breath

| # | Bars | In | Δ | Gen | Shot |
|---|---|---|---|---|---|
| 08 | 47–49 | `24.695` | 3.528 | 5 s | **THE BREATH — near-silence.** Slow motion. She breaks through the underside of the suspended ocean, the water membrane parting and beading around her body. |

### Act IV — WEIGHTLESS · bars 49–57 · `28.223–42.334` · second wave

| # | Bars | In | Δ | Gen | Shot |
|---|---|---|---|---|---|
| 09 | 49–51 | `28.223` | 3.528 | 5 s | Inside the ocean. She decelerates; coat and hair bloom outward in every direction. Bubbles trail downward — *toward the city*. |
| 10 | 51–54 | `31.751` | 5.291 | 6 s | She opens her eyes. Arms drift open. Peace. Shafts of moonlight from the surface far above. |
| 11 | 54–end | `37.042` | 6.652 | 8 s | **THE REVEAL.** Camera pulls back and rotates. Below her, through clear water, the city glitters like a galaxy. She hangs weightless between ocean and city. Holds through the fade. |

**Total: 11 shots, 43.694 s.**

---

## 6. Compliance checklist (brief §4 and §5)

Applied as a negative prompt on every generation and verified on every clip:

- No on-screen text of any kind — no subtitles, no signage, no readable random glyphs
- No logos, trademarks, branded vehicles, clothing, devices or packaging
- No real-person likeness, no celebrity resemblance, no deepfake, no voice
- The official ALEXATOR hero and universe are **not** referenced in any form
- No other people in frame — removes the background-character artifact risk entirely
- No weapons, violence, blood, drugs, smoking, alcohol, extremist or political content
- Character unambiguously adult; no nudity; no sexualised content
- No dialogue and no voiceover — ALEXATOR music is the sole audio element

**Quality gate per clip** (brief §5): faces, eyes, hands and fingers; body movement;
object and water physics; reflections and shadows; character consistency; clothing
continuity; location continuity; lighting continuity; flicker; deformation;
disappearing objects; sudden changes in facial proportion. Any clip failing on any
line is regenerated, not patched.

---

## 7. Delivery package (brief §7)

1. `01_FINAL_ALEXATOR_Rise_Again.mp4` — 9:16, 1080×1920, 43.694 s, 30 fps, stereo, no watermark
2. `02_USED_AI_SOURCES.zip` — only the generations actually used, at original export quality
3. `03_ORIGIN_PROOF.pdf` — services and plan, generation dates, per-service material map,
   commercial-use terms links, workspace screenshots, editing-timeline screenshot,
   track title **Rise Again**, music in/out **00:58.510 → 01:42.204**

Source generations, project file and generation history retained **90 days** post-acceptance.
