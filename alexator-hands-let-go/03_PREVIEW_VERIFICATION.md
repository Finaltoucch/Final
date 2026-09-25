# WHAT THE HANDS LET GO — Preview Cut Verification

**File:** `PREVIEW_WHAT_THE_HANDS_LET_GO.mp4`
**Hosted:** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/f18518ba-b2ae-4d79-89f3-fbd34734b36d.mp4

> **This is a preview, not the deliverable.** The clips underneath were
> rendered at 716×1284 and scaled up to 1080×1920 with a Lanczos filter.
> It is correct in edit, timing, sound and content, but it is soft. It is
> for judging the shots and the cut before paying for the final renders.

## Container

| Property | Value |
|---|---|
| Resolution | 1080×1920 |
| Frame rate | 24/1 |
| Frames | 1098 |
| Duration | 45.752 s |
| Video codec | h264, yuv420p |
| Audio codec | aac, 48000 Hz, 2 ch, 320 kb/s |
| Faststart | yes |

## Automated checks

| Check | Filter | Result |
|---|---|---|
| Black frames | `blackdetect=d=0.05:pix_th=0.10` | **none** |
| Frozen frames | `freezedetect=n=0.002:d=0.5` | **none** |
| Audio clipping | peak analysis | **0 samples** |
| Empty/technical frames | manual frame accounting | none — 1098 of 1098 accounted |

## Cut accuracy

Scene-change detection against the planned bar grid:

| Cut | Detected (s) | Planned (s) | Error |
|---|---|---|---|
| 01→02 | 3.500 | 3.5000 | 0 |
| 02→03 | 7.042 | 7.0417 | <1 frame |
| 03→04 | 10.542 | 10.5417 | <1 frame |
| 04→05 | 14.084 | 14.0833 | <1 frame |
| 05→06 | 19.376 | 19.3750 | <1 frame |
| **06→07 (drop)** | **24.626** | **24.6250** | **<1 frame** |
| 07→08 | 28.168 | 28.1667 | <1 frame |
| 08→09 | 31.668 | 31.6667 | <1 frame |
| 09→10 | 36.960 | 36.9583 | <1 frame |
| 10→11 | 40.460 | 40.4583 | <1 frame |

All 10 cuts detected, all on plan. The drop cut falls at an absolute track
time of 126.878 s against a measured drop of 126.88689 s — **9 ms**, under
half a frame.

## Assembly method

Exact cumulative frame counts via `-frames:v N` — never `-t <duration>` —
so rounding cannot accumulate across 11 segments.

```
FR=(84 85 84 85 127 126 85 84 127 84 127)   # sums to 1098
scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1
libx264 -preset medium -crf 16 -pix_fmt yuv420p -an
concat demuxer -c copy
mux: -c:v copy -c:a aac -b:a 320k -movflags +faststart
```

The conform is a **crop**, never a pad — no black bars are introduced.

## Limitation of this verification

Outbound access to the Higgsfield CDN is blocked from my container by the
org egress policy, so **I cannot see any generated frame.** Every check above
is automated and measures container, timing, levels and frame accounting.
Visual QC — whether the bird looks right, whether her face carries the
moment, whether anything unwanted appears in shot — is yours. This caveat
applies to every delivery in this engagement and is stated on each one.
