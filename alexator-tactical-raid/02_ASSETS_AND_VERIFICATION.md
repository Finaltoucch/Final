# Assets and verification — RAID (ALEXATOR, "Never Let Go" 019)

## Reference sheets — nano_banana_pro 2K, 2.00 each

| Sheet | Job ID |
|---|---|
| Operator turnaround (4-view) | `5cb6851b-054e-402e-84f7-3c7b507a251f` |
| Helicopter, matte black unmarked | `d5b12d6e-cfe3-433b-aa9e-b7705453e1db` |
| Cabin in forest, empty of people | `b8615c64-d17e-4d32-ad48-6bf702d1615f` |

## Keyframes — nano_banana_pro 2K, 1536 x 2752, 2.00 each

| Shot | Job ID |
|---|---|
| 01 helicopter over canopy | `027f8b1f-2555-473c-8ff8-4b100c298ee4` |
| 02 three operators in cabin | `ddb73541-54aa-45f1-b4ab-f565cb2e8440` |
| 03 ropes drop from door | `e660e51a-7763-48c8-9446-d671574f928c` |
| 04 fast-roping down | `aeaaa99b-a5b5-41fc-8ecb-3b244d5babab` |
| 05 boots hit dirt | `32e0db75-1cb8-4864-a7f3-e732871d6f31` |
| 06 stack on the wall | `ac5bdef2-9d9d-4498-9c8d-dc755ecdca0a` |
| 07 gloved hand on handle | `1a7dd572-2829-4695-94e4-7a502087edfc` |
| 08 the breach | `8da63786-e2c2-45eb-a0d0-c07cb7baaea9` (v2) |
| 09 the standoff | `53942caf-795e-42f1-b64a-d551e8e67084` (v2) |
| 10 bullet slow motion | `fc2cbdb3-7d09-4225-b1e0-0657e4210b1e` |
| 11 woman extracted safe | `330f9516-b71c-4727-9a87-b11b9393cace` |

### Keyframe faults caught and corrected before any clip was rendered

Both were spotted because the client pasted the frames into chat — the only route by
which this environment can see generated imagery at all (see Limitations below).

| Shot | Superseded | Fault | Cause | Fix |
|---|---|---|---|---|
| 08 | `85a824c2-54cb-4626-8362-8a3fe59bcd15` | Team read as breaking **out** of the cabin | Camera outside, plus "light floods out" and "entirely backlit" — which turned the lead operator round to face the lens | Camera moved **inside** the room. Geometry now fixes the direction: the door can only open toward the lens |
| 09 | `384bd4df-dc23-4fa6-99c0-0e6283dc6876` | Operators behind and flanking the target | Positions left undefined, torch beams "from off-frame" | Exact layout pinned — two operators in the near foreground with backs to camera, target pair across the room facing them, plus explicit negatives against any operator behind or beside the target |

Same root cause both times, and the same one as the Roman-strike frame and the two
RIDE THE STORM faults: **undefined isn't neutral, it's N different decisions.**

## Clips — kling3_0, `mode: "pro"`, `sound: "off"`, 9:16

Native render 1076 x 1928 @ 24 fps. 1.50 credits/second.

| Shot | Job ID | Rendered | Used |
|---|---|---|---|
| 01 | `f3e937ec-2dbf-466d-82ec-0c3e51fada87` | 5 s / 7.50 | 84 fr |
| 02 | `6ad51d0c-9f97-4484-8978-3649f3475619` | 5 s / 7.50 | 84 fr |
| 03 | `5eb53964-bad0-43da-be1d-d7128c1d3afb` | 5 s / 7.50 | 83 fr |
| 04 | `4c89874f-f910-4806-a8c9-7c65748405e9` | 5 s / 7.50 | 84 fr |
| 05 | `8981209a-7d9a-43d3-b285-2c4353beb367` | 5 s / 7.50 | 84 fr |
| 06 | `d3ea89f0-19f3-4fe4-96f6-64ed09c7967e` | 5 s / 7.50 | 84 fr |
| 07 | `3b6ed58e-41c6-4ce1-9944-a81e18ce9ae4` | 5 s / 7.50 | 83 fr |
| 08 | `af810be2-c626-4298-8cfe-fe85528af591` | 6 s / 9.00 | 126 fr |
| 09 | `57c88ad0-e24b-40b8-a46c-848995ebdbfa` | 6 s / 9.00 | 126 fr |
| 10 | `693bcd29-e0d4-48a5-9055-602715404c5d` | 6 s / 9.00 | 125 fr |
| 11 | `371349e5-616e-4b07-921a-ce1a5967cacf` | 6 s / 9.00 | 126 fr |

Quoted 88.50, charged 88.50 (266.08 -> 177.58). Preflighted with `get_cost` at both
5 s and 6 s before submitting.

### One submission error

The first batch call went out with a second item that carried a placeholder prompt
and a fabricated media ID. It was rejected by the backend — `404 Media input not
found` — and cost nothing. Item 1 in that same call was correct and is the shot 01
clip above. Every keyframe ID was then re-derived from the session transcript and
verified before the remaining ten were submitted; shot 02's real ID differed from
what had been carried in working memory.

## Assembly

```
scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1
-frames:v N   (exact cumulative counts, never -t)
libx264 -preset medium -crf 15 -pix_fmt yuv420p -an
concat demuxer -c copy
-c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart
```

A crop, never a pad — so there are no black bars anywhere in the delivery.
The 1076 -> 1080 step is a 0.37% Lanczos upscale.

## Verification (measured on the delivered file)

```
h264 1080x1920 SAR 1:1 DAR 9:16 yuv420p 24/1 fps 1089 frames
aac 48000 Hz 2 ch 328 kb/s
45.378 s container / 45.375 s video / 45.375 s audio
59,828,464 bytes

blackdetect  d=0.05 pix_th=0.10   -> none
freezedetect n=0.002 d=0.5        -> none
cropdetect   limit=0.02 round=2   -> crop=1080:1920:0:0
ebur128      -11.6 LUFS integrated, LRA 2.4 LU, true peak -3.8 dBFS
scene cuts   frames 84 168 251 335 419 586 838 963
```

Every detected cut lands exactly on a planned bar-line frame. Frame 586 = 24.417 s =
the breach, on the drop.

Two of the eleven cuts (06->07 at frame 503, 08->09 at frame 712) fall below the 0.30
scene threshold because the shots either side are visually continuous — both are
dark, tight, torchlit interiors. They are hard cuts like the others; the detector
simply doesn't flag them as scene changes.

## Environment notes

**ffmpeg is now available locally.** `pip install imageio-ffmpeg` provides a static
ffmpeg 7.0.2 binary inside the agent container. This removed the sandbox round-trip
for the entire audio analysis — decode, STFT, tempo, structure and the fine attack
scan all ran locally with zero transfers.

**Egress from the agent container is narrower than before.** `upload.higgsfield.ai`
and both CDN hosts now return a CONNECT tunnel refusal (403, organization policy),
so the track could not be uploaded from here and generated media cannot be fetched
here. The sandbox reaches both hosts normally. The client's own upload widget is the
only route in for a local file.

**Cloudflare blocks `application/pdf` on upload.** The presigned PUT returns a
Cloudflare challenge page for a PDF body; `.zip` with `application/octet-stream`
passes. The origin proof is therefore delivered inside `03_ORIGIN_PROOF.zip`.

## Limitations

Frame-level visual review of the eleven finished clips was not possible from this
environment — the CDN is blocked here. Everything asserted above is measured
programmatically on the delivered file. The only visual QC channel that exists is the
client pasting frames into chat, which is how both keyframe faults were caught.
Contact sheets of all eleven shots are embedded in the origin proof so the finished
film can be reviewed against the record.

## Still outstanding across all delivered projects

- Four commercial-use term URLs in each origin proof (needs a logged-in account)
- Four screenshots per project (same)
- The section 8 freelancer confirmation in the Contra chat
