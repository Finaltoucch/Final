# WHAT THE SAND KEEPS — Job Manifest

All generations on the client's paid Higgsfield account, 19 September 2026.

## Reference sheets — `nano_banana_pro`, 2K

| Subject | Job ID |
|---|---|
| Girl (~10) | `81bd5666-1072-458f-b3c2-30ccd61938a3` |
| Grandfather (~75) | `9b3ea8a2-f2eb-4a89-848a-ce8ae670f280` |
| Location (dune field) | `4e6e3285-cb85-4825-9769-775cf5465c31` |

## Keyframes → clips

Keyframes `nano_banana_pro` 2K 9:16, each carrying the relevant reference
sheets as `image_references`. Clips `kling3_0`, mode `pro`, `sound: off`,
aspect `9:16`, each keyframe passed as `start_image`.
Declined preset id on every clip submission: `24bae836-2c4a-48e0-89b6-49fcc0b21612`.

| # | Gen | Keyframe job | Clip job |
|---|---|---|---|
| 01 | 5 s | `d1e55550-bf9f-4b3f-b14f-d347e4261ed0` | `ac1dea71-bce0-4b20-9a45-f357bff3e0b1` |
| 02 | 5 s | `59ec4f6a-f306-424a-b552-60aed3af11ae` | `f6bbc9f6-33ae-46c5-b278-89cbe79d0f61` |
| 03 | 5 s | `88e3ae0a-0118-45e3-893e-8cf152fe0ae5` | `4a4b4462-fd3b-4c77-96e0-57c798668ff6` |
| 04 | 5 s | `bd95f61f-df87-4d24-8004-2432b55c1439` | `4a90294a-09ce-4c7e-91fc-1211986fc3da` |
| 05 | 5 s | `856341f3-9225-45a8-96d7-ef2dca3efd29` | `c1b4ea49-52aa-4939-a37d-b3a19b4ca001` |
| 06 | 5 s | `9ce45b9c-4507-4151-8d8b-9acaf8fee4d6` | `7030d73e-9734-4817-a6e5-cf915a2e95bb` |
| 07 | 6 s | `43cd8ab6-08f3-4ce0-9895-49fe63ecba04` | `3b6e1689-e175-4551-82d8-f3d8c923a242` |
| 08 | 6 s | `9328c5c0-214d-4b21-b8a5-96f51ab40b38` | `b38cf3d5-7e6a-4b29-9966-dc526bb6936e` |
| 09 | 5 s | `92981080-2288-4465-85d6-923a4e0b657b` | `5b473c4e-d165-48e3-acc9-e2b67408764f` |
| 10 | 5 s | `f6dd778e-bffa-4763-b0b5-6ed584ce7141` | `0f33aef5-3514-431d-9bd2-2e6acc667767` |
| 11 | 5 s | `21432d7b-1244-46d7-8c47-b36cb4027693` | `b4b53a72-9265-4592-8600-be583a56c0ed` |

All 11 clips completed first time. Zero failures, zero regenerations.

## Assembly

```bash
FR=(85 85 85 85 85 86 127 128 85 85 85)          # sums to 1021
ffmpeg -ss 241.077 -t 42.54167 -i track.mp3 -map 0:a:0 \
  -af "afade=t=in:st=0:d=0.35,afade=t=out:st=42.24167:d=0.30" \
  -ar 48000 -ac 2 -c:a pcm_s24le cut.wav
# per segment
ffmpeg -i src_NN.mp4 -vf "scale=1080:-2,crop=1080:1920,fps=24,setsar=1" \
  -frames:v ${FR[i]} -c:v libx264 -preset medium -crf 16 -pix_fmt yuv420p -an seg_NN.mp4
ffmpeg -f concat -safe 0 -i list.txt -c copy silent.mp4
ffmpeg -i silent.mp4 -i cut.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart \
  -metadata title="What the Sand Keeps" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_ENDLESS_SANDS.mp4
```

Kling returns 1076×1928; `scale=1080:-2,crop=1080:1920` centre-crops it to
spec. A crop, never a pad — so no black bars can exist anywhere in the film.

Segments are cut by **exact frame count**, never by duration. Duration cutting
rounds up per segment and the error accumulates across eleven cuts.

## Delivered media ids

| File | Media ID |
|---|---|
| `01_FINAL_ALEXATOR_ENDLESS_SANDS.mp4` | `2006c2c1-db6a-4320-a433-d2d69457e927` |
| `02_USED_AI_SOURCES.zip` | `58ebfb86-8aa3-4831-b9f4-cf40e636ae6e` |
| `03_ORIGIN_PROOF.pdf` | `690875ae-fb4a-48c9-bafd-286f76b429e7` |
