# Part 9 (the match, Hannah's speech, pre-op, waiting room, recovery, Walter's roses) — Nov 8

Credits at start: ~662. Costs measured: Seedance 720p 7 cr/s, Kling std 1.75 cr/s, seed_audio TTS 0.1 cr.
Budget plan: Elijah on camera (Seedance, his sheet) only for the key moments; his other lines play off-camera in his own voice (Bob, seed_audio) over Hannah's/Dr. Nair's reactions, with the back of his head in the foreground of the over-the-shoulder shots. If credits run out, Part 9 is delivered in two halves (scenes 46–48, then 49–51).
Wardrobe: Elijah hospital gown; Hannah plain grey knit sweater (sc46-47), blue gown + surgical cap (sc48). Dr. Nair white coat over teal scrubs.

## Frames (batch A)
900 room wide `f1c55627` · 901 OTS→Elijah (face) `c428fede` · 902 OTS→Hannah `7886ecec` · 903 Dr. Nair at foot of bed `b8f9b113` · 904 Hannah close `60e62a77` · 905 hands insert `b0d0e88c` · 906 foreheads `fb38c401` · 910 pre-op gurneys `84159080` · 911 OTS→Elijah gurney `71661451` · 912 Hannah gurney `d6b88b35` · 913 hands across gap `cec9767f` · 914 doors `a3fbb2c7`
912b Hannah gurney (fixed: stray white man) `696f6f24` · 913b hands (fixed skin tone) `96a00c2c`

## Frames (batch B, scenes 49-51)
920 waiting wide `fa1e92c6` (door had glass, retired) → 9201 solid wooden doors `5134b5a8` · 921 Richard + Walter arrive `747e99e4` · 922 OTS→Richard `5735bd45` · 923 OTS→Julian `a272ee21` · 924 seated together `8a3d535e`
930 recovery wide `e6ac8c5e` · 931 OTS→Dr. Nair `c3862463` · 932 Hannah close `7eeda345` · 933 OTS→Julian with coat bag `309a2e7c` · 934 phone from pocket `011327b9` · 935 phone open, waveform `9d612979`
940 room wide, Walter at door `14f25f0e` · 941 OTS→Walter `ffda5b75` · 942 Elijah (face drifted, retired) `cd2721e6` → 9421 from 901 `7d8d74cd` · 943 OTS→Hannah with phone `273b6923` · 944 Walter close `b556a007`

## Clips and fixes
- 46-48: as before; 11 "I found the box" VC garbled twice ("waxed") → Maya TTS over the raw clip (d/c11). 6 rebuilt from VC take (TTS "No." + Hannah VC "Dad.").
- 49: 41 arrive (muted), 42/45 Julian (Xavier), 43/44/46 Richard (Barrett), 47 seated (silent). Caption SAINT MARY'S HOSPITAL / Waiting area.
- 50: 61 wide (caption SAINT MARY'S HOSPITAL / Recovery), 62 Nair (Imogen), 63 tears, 64 Julian (Xavier), 65 phone out, 66+67 merged (d/c66): phone plays Marcus's ORIGINAL Part 5 recording (p5 d/c3, phone-filtered), 68 Hannah raw (VC twice garbled "half a"), 69 Julian, 70 Hannah.
- 51: 71 knock, 72 Walter: Kling said "ark" → Arthur TTS "arch" over the clip (d/c72), 731 Elijah "You remembered." Seedance flagged the frame twice (nsfw/likeness) and the Kling take grinned like a famous actor → line played off-camera in Bob TTS over Walter's reaction (d/c731), 74-79 Hannah/Walter (VC; 76 VC also removed a stray "for").
- Muted silent shots where stray murmurs could be heard: 27, 28, 32, 41, 75.
- Fix: a later src.txt line overrode x_c72, so the first builds used the raw "ark" take; re-added x_c72 last and rebuilt ("From the arch." confirmed in the mix).

Edit: 57 shots, 4:26, -14.1 LUFS, no black frames. Captions: SAINT MARY'S HOSPITAL / Pre-op (28), / Waiting area (41), / Recovery (61). Cues: sad 1-10, tender 11-33, suspense 41-47, hope 61-65, dark 66-70, tender (low) 71-74, suspense 75-79.
**Delivered Part 9: media `15a84f68-8ba6-480f-a3be-4d3d26086ccd`** (full scenes 46-51). Credits after: ~2,575.

## Owner fix (Nov 8): hair + voice continuity
- Owner caught Hannah's hair loose in the wide OTS angle (902) vs sleek bun in the close angle (904) in the same scene. All 902 shots (5, 6, 11, 15, 17, 20, 22, 232) re-shot from new frame 9024 `289a96f1` (902 with her bun and the two small moles).
- Owner caught her voice changing within the scene (TTS line 11, raw line 68). Every Hannah line is now Maya VC: re-shoots VC'd; 68 re-shot (681 `b1f6a23e`, VC clean "half a"); "Dad." re-shot (807 picture, 808 VC audio, timed to lips).
- Same rule applied to all characters: Elijah's off-camera lines (3, 6 "No.", 8, 19, 731) and Walter's "arch" (72) passed through Bob/Arthur VC, so no character mixes TTS with VC.
- Checks: per-character strip (all 14 Hannah shots in the bun), pitch check across Hannah's lines (~200-210 Hz), full transcript.
**Re-delivered Part 9: media `f59d015e-785c-4396-9a71-b9a695a0e0ee`** (replaces `15a84f68`). Credits after: ~2,336.
