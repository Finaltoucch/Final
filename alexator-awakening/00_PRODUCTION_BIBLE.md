# ALEXATOR — "THE PASS"
## Project 14 · Track 002 *Awakening* · Delivered 2026-09-30

Vertical AI music video for ALEXATOR under the *AI Short Video Creative Brief*.
9:16 · 1080×1920 · 24 fps CFR · 46.712 s · H.264 / AAC · no watermark, no logos,
no bars, no stock footage, no third-party visual material, no real-person reference.

---

## 1. Concept

A young man in a vintage open-top roadster drives down a tree-lined city street in
late-afternoon sun. A young woman in a floor-length emerald dress waits on the
pavement, dressed for an evening that has not started yet. As he passes, time
stretches. Their eyes meet. She smiles. He drives on.

Nothing is said and nothing is resolved. The whole film is one held glance
between two strangers, cut to sit exactly on the track's lift.

Client direction, verbatim and honoured:
- both leads White European
- both in their twenties
- **no grid and no collage anywhere in the film**

---

## 2. Locked specifications

These travel with **every** prompt that shows the subject. A property left
undefined is not neutral — it is a fresh decision the model makes each time.

### MAN
White European, 25, tall, slim. Short dark brown hair tapered at the sides,
swept back, clean side parting, same taper at the nape in back view. Clean
shaven, light warm tan, dark brown eyes. Open NAVY BLUE linen blazer over a
plain WHITE open-collar shirt, no tie. STONE trousers. TAN loafers. Plain
silver wristwatch.
**NO sunglasses and no glasses of any kind** — the film turns on his eyes
meeting hers.

### WOMAN
White European, 24, slim. Long chestnut brown hair, soft wave, centre parting,
worn loose and swept forward over her **LEFT** shoulder (back view specified to
match). Fair skin, green eyes, warm red lip. Floor-length DEEP EMERALD GREEN
plain silk dress, two thin straps, plain low back. Gold drop earrings, nude
heels, small gold clutch.
**Both arms down at her sides, hands below the waist, nothing crossing the body.**

### CAR
Early-1960s European two-seat open-top roadster, soft top **fully down**. Pale
ivory cream over tan pleated leather. Chrome bumpers, chrome windscreen frame,
chrome wire-spoke wheels on whitewalls. Bodywork completely plain: no badges, no
emblems, no marque or model names, no bonnet ornament, **no number plates front
or rear**.
**LEFT-HAND DRIVE** — steering wheel on the car's own LEFT, in front of the left
seat, dials behind it; right seat empty with no wheel and no pedals.
**The man is in the driver's seat in every shot the car appears in.**

### STREET
Tree-lined city street, pale stone townhouses, shuttered windows, iron
balconies, plane trees, wide pavement, low late-afternoon sun down the far end.
Generated empty of people. No signage of any kind.

### Colour separation
ivory car · navy blazer · emerald dress. Three values that never collide.

---

## 3. Cut list

Eleven shots. Frame counts are **cumulative-rounded** against the beat grid, never
rounded per shot, so the bar total stays exact.

| # | Frames | Cum. | Content |
|---|---|---|---|
| 01 | 86 | 86 | Low front tracking — the ivory car comes down the street, him at the wheel |
| 02 | 86 | 172 | Interior, over his shoulder, hands on the wood rim, street running past |
| 03 | 87 | 259 | Side tracking with the car, trees strobing the light |
| 04 | 86 | 345 | **Reveal** — plane tree fills frame, camera glides sideways and uncovers her, already standing there |
| 05 | 86 | 431 | Her, waiting, both hands down, clutch in one |
| 06 | 86 | 517 | The car enters her foreground, low and close |
| 07 | 87 | 604 | His head begins to turn |
| 08 | 129 | 733 | **THE LOOK** — eyes meet, slow motion. Starts on the lift at 133.550 s |
| 09 | 129 | 862 | Her — the smile arrives |
| 10 | 130 | 992 | Him — he holds it a beat too long, then faces the road |
| 11 | 129 | 1121 | She turns and watches the car go, already at speed, no stop |

`FR=(86 86 87 86 86 86 87 129 129 130 129)` = **1121 frames** = 46.708 s

Hook: the ivory car arrives in frame within the first 12 frames of shot 01.

---

## 4. Verification (measured on the delivered file)

```
1080x1920   SAR 1:1   DAR 9:16   yuv420p   24/1 fps   1121 frames   46.712 s
aac 48000 Hz stereo 332 kb/s     79,247,472 bytes
blackdetect    none
freezedetect   none
cropdetect     1080:1920:0:0
ebur128        -13.0 LUFS, LRA 3.4 LU, true peak -4.3 dBFS
cuts detected  86 172 259 345 431 517 604 733 862 992   (all ten, on plan)
```

All ten cuts detecting is the measured proof that the shot 04 reveal fix landed.
Before the fix, frame 259 was the only cut in the film below the 0.30 scene
threshold — shots 03 and 04 shared framing, palette and content, so the cut read
as the woman materialising rather than as a cut.

---

## 5. Delivery

| File | media_id | Bytes |
|---|---|---|
| `01_FINAL_ALEXATOR_AWAKENING.mp4` | `5589b62f-dcb5-45d7-b718-27c84055dc0d` | 79,247,472 |
| `02_USED_AI_SOURCES.zip` | `1fa006e6-bbda-4926-b092-34a93cbccea8` | 279,499,742 |
| `03_ORIGIN_PROOF.zip` | `414b6786-2815-44d8-8f68-97e6219d0253` | 88,501 |

CDN base: `https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/`
All three verified HTTP 200 and byte-complete after upload.

The origin proof ships inside a `.zip` because Cloudflare rejects a raw
`application/pdf` PUT with a challenge page; `application/octet-stream` passes.

### Still outstanding (needs the client's logged-in account)
- four commercial-use term URLs inside the origin proof
- four account screenshots
- the §8 freelancer confirmation in the Contra chat
