# FORGE — Asset Manifest

Recovery point. Every Higgsfield job ID for the build.

## Character reference (the lock)

`126e17bc-c707-4f7b-84f4-389f4b10707e` — nano_banana_pro, 16:9 split-screen sheet, 2752×1536.
Built on the character-sheet slot architecture with the anti-retouch realism module.
All eleven character keyframes carry it as `image_references`.

## Audio

Source track media_id: pending upload at assembly.
Cut: **123.357 → 166.107** (42.750 s, 1026 frames @ 24 fps).
Fade in 0.35 s; fade out 0.30 s from t+42.45. Verified −13.4 LUFS, TP −4.4 dBFS.

## Shots

| # | in (t+) | frames | Δ | gen | keyframe job | video job |
|---|---|---|---|---|---|---|
| 01 | `0.000` | 85 | 3.54 | 5 s | `d29f1cab-a778-46fc-bb42-4bb41c555d68` | `f22da025-86e7-44e2-8060-66601f267ad2` |
| 02 | `3.529` | 84 | 3.50 | 5 s | `6f86dee9-1116-4a42-8dc9-61dabdc8ff57` | `784aef67-8e1a-460c-9719-73c829d657cf` |
| 03 | `7.058` | 85 | 3.54 | 5 s | `273f46a5-e331-4d71-8047-9b45228c271a` | `5a75a132-bf3a-45cd-900f-f5f791d51567` |
| 04 | `10.587` | 42 | 1.75 | 3 s | `d5475401-a3ef-482a-a335-f63ada346c54` | `8a3beb32-6b67-43c2-9c0b-c6ec0618ed33` |
| 05 | `12.352` | 43 | 1.79 | 3 s | `3e3cc775-afda-430d-9731-7c85ee58e864` | `0eea034d-635c-4fed-b49a-ee609648f7aa` |
| 06 | `14.117` | 84 | 3.50 | 5 s | `9492f0a0-fcf7-48b6-b8b8-5146285c0c52` | `1c2a7134-785f-45ab-8ac7-38319c928c06` |
| 07 | `17.646` | 85 | 3.54 | 5 s | `e50e2bd6-b9b4-415c-b136-58fef946f405` | `4009a936-93ff-4a0c-a8a6-25f0cb93dd2b` |
| 08 | `21.175` | 85 | 3.54 | 5 s | `6c94b61c-6b77-4551-8da9-3f5588948839` | `b9bc3be9-bd36-4476-a313-e3877b41f0a0` |
| 09 | `24.704` | 42 | 1.75 | 3 s | `484b0432-31e2-471d-beed-f32d5310ab84` | `500e58f6-7692-4f0d-a657-3a1318253ab1` |
| 10 | `26.469` | 43 | 1.79 | 3 s | `c7be0515-b403-4afb-92c8-c61329934cbe` | `bc2081f4-969b-4284-9225-30c53a367fdf` |
| 11 | `28.233` | 169 | 7.04 | 9 s | `78bde0cd-793e-4386-84a9-1d90607f3871` | `8b07bc95-5323-408c-84e4-cd655b9108d1` |
| 12 | `35.292` | 179 | 7.46 | 9 s | `2ab9a24c-77fd-4458-840e-a735a8c4f244` | `b59eccf3-5d19-4b48-ac26-c18d0e340cec` |

**1026 frames = 42.750 s. 60 s of generated footage.**

Keyframes 01 and 09 carry no character reference — neither contains the character
(macro on coals; macro on the anvil).

## Automated QC — keyframes

All twelve are 1536×2752. Mean luminance and warm ratio (R/B):

```
shot  luma   R/B   reads as              shot  luma   R/B   reads as
01    39.7   1.02  dark, cool            07    35.3   2.03  dark, forge-lit
02    28.2   0.75  dark, cool            08    65.5   2.16  dark, forge-lit
03    39.0   1.31  dark, mixed           09    41.6   1.61  dark, forge-lit
04    62.9   1.78  dark, forge-lit       10    46.8   1.07  dark, cool
05    29.4   1.89  dark, forge-lit       11    98.7   1.28  mid,  mixed
06    47.5   2.57  dark, forge-lit       12    36.0   1.62  dark, forge-lit
```

The palette arc is doing its job: shot 02 is the coolest point (0.75, moonlight-dominant)
and warmth peaks at the hammer strike (06, R/B 2.57). Eleven of twelve sit in the dark
band (luma 28–66) as a night interior should. Shot 11 is the single bright frame at 98.7,
which is correct for a backlit steam cloud.

## Credits

| Item | Credits |
|---|---|
| character reference | 2.00 |
| 12 keyframes @ 2.00 | 24.00 |
| 12 clips, 60 s @ 1.5/s | 90.00 |
| **Spent** | **116.00** |
