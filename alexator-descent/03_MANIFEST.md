# DESCENT — Asset Manifest
11 shots · 1079 frames @24fps · 44.958 s

## FINAL FRAME PLAN (shot 06 cut for budget; entry still lands on frame 249)
| # | frames | count | keyframe job | clip job |
|---|---|---|---|---|
| 01 |    0– 82 |  83 | `3def34c2-aa1e-41f8-b5e6-abd92b52f670` (redo) | `3cd989c2-a4c2-4f18-a559-3af7dd2ff95c` |
| 02 |   83–165 |  83 | `cb3e667e-36f2-4c2b-852a-9aec2ba05d1a` | `28e0c9cb-cc5c-4930-8d41-4abe2756e52e` |
| 03 |  166–248 |  83 | `d8e94565-2330-4f10-aee3-41eaa5916145` | `44236e6b-fbc9-4172-adc7-1fd9c7d7e956` |
| 04 |  249–352 | 104 | `45e20062-0600-44b3-94f5-4ce17c059aef` | `0248660b-d674-47ff-8cb0-7df1d4be0d69` |
| 05 |  353–456 | 104 | `ec1a22a6-51a4-40f8-ac74-74681c7ddd87` | `f7c88eed-fe43-4a8b-ab42-93d36aa8a29a` |
| 07 |  457–560 | 104 | `4d35d371-9eac-4534-8ba0-366eb6895c91` | `7026c495-b2d2-4f46-ad9a-e40807d26979` |
| 08 |  561–664 | 104 | `4cd8c6ba-f2fe-4a49-87a7-e64dd3dbca1a` | `d16b06f5-8cc9-429a-a5c3-3c3df96c357c` |
| 09 |  665–768 | 104 | `0c2281bb-13b7-4fa9-9fab-20ccf9daf0ca` | `371b7f36-72ee-441b-b424-612c270f7b6d` |
| 10 |  769–872 | 104 | `835323ec-7753-4ba6-b8a6-2add7dc045a4` (redo) | `46cad4d0-6465-4d44-99fe-488519c692ab` |
| 11 |  873–975 | 103 | `370a6ca5-b242-4afc-b792-fcb8e883ab31` | `c47718de-87c9-470c-b65c-174247390b1a` |
| 12 |  976–1078| 103 | `28f25211-4c8e-4f1a-88b3-cd5ed47d0998` | `8abd2370-b838-4c72-8e3a-bedb428489bc` |

Expected scene cuts on the finished file:
`83 166 249 353 457 561 665 769 873 976`

Unused keyframe (shot 06, cut for budget): `a88d3b33-bcba-49de-a284-7841b459af69`
Superseded keyframes: shot 01 `ddf07b18-...` (wore a hood), shot 10 `d22246ab-...` (chest fully exposed).

## REFERENCE SHEETS
| Diver | `6e9b716f-66db-46a9-8626-a54df8965b82` |
| Boat  | `eba110dd-c198-497e-ac3a-c31dc8241ca6` |
| Chest | `ea2a553f-b614-467b-9271-a21ae38b6f17` |
| Tender| `a9abb5db-bd7c-473c-aff9-048ef95f6637` |

## AUDIO
```
media_id 86cfe926-8f67-4cdd-a064-3746140c8742   007-Full-Throttle.mp3
MD5 9287cd6a250c823110d7d38f612ffb23   duration 268.512 s
BPM 138.77937   beat 0.4323409 s   bar 1.7293637 s
-ss 28.469849  -t 44.958333  -map 0:a:0      (attached-picture stream present)
afade in st=0 d=0.600 ; afade out st=44.411 d=0.547
```

## MODELS & SPEND
nano_banana_pro (billed "Nano Banana Pro", backend nano_banana_2) 2.00 / image
kling3_0 mode:"pro" sound:"off" 5 s 7.50
| Item | Credits |
|---|---|
| 4 reference sheets | 8.00 |
| 12 keyframes | 24.00 |
| 2 keyframe redos | 4.00 |
| 11 clips @ 7.50 | 82.50 |
| **Total** | **118.50** |
Balance 123.58 -> ~5.08 remaining.

## BUILD
```bash
ORD=(01 02 03 04 05 07 08 09 10 11 12)
FR=(83 83 83 104 104 104 104 104 104 103 103)        # = 1079
# per shot: scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1
#           libx264 -preset medium -crf 15 -pix_fmt yuv420p -an
# concat, then mux:
#   -ss 28.469849 -t 44.958333 -map 0:a:0
#   -af afade=t=in:st=0:d=0.60,afade=t=out:st=44.411:d=0.547
#   -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart
```

## VERIFY EVERY BUILD
ffprobe dimensions/DAR/fps/frames · blackdetect (none) · freezedetect (none)
cropdetect (must read 1080:1920:0:0) · ebur128 · scene-cut list must match above.
