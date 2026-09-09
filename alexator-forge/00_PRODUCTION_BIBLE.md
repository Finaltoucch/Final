# FORGE
### ALEXATOR — *Through the Fire* · AI Short Video · Production Bible

**Status:** fully staged. Fragment locked and verified. Every prompt written.
Blocked only on Higgsfield credits (balance 0.95, needs ~200).

---

## 1. The idea

A blacksmith's workshop at night. One woman, working steel.
**Cold → heat → transformation → completion** — which is what the music does, and what
the title says.

Every frame is a real thing a camera could photograph: fire, steel, sparks, steam, hands.
No invented physics. That was the lesson from the first concept of the previous project —
imagined physics renders as mush; real materials render beautifully, and fire and sparks
are something the video models are genuinely good at.

**Distinct from RIDE HOME on every axis:** adult not child, night not day, interior
industrial not suburban exterior, orange-on-black not golden pastel, physical force not
gentle drift.

---

## 2. Track and fragment

| | |
|---|---|
| Title (ID3) | **Through the Fire** |
| Artist / album | ALEXATOR / ALEXATOR.COM |
| Source | MP3 320 kb/s, 48 kHz stereo, 233.52 s |
| **Tempo** | **136.010 BPM** · beat 0.44114 s · bar 1.76458 s · 8-bar phrase 14.1166 s |
| Grid anchor | the drop at **137.474 s** absolute |
| **Music in** | **02:03.357** (123.357 s) — phrase downbeat |
| **Body end** | 165.707 s — phrase downbeat, t+42.350 |
| **Music out** | **02:46.107** (166.107 s) |
| Duration | **42.750 s** = 1026 frames @ 24 fps |
| Fade in / out | 0.35 s / 0.30 s from t+42.45 |

Measured on the rendered cut: **−13.4 LUFS**, LRA 2.8 LU, true peak **−4.4 dBFS**.

### Grid validation

Anchoring the bar grid on the drop explains every section boundary in the track:

| phrase | predicted | observed | delta |
|---|---|---|---|
| k=−3 | 95.124 | kick returns strong | −0.12 s |
| k=−1 | 123.357 | kick drops out | +0.64 s |
| **k=0** | **137.474** | **the drop** | −0.47 s |
| k=+3 | 179.824 | heavy | +0.18 s |
| k=+4 | 193.941 | heavy | +0.06 s |
| k=+5 | 208.057 | heavy | −0.06 s |
| k=+6 | 222.174 | peak kick | −0.17 s |

Two independent methods agreed on tempo: flux autocorrelation peaked at 136.0, and the
comb fit landed on 136.010. Raw on-grid counts favour faster grids (a 2× grid trivially
catches every 1× hit plus the off-beats), so the autocorrelation peak was taken as
authoritative. The result is within 0.05 BPM of *Rise Again* — same artist, same tempo.

### Why this fragment

Measured level across the void, 0.25 s steps:

```
t+13.50  -20.5      t+14.00  -11.2   <- THE DROP
t+13.75  -31.1      t+14.25  -11.5
```

A **20 dB jump in a quarter second**, immediately after 1.5 s of near-silence. It is the
strongest edit point available in either ALEXATOR track worked on so far.

---

## 3. Character lock

Fictional, AI-generated, unmistakably an adult. No real-person reference of any kind.

| Attribute | Locked value |
|---|---|
| Age read | Early-to-mid thirties |
| Build | Strong, capable, working physique |
| Hair | Dark, tied back tightly and out of the way |
| Wardrobe | Heavy brown leather apron over a plain dark long-sleeved shirt, sleeves rolled |
| Hands | Thick leather work gloves |
| Eyes | Clear safety glasses — skilled work, correctly protected |
| Accessories | **None.** No jewellery, no watch, no branding anywhere |
| Emotional arc | Stillness (01–04) → concentration (05) → force (06–08) → satisfaction (09–12) |

**The forged object is an abstract spiral form or a simple hook — never a blade.**
This keeps the piece clear of the brief's weapons prohibition.

---

## 4. Palette & lighting

- **Darkness:** near-black workshop, `#0A0806`
- **Forge core:** white-hot to orange, `#FFD9A0` → `#FF7A18`
- **Cold light:** thin blue-grey moonlight through a high window, `#8FA6B8`

**The lighting rule, applied to every shot:** the forge is the only warm source and it is
always *inside* the frame or just off it, motivated. Cold blue-grey fills the rest. As the
piece progresses, warm light takes over more of the frame — the palette itself tells the
story. Any shot that breaks it gets regenerated.

---

## 5. Shot list

Cuts fall on bar lines. Frame counts are exact and cumulative, so no rounding drift
accumulates across the edit.

| # | bars | in (t+) | frames | Δ | gen | shot |
|---|---|---|---|---|---|---|
| 01 | 0–2 | `0.000` | 85 | 3.54 | 5 s | **HOOK.** Macro on dead grey coals in the dark. One ember wakes and crawls orange across the ash. |
| 02 | 2–4 | `3.529` | 84 | 3.50 | 5 s | Cold workshop details — still hammer, hanging tongs, dust in a shaft of moonlight. She enters, ties the leather apron. |
| 03 | 4–6 | `7.058` | 85 | 3.54 | 5 s | She works the bellows. The coals breathe and bloom. Orange climbs her face. |
| 04 | 6–7 | `10.587` | 42 | 1.75 | 3 s | Steel goes into the fire. Close on the bar sinking into the glowing bed. |
| 05 | 7–8 | `12.352` | 43 | 1.79 | 3 s | **THE VOID.** She draws the steel out — white-hot, blinding. Everything else falls to black. Held, dead still. |
| 06 | 8–10 | `14.117` | 84 | 3.50 | 5 s | **THE DROP.** Hammer strike. Sparks explode across the frame. |
| 07 | 10–12 | `17.646` | 85 | 3.54 | 5 s | Rhythmic hammering, a spark burst on every accent. |
| 08 | 12–14 | `21.175` | 85 | 3.54 | 5 s | Her face lit orange from below, sweat, absolute focus. |
| 09 | 14–15 | `24.704` | 42 | 1.75 | 3 s | The spiral shape emerging on the anvil under the hammer. |
| 10 | 15–16 | `26.469` | 43 | 1.79 | 3 s | **THE BREATH.** She stops. Lifts the piece to the light. Examines it. |
| 11 | 16–20 | `28.233` | 169 | 7.04 | 9 s | **QUENCH.** The piece plunges into the water trough. Steam erupts violently. |
| 12 | 20–end | `35.292` | 179 | 7.46 | 9 s | The finished form cooling, her gloved hands turning it. The workshop settling. Final look. |

**Total 1026 frames = 42.750 s. Generated footage 60 s.**

---

## 6. Compliance (brief §4 and §5)

Negative-prompted on every generation and verified on every clip:

- No on-screen text of any kind — no signage, no readable glyphs
- No logos, trademarks, branded tools, clothing or equipment
- No real-person likeness, no celebrity resemblance, no deepfake, no voice
- The official ALEXATOR hero and universe are **not** referenced in any form
- No other people in frame — removes background-character artifact risk entirely
- **No blade, no weapon** — the forged object is an abstract spiral or hook
- Correct protective equipment throughout: apron, gloves, eye protection. Skilled work, not danger
- No violence, blood, drugs, smoking, alcohol, extremist or political content
- Character unambiguously adult; no nudity; no sexualised content
- No dialogue and no voiceover — ALEXATOR music is the sole audio element

**Quality gate per clip:** faces, eyes, hands and fingers; grip on tools; body movement;
fire, spark and steam physics; reflections; character consistency; clothing continuity;
lighting continuity; flicker; deformation. Any clip failing any line is regenerated.

---

## 7. Cost

Kling v3.0 pro/silent bills a flat **1.5 credits per second generated** (measured, not quoted).

| Phase | Credits |
|---|---|
| 1 character reference (nano_banana_pro) | 2.00 |
| 12 keyframes @ 2.00 | 24.00 |
| 12 clips, 60 s @ 1.5/s | 90.00 |
| Music cut, assembly, encode, packaging, origin proof | 0 |
| **Clean first pass** | **116.00** |
| Expected, with keyframe iteration and 3–4 retries | ~156 |
| Plus one client revision round | ~190 |
| Ceiling | ~215 |

**Budget ~200.**

---

## 8. Delivery package (brief §7)

1. `01_FINAL_ALEXATOR_Through_the_Fire.mp4` — 9:16, 1080×1920, 42.75 s, 24 fps, stereo, no watermark
2. `02_USED_AI_SOURCES.zip` — only the generations used, original export quality
3. `03_ORIGIN_PROOF.pdf` — services, plan, dates, per-service materials, commercial-use links,
   screenshots, timeline, track title **Through the Fire**, music in/out **02:03.357 → 02:46.107**
4. Freelancer confirmation posted in the Contra chat

Source generations, project file and history retained **90 days** post-acceptance.

**Deadline: 13 September.**
