# WHAT THE SAND KEEPS — Production Bible

**Project 6 of the ALEXATOR engagement.** Track: *Endless Sands* (018).
Delivered 19 September 2026. Register: **wonder / deep time.**

## Concept

A girl of about ten crosses a vast dune field with her grandfather in hard
late-afternoon sun. She catches a pale curve in the sand, kneels, brushes it
clear — a fossil ammonite. He lowers himself beside her. He knows what it is;
she does not yet. Neither of them speaks. The film pulls back to leave them as
two specks in an ocean of sand that was once a sea.

Nothing supernatural, nothing impossible. A real object, a real desert, a real
thing that happens to children who look down.

## Register across the engagement

| # | Film | Track | Register |
|---|---|---|---|
| 1 | GRAVITY WELL | Rise Again | *rejected* |
| 2 | RIDE HOME | Rise Again | joy |
| 3 | FORGE | Through the Fire | mastery |
| 4 | THE LONG WORK | By Your Side | consequence over time |
| 5 | LAST TRAIN | All for You | kindness |
| 6 | **WHAT THE SAND KEEPS** | **Endless Sands** | **wonder / deep time** |

## Consistency architecture

Three reference sheets generated first, then passed as `image_references` into
every keyframe. This is what holds one girl, one grandfather and one landscape
across eleven separately generated shots.

| Reference | Job ID |
|---|---|
| Girl (~10) — split-screen, full body + close-up on white | `81bd5666-1072-458f-b3c2-30ccd61938a3` |
| Grandfather (~75) — split-screen, full body + close-up on white | `9b3ea8a2-f2eb-4a89-848a-ce8ae670f280` |
| Location — two-panel dune field, shared dark rock outcrop + crescent dune | `4e6e3285-cb85-4825-9769-775cf5465c31` |

Both characters are entirely fictional. No real person referenced at any stage.

## Shot inventory

| # | Bars | In (s) | Frames | Shot |
|---|---|---|---|---|
| 01 | 0–2 | 0.000 | 85 | Macro on the dune crest; sand streaming off the ridge. The hook — movement in frame one. |
| 02 | 2–4 | 3.542 | 85 | Wide. Two tiny figures walking the crest, footprints trailing, heat shimmer on the horizon. |
| 03 | 4–6 | 7.083 | 85 | Low tracking at sand level on her running feet; she slows and stops. |
| 04 | 6–8 | 10.625 | 85 | The grandfather, unhurried, watching her stop. Almost no expression. |
| 05 | 8–10 | 14.167 | 85 | She holds still mid-turn, then begins to lower herself toward the ground. |
| 06 | 10–12 | 17.708 | 86 | Macro. Grains sliding off an exposed curve of pale stone. Nothing else moves. |
| 07 | 12–15 | 21.292 | 127 | Her hand sweeping the sand clear in three strokes until the coil sits exposed. |
| 08 | 15–18 | 26.583 | 128 | The fossil in her open palm, turning in the low sun. **The music empties out here.** |
| 09 | 18–20 | 31.917 | 85 | He settles onto his heels beside her; quiet recognition. He does not reach for it. |
| 10 | 20–22 | 35.458 | 85 | His fingertips tilt her palm to the light. She looks up at him, waiting. |
| 11 | 22–24 | 39.000 | 85 | One unbroken rise and pull-back until they are two specks in an ocean of sand. |

Cumulative: 85, 170, 255, 340, 425, 511, 638, 766, 851, 936, **1021**.

## Carried-forward defect guards

Lessons from LAST TRAIN written directly into the prompts for this film:

- **Hand shots (07, 08):** explicit "exactly five normal fingers", "skin clean
  and unblemished with no cut, wound, scratch, mark or blemish appearing at any
  point". LAST TRAIN shipped a visible finger wound because the wound was
  written into my own prompt.
- **No unintended warm cast:** the light is motivated hard late sun throughout,
  never a stray coloured streak. LAST TRAIN's "warm orange streak of passing
  light sweeping across her hand" was my own prompt error.
- **Character continuity across cuts (09, 10, 11):** "Exactly two people in the
  shot throughout; no third person enters the frame" and "He never takes it from
  her — it stays in her hands the whole time." LAST TRAIN lost both characters
  for one shot because I designed an empty frame between two populated ones.

## Models and cost

| Stage | Model | Cost |
|---|---|---|
| 3 reference sheets | `nano_banana_pro` 2K | 6.00 |
| 11 keyframes | `nano_banana_pro` 2K | 22.00 |
| 11 clips (9× 5 s, 2× 6 s) | `kling3_0` pro, silent | 85.50 |
| **Total** | | **113.50** |

Balance 216.83 → 103.33. No unexplained spend during this project.
