# Delivery — GRAVITY WELL

**ALEXATOR — *Rise Again*** · vertical short video · delivered 31 August 2026

## Download links

All three files live in the Higgsfield media store (24h presigned; re-issue if expired).

| File | Link |
|---|---|
| `01_FINAL_ALEXATOR_Rise_Again.mp4` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/454897b1-d260-4414-93af-e9641211f936.mp4 |
| `02_USED_AI_SOURCES.zip` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/6401fe9d-30b5-4be9-8a91-2b7ababa3166.zip |
| `03_ORIGIN_PROOF.pdf` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/1c39c535-8958-4303-92f7-ccc9c0e01136.pdf |

## Final master — measured

| Property | Value | Brief requires | |
|---|---|---|---|
| Container | MP4 | MP4 | ok |
| Video | H.264 High, yuv420p | — | ok |
| Resolution | **1080 × 1920** | min 1080 × 1920 | ok |
| Aspect | 9:16 vertical | 9:16 | ok |
| Frame rate | **24 fps**, 1049 frames | min 24 fps | ok |
| Duration | **43.711 s** | 30–60 s | ok |
| Audio | AAC-LC 48 kHz **stereo** ~326 kbps | stereo | ok |
| Loudness | −13.6 LUFS · LRA 2.6 LU · TP −4.6 dBFS | — | no clipping |
| Black / frozen frames | none detected | no empty or technical frames | ok |
| Watermark / AI logo | none | none | ok |
| Black bars | none (native 9:16 throughout) | none | ok |
| On-screen text | none | none except permitted marks | ok |

## Cut accuracy against the bar grid

Tempo 136.060 BPM, bar 1.76393 s. Every cut placed on a bar line; scene-change
detection on the final file confirms:

| target (s) | actual (s) | error (frames) |
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

Worst-case error ±0.36 of a frame (±0.015 s), and the errors oscillate around zero
rather than accumulating. The first assembly cut each segment by duration, which
rounded up to a whole frame each time and drifted to 0.127 s (3 frames) late by the
end; the final build cuts on exact cumulative frame counts
(85·84·85·85·84·85·85·84·85·127·160 = 1049) so there is no accumulation.

## Resolution note

Kling v3.0 outputs 1076×1928. The brief sets a floor of 1080×1920, so each shot is
scaled by +0.37 % to 1080 width and centre-cropped to 1080×1920. That is a sub-half-
percent conform, not an upscale of low-resolution material. If the client wants true
native ≥1080, Kling's `4k` mode would require regenerating all eleven shots at 30
credits per 5 s (≈350 credits).

## Outstanding before submission

`03_ORIGIN_PROOF.pdf` is complete on every factual point but has two sections the
freelancer must finish, both clearly marked in red in the PDF:

1. **Commercial-use terms URLs** — the working environment's egress policy blocked the
   providers' websites, so the exact links could not be captured and verified.
2. **Screenshots** — must come from the logged-in account: one generation/workspace
   screenshot per service (Nano Banana Pro, Kling v3.0), a subscription screenshot
   showing the active plan (required, since commercial rights depend on the plan), and
   an editing-timeline screenshot.

Also required by §8: the freelancer confirmation must be posted in the Contra project
chat. The compliance statement in section 8 of the origin proof carries the wording.

## Credit ledger

| Item | Credits |
|---|---|
| 2 × character reference (nano_banana_pro) | 4.00 |
| 11 × keyframe (nano_banana_pro) | 22.00 |
| 11 × video shot (kling3_0 pro, silent) | 88.50 |
| Music cut, assembly, encode, packaging (ffmpeg, local) | 0 |
| **Total** | **114.50** |

Balance after delivery: 1167.01.
