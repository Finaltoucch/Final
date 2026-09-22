# SATURDAY — Production Bible

**Project 8 of the ALEXATOR engagement.** Track: *Just Relax* (020).
Delivered 22 September 2026. Register: **ease.**

## Concept

A woman in her late twenties, a small flat, a hot Saturday morning with nothing
in it. She crosses warm floorboards barefoot, pours coffee, pushes the window
open and leans out of it looking at a day with no plans. Then — because nobody
is watching — she turns the speaker on and dances badly and happily around her
own kitchen. It ends with her sat on the floor under the window, out of breath,
grinning, the whole day still ahead of her.

## How the concept was chosen

I arrived with a different film ready — **GOING IN**, a cold-sea swim, register
courage. Measuring the track killed it.

*Just Relax* is a 133 BPM groove with the kick present 68% of the track, and a
**sparse intro carrying no kick at all for its first 36 seconds**. A panic-and-
shock film would have fought that. The measurement said ease, so the concept
changed to match.

Lesson worth keeping: **measure the track before committing to a concept.** The
title alone would have misled in the other direction — "Just Relax" sounds
downtempo and isn't.

## Register across the engagement

| # | Film | Track | Register |
|---|---|---|---|
| 1 | GRAVITY WELL | Rise Again | *rejected* |
| 2 | RIDE HOME | Rise Again | joy |
| 3 | FORGE | Through the Fire | mastery |
| 4 | THE LONG WORK | By Your Side | consequence over time |
| 5 | LAST TRAIN | All for You | kindness |
| 6 | WHAT THE SAND KEEPS | Endless Sands | wonder / deep time |
| 7 | WHERE THE SOUND IS | Never Let Go | arrival |
| 8 | **SATURDAY** | **Just Relax** | **ease** |

## The structural idea

Shots 01–06 play over the track's **kickless intro** — the morning before she
has put any music on. The drop lands on the cut to shot 07, which is the moment
she presses play.

The music starting inside the story and the music starting in the track are the
same event. This is a stronger version of the door in WHERE THE SOUND IS: there
the drop coincided with a story beat, here it *is* the story beat.

## Consistency architecture

Two reference sheets, generated first, passed as `image_references` into every
keyframe. One character and one room means two sheets instead of three.

| Reference | Job ID |
|---|---|
| The woman (~28, natural curls) | `8de79da8-7756-407f-b89f-c525caac9b9a` |
| The flat (two-panel, empty of people) | `d24d5aca-cfe9-4a94-ac13-2fc5a79217c6` |

## Shot inventory

| # | Bars | In (s) | Frames | Shot |
|---|---|---|---|---|
| 01 | 0–2 | 0.000 | 86 | The curtain breathing in the breeze, backlit white. Hook — movement in frame one. |
| 02 | 2–4 | 3.583 | 86 | Bare feet crossing floorboards through a stripe of sunlight. |
| 03 | 4–6 | 7.167 | 86 | Coffee pouring, steam turning over in a shaft of light. |
| 04 | 6–8 | 10.750 | 87 | She pushes the sash window open; light floods in. |
| 05 | 8–10 | 14.375 | 86 | Leaning **out** of the window on her forearms, looking down the street. |
| 06 | 10–12 | 17.958 | 86 | Macro: fingertip pressing one round button. The last frame before the beat. |
| 07 | 12–14 | 21.542 | 86 | **THE DROP.** She spins in the sunlight, grin breaking, dust blazing. |
| 08 | 14–16 | 25.125 | 86 | Floor level: bare feet dancing in and out of the light. |
| 09 | 16–19 | 28.708 | 130 | Her face, laughing helplessly, the sun bar travelling across it. |
| 10 | 19–21 | 34.125 | 86 | Wide: the whole flat, her alone in a block of sun. |
| 11 | 21–24 | 37.708 | 129 | Sat on the floor under the window, out of breath, grinning. Held. |

Cumulative: 86, 172, 258, 345, 431, 517, 603, 689, 819, 905, **1034**.

## Risk handling

**Dancing bodies** are this film's version of the crowd problem in WHERE THE
SOUND IS. Sustained full-body choreography is where these models fail hardest,
so the dance is shot in fragments — feet, a turn, a face, one wide — never as
continuous whole-body movement. Every dance prompt carries explicit five-finger
and five-toe constraints plus "no extra limbs, no distorted joints".

**Modesty.** One woman alone in a flat needs deliberate handling. Wardrobe is a
loose oversized t-shirt and loose trousers, fully covered; every prompt carries
explicit negatives against suggestive framing, glamour styling and undress; the
framing is documentary throughout.

## Client corrections during production

| Frame | Note | Cause |
|---|---|---|
| 05 | "she should be leaning towards outside the house not inside" | **My error.** The keyframe put her on an interior shelf facing into the room. Rebuilt leaning out through the open window, back to the room. |
| 06, 10, 11 | *(found by me on review)* the portable speaker carried a visible brand logo | Model added branding despite negatives on both the location sheet and the keyframes. |

**The branding fix is worth recording.** The obvious move was to regenerate the
location reference sheet — but that would have changed the room and broken
continuity with the eight shots already correct. Instead the three affected
frames were reframed so branding had nowhere to appear: shot 06 became an
extreme macro showing only a fingertip and one unmarked button, and the speaker
was removed from 10 and 11 entirely. Continuity preserved, compliance restored,
8 credits instead of a full rebuild.

## Cost

| Stage | Model | Credits |
|---|---|---|
| 2 reference sheets | `nano_banana_pro` 2K | 4.00 |
| 11 keyframes | `nano_banana_pro` 2K | 22.00 |
| Keyframe 05 rebuild | `nano_banana_pro` 2K | 2.00 |
| Keyframes 06, 10, 11 rebuild | `nano_banana_pro` 2K | 6.00 |
| 11 clips (9× 5 s, 2× 6 s) | `kling3_0` pro, silent | 85.50 |
| **Total** | | **119.50** |
