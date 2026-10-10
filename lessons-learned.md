# The Maid Who Stayed — Lessons Learned (Parts 1–6)

Every mistake made so far, why it happened, and the rule that prevents it.
**Read this before starting any new part.** Detailed working notes stay in `production-checklist.md`.

---

## 1. The user's standing rules (never break these)

| Rule | Source |
|---|---|
| **No licensed sound or music of any kind.** Score is our own procedural score (`tools/score.py`). | User: "noo i dont want any licenced sound" |
| **No ambience beds.** Dialogue + low score only. Never raise the score unless asked. | User rejected ambience |
| **Every character is an ORIGINAL face** — never resembling a real actor or celebrity. | User: "this is a real actors face" (Harold looked like Samuel L. Jackson) |
| **Two-person dialogue is over-the-shoulder:** speaker sharp and facing camera, listener's back of head/shoulder soft in the foreground. | User: "the person being talked to is slightly showed in the frame, maybe slightly blurred or back view" |
| **Natural human voices, not storyteller/narrator presets** for main characters. | User: "not a random story telling voice" (Harold) |
| **Strict realism and continuity.** Check every image before animating. | Standing instruction |
| **Bradley is the BLOND man** from Parts 2–3, never the dark-haired one. | User flagged twice in Part 5 |
| **Every spoken line must match the screenplay.** | User: "There are a lot of speech errors here" (Part 6) |

---

## 2. Mistake log (what went wrong → fix → rule)

### Faces and identity
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 4, 6 — Harold | Harold's face resembled **Samuel L. Jackson** (prompt "distinguished older Black man, white beard, round glasses, three-piece suit" drifted to a famous actor) | New original Harold v2 (heavy-set, grey mustache, tortoiseshell glasses, navy pinstripe, burgundy bow tie); all 17 shots re-made | Describe specific, ordinary features; add "must not resemble any real actor or celebrity"; inspect every new face for celebrity resemblance |
| Library — Detective | Reference sheet labelled "Detective Sarah Linden" (a TV character) and resembled that actress | Replaced with original detective v2 before use | Check text on reference sheets for real/TV names |
| 1, 5 — Bradley | Old dark-haired Bradley ref looked like Ethan; viewers confused them (Part 5 shots 21, 55, 56) | Locked to blond Bradley refs (`e59ccf4f…`, `9bf308d3…`) | Never use library image `8f021d31…`. **Part 1 S11b and S46 still show the old Bradley (pending fix)** |
| 3 — shots 32, 46 | A dark-skinned man appeared where Ethan should be | Re-made | Check identity of EVERY person, including partly visible ones |
| 5 — shot 20 | Blurred wheelchair listener drawn as a Black man instead of Ethan | Re-made | Blurred listeners get the same identity check as speakers |
| 5 — shots 17, 19 | Blurred Vanessa had a short bob instead of long hair | Re-made | Check hair length/colour of listeners |
| 6 — shot 19 | Blurred Vanessa's hair went orange; first retry went silver (looked old) | "light buttery blonde, NOT white/grey/silver/orange" + her own close-up as reference | Name the exact shade and the shades to avoid |
| 5 — shots 40, 42 | Hospital clerk from behind looked like Mrs Hayes | Clerk changed to a young man in navy scrubs | Minor characters must not resemble main characters from behind |
| 6 — shots 21, 24 | A lone man in a blue shirt filled the foreground — viewer asked "who is this?" (he was a transport attendant only seen tiny in a wide shot) | Both attendants shown together, uniforms with patches, stretcher between them | A minor character never appears alone in an OTS foreground without identifying details |
| 3 — shot 1 | Two orderlies were identical twins | Re-made | Describe each extra differently (age, build, ethnicity, hair) |
| 2 | Grace came out with blue eyes once | Re-made | Check eye colour against reference |

### Bodies, props and continuity
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 4 — shots 22, 24, 28 | "Broom-handle bars" were drawn as whole brooms | "plain smooth round wooden rails" | Describe a prop's shape, never the household object it's made from |
| 4 — shot 42 | Ethan had one arm / empty sleeve | Re-made with both arms | In hand close-ups check the other arm |
| 3, 5 — several | Empty bed / empty wheelchair where a character should be (Part 3 shots 47, 48, 50; Part 5 ER shots 43, 45, 48) | Reframed | If someone is in a bed/chair, no other shot of that room may show it empty; no spare wheelchairs |
| 5 — shot 44 | Grace's braids hung loose instead of tied under the wrap | Re-made | Check hairstyle per scene |
| 3 | Bradley's shirt changed colour within a scene | Feed previous shot's frame as reference | Wardrobe identical inside a scene |
| 6 — shot 41 | Coffee cup in hand AFTER it had shattered in shot 29 | Removed | Track props across the scene |
| 6 — shot 1 | Harold held a book instead of the laptop he brings | Regenerated with the silver laptop | Track props across the scene |
| 6 — shot 32 | Court papers vanished from Harold's hand mid-shot | Re-rolled with "holds the papers the ENTIRE time" | Check middle frames, not just start/end |
| 6 — shot 29 | Feet with the wrong skin tone in a close-up | Regenerated with no people | Avoid ambiguous body parts |
| 6 — shot 32 | Officer's neck too dark | Regenerated | Check skin tones on partial views |
| 6 — shot 3 | Apple logo on the laptop | Unbranded laptop | No brand logos (user's Titans jersey is the only exception, per screenplay) |
| 6 — shot 12 | Fog prompt sprouted smoke puffs | "fog hangs still, no smoke, no steam, nothing appears" | Spell out what must NOT appear |

### Speech and voices
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 6 — shot 28 | "My name is Ethan **is** Caldwell" — caused by dramatic pauses "My name... is Ethan..." in the prompt | Line written plainly | **Never put "..." pauses inside a dialogue line** |
| 6 — shot 32 | "facility of **Hess** choosing" — caused by CAPS "HIS" | Plain wording | **Never use CAPS emphasis inside a line** |
| 6 — shot 33 | "An officer… hear recording" (lost "And," and "a") | "hear this recording" | Avoid tiny unstressed words where a firmer word works |
| 6 — shot 10 | "stopped" instead of "stop" | Re-roll + "in the present tense" | Transcribe every clip and every voice-changed take |
| 6 — shot 9 | "I filed" instead of "I've filed" | "I have filed" | Spell out contractions that tend to get dropped |
| 6 — shots 6, 20 | Voice change dropped the first word ("And", "Ignore") | Word splice: first word raw, rest locked voice | Compare the FIRST word of every voice-changed take |
| 6 — shot 28 | Voice change turned "going" into "doing" twice | Kept Kling's raw take (shout) | Shouts keep the raw take |
| 6 — shots 10, 22 | Kling ad-libbed "Huh?" / "Hey…" before the line | `ss` start-trim | Trim stray words rather than re-roll |
| 4 — Harold | Voice sounded like a generic narrator preset (Barrett → Sterling still wrong) | Cloned a natural voice from Harold's own raw Kling audio ("Harold natural", element `277d8e8e…`) | Main characters get natural voices; clone from raw takes |
| 4 — shot 24 | Voice change garbled a line said through gritted teeth | Re-shot with clearer diction | Transcribe voice-changed takes |
| 5 — shots 17, 42 | Voice change garbled | Raw audio | If two voice-change tries fail, use raw |
| Any | Kling ad-libs words when the line is shorter than the clip | Describe silent action to fill the time | Match clip length to the line |

### Story and editing
| Mistake | Rule |
|---|---|
| Cut straight from normal moment to crisis (Parts 1–2) | Build up with warning signs; use time cards |
| Key action shown only by an object | Show the action itself (the body falls) |
| Emergencies felt slow | "RUNNING at full speed", patient visible on the gurney |

### Pipeline
| Problem | Rule |
|---|---|
| Sandbox resets ~10 s after a call | Start `(sleep 1700 &)` first; re-curl helpers; run builds in background and poll |
| sandbox_exec hard limit ~60 s | Long jobs (whisper medium, builds) in `nohup … &`, poll in later calls |
| Voice change 429 rate limits | ≤6 jobs at a time, after Kling queue drains |
| Big uploads time out | PUT in background; 412 on retry = already uploaded |
| Files into the sandbox | Commit + push, curl from raw.githubusercontent.com at the commit SHA |

---

## 3. Pre-flight checklist for every new part

**Writing prompts**
1. Every person described unambiguously (race, age, hair colour/length/style, wardrobe); use the character-lock references (Bradley blond, Harold v2, Detective v2).
2. Over-the-shoulder for all two-person dialogue; listener identifiable (main character or clearly marked minor character with props).
3. Dialogue lines written plainly: no "...", no CAPS, contractions spelled out when risky; delivery described outside the quotes.
4. Physical state stated (Ethan standing/wheelchair/bed as per the story point); props tracked shot-to-shot.
5. Negative instructions for known failures (no smoke, no duplicates, no logos, no empty wheelchair, "must not resemble any real actor").

**Checking frames (before animating)**
6. Every face, including blurred/back views: identity, skin tone, hair, eye colour, wardrobe, props, no celebrity likeness.

**Checking clips**
7. Frames at 12 / 50 / 92 % of every clip (props mid-shot, extra people, morphing).
8. Transcribe raw take AND voice-changed take with whisper; compare word-for-word with the screenplay, especially the first word.

**Checking the final cut**
9. Contact sheet at 1 frame / 2 s; check short clips (<2 s) by timeline position.
10. Full transcript of the final mix with whisper `medium.en`; any mismatch re-checked on the isolated shot.
11. Only then deliver the link.

---

## 4. Locked references

| Character | Reference | Voice |
|---|---|---|
| Grace | library GRACE_* | Naomi `caeba733…` |
| Ethan | library ETHAN_* | Benji `e6f9b893…` (raw for shouts) |
| Vanessa | library VANESSA_* (light buttery blonde) | Celine `57ccb351…` |
| Bradley (blond) | `e59ccf4f…`, `9bf308d3…` | Reid `66469f5a…` |
| Mrs Hayes | `a06cf4f3…` | Helena `3c2b83c0…` |
| Harold v2 | `7d7b513f-a9ea-4ddc-8cf8-4c7ae77cc5bf` | "Harold natural" clone `277d8e8e…` (element) |
| Detective v2 | `9d7a04cc-bbfd-49a6-ad6e-59077f966591` | raw Kling |
| Denise, Reyes, clerk, attendants, Sam | library | raw Kling |

**Retired — never use:** Harold v1 `9d1044f9…`, Detective v1 `9d45d4c2…`, old Bradley `8f021d31…`.

---

## 5. Added during Part 7
| Mistake | Fix | Rule |
|---|---|---|
| Story beat contradicted: they kissed when the screenplay says she stops a breath away | Start frame with a visible gap + "their lips never touch" | Check every action against the screenplay's stage directions, not just dialogue |
| Start frame too close → Kling closes the gap | Regenerate the start frame | Kling continues motion from the start frame; set up the frame so the wrong outcome is unlikely |
| A character's face drifted (older, receding hair) when only the library sheet was used | Use the most recent approved close-up as the face reference | Always feed the latest approved close-up of each main character |
| Reverse-angle OTS put the speaker alone mid-bench | Generate the reverse from the matching OTS frame ("reverse angle of reference") | Keep seating geometry consistent across OTS pairs |
| Voice change dropped "'d" in "I'd better" | Raw take | Contractions like 'd and 've are fragile; check them in the voice-changed take |
| Sandbox reset killed a build while I was busy elsewhere | Restart and poll continuously | Never leave a running build unpolled for more than ~10 s |

## 6. Added during Part 8 (group scenes)
| Mistake | Fix | Rule |
|---|---|---|
| Room empty / people missing / people in the wrong seats between shots of the same scene | Keep a seating chart; generate every group frame from the latest approved group frame | In group scenes, write the seating chart into the prompt and check every person in every frame |
| A character changes position (Bradley at the head after giving up the chair) | Explicitly state the new position in every later prompt | When the blocking changes, update every later frame's prompt and references |
| Villains raising their hands in a vote against themselves | Name who does NOT act | For group actions, list who acts AND who does not |
| A prop (cane) vanished three takes in a row because the start frame had a hand in a pocket | New start frame with the prop clearly gripped; cut away before it vanishes | Start frames must show props clearly held; if Kling still drops it, cut to a reaction shot and carry the dialogue as voice-over |
| A character standing at the door also appeared seated in the background | Remove duplicates in the background | Check backgrounds for duplicates of main characters |
| Kling adds speech to non-dialogue shots ("Thank you" over applause) | Mute that clip | Transcribe silent/ambient clips too |

## 7. Added during Part 9 (the proposal & wedding)
| Mistake | Fix | Rule |
|---|---|---|
| Kling dropped a key line from a long read ("Marry her." vanished; heard as "Love her, Mom") | Cut the shot after the last correct word and generate a short continuation from that exact frame saying only the missing words | For 12 s monologues, check the LAST sentence especially; patch with a continuation from the cut frame instead of re-rolling the whole take |
| Kling inserted a hard camera cut (wide → close-up) inside a 3 s shot, and the prop vanished | `maxdur` before the cut (found with ffmpeg scene detection) | Run scene-change detection on every clip, not just eyeball 3 frames |
| Voice change turned "Ethan." into "equal" | Raw take | One-word lines are the most fragile in voice change; always transcribe them |
| Kling ad-libbed "You know," before a line | `ss` trim to just before the first scripted word | Whisper medium hears ad-libs that base misses; use medium for the check, base for timestamps |
| Licensed songs in the screenplay (Johnny Cash, "I Walk the Line") | Replaced with the original procedural score | Never use a song named in the screenplay; the score carries the moment |
| Voice change rate-limited (429) while Kling was still rendering | Submit voice changes only after the Kling batch drains, 3 at a time | Queue voice changes behind Kling, don't spam retries |

## 8. Added during the Parts 1–2 over-the-shoulder remake
| Mistake | Fix | Rule |
|---|---|---|
| Parts 1 and 2 shot conversations as separate singles, never as speaker-sharp / listener-blurred OTS | Every conversation line re-shot from a two-person OTS frame (`part1r_shots.py`, `part2r_shots.py`), cut one clip per line | Every two-person exchange is OTS, both directions, from the first part on |
| The model kept painting Grace's cross pendant on her BACK in OTS foregrounds (D1, I1, J1, L1) | Image edit: "remove the necklace from her back" | Add "no jewelry visible from behind" to every OTS prompt, and check the blurred shoulder in every frame |
| Voice change swapped small words: "Then" → "And", "dirty" → "Dodie", "a clean table" → "the clean table", "nim" for "ma'am" | Raw take for those lines | Compare the voice-changed transcript word by word, articles included |
| Voice change caps jobs in flight (429 after ~9) | Submit in batches of 9, collect, then submit the next | Batch of 9, never more |
| Kling turned a panic shout into an excited grin (Part 2 "my legs") | Re-rolled with "terrified, never smiling, frightened to the very last frame" | Check the LAST second of every emotional shot, not just the middle |
| Kling added a spoken line ("I'll take over.") to a silent beat | `ss` past it | Transcribe silent shots too |
| A kept old cutaway (uniform sleeve, daylight) no longer matched the remade scene (evening, sundress) | Two new shots from the remade frames | When a scene is remade, re-check every old shot left inside it for wardrobe and light |
| Raw Kling lines run 1–2 s of dead air before the first word | `mkremake.py` trims each line to speech −0.3 s / +0.55 s and loudness-matches it to −25 LUFS | Measure (`meas.py`) and trim every dialogue clip; never cut on the clip's full length |

## 9. Added after the viewer notes on the OTS remake
| Mistake | Fix | Rule |
|---|---|---|
| Remade lines were copied from the old shot list, which had shortened the screenplay ("can wait" for "should be able to wait", missing "Don't be sorry.", "He works too hard.", the guard's "Is it that obvious?" exchange) | 18 lines re-shot word for word | Diff every line against the SCREENPLAY (`tools/script_check.py`, `tools/script_check_all.py`), never against an older shot list |
| Pantry: Grace stood face-to-face with Bradley during his secret phone call | New first shot from behind Grace in the hallway, Bradley's back to her; he turns and sees her only after the call | Overheard moments are shot from the eavesdropper's hiding place, from behind them |
| A peeking face pasted onto the door frame read as "inside the door" | Show the eavesdropper's back and shoulder at the door edge, clearly outside | Hiding = back of the head at the frame edge, never a face flattened against the wood |
| Coffee carafe refilled itself after pouring; mug changed between shots | New burn shot starting with the carafe already set down; ice cube into the same tall white mug | Start a shot after the risky action, and reference the exact prop from the neighbouring frame |
| Vanessa knew about the inhaler with no way of hearing it (plot hole in the screenplay itself) | New mansion-hallway shot: Grace on the phone about the inhaler, Vanessa listening in a doorway; screenplay scene 15b added | Every threat or reveal must be set up on screen where the character could learn it |
| Part 4 lawyer delivered his lines straight into the lens | OTS: Harold talks to Grace (blurred from behind), plus her silent nod | No character addresses the camera; every line has a listener in frame |
| Regenerating Harold from text drifted into a celebrity-like face | Edit from a still of the approved Harold (uploaded frame) instead of describing him | Recurring minor characters: always edit from an approved still, never re-describe |
| Kling ad-libbed before scripted lines ("Train is manned", "Hey, it's me") | `ss` trim to the first scripted word | Read word timestamps of every take, not just the transcript text |
| Voice change dropped "Ah!" from "Ah! Every single morning." | Raw take | Exclamations are dropped as often as short words |

## 10. Added during the Parts 3–4 over-the-shoulder pass

| Problem | Fix | Rule |
|---|---|---|
| The listener was wrong for a line said to a third person (Ethan answering Vanessa with Grace's back in frame) | Re-edit with the person actually being addressed in the foreground | Map the listener from the screenplay line being answered, not from who stands nearest |
| A back-of-head edit showed Mrs. Hayes's pearl necklace | Edit the frame again to remove it | Check every foreground back for jewelry before animating |
| Mama's back views had gray hair and a cardigan she does not wear in her own close-ups | Edit the backs (and one close-up) to match her front shot | Use the speaker's own approved frame as the reference for their back |
| The small whisper model "heard" a "What?" over silent score | Re-check the section with medium before cutting anything | Confirm any unexpected word with the medium model on that exact time range |
| Vanessa (3057) looked almost into the lens with a toothy grin | New frame: head turned three-quarters to the listener, closed-mouth thin smile; prompt "subtle, restrained, never looks toward the camera" | Check the speaker's eyeline in the start frame; a near-frontal face drifts into the lens when animated |
| Kling ran "nice, sir" together ("nicer") | Re-roll with "nice... sir" and a stated pause | Short words after commas need an explicit pause in the prompt |
| Voice change turned "He needs help" into "She needs help" | Second voice-change pass was correct | Re-run a garbled voice change once before falling back to the raw take |
