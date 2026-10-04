# DESCENT — Delivery (v2, phrase-complete cut)

## THE THREE FILES
| # | File | Link |
|---|---|---|
| 01 | `01_FINAL_ALEXATOR_FULL_THROTTLE.mp4` | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/e57c95a4-3588-40c7-b152-33df9d1a4f06.mp4 |
| 02 | `02_USED_AI_SOURCES.zip` (284,612,576 B) | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/7a246e27-d3ae-4282-8ac5-06ebeee471a1.zip |
| 03 | `03_ORIGIN_PROOF.zip` (46,325 B, contains the PDF) | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/42aa6093-330b-4d39-8fc4-31c093da9018.zip |

PDF sha256 `125cf9b41d1cd0e58f2cb78198125d1895a1bffdca5a0a74e241edff4523d43f`
Film MD5 `a364ded1822f660412f2a0f1935da8c1`

## WHY v2 EXISTS — the lesson
v1 was 26 bars, ending at 73.428 s. The post-drop phrase of this track runs a
clean **24 bars from the drop at 38.846032 s to the kick drop-out at 80.351 s**.
v1 gave that phrase only 20 bars, cutting the climax off 4 bars early with the
fade landing mid-statement. That is exactly the fault the client warned about.

**RULE ADDED: find where the musical phrase RESOLVES before choosing the
section length. Never pick a bar count because it is convenient for the shot
count or the duration window.** The resolution point was already measured and
printed during the music analysis and simply was not carried into the
out-point decision.

v2 is 30 bars: 6 before the drop, 24 after. The climax plays in full.

## FINAL SPEC
```
1080x1920  DAR 9:16  24 fps  1245 frames  51.875 s  90,770,749 bytes
audio AAC 48 kHz stereo 320k, 51.875 s
blackdetect none · freezedetect none · cropdetect 1080:1920:0:0
ebur128 -14.5 LUFS · LRA 1.4 LU · true peak -5.2 dBFS
IN 28.469849 s   OUT 80.344849 s   drop on frame 249
fade in 0.600 s · fade out 0.547 s from 51.328 s
```
Scene cuts detected: `83 166 249 360 471 692 803 914 1025 1135`
Planned: `83 166 249 360 471 581 692 803 914 1025 1135`
The 581 boundary (shot 06 -> 07) is not detected because both shots are dark
blue underwater footage of the same diver and fall under the 0.28 threshold.
Every detected cut matches plan and the total is exactly 1245 frames, which
confirms the allocation. Not a defect.

## FRAME PLAN
| # | frames | n | # | frames | n |
|---|---|---|---|---|---|
| 01 | 0–82 | 83 | 07 | 581–691 | 111 |
| 02 | 83–165 | 83 | 08 | 692–802 | 111 |
| 03 | 166–248 | 83 | 09 | 803–913 | 111 |
| 04 | 249–359 | 111 | 10 | 914–1024 | 111 |
| 05 | 360–470 | 111 | 11 | 1025–1134 | 110 |
| 06 | 471–580 | 110 | 12 | 1135–1244 | 110 |

Shot 06 clip (added for v2): `17ba2d91-588c-4a17-be5c-0c92d4cdfb80`

## TOTAL SPEND
| Item | Credits |
|---|---|
| 4 reference sheets | 8.00 |
| 12 keyframes | 24.00 |
| 2 keyframe redos | 4.00 |
| 11 clips (v1) | 82.50 |
| 1 clip (shot 06, v2) | 7.50 |
| **Total** | **126.00** |

## STILL OUTSTANDING — needs the logged-in account
The origin proof carries a clearly marked section listing six items that
cannot be produced without the account holder:
- 4 commercial-use terms URLs (stills model, motion model, platform, tier)
- 4 account screenshots evidencing the generations
- signature and date
Also still to do: the §8 freelancer confirmation message in the Contra chat.
