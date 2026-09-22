# SATURDAY — Job Manifest

All generations on the client's paid Higgsfield account, 22 September 2026.

## Reference sheets — `nano_banana_pro`, 2K, 16:9

| Subject | Job ID |
|---|---|
| The woman (~28) | `8de79da8-7756-407f-b89f-c525caac9b9a` |
| The flat (two-panel, empty) | `d24d5aca-cfe9-4a94-ac13-2fc5a79217c6` |

## Keyframes → clips

Keyframes `nano_banana_pro` 2K 9:16 with reference sheets as `image_references`
(API role key is `image_references`, not `image_reference`). Clips `kling3_0`,
mode `pro`, `sound: off`, each keyframe as `start_image`, declining preset
`24bae836-2c4a-48e0-89b6-49fcc0b21612`. No submission bounces.

| # | Gen | Frames | Keyframe job | Clip job |
|---|---|---|---|---|
| 01 | 5 s | 86 | `32e2566b-df6b-4804-9c5c-12fb1bebb7ce` | `22725297-3700-4936-b5a3-d87f29a6422b` |
| 02 | 5 s | 86 | `872e60b0-c10a-42c6-b22f-1d9c9e984d09` | `5f38c477-efc7-4778-84af-38ae24df1d02` |
| 03 | 5 s | 86 | `d4915f8d-61ce-4036-be1d-1e8feed83739` | `399afc86-3d73-4bad-b06e-5984cde7458d` |
| 04 | 5 s | 87 | `22936727-2c06-448e-8464-ad9e8fec6058` | `4ca40491-2442-44ea-8d62-464315c68c7d` |
| 05 | 5 s | 86 | `951f9f49-b260-47cc-bc2f-c6f2ed2cd8a9` *(v2)* | `9a9cd78a-894d-4996-9cc3-63d8f8d5ffd9` |
| 06 | 5 s | 86 | `b359d321-a49f-44c2-a244-e27ba7b02d2f` *(v2)* | `66682d6d-afe2-4f7a-bdc0-7bfd0b4e7d74` |
| 07 | 5 s | 86 | `3eeab001-6c90-4ba8-8c00-55d794385aaa` | `338c0e78-1cd8-4793-b6ef-5e6392752d42` |
| 08 | 5 s | 86 | `b3f4084b-0d7b-44ac-a57f-ceba8af0d1fa` | `7f724464-7e2c-41d9-ad23-a7bc3842b686` |
| 09 | 6 s | 130 | `14645ef7-9d32-4100-a75e-b5c9a4a665e9` | `ad397bbd-a23c-4d2c-b3f3-136fcc2b970a` |
| 10 | 5 s | 86 | `794fcdb1-3420-43a3-87a2-62cd5a687899` *(v2)* | `3d07e8d9-f595-48fc-9f43-ff0673176239` |
| 11 | 6 s | 129 | `3b9ddb13-578c-4e0e-a910-644d4e3b5173` *(v2)* | `d341d8b6-b30c-4afc-b643-305743d9589d` |

Superseded first-pass keyframes (not in the delivery):
`34512dca-7fd3-41b4-8cd0-0d492918c2d6` (05),
`63a65b78-d6ee-404f-8c8f-e8e84d75cdff` (06),
`643fe990-68f5-403a-af64-c84ac16be9df` (10),
`349c7a06-0e25-4bb6-9240-0f4c261144ba` (11).

All 11 clips completed first time. Zero failures, zero regenerations at the
clip stage.

## Assembly

```bash
FR=(86 86 86 87 86 86 86 86 130 86 129)          # sums to 1034
ffmpeg -ss 14.52175 -t 43.333333 -i track.mp3 -map 0:a:0 \
  -af "afade=t=in:st=0:d=0.35,afade=t=out:st=42.783333:d=0.30" \
  -ar 48000 -ac 2 -c:a pcm_s24le cut.wav
# per segment
ffmpeg -i src_NN.mp4 -vf "scale=1080:-2,crop=1080:1920,fps=24,setsar=1" \
  -frames:v ${FR[i]} -c:v libx264 -preset medium -crf 16 -pix_fmt yuv420p -an seg_NN.mp4
ffmpeg -f concat -safe 0 -i list.txt -c copy silent.mp4
ffmpeg -i silent.mp4 -i cut.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart \
  -metadata title="Saturday" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_JUST_RELAX.mp4
```

## Delivered media ids

| File | Media ID |
|---|---|
| `01_FINAL_ALEXATOR_JUST_RELAX.mp4` | `b5d3d91a-c1f0-44a3-bbd9-4126769da28a` |
| `02_USED_AI_SOURCES.zip` | `654a2965-57ac-49e5-9df7-e73399f346b7` |
| `03_ORIGIN_PROOF.pdf` | `db2aecc8-440a-4593-bed1-b47ed898748f` |
