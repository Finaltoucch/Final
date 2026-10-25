# Studio Playbook: how we make a full AI drama movie

This playbook is everything we learned making **The Maid Who Stayed** (a 36-minute, 9-part drama with a hook). It is written so a new story can start in a fresh chat and reach the same standard on the first pass. **Read the whole file before writing a single prompt.**

Companion files in this repo:
- `lessons-learned.md`: the full mistake log, with each mistake, its fix and the rule it produced.
- `production-checklist.md`: working notes and links for the final cut.
- `voices-and-sound.md`: the voice library and the score design.
- `youtube-upload-kit.md`: the upload kit for the finished film, to use as a template.
- `the-maid-who-stayed-movie-screenplay.md`: a screenplay in the format that works.
- `tools/`: the build pipeline, which works for any story. See section 8.

---

## 1. The owner's standing rules (never break these)

| # | Rule |
|---|---|
| 1 | **No licensed music, songs or ambience beds.** Use only our original procedural score (`tools/score.py`) plus its SFX. If a screenplay names a song, the score replaces it. |
| 2 | **Original faces only.** No character may resemble a real actor or celebrity. Describe ordinary, specific features, add "must not resemble any real actor or celebrity", and inspect every new face. |
| 3 | **Two-person dialogue is over-the-shoulder (OTS)** in both directions. The speaker is sharp and the listener is the soft back of the head and shoulder in the foreground. |
| 4 | **Nobody looks into the camera.** The eyeline always goes to a listener in frame, in profile or three-quarter view. |
| 5 | **Natural human voices**, never narrator or storyteller presets. Shouts, screams and crying keep Kling's raw take. |
| 6 | **Every spoken line matches the screenplay word for word.** Check against the screenplay, never against an older shot list. |
| 7 | **Strict realism and continuity**: wardrobe, props, hair, seating, day or night, standing, wheelchair or bed. |
| 8 | **No jewelry visible from behind** on OTS foreground backs. |
| 9 | **No lookalikes.** Each lead has a unique look (for example "the only dark-haired bearded man"), and no extra may share a lead's face. Zoom into every crowd shot. |
| 10 | **The hook is the real story, not a patched trailer.** It opens on the strongest true moment (toast → collapse in slight slow motion → call for help → ER rush), then the title card, then "A FEW WEEKS EARLIER". The same shots are reused in the movie. |
| 11 | **The final movie has no "PART N" cards and no blank black gaps.** Time and place cards ("TWO WEEKS LATER") are fine. |
| 12 | **Check the work before showing it.** The owner will catch it otherwise. |
| 13 | **Don't use the #AIMovie hashtag or an "ai movie" tag** in the YouTube metadata. The YouTube synthetic-content checkbox is still set to Yes, because the platform requires it. |

---

## 2. Story formula (what worked)

- **Length:** about 36–40 minutes as a hook plus 9 parts of 2–6 minutes each, built and checked one part at a time.
- **Shape:**
  1. Humble hero arrives.
  2. Kind rich lead.
  3. Cruel rival or fiancée.
  4. A crisis at a big event (the collapse).
  5. Everyone abandons the lead.
  6. The hero stays and helps.
  7. A hidden villain plot is uncovered (poison or pill swap).
  8. The hero is framed.
  9. A rescue.
  10. A public reckoning (the boardroom).
  11. A proposal or wedding, then closing quote cards.
- **Show the key action on screen** (the body falls), never just an object standing in for it.
- **Build up to every crisis** with warning signs: a hand to the temple, a forced smile, a time card.
- **Every reveal or threat is set up on screen** where the character could have learned it. Plot holes get a new scene.
- **Overheard moments** are shot from behind the eavesdropper, with the back of their head at the edge of the frame.
- **Title options** follow a contrast plus a promised payoff: "Everyone Left the Paralyzed CEO… Only the Maid Stayed | Full Movie".

---

## 3. Camera and shot language

| Situation | Shot recipe |
|---|---|
| **Two-person dialogue** | OTS: the speaker in medium close-up, sharp and facing three-quarter toward the listener. The listener's back of head and one shoulder sit soft in the foreground (left or right). Prompt: "seen only from behind, no face visible, no jewelry visible from behind." Shoot the reverse from the matching OTS frame so the seating geometry holds. |
| **Line addressed to a third person** | The person actually being answered goes in the foreground. Work out the listener from the screenplay line, not from who stands nearest. |
| **A minor character speaking** (lawyer, doctor) | OTS to a main character, never into the lens. Always edit from an approved still of that character, never re-describe them. |
| **Doctor or authority figure in motion** | Side tracking shot, profile eyeline on the patient or colleague. |
| **Collapse or fall** | Wide shot, the body falls in **slight slow motion** and realistic weight, with a separate glass-shatter insert, then the crowd's reaction. Seedance 2.5 does this best. |
| **Call for help** | The hero kneels on the ground beside the lead, phone to ear, reading out the address and the time. The lead stays visible. |
| **Emergency gurney** | Side tracking at running speed, the patient clearly on the gurney, nurses described differently (no male lookalikes), the doctor in profile. |
| **Entrances** | Through solid wooden doors set in a wall, coming from a corridor. **Never through glass doors that open onto sky or skyline** ("people don't fly"). The skyline appears only in side windows. |
| **Eavesdropping** | From behind the hidden character in the hallway, the target's back to them, and they turn only after the call ends. |
| **Group scenes** (boardroom, party) | Write the seating chart into every prompt. Generate each group frame from the latest approved group frame. List who acts and who does not ("only the blond man and the blonde woman keep their hands down"). |
| **Hands and props** | Start frames show props clearly gripped. If a prop keeps vanishing, cut away to a reaction shot. Check every hand for stray or disembodied hands. |
| **Emotional peaks** | Describe the emotion through to the last frame ("terrified, never smiling, frightened to the very last frame"). |

**Prompt rules for every frame:**
- Describe every person unambiguously: race, age, hair colour, length and style, beard or not, and wardrobe.
- State the physical state (standing, wheelchair or bed), carry props from shot to shot, and keep wardrobe identical within a scene.
- Spell out the negatives: no duplicates, no logos, no smoke or steam, no empty wheelchair, no extra hands, "must not resemble any real actor."
- Name hair shades and the shades to avoid ("light buttery blonde, NOT white/grey/silver/orange").
- Describe a prop's shape, not the household object it was made from ("plain smooth round wooden rails", not "broom handles").
- Avoid ambiguous body parts. Show either the whole person or no people.

**Dialogue prompt rules** (for Kling lip sync):
- Write lines plainly: **no "..." inside a line, no CAPS emphasis.** Spell out fragile contractions ("I have filed").
- After a comma, state the pause explicitly if the short word matters ("nice... sir" plus "a short pause").
- Fill the clip length with silent action, or Kling will ad-lib.
- Add "Only the person facing the camera speaks; everyone else stays silent. Each word is said exactly once."

---

## 4. Models and costs (Higgsfield)

| Job | Model and settings | Notes |
|---|---|---|
| Character sheets, frames, thumbnails | `nano_banana_pro` (may report as nano_banana_2), 2k or 4k, 16:9 | Image edits ("edit this exact image…") are the best way to fix one detail. |
| Dialogue and most shots | `kling3_0`, mode `pro`, 3–5 s, `start_image`, `declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612` | Lip sync is good. It ad-libs if the clip is longer than the line. |
| Hero action (fall, ground scene, gurney, crowds) | `seedance_2_5`, mode `omni_reference`, `image_references` | **Draft first** (`draft:true`, 480p, about 3 credits/s), then finalize with `draft_job_id` and identical params (about 12 credits/s at 1080p, 7/s at 720p). The finalize is charged at full price. |
| Voices | `voice_change` with preset voice IDs | About 9 jobs in flight at most. It returns 429 while Kling is busy, so queue it after the Kling batch finishes. |
| Natural custom voice | `create_voice` cloned from the character's own raw Kling take | Used for "Harold natural". |

**Face references:** the faces the owner accepts as "the real characters" are **frames grabbed from the movie itself**, not the original library sheets, which drifted. Grab a clean front frame of each lead early and use it as the reference for every later shot, thumbnail and poster.

---

## 5. Voices

- Lock one preset voice per character in a table on day 1, with the voice ID. Example cast from The Maid Who Stayed:

  | Character | Voice | ID |
  |---|---|---|
  | Grace | Naomi | `caeba733-3c17-43db-863e-69c7025512cd` |
  | Ethan | Benji | `e6f9b893-51b1-51d3-afe9-9e0482cb7ac1` |
  | Vanessa | Celine | `57ccb351-84d7-54ba-afd4-26b566ca6023` |
  | Bradley | Reid | `66469f5a-10db-586a-bab1-72f6ee66ba69` |
  | Mrs. Hayes | Helena | `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd` |
  | Mama Ruth | Opal | `66f35c82-2088-55eb-a0aa-7bf715dc03b7` |
  | Dr. Patel | Elena | `ca83ca7f-c186-493d-bd69-0d765fa861b2` |
  | Guard | Desmond | `563f728c-e249-5a85-97ab-8461e8c09da6` |

  Reuse these voices for new characters of the same type, or pick new ones by description.
- **Voice change garbles small words.** Transcribe every voice-changed take and compare it with the screenplay word by word, especially the first word, articles, one-word lines, exclamations, and contractions like 'd and 've.
- **If a voice change garbles a word:** re-run it once. If it fails again, keep Kling's raw take.
- **Shouts, screams and crying stay raw.** Voice change flattens them by about 10 dB.
- Voice change shifts loudness. Fix it with `gain` in the edit list rather than switching to the raw take.

---

## 6. Music and sound (`tools/score.py`)

- **Original procedural score only.** It uses no samples, so there's no Content ID risk. Cues:

  | Cue | Use |
  |---|---|
  | `hope` | Soft piano arpeggios for arrivals and new beginnings |
  | `elegant` | Piano waltz for the mansion and parties |
  | `tender` | Piano and strings for romance |
  | `suspense` | Plucked ostinato with a drone for scheming and bullying |
  | `tension` | Heartbeat, drone and dissonance for discoveries |
  | `dark` | Braams, heartbeat and cluster for threats and betrayal |
  | `panic` | Fast strings and drums for the collapse and the ER |
  | `sad` | Slow strings for the hospital and grief |

- **SFX:** `riser` (with `len`), `impact`, `stinger`, `braam` and `whoosh`. A whoosh plays automatically on every title card.
  - Collapse pattern: a riser into an impact on the fall (for example `{"sfx":"riser","at":"n10","len":3.3}` plus `{"sfx":"impact","at":"n10","off":3.3}`), then `panic`.
  - Title card: a braam.
- **Levels:**
  - The music sits at about −40 dB RMS, very low.
  - It ducks about 12 dB under dialogue automatically.
  - The final mix is normalized to **−14 LUFS**, TP −1.5.
  - **Never raise the score unless the owner asks.**
- **No ambience beds** (they were tried and rejected).

---

## 7. QA: check everything before the owner sees it

1. **Frames, before animating:** check every face, including blurred backs, for identity, skin tone, hair, eye colour, wardrobe, props, jewelry on backs, celebrity likeness and lookalikes in crowds. Check the eyeline (no near-frontal faces). Check doors and windows (no entrances from the sky). Check for disembodied hands.
2. **Clips:**
   - Look at frames at about 12 %, 50 % and 92 % of each clip.
   - Run ffmpeg scene detection to catch hidden camera cuts, then use `maxdur` before the cut.
   - Check the last second of emotional shots.
3. **Speech:**
   - Run Whisper on both the raw and the voice-changed takes. Use `medium.en` for checking and `base.en` for timestamps.
   - Diff the result against the **screenplay** (`tools/script_check.py`).
   - Transcribe silent shots too, because Kling adds lines.
   - Trim ad-libs with `ss`.
4. **Each part:** make a contact sheet at 1 frame every 2 s, then transcribe the full mix with Whisper medium.
5. **Full movie:**
   - Run blackdetect for blank stretches.
   - Confirm there are no PART cards.
   - Confirm the hook order: toast → fall → call → ER → title.
   - Check every part boundary.
6. Report honestly what was checked and what wasn't.

---

## 8. Build pipeline (reusable for any story)

**Edit list** (`tools/<part>_edit_list.json`): an ordered list of entries.
- Card: `{"card": "TWO WEEKS LATER", "sec": 2.6}`.
- Clip: `{"n": 12, "t": {"G": "<job stem or full URL>"}, "ss": 1.2, "maxdur": 6.5, "gain": -2, "mute": [[a, b]], "lt": [["DR. PATEL", "Emergency physician", 1.0, 4.0]], "vo": "<stem>"}`.
  - `ss` trims the start.
  - `maxdur` is the absolute end time within the clip.
  - `lt` adds a lower-third caption.
  - `vo` replaces the audio with another take.

**Cues** (`tools/<part>_cues.json`):
- Music: `{"cue": "tension", "from": "n6", "to": "n9", "gain": -2}`.
- SFX: `{"sfx": "impact", "at": "n10", "off": 3.3}`.
- Keys are `n<shot number>` or `c:<CARD TEXT>`.

**Build** (in the Higgsfield sandbox, in the background, polling until done):
```bash
R=https://raw.githubusercontent.com/<owner>/<repo>/<commit-sha>/tools
curl -sfO $R/mb.py; curl -sfO $R/score.py; curl -sfO $R/part1_edit_list.json; curl -sfO $R/part1_cues.json
python3 mb.py part1_edit_list.json            # writes vid.mp4, dlg.wav and timeline.json (frame-exact 24 fps)
python3 score.py timeline.json part1_cues.json dlg.wav vid.mp4 part1.mp4
```
Then run `media_upload`, PUT the file with `Content-Type: video/mp4` and `If-None-Match: *`, and call `media_confirm`.

Other helpers:
- `meas.py`: measures speech start and end and loudness.
- `mkremake.py`: trims each line to the speech and loudness-matches it.
- `script_check.py` / `script_check_all.py`: diff the transcript against the screenplay.
- `sheet.sh`: makes contact sheets.
- `tr.py` / `trm.py`: Whisper transcription.

**Full movie:**
1. Build the hook and every part, then re-encode each piece in parallel (x264 veryfast, 1.5 Mbps video, 160 kbps AAC).
2. Concat with `-c copy` and `+faststart`.
3. **The upload limit is about 500 MB** (690 MB returned 413; 499 MB uploaded fine), so stay around 450 MB.

**Sandbox gotchas:**
- Foreground calls are limited to about 60 s, so run long jobs with `background:true` and poll.
- A `pgrep -f` wait loop matches its own command line.
- The local container can't reach CloudFront (403), so everything media-related runs in the sandbox.
- Show results to the owner with `show_result(media_id)` for videos and `show_generation_by_ids` for images. Links alone aren't enough.

---

## 9. YouTube packaging (template: `youtube-upload-kit.md`)

- **Thumbnail that worked:** in the style of "The Billionaire Maid".
  - The hero is in uniform with a prop, glancing back, and the love interest leans in behind.
  - A cold rival (red dress, arms folded, engagement ring) stands on the other side of a gold lightning split.
  - Use a warm, blurred mansion background and photorealistic faces taken from movie frames.
  - Nobody looks at the camera.
  - The owner preferred **the no-text version**. A gold serif title with a crown and red ribbon is the optional text version.
  - Deliver at 1280×720 JPG, under 2 MB.
- **Captions:** transcribe with Whisper small.en in 8 parallel chunks, then fix names and terms against the screenplay. Remove the repeated lines Whisper invents over music (for example "I'm sorry" ×12) and cap how long each caption stays on screen.
- **Description:** a 3-line hook paragraph, then a story paragraph, then chapters (start at 0:00, one per part), then a question, then subscribe, then 3 hashtags, then the fiction disclaimer.
- **Pinned comment:** write it as the creator, personal and story-specific. Don't quote a random line with a timestamp. Example: "I made this one for everyone who has ever been the only person who stayed… what would YOU have done in her shoes? And did you see the twist coming?"
- **Upload time** for this channel (from Studio analytics):
  - The audience peaks around 6–10 PM GMT+1 every day, strongest Friday to Sunday.
  - Schedule for **Friday about 3–4 PM GMT+1**.
  - 99.5 % of watch time is from non-subscribers, so the thumbnail and title matter most.
- **Settings:**
  - Not made for kids.
  - Altered or synthetic content set to **Yes**.
  - Category Film & Animation.
  - End screen in the last 10 s, kept clear of the closing quote cards.

---

## 10. Order of work for a new story

1. Write the screenplay: a hook plus 9 parts, with every line final. Fix plot holes before shooting.
2. Write the cast sheet (unique look per lead, no lookalikes), generate the character sheets, check them for celebrity likeness, and lock the voices.
3. Make the location sheets. Doors go in interior walls.
4. Work through one part at a time:
   1. Write the shot list (`tools/partN_shots.py` style).
   2. Generate the frames and check them.
   3. Generate the clips and check them.
   4. Voice-change the clips and transcribe them.
   5. Build the edit list and cues, build the part, run QA, and deliver it.
5. Build the hook last, from the real best moments (Seedance for the action), and reuse its shots in the matching part.
6. Assemble the full movie, run QA on it, and upload it.
7. Prepare the YouTube kit: thumbnail, title, description and chapters, tags, captions, pinned comment and schedule.
8. Log every new mistake in `lessons-learned.md` as it happens.
