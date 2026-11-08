# Audit of Hook and Parts 1–8 against the Nov 8 hard rules

The owner asked for this on Nov 8 ("yes start"). It checks the two hard rules in `gardener-references.md`:
1. Hair, wardrobe and props are locked per scene. Every frame of a scene is compared side by side.
2. Each character has one voice source. Every line goes through that character's voice change (VC), with no raw model voices and no un-VC'd TTS. The words must match the screenplay exactly.

## How it was checked
- **Visual:** a contact sheet for every built part (one frame per shot). Every scene was inspected per character for hair, wardrobe and props. Suspicious shots were zoomed side by side.
- **Words:** each part was transcribed whole with medium.en (`lt.py`) and aligned against that part's screenplay dialogue. Every mismatch was then re-checked on the isolated shot. Transcriber normalisations were ignored (numbers, "all right"/"alright", contractions, elided "liked the").
- **Voice:** traced the source of every on-camera line (raw Kling, TTS or VC) and voice-changed anything that wasn't VC.

## Fixes made

### Voice source (rule 2)
| Part | Shot | Line | Problem | Fix |
|---|---|---|---|---|
| Hook | 9 | "Gardener." | TTS | TTS→VC Bob; the stray "Right." before it was replaced with room tone |
| Hook | 5 | (reaction shot) | stray intelligible "around the deuces" in the ambience | ambience replaced with clean dining-room tone |
| 1 | 1, 19, 25 | Halbrook / Greenfield / "And you'll have a dad…" | raw Kling (25 also dropped "And") | re-shot from first frame with the exact line, then VC (Maya/Maya/Bob) |
| 1 | 9 | "I'll work a couple of years and—" | "of" missing | TTS composite of the exact line, then Maya VC |
| 1 | 35, 46, 48 | short lines | raw | TTS composite, then VC |
| 2 | 4 | "Sunday. Lunch at my sister's…" | raw | re-shot, then Grady VC |
| 2 | 18, 25 | "He is." / "…keep doing this." | raw ("this" became "that" in a grouped VC) | composite, then individual Maya VC |
| 2 | 38, 43, 60 | "handicap" / "…on this." / "…Celeste is a lot." | garbled or last word clipped at clip end | re-shot with a silent tail, then Vesper/Vesper/Maya VC |
| 3 | 7, 10, 15, 20, 29 | short lines | raw | composite, then VC |
| 3 | 18 | "That's it? That's the secret?" | raw | Xavier-preset TTS composite, then Xavier VC |
| 3 | 31, 33 | "I heard you." … / "You don't know these people…" | raw | re-shot, then VC |
| 4 | 6 | "Mine's a disgrace…" | raw | re-shot, then Vesper VC |
| 4 | 29, 30 | "Boots." / "Ma'am?" | raw; VC turned "Ma'am" into "Man" | Vesper TTS→VC; "Ma'am" spliced from Elijah's verified VC'd "Ma'am." (same Bob voice) |
| 5 | 1, 3, 31 | Marcus's phone call and the recording excerpt | TTS, never VC'd | Grady VC; stray leading "And" muted; phone excerpt rebuilt from the VC'd audio |
| 5 | 19, 28, 34, 50 | short lines | raw ("Okay" TTS was silent and was regenerated) | composite, then VC |
| 6 | 5, 27, 51 | "In his coat, sir?" / "You eat?" / "Dad—" | raw | composite, then VC (Arthur/Bob/Maya) |
| 6 | 47, 65 | "I'd have carried them." / "I finish the arch." | TTS | Bob VC |
| 7 | 19 | "No. He only has one." | TTS | Imogen VC |
| 8 | 41 | "Then we'd better hurry." | TTS | Xavier VC |

### Hair, wardrobe and props (rule 1)
| Part | Shots | Problem | Fix |
|---|---|---|---|
| 1 | 46, 49 (graduation) | Hannah's long braids disappear in the front shots but are clearly there from behind | frames rebuilt with braids; 46 re-shot (line, then Maya VC); 49 re-shot with the original ambience |
| 3 | 2, 4, 6, 13 (kitchen) | Delia has grey hair from the front but dark brown from behind | frames rebuilt with her grey low bun; re-shot with exact lines, then Bob VC |
| 3 | 26, 27, 29, 31, 34 (night garden) | Hannah's slip dress shows straps from the front but reads as off-shoulder from behind | frames rebuilt with spaghetti straps; re-shot with exact lines, then VC; "Delia can cook" spliced from the verified VC take |
| 5 | 9, 11 (Marcus and Elijah at the hedge) | from behind, Marcus has grey, longer hair instead of his dark slicked-back hair and glasses | frames rebuilt; re-shot, then Bob VC; "Deadheading" spliced from the verified VC take |

Parts 2, 4 and 6, and the hook, passed the per-character visual check unchanged. Parts 7 and 8 were only rebuilt for the VC swaps listed above.

### Known transcriber artefacts (checked by ear and accepted)
- "They liked the wine": the elided "d" is heard as "like", even on a TTS of the exact sentence.
- "Halbrook" is sometimes transcribed as "Hal broke".
- "eleven dollars" is transcribed as "$11".

### Not changed (noted for the owner)
- Celeste's hair across parts: a chignon in the hook and Parts 2–4 and 11, a short bob in the Part 10 corridor. This is a different scene and day, so it isn't a rule-1 breach, but it is a cross-part inconsistency the owner may want fixed.
- Walter's look across parts: balder in Part 2 than in Parts 4–6.

## Re-delivered cuts (Nov 8, after the audit)
These replace the earlier deliveries of the same parts. All are -14 LUFS.

| Part | Length | Media ID |
|---|---|---|
| Hook | 55.4 s | `84a47a45-a3dc-4def-8148-d51d0ea6baea` |
| Part 1 | 237.5 s | `ffcef35a-19e6-4fb4-9fb0-5aedd6863828` |
| Part 2 | 256.9 s | `28090169-cbcc-4367-a81d-0919343c628b` |
| Part 3 | 202.4 s | `1c4149ac-6ecb-4a63-9f8a-d6ba54c6de6e` (embeds the new hook) |
| Part 4 | 183.6 s | `0e6fa846-083f-4fc1-b892-2fbea65dbffa` |
| Part 5 | 249.0 s | `c2125dbd-bcdb-46ea-9c79-96f0741e2bd5` |
| Part 6 | 385.4 s | `8adad23b-7c01-47dd-9cc5-babca2c97ab8` |
| Part 7 | 187.9 s | `fab8a887-6b3e-4528-9fc2-63e91bcd0315` |
| Part 8 | 196.2 s | `cd5bb2f0-7940-4ba9-a22c-27376a00558d` |

URL format: `https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/<id>.mp4`

Listen-through similarity to the screenplay (medium.en, before the per-shot re-checks):
- Part 1: 0.970
- Part 2: 0.959
- Part 3: 0.932 (the embedded hook counts as an insert)
- Part 4: 0.973
- Part 5: 0.962
- Part 6: 0.980
- Part 7: 0.965
- Part 8: 0.990

Every residual difference was re-checked on the isolated shot and is a transcriber artefact, except the lines fixed above.

Parts 9–11 were built after the Nov 8 rules and were audited then (see their shot logs).

## Build note
The sandbox kills background jobs after 15 minutes, so run each part build (`bash build.sh`, about 5–7 min) as its own job, never chained. `h2/build4.sh`'s loudnorm pass is broken; finish the hook with `h2/fin4.sh` (ebur128 measurement, then volume and limiter).
