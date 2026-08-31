# Shot Manifest — GRAVITY WELL

Higgsfield job IDs for every asset. Keyframes are the `start_image` inputs for the
video pass; this file is the recovery point if the session is lost.

**Source track:** ALEXATOR — *Rise Again* · media_id `05ea62db-e06d-4976-8e53-51a53b3ac6c6`
**Character reference:** `af29ef8d-1e41-4fac-b6b2-4d0e571d8d01` (nano_banana_pro, approved)

## Audio cut

```
IN 58.5097s   BODY END 100.8440s   OUT 102.2040s   DURATION 43.694292s
fade in 0.35s   fade out 1.36s (starts at 42.3343s)
verified: 48kHz stereo 24-bit, -13.5 LUFS, LRA 2.5 LU, true peak -4.6 dBFS
```

## Keyframes (all nano_banana_pro, 1536x2752, 2K)

| # | In | Δ | Gen | Job ID | Ref |
|---|---|---|---|---|---|
| 01 | `0.000` | 3.528 | 5s | `56948c2f-7d36-4794-bc6a-91c81639e6f6` | char |
| 02 | `3.528` | 3.528 | 5s | `aa5e8591-367b-40f6-b617-09b926264157` | char |
| 03 | `7.056` | 3.528 | 5s | `4896cc3b-9e4b-4f37-97cc-b469def7cc99` | char |
| 04 | `10.584` | 3.528 | 5s | `1c654506-f4bd-44a9-b5b6-e42810878028` | — |
| 05 | `14.111` | 3.528 | 5s | `84a4f6ea-4b27-4f3b-94fd-ecdd5c2bf7a1` | char |
| 06 | `17.639` | 3.528 | 5s | `a75aa5c2-95c5-424e-b78a-91bb2b837123` | char |
| 07 | `21.167` | 3.528 | 5s | `365f4686-0295-41a2-b672-ac1480204bcf` | char |
| 08 | `24.695` | 3.528 | 5s | `00ab5c80-9013-4987-99c5-bdcd8ec49d88` | char |
| 09 | `28.223` | 3.528 | 5s | `a9e1c46e-d8f8-4b35-bf02-d53421815be1` | kf08 |
| 10 | `31.751` | 5.291 | 6s | `37674c52-4b48-4dd2-8c14-8094304b89c8` | kf08 |
| 11 | `37.042` | 6.652 | 8s | `f926193e-f44f-4489-b72a-02e5e97c21e2` | kf08 |

Keyframes 09–11 chain off keyframe 08 rather than the character reference — all three
are underwater and follow directly from the breach, so the nearer ancestor holds
wardrobe and water continuity better.

## Automated QC — keyframes

All 11 pass the two-tone lighting rule (bottom-third R/B ratio exceeds top-third,
i.e. cool above / warm below):

```
shot  top R/B  bottom R/B      shot  top R/B  bottom R/B
01    0.452    1.011           07    0.585    2.539
02    0.406    1.277           08    0.729    0.883
03    0.255    1.413           09    0.717    0.934
04    0.409    1.383           10    0.751    0.999
05    0.273    2.840           11    0.556    0.953
06    0.447    1.350
```

The ratio falls as the sequence goes underwater (08–11), which is correct — the city's
warm bounce is attenuated by depth. The arc is visible in the numbers.

All 11 are 1536×2752 (ratio 1.7917 vs true 9:16 1.7778) — centre-cropped to exactly
1080×1920 at assembly.

## Video pass — planned

Model `kling3_0`, mode `pro`, `sound: off`, aspect `9:16`, each keyframe as `start_image`.
9 × 5s @ 8.75 + 1 × 6s @ 10.5 + 1 × 8s @ 14 = **103.25 credits**.

## Credit ledger

| Item | Credits |
|---|---|
| 2 × character reference | 4 |
| 11 × keyframe | 22 |
| **Spent to date** | **26** |
| Video pass (planned) | 103.25 |

## Egress constraint

The Higgsfield CDN (`d8j0ntlcm91z4`, `d2ol7oe51mr4n9`.cloudfront.net) is blocked by the
session's egress policy — uploads to S3 succeed, downloads return 403. All media
processing therefore runs in the Higgsfield `sandbox_exec` environment, which can reach
both the CDN and the media store. Visual review is the client's; automated QC covers
dimensions, ratio, fps, duration, black/frozen frames, cut-point scene changes and
colour continuity.

## Video pass — submitted

Model `kling3_0`, mode `pro`, `sound: off`, aspect `9:16`, keyframe as `start_image`.

| # | Δ | Gen | Video job ID |
|---|---|---|---|
| 01 | 3.528 | 5s | `a951670e-94bf-42b7-a8a7-3fee2cef96ff` |
| 02 | 3.528 | 5s | `79487c01-4ca1-45e5-a968-9595a24a1dfc` |
| 03 | 3.528 | 5s | `27f71457-abe5-4e84-881d-3007158df866` |
| 04 | 3.528 | 5s | `cbe6da36-4f5f-48f2-b886-234e3f13644a` |
| 05 | 3.528 | 5s | `d97f8e16-bdff-4c8c-8f59-b7d1d33df0dd` |
| 06 | 3.528 | 5s | `1d36fa56-fe52-4848-bc89-78d95716fe2c` |
| 07 | 3.528 | 5s | `d3b2e928-429e-45b4-961d-241947caba67` |
| 08 | 3.528 | 5s | `bc7804ab-cf1c-4adf-8fd4-632557d8504a` |
| 09 | 3.528 | 5s | `c26f4b9d-269b-4b24-a983-754841103b1a` |
| 10 | 5.291 | 6s | `986a536b-9319-4a21-8422-22c36430a20c` |
| 11 | 6.652 | 8s | `62a11621-7f7a-434b-bf6c-115aa585ab84` |

Shot 09 was resubmitted with `declined_preset_id` after the API returned a preset
recommendation ("IN THE DARK") instead of a job.

**Video pass cost: 103.25 credits.** Running total: 129.25.

## Assembly plan

Each generated clip is longer than its slot, giving handles. Trim from the head of
each clip to the exact Δ, centre-crop to 1080×1920, concatenate in order, mux against
`cut.wav`, encode H.264 High yuv420p + AAC 320k stereo, 30 fps, `+faststart`.

```
shot  in        Δ         cut on bar
01    0.000     3.528     33
02    3.528     3.528     35
03    7.056     3.528     37
04    10.584    3.528     39
05    14.111    3.528     41   <- DROP
06    17.639    3.528     43
07    21.167    3.528     45
08    24.695    3.528     47   <- BREATH
09    28.223    3.528     49   <- second wave
10    31.751    5.291     51
11    37.042    6.652     54 -> end (holds through fade)
```
