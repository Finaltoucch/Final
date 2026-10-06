# Part 2 — The Collapse: shot list and jobs

## ✅ Part 2 v4 — film score (current)
- **Video:** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/9967082e-5dd2-483f-8393-bd8c3e562e91.mp4
- Original score from `tools/part2_cues.json`. A riser builds into the impact as Ethan's glass shatters, followed by panic strings and drums and sad hospital strings. Measured −14.9 LUFS.

## Part 2 v3 (superseded)
- **Video:** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/d3757389-7b6d-4934-86cd-52e9d1fd9a1f.mp4
- **Ambience remix:** same as Part 1 v4. Measured: −15.7 LUFS integrated. Loud speech sits about 22 dB above the ambience in pauses, and about 34 dB above it under dialogue.

## Part 2 v2 (superseded)
- **Video:** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/76bcfb71-3443-41cb-86ea-a18e2233b56f.mp4 (media `76bcfb71-3443-41cb-86ea-a18e2233b56f`)
- **Shot 46 fixed.** The old frame showed Grace twice. The new frame is `98c15e2c-d37c-47c1-9373-7fde373644b8` (GPT Image 2.5, built from shot 44's frame), the Kling clip is `49c9b61c-cd11-4340-bb2e-3d96e454b44c`, and Grace's voice is `6163086e-d68d-4e5d-9298-4d21df75537f`.
- I checked every other Part 2 shot on contact sheets and found no other duplicates or errors.

## Part 2 v1 (superseded)
- **Video:** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/ff718e91-35db-45a6-a106-a92ef540b0fd.mp4 (media `ff718e91-35db-45a6-a106-a92ef540b0fd`)
- 5 min 01 s · 1920×1080 · 16:9 · 24 fps. Sound and picture stay in sync across the whole cut (0.013 s difference).
- **Title cards:** Part 2 · The Collapse, The Engagement Party, 3:00 A.M., The Next Morning, That Night, Days Later.
- **Name captions:** Bradley Caldwell and Dr. Patel.
- **Ambience:** no licensed sound. Each scene's background is synthesized: party crowd murmur and crickets, a low tension drone, a distant siren, hospital air hum and heart-monitor beeps. The only recording is the public-domain birds track.
- Edited with `tools/movie_build.py` from `tools/part2_edit_list.json`.

Built Oct 6 2026. **One speaker per shot, facing the camera.** This gives Kling much cleaner lip sync than shots where two people talk. Speech recognition matched every line to the script.

Settings:
- **Frames:** Nano Banana Pro, 2K, 16:9. Shot 3 used GPT Image 2.5 after two failed attempts.
- **Clips:** Kling 3.0 pro. Sound is on for speaking shots and off for silent ones.
- **Voices:** Higgsfield Voice Change with the locked character voices. Dr. Patel is **Elena** `ca83ca7f-c186-493d-bd69-0d765fa861b2`, chosen because the Kling clip is female-pitched at about 180 Hz. The nurse keeps Kling's own voice.
- **Shot 38:** the line "Yesterday I ran three hundred trucks…" is a voice-over. Its audio comes from clip 381, which is never shown on screen.

| # | Speaker | Sec | Ambience | Frame | Kling clip | Voice-locked |
|---|---|---|---|---|---|---|
| 1 | — | 5 | party | `eb79269b` | `20261006_202642_f85e5e5a-404c-44cc-944b-1fb7c9dc43b7` | — |
| 2 | Bradley | 6 | party | `df11dcde` | `20261006_202642_f0314c63-c8fc-4dca-8020-0522db89ba8a` | `20261006_204329_d53fa4e4-b64b-43db-a42b-b18b09b6a28f` |
| 3 | — | 5 | party | `c3309c60` | `20261006_203021_4a8c2f48-f8de-423f-b520-bdf4617c37ff` | — |
| 4 | — | 5 | party | `e3879bab` | `20261006_202642_92d4c5c2-ce40-416d-aa1e-b998ae7d5656` | — |
| 5 | — | 5 | party | `4cb9fdc4` | `20261006_202642_d2717896-79bf-4e80-80eb-6c70269634e3` | — |
| 6 | Bradley | 6 | party | `5de0b7d6` | `20261006_202642_6d29340b-1548-4d24-b287-0b98c054188f` | `20261006_204350_5c27ca08-7530-486e-a8e3-cb7c49d2f3c3` |
| 7 | Ethan | 5 | party | `29137215` | `20261006_202642_19721bd5-2dcc-4a59-82a3-ccff4d15c41e` | `20261006_204350_68d26271-a971-42a0-ad28-87b1913a2f8c` |
| 8 | — | 5 | party_drone | `4d42ab15` | `20261006_202643_31f87cb0-1e81-48f7-b633-7770f4c83726` | — |
| 9 | Ethan | 8 | party_drone | `31b072b9` | `20261006_202642_386b2572-e78d-4799-9d8a-73e678706d29` | `20261006_204350_94ad9652-e55d-462c-9a4e-9298b34e434b` |
| 10 | — | 5 | party_drone | `e73cf895` | `20261006_202643_8fb55ba8-139b-4331-bb19-6ba7e9b9637b` | — |
| 11 | — | 5 | party_panic | `1e2f6ac5` | `20261006_202642_425f7626-a85a-4ec2-9493-cd4a3ff4022c` | — |
| 12 | — | 5 | party_panic | `e5914aa0` | `20261006_202642_6d6a6f77-5cd3-4256-af40-2f22bd65bbb4` | — |
| 13 | Grace | 8 | party_panic | `6792044c` | `20261006_202844_59849d16-8d0a-4d2a-bb6e-816f8592f6b9` | `20261006_204351_0c3589c1-89d4-43f2-bfd8-b298c6de0140` |
| 14 | — | 5 | party_panic | `1d2971cb` | `20261006_202744_74cd0d9c-6c04-4a27-aafa-3314ad8bf8ff` | — |
| 15 | Grace | 5 | party_panic | `17b5100f` | `20261006_202744_92c1d2cf-39c7-4695-ba97-de8e535cd5f7` | `20261006_204351_5eeb386e-0771-40d3-b2a1-6ee6b527656c` |
| 16 | Vanessa | 8 | party_panic | `3d71fccd` | `20261006_202744_2fd53fc9-53ca-4aa7-8f57-d3009dcb68c9` | `20261006_204542_8bf06361-5a56-45dd-aaa6-a5edda0ae6b9` |
| 17 | Grace | 5 | party_panic | `85a43053` | `20261006_202744_b08863f0-d528-4d40-926f-0bcc0bbbb176` | `20261006_204541_9a112c2a-dd5b-4697-b4c4-e42137e857c2` |
| 18 | Grace | 10 | party_panic | `7bd520cf` | `20261006_202745_515daf80-507d-4ce4-bd70-af747f4e0b8b` | `20261006_204542_40c251f6-1d37-45b3-8685-d8ec776de6e4` |
| 19 | Grace | 7 | party_siren | `9074f1d7` | `20261006_202745_58754690-3775-49a2-bfe2-f33d22f35afe` | `20261006_204541_5a498ff7-d046-43d6-875f-792bb65ee1bc` |
| 20 | Dr. Patel | 8 | hospital_rush | `41fc7543` | `20261006_202745_0b1c78a4-0390-4700-ae19-ddfff4da1925` | `20261006_204541_40928864-2a37-4cce-b67e-d8332907025d` |
| 21 | Nurse | 4 | hospital_rush | `fe86eb16` | `20261006_202745_09c6e8d0-2bed-4a8f-a80e-49ebc2612bdd` | — |
| 22 | Dr. Patel | 5 | hospital_rush | `3389df2a` | `20261006_202744_74399ff7-baf2-4ee4-8f80-dc640760ea33` | `20261006_204541_f1999e0f-dcbf-4fa7-af9b-85258bcdf788` |
| 23 | — | 6 | hospital_night | `0252af35` | `20261006_202845_827a3b54-11dc-4546-bf3d-fdc485736911` | — |
| 24 | Mrs. Hayes | 5 | hospital_night | `70fa4228` | `20261006_202847_9f3073f3-ebdf-4684-b010-6f81cd3ee9e5` | `20261006_204648_036e3707-c114-4e34-aabb-47ffc8fdc846` |
| 25 | Grace | 6 | hospital_night | `8c9a5a51` | `20261006_202844_fe2721cb-ced9-4522-9f01-06334a722586` | `20261006_204648_7627ce4f-fe73-4914-8990-fb9516e2ffe2` |
| 26 | — | 5 | hospital_night | `3812311e` | `20261006_202845_d34ee811-0f03-4e08-bb82-1662c9b0175e` | — |
| 27 | Ethan | 5 | hospital_day | `9cc18628` | `20261006_202844_7dd292e5-4b96-4502-98f9-515c569a55ae` | `20261006_204648_179ae10a-28af-4cb9-ad8d-82fc1e689dba` |
| 28 | Dr. Patel | 5 | hospital_day | `5992e2d8` | `20261006_202846_576c34f0-7515-4915-8655-8b583f18ccf7` | `20261006_204647_7ddb65b6-fa34-45a7-983b-4618317c4fb0` |
| 29 | Ethan | 4 | hospital_day | `f83818e8` | `20261006_202844_585abe2d-0c4b-4642-8f2b-7eb2fa2fbc45` | `20261006_204647_071d7c21-ec12-4a2d-98ea-31c719fcf7a8` |
| 30 | Dr. Patel | 6 | hospital_day | `34c581b4` | `20261006_202844_71b6ce9c-7dd7-4f81-97ef-ad641fc6bebc` | `20261006_204648_18cb7810-c94e-4c96-a408-084378f97338` |
| 31 | Ethan | 8 | hospital_day | `a4dead88` | `20261006_202845_c9003d36-139f-4104-b748-28ba9bf547c9` | `20261006_224207_7c99fb63-ee94-43d6-93a2-1c2fb813c547` |
| 32 | Vanessa | 6 | hospital_day | `fbdb5789` | `20261006_202845_7812f40d-2afd-4196-9de3-81f0953f81f5` | `20261006_224207_e9cbece2-7341-4748-96e2-3043fcbb6444` |
| 33 | Ethan | 6 | hospital_day | `ccebb399` | `20261006_202848_82d6cf8a-d389-498d-9abc-80afd7338afe` | `20261006_224207_55cb2fac-92cb-4b49-acf0-fb22e804ad8c` |
| 34 | Dr. Patel | 10 | hospital_day | `50cc4ad6` | `20261006_202940_1a7a4f84-5ac4-4bd6-bf62-3f33a0b06d69` | `20261006_224208_22afadc8-627b-46e1-8514-b4898ea17822` |
| 35 | — | 5 | hospital_day | `de17c1e5` | `20261006_202940_010840b2-ab32-4115-be43-3dbac2139ede` | — |
| 36 | Vanessa | 12 | hospital_hall | `37ba74a9` | `20261006_202940_61c76307-dd12-474f-b4f4-29a916ad7cfc` | `20261006_224208_f01e368f-8b3f-4eca-90ca-97d1aad79ba2` |
| 37 | — | 5 | hospital_hall | `97f13143` | `20261006_202940_4677e89c-68ab-416c-99bc-d01318d550ae` | — |
| 38 | — | 10 | hospital_night | `076530c3` | `20261006_202940_6527208d-c8ee-4b55-b6f4-8835b2627066` | — |
| 381 | Ethan | 8 | hospital_night | `4f705eee` | `20261006_202939_e252facc-4c70-4a2f-a133-ddc114403232` | `20261006_224208_1e96134d-07a0-4dd0-970b-46db9644a4ba` |
| 39 | Grace | 8 | hospital_night | `09f68e4e` | `20261006_202941_48220db9-5f06-473e-bae1-474c16a58008` | `20261006_224335_215e02cc-4ee2-44a6-896e-a56aa28490bc` |
| 40 | Ethan | 4 | hospital_night | `3ba39d38` | `20261006_202941_19aaf8fa-da24-443e-a9b0-b9f5e3131c50` | `20261006_224229_e41bc773-63a2-409e-88ac-be3f965f1998` |
| 41 | Grace | 5 | hospital_night | `c61bd21f` | `20261006_202940_3073a2ad-007e-470d-8f5d-2932c559e036` | `20261006_224229_a136d41d-5437-4a46-aec5-a854bea189ec` |
| 42 | — | 6 | hospital_night | `cd7e03aa` | `20261006_202940_703bda32-5629-4ece-841a-565a0f26ddb4` | — |
| 43 | Ethan | 10 | hospital_day | `db0582fb` | `20261006_202940_1d872626-5f9e-424a-bd45-b6d5722c3e54` | `20261006_224229_1271ad48-3898-4441-b0f9-d7b18312d504` |
| 44 | Grace | 4 | hospital_day | `9a036665` | `20261006_203021_774ef143-6343-4496-ae35-47df06578090` | `20261006_224229_9463363a-497f-4995-b44d-2e8ff090b207` |
| 45 | Ethan | 4 | hospital_day | `8e7f2064` | `20261006_203021_0a67a3fe-3b6f-452b-9416-6f64da45cdae` | `20261006_224335_347b7272-5af2-4244-8512-ae55ec5188d4` |
| 46 | Grace | 5 | hospital_day | `1252d290` | `20261006_203021_8c6fce64-5f99-41df-9717-184d44877ba6` | `20261006_224229_b9485a3a-b404-4fa9-b941-ade4d355c1b1` |
| 47 | — | 6 | hospital_day_soft | `6a383a2b` | `20261006_203022_511fe1f9-1d9b-4c00-a08a-df2c086bdfc4` | — |

## Shot descriptions

- **1** — card: THE ENGAGEMENT PARTY: Slow crane shot drifting down over the glamorous night garden party, guests mingling, string lights twinkling. Realistic natural motion, no dialogue.
- **2**: The blond man raises his champagne glass high and shouts cheerfully: "To my big brother! The man who has everything!" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **3**: The couple smile and raise their glasses as the crowd cheers and applauds around them. Realistic natural motion, no dialogue.
- **4**: The blond man and the blonde woman lock eyes for a moment; a tiny, secret, conspiratorial smile passes between them, then they look away. Realistic natural motion, no dialogue.
- **5**: The young maid with the tray watches across the garden, her smile fading into a slight frown of curiosity. Realistic natural motion, no dialogue.
- **6**: The blond man shakes two pills into his palm and holds them out with a charming smile, saying: "Don't forget your blood pressure meds, old man." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **7**: The handsome man smiles gratefully and says: "Thanks, Brad." Then he swallows the pills with a sip of water. Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **8**: The young maid's eyes narrow; she studies someone across the party, troubled, something feels wrong. Realistic natural motion, no dialogue.
- **9**: The handsome man begins a toast, smiling, then his glass starts trembling, his speech slurs and he struggles: "I want to thank... thank... everyb—" His face goes slack. Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **10**: Slow motion: the champagne glass falls and shatters on the stone path, champagne splashing. Realistic natural motion, no dialogue.
- **11**: The man in the tuxedo collapses onto the grass; guests gasp and step back in horror. Realistic natural motion, no dialogue.
- **12**: The maid drops her tray, glasses crashing, and runs toward camera through the crowd. Realistic natural motion, no dialogue.
- **13**: The maid kneels over the fallen man, cradling his face, and says urgently: "Mr. Caldwell! Ethan! Look at me. Smile for me." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **14**: The man on the grass tries to smile but only one side of his mouth moves; the other side of his face droops. His eyes are scared. Realistic natural motion, no dialogue.
- **15**: The maid looks up at the crowd and shouts desperately: "He's having a stroke! Someone call nine-one-one!" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **16**: The blonde woman in red grips the maid's arm and hisses angrily: "Don't you dare call nine-one-one! There's press here! We'll take him in our car, quietly..." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **17**: The maid pulls her arm free, lifts her phone and says firmly: "He doesn't have time for quietly!" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **18**: The maid speaks clearly and fast into the phone: "I need an ambulance at forty-one hundred Belle Meade Boulevard. Stroke. Thirty-four-year-old male. Symptoms started at nine forty-two." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **19**: Holding his hand, the maid says softly but fiercely: "Stay with me. You hear me? You stay with me." Blue ambulance lights flash across her face. Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **20**: The doctor rushes alongside the gurney and shouts: "Ischemic stroke, get him to CT now! Who noted the time of onset?" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **21**: The nurse glances at the doctor and answers quickly: "The maid, doctor." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **22**: The doctor pauses, nods slowly and says: "Then the maid just saved his life." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **23** — card: 3:00 A.M.: The older woman gently places a coat around the young maid's shoulders and sits beside her. Realistic natural motion, no dialogue.
- **24**: The older woman asks quietly: "Where's Miss Pierce?" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **25**: The tired young maid answers softly: "She said she'd come in the morning. She was tired." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **26**: The older woman says nothing, but her face hardens with silent judgment; she slowly shakes her head. Realistic natural motion, no dialogue.
- **27** — card: THE NEXT MORNING: The man slowly opens his eyes, confused, and mumbles, slightly slurred: "Where... am I?" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **28**: The doctor says gently: "Vanderbilt. You had a stroke, Mr. Caldwell." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **29**: The man in the bed says in disbelief: "I'm thirty-four." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **30**: The doctor answers calmly: "It happens. Rarely. We're running tests to understand why." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **31**: The man tries to move his arm and legs and can't. Panic rises in his face and he shouts: "My legs. Why can't I... Why can't I move my legs?!" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **32**: The blonde woman with the flowers stops dead in the doorway, stares, and whispers: "Ethan..." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **33**: The man swallows hard and says: "Doctor. Tell me the truth. Will I walk again?" Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **34**: The doctor answers carefully: "I can't promise you that. With intensive therapy, there's a chance. But it will be months. Maybe longer." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **35**: Slowly, very slowly, she sets the flowers down on the table and pulls her hand away. Realistic natural motion, no dialogue.
- **36**: The blonde woman whispers into the phone coldly: "Months, Brad. Maybe never. I didn't sign up to push a wheelchair." She pauses, listening, then: "No. Not on the phone. Tonight." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **37**: The young maid freezes at the corner, clutching the bag, shocked by what she just overheard. Realistic natural motion, no dialogue.
- **38** — card: THAT NIGHT: The man stares silently out the window at the city lights, motionless, a single tear on his cheek. Realistic natural motion, no dialogue.
- **381**: The man says quietly and bitterly: "Yesterday I ran three hundred trucks across six states. Today I can't hold a glass of water." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **39**: The maid knocks softly, smiles, and says: "Mrs. Hayes sent soup. Real food. The hospital stuff could kill a healthy man." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **40**: The man turns his face away and says flatly: "I'm not hungry." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **41**: She holds the spoon out steadily and says: "I didn't ask if you were hungry." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **42**: He glares at the spoon. It doesn't move. After a long beat, he gives in and eats the soup. Realistic natural motion, no dialogue.
- **43** — card: DAYS LATER: He scrolls through his phone, then says with a bitter laugh: "You know what's funny? When I had everything, I couldn't get a minute alone. Now nobody picks up." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **44**: She says simply, with a small smile: "I picked up." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **45**: He says dryly: "You work for me." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **46**: She shakes her head gently and says: "Not today, sir. Today's my day off." Realistic facial acting and precise lip sync, American accent, no music, clear dialogue. Only this one person speaks.
- **47**: He looks at her, really looks, for the first time. A small, surprised softness crosses his face. Slow push-in. Realistic natural motion, no dialogue.
