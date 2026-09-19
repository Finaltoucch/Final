# WHERE THE SOUND IS — v2 revision

Client raised four defects on v1. Six of eleven shots rebuilt. The bar grid,
music section, frame plan and shots 01–04 and 09 are unchanged.

## Defects and fixes

| Shot | Client note | Diagnosis | Fix |
|---|---|---|---|
| 05, 06 | "from 0.13 when she stands up she should immediately face the party door and open it" | **My blocking error.** Shot 05 had her rise without committing to a direction, and 06 was a walk-up ending on a *held* hand on the handle. Two shots of approach where the beat wanted one. | 05: she rises already turning, squares to the door, walks straight at it, never looks away. 06: opens with both hands already driving the push-bar and the door already moving. Explicit negatives for hesitating, pausing, glancing around. |
| 07 | "when she opens it it should be the straight partly not some empty corridors first" | **My prompt error.** The v1 keyframe said the room beyond was "a bright indistinct blaze of colour and haze with the overhead lighting truss just suggested" — that reads as empty space, and the model filled it with a corridor. | Doorway now opens directly onto the packed floor with the booth visible straight ahead. Explicit negatives on both keyframe and motion: no corridor, no hallway, no passage, no lobby, no stairs, no empty space. |
| 08, 10 | "the dj is not visible on the stage, she should be" | **My design error.** I gave the DJ no reference sheet and wrote her as "near-total silhouette" in shot 11 only — so shots 08 and 10 had an empty glowing booth as the destination. A film about walking toward a DJ needs a visible DJ. | New DJ character sheet (`783a0ad0-5bf3-4f9a-801d-d75accd89462`) passed as a reference into 08, 10 and 11. She is lit, readable and directed never to be hidden, cropped or obscured by the crowd. |
| 11 | "should not bee like a close eyes worship, its a vibe song so she should be seen smiling , excited and dancing with two hands up" | **My tonal misread.** I wrote the ending as reverent stillness — eyes closed, hands loosely raised, camera settling. Wrong register for the track. | Rebuilt: dancing throughout, grinning broadly, eyes open, both arms up and both hands in the air, bouncing on the beat, camera loose and moving with her. Explicit negatives for closed eyes, solemn, serene, praying, still. |

Three of the four were mine, not model failures. The pattern across LAST TRAIN
and this film is the same: **ambiguity in a prompt gets filled by the model,
and it fills it wrongly.** "Indistinct blaze" became a corridor exactly as
"a small healing cut on one knuckle" became a visible wound.

## New jobs

| # | Keyframe | Clip |
|---|---|---|
| DJ ref | `783a0ad0-5bf3-4f9a-801d-d75accd89462` | — |
| 05 | `ec69939e-6e7d-4a81-a3ec-79b0d35d4cca` | `3c3c8a3a-65ed-4433-a491-7b5247cda1f4` |
| 06 | `97ce28b0-9d60-4f19-9746-b79c1e7fa801` | `325f0683-9e6a-4662-a42a-c78a4c99ee38` |
| 07 | `bf010557-b4ff-4346-9879-475bbbaa858b` | `a3d3131f-b7e0-4e36-906e-bccaa6d18fc7` |
| 08 | `ddddb0f1-32be-47ab-af7f-e48b2eebb119` | `66023fcd-7ca9-476a-aedb-c972c3c30d9d` |
| 10 | `45f55532-69fa-43c7-8f1c-198c3974afd3` | `910ba853-b8c5-442b-9d6b-d5d69330c368` |
| 11 | `f3da96ed-fcec-468d-aa1a-e342b323bc4e` | `0288d7b4-bf95-444b-8f34-1e217ae4afb4` |

All 13 new generations completed first time.

## v2 delivery

| Part | File | Size | Link |
|---|---|---|---|
| 1 | `01_FINAL_ALEXATOR_NEVER_LET_GO.mp4` | 50.8 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/550ba9c2-cb3f-48df-b696-014e93084cf4.mp4 |
| 2 | `02_USED_AI_SOURCES.zip` | 234.8 MB | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/8fba1008-5d39-4c68-ac5d-bb9d31c284dc.zip |
| 3 | `03_ORIGIN_PROOF.pdf` | 141 KB | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/14d8baec-c7d4-4b90-86db-95bfc9f82f05.pdf |

ZIP now carries 4 reference sheets (the DJ added), 11 keyframes, 11 clips.

## v2 verification

Identical grid, identical result.

| Check | Result |
|---|---|
| Frame count | 1016 exact |
| Duration | 42.336 s |
| Resolution / fps | 1080 × 1920 · 24 fps constant |
| Black frames | none |
| Frozen frames | none |
| Integrated loudness | −12.7 LUFS |
| Loudness range | 2.5 LU |
| True peak | −4.2 dBFS |
| Cut boundaries | all 10 present, max error 0.055 frame |
| Drop alignment (shot 07) | +9.0 ms = 0.22 frame |

## Credits

| Stage | Credits |
|---|---|
| DJ reference sheet | 2.00 |
| 6 keyframes | 12.00 |
| 6 clips (5× 5 s, 1× 6 s) | 46.50 |
| **v2 total** | **60.50** |

89.83 → 29.33. Project total across v1 and v2: **174.00**.

## Standing caveat

Unchanged: the CDN hosts are blocked from my container, so I cannot view any
frame. Highest-risk shots to review by eye in v2 are **07** (does the party
really start at the threshold?), **08 and 10** (is the DJ visible and is the
crowd holding up?) and **11** (is she actually dancing?).
