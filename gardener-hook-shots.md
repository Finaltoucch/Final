# Hook shot list (Seedance 2.5, 720p) — Nov 7

| # | Shot | Line | Start frame | Clip job | Voice |
|---|---|---|---|---|---|
| 1 | Wide: dinner table, Elijah pouring along the table | (chatter) | `59a14b66-bf00-404b-bbd7-4d442ae98283` | `976672ae-e2ad-4025-9d65-2cf2a011e2d5` | raw |
| 2 | OTS over Hannah → Celeste, Elijah pours her wine | CELESTE: And who's this? He's very good. | `3172cf33-5c42-4c0c-8f24-fe2612965c3c` | `53c8aba5-de05-458e-8723-ebdcafc6de0f` | Vesper |
| 3 | OTS over Celeste → Hannah freezes | HANNAH: Oh. He's just our old gardener. | `48e4ae94-2852-4429-a20a-1eeeed90a800` | `9627e496…` → VC Maya `f4759b9c-1196-4830-87d7-377a157b1e79` (words verified) | Maya ✔ |
| 4 | OTS over Hannah → Celeste | CELESTE: Well. He pours better than he dresses. | `3172cf33…` | `32abd3ec-fa9f-4360-adf3-6a8b927721c9` | Vesper |
| 5 | Julian doesn't laugh, Richard's look | (laughter) | `6982e0ae-712e-4040-9ff4-9b9229edf1a9` | `91cd3a96-d596-4017-8266-ccfb2250f594` | raw |
| 6 | OTS over Celeste → Elijah's bow | ELIJAH: Enjoy your dinner, ma'am. | `d8b92407-61e7-4ed1-81d8-a18bc84c1257` | `aaea68d0-7cee-4eef-96fc-084749e97efc` | Bob |
| 7 | Elijah fills Hannah's glass last, her hand shakes | — | `13659a47-cb82-49ca-875d-af02ea38e0a1` | `d7824994-cc27-407f-8155-76cfe1bc1747` | raw |
| 8 | Kitchen: through the swing door, bottle down, apron off | — | `9d019530-3a4f-4165-88ed-20a86f313143` | `a4d53297-66ac-411f-9de1-295b4b1b3c3f` | raw |
| 9 | The scar, "Gardener.", palm to scar, eyes close (10 s) | ELIJAH: Gardener. | `e7a59c53-a693-4f86-86c0-91c5a930cb4c` | `129dff9e-46cf-4104-9a0b-437d51aefecb` | Bob |
| — | TITLE CARD: JUST OUR OLD GARDENER [braam] / CARD: EIGHT YEARS EARLIER | | | | |

Notes: Celeste's hair renders pale platinum, matching her approved sheet; keep it consistent. Maya VC is ~3 dB quieter than raw → gain +3 in the edit.

## Hook v1 built (Nov 7)
- Final: media `272705b6-b5d2-4756-a7f0-1debdccd24f7` — https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/272705b6-b5d2-4756-a7f0-1debdccd24f7.mp4 (55.3 s, about -16 LUFS)
- Voice change used: 2 Vesper `d7d24dec…`, 3 Maya `f4759b9c…`, 4 Vesper `8216d520…`, 6 Bob `3218981f…` (all transcribed word-perfect).
- Shot 9 ("Gardener."): Bob voice change garbled the word twice ("Good idea", "Go ahead, you know") → RAW Seedance take kept (made with Bob's voice as a reference).
- Score: tools/score.py from claude/brave-allen-oc95k1 (elegant n1–n7, braam on title). Edit list and cues in the Higgsfield sandbox at /home/user/hook.

## Hook v2 — 1080p reshoot after owner notes (Nov 7)
Owner notes on v1: (1) use Seedance 1080p for the hook; (2) Elijah drifted to a celebrity lookalike in the kitchen; (3) dining room/house too small and ordinary; (4) Richard looked pasted-in.
Fixes: new grand house — dining `cade3d42-1c41-4b23-8d76-bb0f1be1af75`, kitchen `ea7e3808-adaf-4716-b570-aa0fcd147673`, exterior night `094ee923-b9e2-47fa-8db4-85ce54969c64` (day exterior `d432fb53…` is a different house → redo). All frames regenerated fresh (no edit-patching of faces). Every Seedance clip now gets the character sheets as image_references (identity lock), not just a start frame. Elijah frames compared side by side with his sheet.

| # | Frame | 1080p clip |
|---|---|---|
| 1 | `052acad1-96a5-4f0f-949e-d526e6f3df63` | `371d32d9-2d6e-4379-8449-847d10a7f268` |
| 2 | `f2abebcb-dd0d-4a08-9d90-426de9182beb` | `293a63c2-8c18-4cb0-995e-5015611055a9` |
| 3 | `654ca7f5-e95c-4eb4-b303-8197731aa91f` | `cf5f834a-5082-4ef5-ac14-ddc9fcc193c5` |
| 4 | `f2abebcb…` | `bb427a94-8b5e-40f7-b353-cc4cb5a90dbf` |
| 5 | `61c79a50-109c-4fa1-9079-d02fdd5b4bbc` | `5f32d066-2135-4e29-89d3-8194b203c4b5` |
| 6 | `315d34c8-f1e5-4e38-ad6e-ac8c377021d2` | `0e5d22e6-5b13-41a1-a9e7-832b0267d272` |
| 7 | `2e6b7399-e9da-4f03-9b59-41160f638c58` | `5ca2ff31-0b0a-4ea3-ab9e-1dc4d5321274` |
| 8 | `e52d0ec4-7921-4c48-af44-7bfab0180e8d` | `ca55c7d3-01a7-47d1-9c9c-02729ecbd6f2` |
| 9 (10 s) | `83285611-e151-4182-9cbe-ac9c995261b7` | `037a13b0-88d6-4e0b-ac04-38a6a784824f` |

New lessons: lit dramatic side profiles of older Black men drift toward a famous actor — use soft front light, 3/4 view, stubble visible, and pass the sheet as identity ref. Never fix a face by editing a group frame; regenerate. Seedance 1080p = 80 credits / 5 s.

### Hook v2 built (Nov 7)
- Final 1080p: media `b5df341a-3755-4ee7-bf57-6b224b4ddc28` — https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/b5df341a-3755-4ee7-bf57-6b224b4ddc28.mp4 (55.4 s, 1920x1080, -14.9 LUFS)
- Voice change used: 2 Vesper `40eec92e…`, 3 Maya `20a7fec1…`, 4 Vesper `742f8bdd…`, 6 Bob `cabfa8e7…` (all word-perfect).
- Shot 9: Bob VC garbled twice (added words, lost "Gardener") → raw take kept (only word: "Gardener").
- Whisper invents words over room tone ("Thank you very much", "I'm right for you") — always re-check with vad_filter=True before calling it an ad-lib.
- Build files: Higgsfield sandbox /home/user/h2 (edit.json, cues.json, build.sh).
