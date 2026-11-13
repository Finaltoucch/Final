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
| 10 | Richard | voice robotic, wants a natural elderly voice | 5 preset auditions rejected; the owner picked take B of his 8 original on-camera takes. Cloned as element `f393b386…`; all 9 Richard lines (Part 2 n42; Part 9 n43, n44, n46; Part 10 n6, n20, n33, n35, n37) re-voiced from the raw takes and verified word for word in the built cuts |
| 11 | dance 2:08 | bride and father were not Hannah and Elijah; wants an emotional ending love song | Wide dance frame rebuilt and corrected to Hannah's master (skin tone, moles, figure); new ending song (original lyrics), restructured so its vocals start only after the dance dialogue; the stray "Thank you very much" is gone |

Known transcriber artefact: in Part 11 "Good. Keeps us even." the transcriber adds a phantom "She" whenever any background sound is present (pink noise reproduces it). The dialogue track alone reads correctly, and the breath before "Keeps" is muted.

### Re-delivered (Nov 9, round 2)
| Part | Media ID |
|---|---|
| Part 2 | `753483b9-e6af-46b8-b154-fa50acdf5114` (flashback, garden scene, signing insert, Richard's new voice) |
| Part 4 | `ad042e86-abdc-4437-98e6-486430e592d4` |
| Part 5 | `810b9fbb-8ecf-42ef-b44e-8cddb5a26f75` |
| Part 7 | `ae6f362f-f1fa-49e9-8fca-ee7671a2af7c` |
| Part 8 | `046b5aad-fcb4-458d-a499-d413d594b139` |
| Part 9 | `b5e1f2a4-e561-4766-8f11-5c5232c9ba82` (bun fix + Richard's new voice) |
| Part 10 | `ea3157ab-af8d-4a4c-a695-48ebd36a903e` (Richard's new voice) |
| Part 11 | `e054777d-55f4-40f4-9d43-6d39b78f9a08` |

Audit in progress (contact sheet per part, one frame per shot): Parts 3, 6 and 8 pass. Part 10 has an open finding: Celeste wears a low chignon in the boardroom (n22) but a short bob in the corridor right after (n51–n56), on the same day.

## Nov 9 — Part 10 corridor hair fix

Celeste wore a bob in the corridor (n51–n56) but a low chignon in the boardroom the same day. The corridor frames were edited to the boardroom chignon (nano_banana_pro; ref = boardroom over-shoulder at 100.5 s): n51 `34ce4eba…`, n52/54/56 `b2ae5e9b…`, n53/55 `84112b71…`.
Re-shot in Kling 3.0: 51 `23be6753…`, 52 `751dba58…`, 53 `ff7ac041…`, 54 `607b6150…`, 55 `97520a75…`, 56 `b44a0e5b…`.
VC: 52 `5fd1715e…`, 54 `6c7ef377…` (Vera); 53 `af860df0…`, 55 `5c450422…` (Maya). The onset pop in 53's first 0.2 s was faded out. 51 uses room tone from 56 (the raw take had stray mumbling).
All four lines are word for word in the final cut, and the chignon holds in every frame. Part 10 is now 215.3 s, −14 LUFS → **`ad32dd22-4a35-4eac-bfc7-43284bdaaab6`**.

## Nov 9 — Julian re-voice (done)

The owner said Xavier sounded robotic. Reel of Julian's raw Kling takes A–H (media `3aa2559b…`); the owner picked **D** (Part 8 n28, "I know. I should have seen it at the dinner…"). Cloned as **Julian natural (D)** `2385cbbf-bcf8-4083-8dd5-778860097423` (element) from 0.4–7.5 s of that take, ×2 (14.9 s, media `e1c2220d…`). A voice-slot limit (3) needed the owner to delete the unused "Harold natural" first.

Every Julian line was found by transcribing every shot of every part as cut (Parts 1, 4, 5, 6 and 10 have none; the hook has only his non-laugh): 34 lines.
- Part 2: 40, 41, 46, 47, 49, 52, flashback 73, 75, 77, 79, 81, 83
- Part 3: 10, 14, 16, 18, 20, 23
- Part 7: 8, 10
- Part 8: 18, 20, 22, 24, 28, 35, 37, 39, 41
- Part 9: 42, 45, 64, 69
- Part 11: 9

Each line's current source (the composite or fixed version where one existed) went through VC with the new voice; files are in sandbox `aud/jul/`. Each was checked with medium.en against the previous wording.
- VC garbled two lines, which were redone from the raw Kling take: Part 9 n45 ("I even had tellers" → "Are you going to tell her?", from raw `d8b95a48…`) and Part 11 n9 ("Thank you, Star" → "Thank you, sir.", from raw `acdab416…`).
- Part 2 n79 had a pre-line breath heard as "If": the original bed was kept for 0–0.42 s, with a 0.1 s fade-in at 0.40 → both models read "I'm Julian."
- In the final cuts every Julian line reads word for word (medium.en for the short ones under music: P8 "Marcus says." / "Why?", P3 "That's it? That's the secret?").

Delivered (all −14.0/−14.1 LUFS):
- Part 2 → **`738dc44c-a63f-4fd4-9bc2-207e08cdd39b`** (325.4 s)
- Part 3 → **`744a99c3-89fc-4d2c-804b-fcc7a73092cb`** (202.2 s)
- Part 7 → **`3a946998-86eb-4229-bcd0-20a5e4f09ac0`** (188.1 s)
- Part 8 → **`0caa83e6-b1f4-4dc1-b8e8-73005c47e953`** (196.1 s)
- Part 9 → **`b31fa359-d281-4d86-bb29-3ac9425fb608`** (265.8 s)
- Part 11 → **`caa6f5e7-ca10-44c9-8e3f-963ffb474862`** (189.5 s)

Credits ran out on the last two VC retries (the extra copies of 45/9 were not needed).

## Nov 9 — last two flags, and the full movie

- Part 2 n51 (embrace after "Yes, yes, get up.", a silent shot): the raw take had a stray "Thank you." that sat at −30 dB under the score. Its audio is now true silence (`aud/jul/p2_51silent.mp4`), so only the score plays. Part 2 → **`72fd7808-92f6-41ba-9a88-5def34b642cc`** (325.4 s, −14.1 LUFS).
- Part 3 n21: no change. "Elijah. Nice to meet you, sir." is screenplay clips 21+22, deliberately merged into one Seedance take (see part 3 notes); Julian's reply "Please don't call me sir" depends on it.

Full movie = Hook + Parts 1–11 (latest cuts). Each part was re-encoded once at near-lossless quality (x264 CRF 17, 1080p24, AAC 192k) with a 0.4 s fade-in and a 0.45 s video / 0.8 s audio fade-out. The audio fade was shortened where dialogue runs to the last frame (P7 0.5 s, P9 0.08 s). Parts are joined with 0.5 s of black and stream-copied. Total 44:59 (2699.2 s), −14.1 LUFS; A/V offset is a constant 21 ms (AAC priming) with no drift.
The upload server and the app both cap a single file at 500 MB (the 1.38 GB master was refused), so the master was delivered as three volumes cut at part boundaries, with no further re-encoding:
- Vol 1 (Hook–Part 3, 13:42) **`e86a1a5b-b803-4042-a816-0234753411a1`**
- Vol 2 (Parts 4–7, 16:48) **`ee96b35c-57a4-4f43-878e-27ec98b0f890`**
- Vol 3 (Parts 8–11, 14:28) **`f4aacd8e-20e6-4e93-a44b-6c056704f9e4`**

Sandbox: `/home/user/movie/movie.mp4` (sha256 e49dd481…).

## Nov 9 — Elijah re-voiced with "Elijah natural (H)", and the Part 1 graduation fix

The owner found Elijah's voice (Bob) robotic and picked voice H from a reel of eight takes cut from his own original performances. It was cloned as a workspace element, `de6e1933-bc85-44f2-a436-5011ec80b58e`.

All 102 Elijah lines were voice-changed with the new element: Hook 2, Part 1 18, Part 2 9, Part 3 13, Part 4 13, Part 5 14, Part 6 16, Part 9 10, Part 11 7. Each line's current source (the fixed or composite clip already in the cut) went through VC. Results are in sandbox `aud/eliraw/vc/`. Every result was transcribed with medium.en and compared with the screenplay.

Lines VC garbled were rebuilt in `aud/eliraw/fix/`. The garbled word was muted and a clean line in the same element voice was laid in at the original mouth timing:

| Line | VC heard | Fix |
|---|---|---|
| Hook 9 | "She's a gardener." | seed_audio "Gardener." |
| P1 10 | "Yo, girl." | seed_audio "You'll go." |
| P1 4 | "They are pleased." | seed_audio, second sentence only |
| P1 35 | "Never met Hoop." | seed_audio "Never met who?" |
| P1 48 | "mayhem" | seed_audio "Ma'am." |
| P2 21 | "Did your eat?" | seed_audio "Did you eat?" |
| P2 56 | "Warred 11 years." | ElevenLabs (element voice) "Wore it eleven years.", second sentence only |
| P2 63 | "I watch the game." | ElevenLabs (element voice) "It's fine. I'll watch the game." |
| P4 30 | "Man." plus a laugh-like artefact | seed_audio "Ma'am?"; artefact muted |
| P5 16 | "Send out a minute." | seed_audio "Sit down a minute." |
| P6 37 | "Lockers." | seed_audio "Marcus?" |
| P9 6 | "No. Fjag." (VC also converted Hannah's "Dad.") | seed_audio "No." + Hannah's original "Dad." restored from 2.5 s |
| P9 29 | "You were scared." | seed_audio "You scared?" |
| P11 42 | "You got it." | seed_audio "Left." |
| P3 29 | "Delia can…" ("cook" too quiet) | "cook" lifted +9 dB |

Every fixed clip was re-checked with medium.en and reads word for word.

Part 1 graduation (movie 4:42): "Congratulations, Miss…" ran straight into "Ma'am." because shot 47's line was cut off at the edit.
- Shot 47 is now a Kling retake (`ba262492…`), voice-changed with H and trimmed from 1.5 s so it opens just before the full line "Congratulations, Miss Moore."
- Shot 48 "Ma'am." is the fixed H line.
- Shot 49 (silent) carries the graduation crowd ambience (`aud/p1fix/p1b_49amb.mp4`).

Patch maps: each part's `patch.json` was backed up as `patch.json.preeli` before the Elijah entries were added. The hook's `edit.json` was backed up as `edit.preeli.json`. Part 3's `d/hookseg.mp4` was re-cut from the new hook (first 49.25 s).

Final-mix checks: every Elijah shot was cut out of each rebuilt part and transcribed with medium.en against the screenplay; all lines match. Three needed further fixes after that check:
- P3 29: "can cook" was masked by the score. The phrase was rebuilt from ElevenLabs (element voice) and the shot extended by holding the last frame for 0.25 s.
- P3 34: the final "s" of "slugs" was clipped by the shot cut. Fixed with the same 0.25 s last-frame hold.
- P11 451: a breath before "Keeps" read as "She". The breath was muted.

New volume 2 came to 502.6 MB, over the 500 MB upload limit. To avoid re-encoding, the movie is now delivered in four volumes (same fades and 0.5 s black between parts, stream-copied):
- Vol 1, Hook–Part 3 (13:41): **`bf1af0c6-43e2-46f0-a7da-d93a0951a2dd`**
- Vol 2, Parts 4–6 (13:39): **`d9d37f48-ea1b-468d-86eb-12f110f04db8`**
- Vol 3, Parts 7–9 (10:51): **`1815c059-94b1-403e-93c6-83579445352c`**
- Vol 4, Parts 10–11 (6:45): **`f713cb16-962f-49ce-a1ea-d2742510e287`**

## Nov 13: new emergency hook (Seedance 2.5, 1080p)

The owner replaced the dinner hook with a suspense/emergency cold open:
- **Shots:**
  - Pre-dawn fog at the arch.
  - Elijah's hand in the grass.
  - Walter finds him and calls 911 ("A man's collapsed…"), then "Stay with me…".
  - Hannah's phone, with Julian in his car asking "Hannah, is he your father?" and her "Yes."
  - A black-and-white flashback of "Oh, he's just our old gardener." / "Enjoy your dinner, ma'am."
  - The ER rush, Hannah running in, the doors closing.
- **Sound:** no dialogue from the ER to the end (owner's call). An ElevenLabs Music suspense score runs under the hook, ducked under the dialogue.
- **Hannah's frames** were rebuilt from her master sheet `ab01076b` (sleek low bun, moles). Her "Yes." is her Part 7 recording.
- **Ending:** the original "JUST OUR OLD GARDENER" and "EIGHT YEARS EARLIER" cards from the old hook.
- **Files:**
  - Standalone hook: **`bc733b7c-127a-4e9c-8e5b-30af54d8422d`** (64.4 s; timestamps rebuilt CFR).
  - Vol 1 rebuilt: **`ac598b0b-1518-4090-94be-e92fb18007b4`** (13:52, 477.6 MB). Parts 1–3 are stream-copied with sync verified: audio and picture both shifted by +11.725 s.
  - Vols 2–4 are unchanged.
- **Chapters and captions** shifted +11.724 s after the hook; the hook captions were replaced with the new lines.
