# RIDE HOME v2 — locked character, Nano Banana Pro

Supersedes the soul_2 pass. One character reference drives every frame, which is
what fixes the identity drift.

## Character reference (the lock)

`7db1423c-466e-4b1f-b561-5926495ee162` — nano_banana_pro, 16:9 split-screen sheet,
2752×1536. Built on the character-sheet slot architecture with the anti-retouch
realism module: visible pores, natural asymmetry, matte complexion, explicit
negatives against beauty-filter / airbrushing / plastic skin.

**Locked identity:** boy ~11, warm deep-brown skin, short tightly-coiled black hair
in a low fade, slim child's frame. Plain navy crew-neck jumper, no crest. White
collared shirt, grey trousers, plain black lace-up shoes. Plain grey backpack, both
shoulders, no branding. **Wired white earphones — white earbud, thin white cable to
the pocket.** No jewellery, no watch, no logos anywhere.

## Keyframes — all nano_banana_pro 9:16 2K, all chained to the reference

| # | In | Δ | Shot | Keyframe job | Video job |
|---|---|---|---|---|---|
| 01 | `0.000` | 3.528 | shoes dragging, long shadow | `02d14951-242b-4a65-8041-7c39a41b1727` | `10d13902-ffa4-4cfc-ad06-c93a6b5c7211` |
| 02 | `3.528` | 3.528 | walking away, cable down his neck | `d3bb0f75-860e-4d13-bec3-4c9a8be99976` | `31ccb728-958e-480a-ad5e-c197ef8e7cc3` |
| 03 | `7.056` | 3.528 | close profile, flat and tired | `72098842-0f8c-4b52-94fc-0f34a143d7b2` | `bc27c49f-0f4b-4866-87fc-4dfb90e8cb04` |
| 04 | `10.584` | 3.528 | wide empty road, walking to the rack | `508f2b47-5f10-4514-b508-d96f68e5b57a` | `5c99e2a4-eefa-4fcf-909b-4c9e866a2b28` |
| 05 | `14.111` | 3.528 | **THE DROP** — eyes lift, smile spreads | `97f8f055-4289-4354-9099-55595c711880` | `42cd5410-2f17-4e5f-96b2-4db7f8463608` |
| 06 | `17.639` | 3.528 | bike off the rack, swinging to the road | `81ea81e2-06a7-4e3a-a964-4d847f97e285` | `0b9673a9-69c2-4bc0-bcf7-6490097ad2fd` |
| 07 | `21.167` | 3.528 | first pedal stroke, wheel blurring | `03f0e596-176a-4ec8-9068-3341358b67f0` | `b3bc3faf-3be4-4b94-a611-a3d46625f7eb` |
| 08 | `24.695` | 3.528 | **THE BREATH** — coasting, eyes closed | `6d8d4227-e2ef-4235-9472-7ed9e833db91` | `16262ec8-6547-4c7f-a7a7-cbc34d954030` |
| 09 | `28.223` | 3.528 | riding fast, grinning, trees streaking | `b90536d8-01a9-4aa6-8ae6-fd694939d392` | `ba0e9b96-778f-407e-a9e9-72b88c43e72c` |
| 10 | `31.751` | 5.291 | **DRONE** — rises and pulls back | `b7c89ef4-88d3-4af5-b1fc-20d2babe5fd7` | `e1d8651e-bbf5-46aa-aebf-dbd3cda51831` |
| 11 | `37.042` | 6.652 | **THE LIFT** — wheels leave the road | `149ad1d1-ffcc-4254-81c3-02e544a34a1f` | `b60f65a1-1485-4f1b-aa9e-1053256ac714` |

Shots 04 and 08 were resubmitted with `declined_preset_id` after the API returned a
preset recommendation instead of a job.

## Frame counts (24 fps, no accumulated drift)

`85 · 84 · 85 · 85 · 84 · 85 · 85 · 84 · 85 · 127 · 160 = 1049 frames = 43.708 s`

## Realism approach

The previous concept failed because it asked the renderer to sell invented physics.
This one is ordinary reality with one lift at the end, and every prompt carries:
late-afternoon natural light, documentary lens language (28/35/50/85mm), shallow
depth of field, visible skin texture, film grain, and explicit negatives against
smoothing, beauty filter, airbrushing and plastic skin.

## Credits

| Item | Credits |
|---|---|
| character reference | 2.00 |
| 11 keyframes × nano_banana_pro | 22.00 |
| 11 video shots × kling3_0 pro silent | 88.50 |
| **This pass** | **112.50** |

## Delivered

| File | Link |
|---|---|
| `01_FINAL_ALEXATOR_Rise_Again.mp4` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/bc283ad1-0780-473a-a596-53e84131350f.mp4 |
| `02_USED_AI_SOURCES.zip` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/bf129763-0a41-4f3b-afcb-9201d8686f94.zip |

### Master — measured

H.264 High, yuv420p, **1080×1920**, **24 fps**, 1049 frames, **43.711 s**, 90.1 MB.
AAC-LC 48 kHz stereo. −13.6 LUFS, LRA 2.6 LU, true peak −4.6 dBFS.
No black or frozen frames. No watermark, no black bars, no on-screen text.

### Cut accuracy

| target | actual | error (frames) |
|---|---|---|
| 3.528 | 3.542 | +0.34 |
| 7.056 | 7.042 | −0.33 |
| 10.584 | 10.584 | +0.01 |
| **14.111 — the drop** | 14.126 | **+0.35** |
| 17.639 | 17.626 | −0.32 |
| 21.167 | 21.168 | +0.02 |
| **24.695 — the breath** | 24.710 | **+0.36** |
| 28.223 | 28.210 | −0.31 |
| 31.751 | 31.752 | +0.03 |
| 37.043 | 37.044 | +0.04 |

Worst case ±0.36 of a frame, no accumulated drift.

### Still outstanding

`03_ORIGIN_PROOF.pdf` needs regenerating for this concept (the existing one describes
GRAVITY WELL). Its two blocked sections remain: commercial-use term URLs, and the
per-service workspace / subscription / timeline screenshots.
