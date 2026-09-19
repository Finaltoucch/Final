# WHERE THE SOUND IS — Production Bible

**Project 7 of the ALEXATOR engagement.** Track: *Never Let Go* (019).
Register: **arrival** — the moment music stops being background and pulls you in.

## Concept

A young Black American woman sits alone outside a party, bored, on a concrete step in a cold
wet alley beside a heavy metal door. Coloured light pulses out from under it.
She isn't listening — until her fingers start tapping the concrete on their own,
in time, before she notices.

She stops. She looks at the door. She gets up, crosses the few steps, and opens
it. Light and sound blast out over her. She moves through the crowd, and
somewhere in that crossing her face changes completely. She keeps going until
she is at the front, under the truss, looking up at the DJ.

That's the whole film. One decision and one walk.

## Why this one works

- **Register is unused.** Joy, mastery, consequence-over-time, kindness, wonder
  — none of them is *being pulled out of yourself by sound*.
- **It's structurally a music video, not a story with music on it.** The door is
  the drop. Everything before it is the build. No previous film in this set has
  had the picture and the arrangement do the same thing at the same instant.
- **Maximum contrast with all six predecessors.** Night, interior, neon, crowd,
  motion. Against a desert, a forge, a night train, a suburban street and a
  workshop, it shares no palette and no tempo with any of them.
- **It's completely realistic.** A person outside a party who decides to go in.
  Nothing supernatural, nothing impossible.

## The one hard structural rule

**Shot 07 — the door opening — must land exactly on the drop.**

Everything before it is cold, blue-grey, desaturated, quiet, largely static
camera, one person alone. Everything after it is saturated, moving, crowded,
lit. The cut is the drop. If that lands even a few frames off, the film loses
its entire reason to exist, so the bar grid gets anchored to the drop first and
the shot lengths are fitted around it, not the other way round.

## Deliberate colour break — NOT a defect

Shots 01–06 are cold (blue-grey, low saturation). Shots 07–11 are warm and
heavily saturated (magenta, cyan, amber).

The post-assembly per-channel colour check will therefore show a **strong warm
cast from shot 07 onward**. That is intended and is the point of the film. On
LAST TRAIN a warm cast was a defect I had written into my own prompt; here it is
the design. Noting it so a later QC pass doesn't flag the film as broken.

## Age and venue — brief compliance decisions

- **She is a Black American woman of about twenty-two, clearly an adult, with long
  dark box braids.** Specified by the client. The brief prohibits minors
  in unsafe situations, and a nightclub interior is exactly that. Set at ~22 and
  written into the character sheet so it holds across every shot.
- **This is a music event, not a drinking event.** No alcohol, no bottles, no
  glasses, no bar, no smoking, no vaping, no drugs anywhere in frame. Written as
  an explicit negative on every interior prompt.
- **No sexualised dancing and no physical contact between strangers.** The crowd
  is people facing the music with their hands up, which is also what real crowds
  at this kind of event look like.
- **No brand names or logos** on clothing, equipment, the booth or the walls.

## The crowd problem, and the fix

Crowds are the single hardest thing for these models — background faces warp,
limbs merge, hands multiply. This is the main technical risk in the project.

The fix is also what real club footage looks like, so it costs nothing
dramatically:

- The crowd is **backlit and silhouetted** in every shot it appears in.
- Background faces are **out of focus** and never sharp in the foreground.
- Motion blur and haze carry the density rather than detail.
- **Only the hero character is ever in focus.**
- Explicit negatives on every crowd shot: no sharp background faces, no
  distorted faces, no extra limbs, no merged bodies, no duplicate people.

## Shot plan

Bar allocations are provisional and get fixed once the track is measured. The
drop lands on the head of shot 07.

| # | Bars | Act | Shot |
|---|---|---|---|
| 01 | 2 | OUTSIDE | Hook. Her face in near-dark, coloured light pulsing across it from the doorway. She is still; only the light moves. |
| 02 | 2 | OUTSIDE | Wide. Alone on the step beside the grey metal door, wet empty alley, one thread of colour in a puddle. |
| 03 | 2 | OUTSIDE | Close on her hand. Fingers tapping the concrete in time, involuntarily. The puddle trembling on each beat. |
| 04 | 2 | OUTSIDE | Her face. The tapping stops. Her eyes come up and fix on the door. |
| 05 | 2 | OUTSIDE | Low angle. She rises into frame off the step, the strip light over the door catching her. |
| 06 | 2 | THRESHOLD | Behind her. The few steps to the door, empty alley receding, her hand coming up to the handle. |
| 07 | 2 | **DROP** | **The door swings open.** Light and haze blast out over her. She is a silhouette against it; the alley behind her floods magenta. |
| 08 | 2 | INSIDE | Behind her head, moving. Into the crowd — bodies and raised hands streaking past in silhouette, beams cutting across. |
| 09 | 3 | INSIDE | Her face, close. The moment it changes. Colour moving across her skin, hair lifting, the beginning of a real smile. |
| 10 | 2 | INSIDE | From beside her, forward. Raised hands in silhouette, the truss above, the booth glowing at the far end through haze. |
| 11 | 3 | ARRIVAL | She reaches the front. The DJ backlit to near-silhouette, hands working. She looks up into the light. Held. |

**24 bars total, drop at bar 12** — a symmetrical 12-bar build and 12-bar
payoff. If the supplied track builds over 16 bars instead, this goes to 32 bars
(~57 s at 135 BPM, still inside the 30–60 s requirement) with the extra length
absorbed into shots 02–05 and 09–11 rather than by adding shots.

## Consistency architecture

Three reference sheets, generated first, passed as `image_references` into every
keyframe — same architecture that has held across the last four films.

| Reference | Purpose |
|---|---|
| The young woman (~22, braids) | Split-screen sheet, full body + close-up on white |
| Location A — exterior | The grey metal door, black downpipe to its left, low concrete step, puddle. Cold blue-grey. |
| Location B — interior | Overhead light truss, raised DJ booth silhouette at the far end, haze, magenta/cyan/amber scheme. |

The DJ gets no sheet. They are backlit to near-silhouette in the two shots they
appear in, so a sheet would buy nothing — saves 2 credits.

## Wardrobe (fixed across all 11 shots)

Dark charcoal oversized jacket, plain cream crew-neck top, dark indigo jeans, white
trainers, long dark box braids past the shoulders, small plain gold hoop earrings,
no other jewellery, no watch, no logos or text on any garment.

Cream reads cleanly under saturated coloured light, which keeps her separable
from a silhouetted crowd without needing a key light that wouldn't exist in the
room.

## Carried-forward defect guards

From LAST TRAIN and WHAT THE SAND KEEPS, written directly into the prompts:

- **Hands (shots 03, 06, 11):** explicit "exactly five normal fingers", "skin
  clean and unblemished with no cut, wound, scratch, mark or blemish".
- **Character continuity:** no shot between two populated shots is ever written
  as empty. LAST TRAIN lost both characters for one shot because I designed an
  empty frame in the middle of the film.
- **No unintended light sources:** every coloured light in every shot is
  motivated by the truss, the booth or the doorway. No stray streaks.
- **Cloth stability:** on the two held closing shots the camera is locked or
  near-locked and the subject is near-still. LAST TRAIN warped a coat during a
  push-in on a static figure.

## Cost

| Stage | Model | Credits |
|---|---|---|
| 3 reference sheets | `nano_banana_pro` 2K | 6.00 |
| 11 keyframes | `nano_banana_pro` 2K | 22.00 |
| 11 clips (9 × 5 s, 2 × 6 s) | `kling3_0` pro, silent | 85.50 |
| **Total** | | **113.50** |

**Available: 103.33. Short by ~11.** Needs a top-up before the clip batch.
