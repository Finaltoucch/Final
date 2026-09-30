# ALEXATOR — AWAKENING / "THE PASS" — HANDOFF

## THE ONE RULE THAT MATTERS
The car is LEFT-HAND DRIVE. Whether the wheel reads left **in the picture**
depends ONLY on where the camera is:

| Camera position            | Driver + wheel appear |
|----------------------------|-----------------------|
| Front / front three-quarter| viewer's RIGHT  ← WRONG, always |
| Directly behind, receding  | viewer's LEFT   ← ok |
| Car's LEFT flank, side-on  | viewer's LEFT   ← ok |
| Car's RIGHT flank          | far side of cabin ← avoid |

**NEVER POINT THE CAMERA AT THE FRONT OF THE CAR.** No prompt wording
overrides this. It is a mirror, not a prompt failure.

## WHAT IS BROKEN RIGHT NOW
Current delivered cut: 10 shots, 24 bars, 43.13 s
https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/fb521e6d-f923-4153-9f6b-9b7d57c0b2b7.mp4

**SHOT 01 (frames 0-86) IS A FRONT THREE-QUARTER.** That is the remaining
steering-side error. Two options:
 A. Re-angle side-on. Keyframe `afb8b985-0d42-45a1-b9cb-e1a6c2f66520`
    already exists (2.00 already spent) — MUST BE VIEWED BEFORE USE.
    Then 7.50 for the clip.
 B. Drop shot 01 entirely, re-cut to 9 shots. Costs nothing.

## HARD PROCESS RULE (was broken repeatedly)
Never assemble, never deliver, until every changed shot has been LOOKED AT
as a still. Two ways to look:
 1. ffmpeg -> 66px wide -> base64 -w0 -> paste into local heredoc -> decode -> Read.
    MUST stay under ~5000 base64 chars or stdout truncates.
 2. ffmpeg drawtext + hstack contact sheet -> media_upload -> PUT -> media_confirm
    -> give the user the CDN link.

## BUILD (10-shot, 24-bar)
ORD=(01 02 03 04 05 07 08 09 10 11)
FR=(86 86 87 86 86 86 130 129 129 130)   # 1035 frames = 43.125 s
audio: -ss 108.400488 -t 43.125 -map 0:a:0
       afade in st=0 d=0.60 ; afade out st=42.578 d=0.547
expected cuts: 86 172 259 345 431 517 647 776 905

## CURRENT ASSETS
01 kf 329a3351 / clip 0b3c9679   <-- BROKEN ANGLE
02 kf 80819421 / clip e224259b
03 kf 50939c05 / clip 16807b0b   (camera-locked)
04 kf 251d0afb / clip b6fc4597
05 kf 28aa6c52 / clip 0d5c866a
07 kf 3a6f7afd / clip 235a74d9
08 kf 15da6d16 / clip f111f729
09 kf d448420e / clip 54653b4c
10 kf 1bcc9ca1 / clip 87ccf83a
11 kf 2cbf7c41 / clip 3a5dc650
(shot 06 removed at user request)

## REFERENCE SHEETS
man 92c5edfd-9cd7-45ab-bc34-25d86ab8a374
woman 24895e4c-51b6-480c-9568-2cc8dbd7a851
car LHD 5324843f-529b-45e3-8e87-bd8776fd7d83
street 9d37fcec-3beb-4c0e-8a3a-6729b216b083

## API FACTS THAT COST MONEY WHEN FORGOTTEN
- generate_image_batch MUST carry aspect_ratio:"9:16" (omitting = 2048x2048 square)
- image model nano_banana_pro = 2.00 ; kling3_0 pro sound:off = 7.50 (5s) / 9.00 (6s)
- video role start_image ; image role image_references (max 3)
- mp3 has an attached-picture stream -> -map 0:a:0 is mandatory
- Cloudflare rejects application/pdf PUT -> ship PDF inside a .zip as octet-stream

## STILL OUTSTANDING
- 02_USED_AI_SOURCES.zip and 03_ORIGIN_PROOF.zip are STALE (document 11 shots)
- commercial-use term URLs + account screenshots need the user's logged-in account
- Contra chat confirmation not yet sent
