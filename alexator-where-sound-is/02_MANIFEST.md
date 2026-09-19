# WHERE THE SOUND IS — Job Manifest

All generations on the client's paid Higgsfield account, 19 September 2026.

## Reference sheets — `nano_banana_pro`, 2K, 16:9

| Subject | Job ID |
|---|---|
| The young woman (~22, box braids) | `8bb0e43a-26cf-4c6d-b109-9aa2aaeb59a9` |
| Location A — the alley (two-panel) | `65edf4ba-4877-4375-b30d-79b1c5d5aaca` |
| Location B — the venue (two-panel) | `f9dbab10-6e96-467b-966c-51c676aefbd4` |

Location sheets were generated **empty — no people** so that a crowd could not
be baked into the reference and then contradict the per-shot crowd direction.

The DJ gets no sheet: near-total silhouette in the two shots they appear in.

## Keyframes — `nano_banana_pro`, 2K, 9:16

Each carries its reference sheets as `image_references`. Note the API role key
is `image_references`, not `image_reference` — the server coerces but logs an
adjustment.

| # | Refs used | Keyframe job |
|---|---|---|
| 01 | girl + alley | `2c5544ca-fb18-4e35-a28e-98265e3d70e0` |
| 02 | girl + alley | `e82e69df-dd01-4570-8010-fc982b1cb9e6` |
| 03 | girl + alley | `1e51c3df-d966-4c29-b0bd-d5e16f1f8430` |
| 04 | girl + alley | `99d05a8d-36e3-497e-9d21-b7c904304e9a` |
| 05 | girl + alley | `e2db60e6-401c-498d-aa67-f3b2b2080c8c` |
| 06 | girl + alley | `edc290e6-ca80-4369-9b03-cb271ba15c8d` |
| 07 | girl + alley + venue | `1956c067-f81c-4e82-b071-bf38d78fa8d4` |
| 08 | girl + venue | `d2c9a723-5929-4bfe-9f6d-577eb08bd1b3` |
| 09 | girl + venue | `512905c4-a211-4806-a4cc-4d4610b1ee61` |
| 10 | girl + venue | `2e74d7c5-1c68-4746-8ef0-c3e550a41460` |
| 11 | girl + venue | `a716ae06-d07c-4bab-9dde-20c59124bb82` |

Shot 07 is the only keyframe carrying all three references — it is the one frame
that contains both locations at once.

All 14 images completed first time. Zero failures, zero regenerations.

## Contact sheets sent to the client

| Sheet | Link |
|---|---|
| 11 keyframes | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/800017c8-1850-4ea0-8d8e-b3dd00c642f1.jpg |
| 3 reference sheets | https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/20de17e8-5471-4c39-9e69-6a3c784b156f.jpg |

## Clips — `kling3_0`, mode `pro`, `sound: off`, 9:16

Each keyframe passed as `start_image`. Declined preset
`24bae836-2c4a-48e0-89b6-49fcc0b21612` on every submission — no bounces.

| # | Gen | Frames | Clip job |
|---|---|---|---|
| 01 | 5 s | 85 | `eb787510-f660-4dbe-8f76-e7d0ccfa30a1` |
| 02 | 5 s | 84 | `9595ea39-8349-4b69-b0ca-d693bd7bc57c` |
| 03 | 5 s | 85 | `d9784902-2612-42ea-bc90-8572e8f8d255` |
| 04 | 5 s | 85 | `f0138992-44c3-4321-a7fa-2f0fdb737f28` |
| 05 | 5 s | 84 | `67f81859-c17e-4fd2-b6c7-9018e051754a` |
| 06 | 5 s | 85 | `881e2d29-bdbd-4b27-aca8-d1e860aeb829` |
| 07 | 5 s | 84 | `f4b8a653-743f-403f-b438-2536f790d5d8` |
| 08 | 5 s | 85 | `853aed4b-8f01-4a45-9501-f0b491420dfd` |
| 09 | 6 s | 127 | `7c48a2cf-7f81-4ea0-8f97-83824c4020f0` |
| 10 | 5 s | 85 | `249b1e24-61e9-4119-8152-ad4589fa3399` |
| 11 | 6 s | 127 | `705bc202-ad52-48b7-a808-8f7a277fb1a1` |

Frame counts sum to 1016. All 11 completed first time.

## Assembly

```bash
FR=(85 84 85 85 84 85 84 85 127 85 127)          # sums to 1016
ffmpeg -ss 53.925556 -t 42.333333 -i track.mp3 -map 0:a:0 \
  -af "afade=t=in:st=0:d=0.35,afade=t=out:st=42.033333:d=0.30" \
  -ar 48000 -ac 2 -c:a pcm_s24le cut.wav
# per segment
ffmpeg -i src_NN.mp4 -vf "scale=1080:-2,crop=1080:1920,fps=24,setsar=1" \
  -frames:v ${FR[i]} -c:v libx264 -preset medium -crf 16 -pix_fmt yuv420p -an seg_NN.mp4
ffmpeg -f concat -safe 0 -i list.txt -c copy silent.mp4
ffmpeg -i silent.mp4 -i cut.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart \
  -metadata title="Where the Sound Is" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_NEVER_LET_GO.mp4
```

## Delivered media ids

| File | Media ID |
|---|---|
| `01_FINAL_ALEXATOR_NEVER_LET_GO.mp4` | `89fc5e4e-b82b-4b7f-96f3-c399c9cac045` |
| `02_USED_AI_SOURCES.zip` | `40db1dd5-0ea0-43ac-b911-87c80764239e` |
| `03_ORIGIN_PROOF.pdf` | `888d1122-72cc-4554-bd8c-946ba6a35e24` |

## Final status

| Stage | Credits | State |
|---|---|---|
| 3 reference sheets | 6.00 | done |
| 11 keyframes | 22.00 | done |
| 11 clips | 85.50 | done |
| **Total** | **113.50** | delivered |

Balance 175.33 → **89.83**. 25 generations, zero failures, zero regenerations.

See `03_DELIVERY.md` for links, verification results and what remains
outstanding on the account holder's side.
