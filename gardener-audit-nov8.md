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

## Nov 9 corrections

### Celeste's voice: Vesper → Vera (owner's choice)
The owner said Celeste sounded robotic. Vesper had been my pick, not theirs. After a five-voice audition they chose **Vera** (`0c51919f-0756-5f8d-8169-026a339d8fd7`). All 32 Celeste lines were redone through Vera VC:
- Hook: 2
- Part 2: 6
- Part 3: 2
- Part 4: 10
- Part 8: 4
- Part 10: 6
- Part 11: 2

Every line was transcribed in the built cut and matches the screenplay. Fixes found along the way:
- **Part 3 n7 "Still no father tonight, Hannah?":** "Hannah" fell in the last 0.08 s of the shot and was clipped. Rebuilt as a TTS composite that starts 0.5 s earlier (Celeste is wide and mid-sip, so lip-sync holds), then Vera VC. Now complete.
- **Part 2 n38 "What's his handicap?":** garbled in every Kling take ("hand a pack", "handle cap") and had a stray burst at the head. Rebuilt as a Vera-preset TTS composite, then Vera VC. Both transcribers read it exactly.

### Hook v5: scar reveal
- n9 re-shot as a slow tilt from Elijah's face down to the kidney-operation scar on his side.
- Sound: low tension bed under the kitchen scene, a riser peaking as the scar appears (about 7.6 s), a soft stinger on the reveal, then the existing braam on the title card.

### Part 2 terrace lunch: everyone seated
The owner flagged shots with empty chairs. All 12 lunch shots (n31–n43) were rebuilt from three frames with everyone seated (Richard at the head, Celeste with Marcus beside her, Julian then Hannah opposite), with the camera over the shoulder onto whoever is speaking. The contact sheet shows no empty table. Celeste's silver low chignon matches front and back. Two fixes:
- **n37:** VC turned "He's" into "She's"; fixed with a Maya-preset composite, then Maya VC.
- **n40, n43:** trimmed stray words.

The scene's transcript matches the screenplay word for word.

### Re-delivered cuts (Nov 9)
All are -14 LUFS. These supersede the Nov 8 IDs above for these parts; Parts 1, 5, 6, 7 and 9 are unchanged.

| Part | Length | Media ID |
|---|---|---|
| Hook | 55.4 s | `f1610bb9-bf19-49f7-80b6-a1498f71a1aa` |
| Part 2 | 265.6 s | `92ba1a6a-849a-48f0-b2fc-0c8ed7691752` |
| Part 3 | 202.2 s | `42b5e7d3-b107-4a04-99ce-d2a4e26639b3` (embeds hook v5) |
| Part 4 | 183.6 s | `aedb099e-c137-4511-afde-ddc6343d69b2` |
| Part 8 | 196.2 s | `662caab9-3fb5-49c7-9850-dc350ad221d3` |
| Part 10 | 212.2 s | `0b805f5b-2d6b-4695-afba-7eeb6c9df63b` |
| Part 11 | 189.5 s | `3aaeb3f2-3e32-4a1e-ab52-556488dd4f78` |

## Nov 9, round 2 (owner review notes)

| Part | Where | Owner note | Fix |
|---|---|---|---|
| 2 | new scene | "We didn't show how the couple met" | New flashback ONE YEAR EARLIER → PRESENT DAY: courthouse steps meet-cute, love at first sight, original romantic score; see `gardener-part2-shots.md` |
| 2 | opening garden 0:00–0:40 | slop and glitches | Hannah's reverse shots rebuilt so she stands at arm's length (she had been ten metres away); goodbye shot rebuilt at the same rose arch (kiss, lunch bag, rose into her tote); Elijah's pill shot rebuilt at the same arch, stray "Okay" removed |
| 2 | signing insert ~1:09 | "they are sitting apart" | Insert rebuilt across the desk: her hands sign, his hand taps the flags from the far side |
| 4 | luncheon 2:00–2:45 | Hannah appears from nowhere; cuts not smooth | Celeste's reverse angle had her standing at a small round table, alone. New reverse frame has her seated at the long table with her friends (no empty chairs). Napkin slide added; she never takes the napkin; Hannah now steps out through the terrace doors. Lines re-voiced (Vera/Bob/Maya); "Ma'am?" and "Since you're here." rebuilt as exact-line composites |
| 5 | 3:54 | unfinished line; owner changed it to "Good night, Dad." | Maya VC kept turning "Dad" into "Gad", so I spliced "Good night," (new VC) with the verified Maya "Dad." from the earlier take; both transcribers read "Good night, Dad." |
| 7 | 0:00 | the man on the ground is not Elijah | Frame rebuilt from Elijah's references (grey hair, brown wool coat); re-shot |
| 8 | 1:25 | "Call whoever you like. I'm still marrying her." | "her" was clipped at the cut; exact-line Xavier composite placed earlier, then VC |
| 9 | 0:21 | Hannah's hair loose | Frame fixed to her sleek low bun; picture re-shot; the verified audio was kept |
| 10 | Richard | voice robotic, wants a natural elderly voice | 5 preset auditions rejected; offered his 8 original on-camera takes (A–H) to clone a natural voice. **Waiting for the owner to pick.** |
| 11 | dance 2:08 | bride and father were not Hannah and Elijah; wants an emotional ending love song | Wide dance frame rebuilt and corrected to Hannah's master (skin tone, moles, figure); new ending song (original lyrics), restructured so its vocals start only after the dance dialogue; the stray "Thank you very much" is gone |

Known transcriber artefact: in Part 11 "Good. Keeps us even." the transcriber adds a phantom "She" whenever any background sound is present (pink noise reproduces it). The dialogue track alone reads correctly, and the breath before "Keeps" is muted.

### Re-delivered (Nov 9, round 2)
| Part | Media ID |
|---|---|
| Part 2 | `bd6ae0ee-2e70-4058-a680-ff11c8532a33` (flashback + garden scene + signing insert) |
| Part 4 | `ad042e86-abdc-4437-98e6-486430e592d4` |
| Part 5 | `810b9fbb-8ecf-42ef-b44e-8cddb5a26f75` |
| Part 7 | `ae6f362f-f1fa-49e9-8fca-ee7671a2af7c` |
| Part 8 | `046b5aad-fcb4-458d-a499-d413d594b139` |
| Part 9 | `f0053b4f-a6a6-4ff4-b615-11aaae4ce356` |
| Part 11 | `e054777d-55f4-40f4-9d43-6d39b78f9a08` |
