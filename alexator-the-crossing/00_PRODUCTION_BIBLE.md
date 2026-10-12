# THE CROSSING
Vertical 9:16 AI music video. Client concept 3: *"A cat who tries to cross a very
busy road in dramatic different angle shots, it finally succeeds."*

**This bible was written after delivery, which is the mistake it exists to stop
anyone repeating.** The film was built, delivered and then revised twice before
anything was written down, so when the sources package was finally needed none
of its job ids existed anywhere. All 23 had to be recovered from the account's
generation history and the mapping proved by timestamp clustering: plates at
16:20, the first keyframe batch at 16:23, the two keyframe redos at 16:26, the
clip batch at 16:29, the shot-03 redo at 17:13 the same day. Its music grid had
to be re-derived by cross-correlating the finished film against the master.
**Write the bible before the build, not after it.**

## CONCEPT
Ten deliberately different angles on one small event. Macro eye, paws at the
kerb, the bolt on the drop, straight-down overhead, under a parked car, a tyre
into a puddle, frozen in the glare, the launch away, paws hitting the far kerb,
and the cat sitting on the far pavement grooming, finished with the road.

## TRACK — 015 Break New Ground
```
media_id  06810fb8-0829-4b6f-820f-118dddf94e4a
MD5       5184c87520a4f9c73af1985520d052bf    length 286.600 s
```

## MUSIC GRID — recovered after the fact, by measurement
```
BPM  134.6200      beat 0.4457150 s      bar 1.7828600 s
IN    67.3440 s
DROP  74.4690 s    = IN + 4 bars   = FRAME 171
OUT  117.2640 s    = DROP + 24 bars
28 bars = 49.9201 s -> 1198 frames @24fps = 49.9167 s
```
The IN point was recovered by FFT cross-correlation of the delivered film's
audio against the full master: a clean normalised peak at 67.344 s. The result
is self-checking — 49.920 s is 28.00 bars at that tempo, and the drop at frame
171 lands exactly on bar 4. The rebuild made from these numbers measured
-14.9 LUFS, identical to the original delivery, which confirms the section.

## FRAME PLAN — sums to exactly 1198
| # | frames | n | beat |
|---|---|---|---|
| 01 |    0– 85 |  86 | THE EYE (hook) |
| 02 |   86–170 |  85 | PAWS ON THE KERB |
| 03 |  171–299 | 129 | **THE BOLT — ON THE DROP** |
| 04 |  300–428 | 129 | STRAIGHT-DOWN OVERHEAD |
| 05 |  429–557 | 129 | UNDER A CAR |
| 06 |  558–685 | 128 | TYRE INTO THE PUDDLE |
| 07 |  686–813 | 128 | FROZEN IN THE GLARE |
| 08 |  814–941 | 128 | THE LAUNCH AWAY |
| 09 |  942–1069 | 128 | PAWS HITTING THE FAR KERB |
| 10 | 1070–1197 | 128 | SITTING, SAFE |

Measured cuts: `86 171 300 429 558 686 814 942 1070` — 9/9 exact.

## ASSET IDS
| Plate | Job ID |
|---|---|
| The cat, full body | `ee458d76-e1a6-4f20-9f3b-1548e065b897` |
| The cat, head and face | `a6b2339d-93c5-4594-8f7d-2059610f5d19` |
| The road at night | `e2811afd-fb4e-414b-a0bb-d7241ae48e3e` |

| # | keyframe | clip |
|---|---|---|
| 01 | `b525435f-7cda-4152-8e7d-f474633765ea` | `13867ef0-5a3d-40de-bd01-4a23232d40ee` |
| 02 | `14f6d34b-ccb7-4841-b89a-7b852d02d4a5` | `ecb467f8-6f58-4e83-b5ba-bd8367c59070` |
| 03 | `f535cb31-c19b-46ac-8bca-70632ef17ffc` | `80cfea6e-502f-4161-a1a3-c2269832604d` |
| 04 | `1057ce74-273d-4239-a3e7-260eaa69e488` | `5996baee-c9e0-4864-ba84-b5f73d127b58` |
| 05 | `f210776b-cf62-44d6-bd5b-36661c52c64f` | `9a7e6527-5904-4fa0-ad0d-1d4dff9e2ed6` |
| 06 | `73b8aa78-9b54-431d-a17b-83058292be1e` | `e4dd2928-d660-4516-8dd3-d36c84d8884c` |
| 07 | `6b70a300-8cd9-4481-a3de-cddc33898089` | `53160007-3ea0-4a82-a4e7-6f2ffc8fc7fb` |
| 08 | `e527e8d0-97f2-42d6-9583-040ee7ff2132` | `7c6bce9e-e748-42b2-a27e-f1cd4effefa2` |
| 09 | `d07f5f11-2d3c-4351-a542-16fd7d855678` | `e7841309-bf40-4cb7-a03e-883654098b37` |
| 10 | `38d5f3a1-5d55-458f-b392-82383db079d5` | `0c4f6d69-4d3c-41b5-a49d-bd84e3424263` |

Superseded: keyframes `b347bf9f-…` and `11c0bf4e-…` (the first sprint and glare
frames); clips `587fd8fc-…` (shot 03, the gallop that settled into a walk),
`3d70c3dc-…` (shot 04, the collision), and for shot 08 keyframe `82440343-…`
with clips `e576780a-…` and `04e9b602-…`, both of which opened a pit in the road.

## CLIENT-FLAGGED FAULTS AND WHAT THEY TAUGHT
**Shot 03, twice.** A perfect airborne gallop keyframe produced a clip of a cat
walking, twice. Text instructions did not fix it. **The fix was to make the
CAMERA carry the speed** — a whip-track with the background smeared into
horizontal blur — rather than asking the subject to hold an extreme pose.

**Shot 04 — a car drove over the cat.** The keyframe had the cat in a clear gap;
the clip closed the gap and by the end the animal was a flattened pale smear
under a silver car. This reversed the meaning of the whole film. The re-roll
states the separation as the shot's governing rule: the cat's lane stays empty
for the entire shot, with clear tarmac on every side and several car lengths to
the nearest vehicle in every frame, plus an explicit ban on the cat flattening
or smearing. **An animal and a vehicle in one frame need the gap specified as a
hard rule, not implied by "it is in a clear gap".**

**Shot 08 — the road opened into a pit, twice.** The cat appeared to fall into
it. The first re-roll declared the surface flat and unbroken and banned hole,
pit, crater, trench, manhole, sinkhole, dip and depression **by name** — and the
pit came back anyway, which I only caught because I checked a single frame of
the raw clip instead of the assembled film. **Naming the artefact was not
enough.** The real cause was structural: the shot let the cat recede down a wide,
dark, reflective road, and the model reinterpreted that dark zone as an opening
and let the animal vanish into it. The fix was to remove the dark zone and the
recession together — a new keyframe on brightly lit, evenly textured tarmac with
visible grain and a crisp lane line, the far distance held as bright bokeh so
there is no dark vanishing point, and a camera that tracks with the cat so it
stays large and never shrinks into the distance. **When a ban word fails, the
artefact is being produced by the composition, not the wording: remove the
conditions that let the model invent it.**

## COLOUR GRADE — disclosed
Shot 03's replacement came back colour-neutral against the other nine (measured
R−B of −1.4 where every other night shot ran +21 to +41). Corrected in assembly
with one pass, `colorchannelmixer=rr=0.885:gg=0.759:bb=0.626`, giving mean-Y
84.2 and R−B +26.6, inside the range of the untouched shots. No other shot was
graded and nothing was cropped.

## DELIVERY — verified
```
1198 frames · 49.920 s · 1080x1920 · 9:16 · 24 fps · AAC 48k stereo 320k
122,504,141 B   MD5 977b5b92b2b030486d5ab521a5d62caa
black 0 · freeze 0 at d=0.5, 0.4 AND 0.3 · cropdetect 1080:1920:0:0
-14.9 LUFS · LRA 1.9 LU · peak -5.0 dBFS
cuts 86 171 300 429 558 686 814 942 1070 — 9/9 exact
served file byte-identical to the local build
```
media_id `82c6f67c-92fb-4ad6-bdab-1f0951a4e3b3`

Scene detection also returns four extra hits at frames 1, 301, 173 and 559. All
were checked frame by frame and are false positives: frame 1 is the opening
fade, the rest are double-triggers one or two frames after a cut into a
high-motion shot.

## CORRECTION ROUND 3 — SHOT 04, THE HEAD OF THE SHOT
The client came back with a screenshot at 0:12: the cat still fused into the
back of a car. **They were right, and the reason I missed it is the whole
lesson of this round.**

Round 1 re-rolled shot 04 and I pronounced it fixed after checking frames 340,
380, 410 and 428 — the middle and the end of the shot. The overlap is at frames
300 to 319. **I checked the tail because the last failure had been in a tail,
and so I looked where I had last been burned instead of looking everywhere.**

Two rules now, not one:
- **Check the head, the middle AND the tail of every shot.** A defect sits
  wherever it sits; it does not care which part of the previous shot was wrong.
- **Sweep the whole film before declaring any shot fixed.** Before this rebuild
  the entire film was sampled at ten-frame intervals across all 1198 frames —
  twenty contact sheets, every one looked at. Shot 04 was the only defect in the
  film. That sweep costs minutes and would have caught this two rounds ago.

### The fix cost nothing
The Kling generation is 145 frames and only the first 129 had been used.
Inspected frame by frame, the cat–car overlap occupies **source frames 2 to 17**
and everything from frame 20 on is clear, including the 16 tail frames that had
never been used. So the shot was rebuilt from **source frames 20–144** (125
frames) and re-timed by `setpts` ×1.040 to fill the same 129-frame slot.

```
trim=start_frame=20,setpts=1.040*(PTS-STARTPTS),scale=1080:-2:flags=lanczos,
crop=1080:1920,fps=24,setsar=1    -frames:v 129
```

Every cut stays exactly on its bar line, the duration is unchanged, and **no
generation was commissioned — 0.00 credits.** The clip in the sources archive is
the same unaltered file, so `02_USED_AI_SOURCES.zip` is untouched and was not
re-uploaded. Only the master and the PDF changed.

**Before reaching for a re-roll, check whether the source clip is longer than
the slot.** Kling returns 145 frames for a 6 s job and a 129-frame shot uses 129
of them. A defect in the first or last few frames is often a re-time, not a
re-roll.

## DELIVERY — verified (round 3, supersedes the figures above)
```
1198 frames · 49.921 s · 1080x1920 · 9:16 · 24 fps · AAC 48k stereo 320k
121,485,636 B   MD5 6a6af1c5eb13be4559d1eec699a69fa3
black 0 · freeze 0 at d=0.5, 0.4 AND 0.3 · cropdetect 1080:1920:0:0
-14.9 LUFS · LRA 1.9 LU · peak -5.0 dBFS
cuts 86 171 300 429 558 686 814 942 1070 — 9/9 exact
served file byte-identical to the local build
```
master  media_id `9a0c82dc-b079-4837-acee-532f4c35c7e5`
proof   media_id `ff8f71fc-c9ea-4638-9ba4-dca74d08ee3a`  (7 pp, MD5 f982426577fb1dcf0211faf96a05e00d)
sources media_id `5ae3c1f3-8c92-472c-9a9d-c070f734af84`  (unchanged)

The extra scene-detect hits are now frames 1, 173, **314** and 559 — all checked
frame by frame, all false positives. 314 replaces the old 301: it is the fast
traffic at the top of the re-timed shot 04 crossing the 0.10 threshold, and
frames 308–318 run perfectly smooth with the cat clear of every vehicle.

## SPEND
| Item | Credits |
|---|---|
| Original build (3 plates, 10 keyframes, 2 keyframe redos, 10 clips, 1 clip redo) | 126.00 |
| Correction round 1: shots 04 and 08 re-rolled @ 9.00 | 18.00 |
| Correction round 2: shot 08 keyframe 2.00 + clip 9.00 | 11.00 |
| Correction round 3: shot 04 re-timed from the unused tail of its own clip | 0.00 |
| **total** | **155.00** |

## TRACK — identified from the master's own ID3 tags
**015 — Break New Ground** · album ALEXATOR.COM · artist ALEXATOR · 2026

Delivered as `01_FINAL_ALEXATOR_015_Break_New_Ground.mp4`.

The client asked on 12 October 2026 that every Origin Proof carry the release
number and the exact title together, in the form `006 — Towards the Dream`.
That is now in all three PDFs and applies to every future delivery. An earlier
version of this bible said the master carried no title tag — it always did;
`TRACK_REGISTER.md` records why the probe said otherwise.
