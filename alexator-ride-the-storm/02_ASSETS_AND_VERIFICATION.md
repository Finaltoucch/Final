# RIDE THE STORM — Assets, Spend and Verification

## Reference sheets (nano_banana_pro, 2K, 9:16) — 4.00 credits

| Sheet | Job ID |
|---|---|
| Rider and motorcycle | `83fa9237-8862-458f-a11b-ed68a67c8936` |
| Road and storm | `136f762e-a1c5-4671-95cb-ba90c724a7e3` |

Two sheets, not three — one character, one location. The location sheet was
generated deliberately empty of vehicles, people, buildings, poles and signs.

## Keyframes (nano_banana_pro, 2K, 9:16) — 22.00 credits

All generated against both sheets via `image_references`.

| Shot | Job ID |
|---|---|
| 01 | `15836af9-9d81-487d-b2cc-516d0fab01a1` |
| 02 | `663f6c15-4565-4148-8770-5ad386bfb1f9` |
| 03 | `86a9d0ef-9a06-4a4a-a831-8fd3c951af65` |
| 04 | `62507d80-cea2-4aef-bf67-7749e18aff3c` |
| 05 | `ddaee22b-29b0-4576-82e1-914617e768d0` |
| 06 | `737251b9-80ae-43fa-8795-976227c348e8` |
| 07 | `3dca19be-08b3-483e-b863-c8fa89349bfe` |
| 08 | `30150127-4e15-46bd-b9f8-c155eeadadc5` |
| 09 | `90f03a1a-1f05-4933-be51-5b8b0c5b065b` |
| 10 | `d051fb1b-697f-4709-b9d8-4d1ca5a855c6` |
| 11 | `8c3f1510-8162-4cb5-9b9a-0d589c01164c` |

## Clips (kling3_0, mode pro, sound off) — 88.50 credits

All returned **1076×1928 native**.

| Shot | Job ID | Length |
|---|---|---|
| 01 | `7762f73e-049a-49b5-acde-87e907e09b69` | 5 s |
| 02 | `79c5b7e7-a1f9-4d2f-905d-edc89dd0a756` | 5 s |
| 03 | `cb71a7cd-113e-4ea3-a1ae-c6a462d7964b` | 5 s |
| 04 | `3d759d44-fb4b-4b05-8104-4a539f615b7b` | 5 s |
| 05 | `9192947e-1e01-4058-ab05-32fe8b51f63f` | 5 s |
| 06 | `e49909ee-0fc0-4204-afc1-e09d5d880a9a` | 5 s |
| 07 | `5624ef8b-da91-48e6-a278-f5c3a19389d8` | 5 s |
| 08 | `4a251ff8-38d9-4935-9886-f3d9822200a0` | 5 s |
| 09 | `357d8149-ca7b-459b-a951-8186c43881ef` | 6 s |
| 10 | `d6233f2c-ce01-4261-80c5-3fca921a52c7` | 6 s |
| 11 | `89d38373-2c46-4ccf-9086-3ee928363ec9` | 7 s |

## Spend

| Item | Quoted | Charged |
|---|---|---|
| 2 reference sheets + 11 keyframes | 26.00 | **26.00** |
| 11 clips | 88.50 | **88.50** |
| **Total** | **114.50** | **114.50** |

Every figure was preflighted with `get_cost` before submission and matched
exactly. This is the rule taken from the *Brighter Days* error, where a
quote from memory produced a 103.25 charge against an 88.50 quote.

Balance trace: 200.08 → 174.08 (images) → 85.58 (clips). No unexplained
movement at any point.

## Verification of the delivered master

| Requirement | Measured | Result |
|---|---|---|
| Aspect ratio 9:16 | 1080×1920 | Pass |
| Minimum 1080×1920 | 1080×1920 from native 1076×1928 | Pass |
| Duration 30–60 s | 45.172 s | Pass |
| Container | MP4, H.264, yuv420p, faststart | Pass |
| Minimum 24 fps | 24/1 constant, 1084 frames | Pass |
| Stereo | AAC 320 kb/s, 48 kHz, 2 ch | Pass |
| No black bars | cropdetect 1080×1920 at x=0 y=0 | Pass |
| No black frames | `blackdetect=d=0.05:pix_th=0.10`: none | Pass |
| No frozen frames | `freezedetect=n=0.002:d=0.5`: none | Pass |
| No clipping | peak −1.50 dBFS, 0 clipped samples | Pass |
| Loudness | −12.7 LUFS, LRA 1.8 LU | Pass |

### Cut accuracy

| Cut | Detected | Planned | Error |
|---|---|---|---|
| 01→02 | 3.459 | 3.4583 | <1 frame |
| 02→03 | 6.959 | 6.9583 | <1 frame |
| 03→04 | 10.418 | 10.4167 | <1 frame |
| 04→05 | 13.877 | 13.8750 | <1 frame |
| 05→06 | 17.377 | 17.3750 | <1 frame |
| **06→07 (throttle)** | **20.836** | **20.8333** | **3 ms** |
| 07→08 | 24.295 | 24.2917 | <1 frame |
| 08→09 | 27.795 | 27.7917 | <1 frame |
| 09→10 | 33.004 | 33.0000 | <1 frame |
| 10→11 | 38.213 | 38.2083 | <1 frame |

Assembly used exact cumulative frame counts (`-frames:v N`, summing to 1084),
never durations, so rounding cannot accumulate across segments.

```
FR=(83 84 83 83 84 83 83 84 125 125 167)
scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1
libx264 -preset medium -crf 15 -pix_fmt yuv420p -an
concat demuxer -c copy
mux: -c:v copy -c:a aac -b:a 320k -movflags +faststart
```

The conform is a **crop**, never a pad — no black bars are introduced.

## Delivery

| File | Size |
|---|---|
| `01_FINAL_ALEXATOR_RIDE_THE_STORM.mp4` | 76.9 MB |
| `02_USED_AI_SOURCES.zip` | 238 MB, 29 files |
| `03_ORIGIN_PROOF.pdf` | 1.19 MB, 10 sections |

---

# Note: the five rejected concepts that preceded this one

Recorded because the pattern matters more than any single rejection.

| Concept | Verdict |
|---|---|
| THE HAND — Iliad wrestling match | "nonsense" |
| THE TOP OF THE TOWER — turbine technician | "not creative" |
| THE MIRROR — salt flat, inverted frame | "not creative" |
| THE CAST — Roman spear duel | superseded |
| Roman sword duel | built, keyframes failed |

**The diagnosis.** Across twelve films the subject kept changing and the form
never moved: one protagonist performing a modest activity in a striking
location, cut in slow 2–4 bar holds. Swapping the activity is not a new
concept. The client's word for this was accurate.

**The Roman duel's failure was renderability, not taste.** One prompt clause
— "drives down hard over the top rim" — invited an overhead swing, and the
swing dragged five separate faults behind it: a 90cm longsword instead of a
gladius (an overhead swing needs reach), the attacker's shield dropped to
free the arm, a second sword left in the scabbard, the defender bent double
underneath so it read as an execution, and the blade punching through the
shield. **One bad verb, five errors.**

**What this project did differently.** Instead of designing for the image and
hoping it renders, the design starts from what the tools reliably produce:

- Full-face helmet, visor down, in every shot → face drift eliminated
- One body → no two-figure contact, no relative scale to hold
- No weapons, no armour, no handled props
- Bike specced plain → no surface to grow lettering or badges
- Two reference sheets instead of three → 26.00 rather than 28.00

Nothing was refused and no frame needed a re-do.

## A change in what verification is possible

The client pasted a keyframe directly into the chat during this session, and
it was reviewable — nine faults were identified from it. Outbound access to
the generation CDN is blocked, so generated frames cannot be fetched, **but
pasted images can be read.** Visual QC is therefore possible on any frame the
client chooses to paste, which it has not been on the previous eleven
deliveries. Worth using before clip spend rather than after.
