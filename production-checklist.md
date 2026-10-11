# Production Checklist: Lessons from Parts 1–2

Apply this checklist to every part.

## Story and pacing
- **Build up to big events.** Never cut straight from a normal moment to a crisis. Show warning signs first, such as a hand to the temple or a forced smile, and add a time card ("TWENTY MINUTES LATER") when time must pass.
- **Show the key action on screen.** If someone collapses, we see the body fall, not an object standing in for it.
- **Use time cards between scenes** and **name captions** the first time a character appears.

## Shots and frames
- **One speaker per shot, facing the camera.** Kling lip sync breaks when two people talk in the same clip.
- **Spell out the physical state in every frame and clip prompt.** Who is standing, lying, sitting or in a wheelchair, and it must match the scene. After the stroke, Ethan is always in the wheelchair or the bed and never standing.
- **Identify people unambiguously.** For example: "the WHITE man with short dark-brown hair and a beard". Over-the-shoulder shots must make it clear who is in the foreground, otherwise the model invents strangers.
- **Ask for one person per character.** Add "only ONE person, no duplicates" when a character appears alone, because the model sometimes doubles people.
- **Emergencies must move fast.** Prompt for "RUNNING at full speed", and include the patient on the gurney.
- **Keep necklines modest.** Low-cut frames can be blocked by Kling's content filter.
- **No empty wheelchairs in the background** while Ethan is sitting in his. The models love to add a spare one.
- **Keep wardrobe identical inside a scene.** Feed the previous shot's frame as a reference (Bradley's shirt changed color in Part 3).
- **Kling ad-libs extra words when a line is shorter than the clip.** Fill the time in the prompt ("glares in silence for two seconds, then...") and whisper-check every clip.
- **Check the identity of EVERY person in the frame, not just the subject.** Partly visible people (backs of heads, a sleeper in the background, over-the-shoulder figures) are where the model swaps in strangers: Part 3 shots 32 and 46 had a dark-skinned man in Ethan's place. Zoom in on each one and confirm skin tone, hair and beard.
- **Background extras must not be twins.** Describe each extra with different age, build, ethnicity and hair (Part 3 shot 1 had identical orderlies).
- **If a character is in bed or in a chair in one shot, every other shot of that room in the same scene must not show it empty** (Part 3 shots 47, 48 and 50). Use tight close-ups against a wall if needed.
- **Check eye color and wardrobe against the reference** (Grace came out with blue eyes once).
- **Check every frame by eye before making the clip.** Use sandbox_exec with image_paths.
- **After the cut, check the middle and end of every shot** on contact sheets, not just the opening frame.

## Voices
- **Calm lines:** use Voice Change with the locked character voice.
- **Shouted, screamed or crying lines:** keep Kling's original take. Voice Change flattens them by about 10 dB and drops the pitch, which turns screams into normal talking. Measure the original take against the voice-changed one, and if the voice-changed version is more than 6 dB quieter, use the original.
- **One-off minor characters** (nurse, board chair) and **Dr. Patel** keep Kling's own voice.
- **Voice Change changes loudness, often 5–11 dB quieter for Grace (Naomi).** For calm lines keep the locked voice and add a level-matching `gain` in the edit list rather than switching to raw.
- **Voice Change is rate-limited.** Submit about 6 jobs at a time, after the Kling queue has drained.

## Sound
- **No ambience beds.** The user rejected them.
- **Original procedural score from `tools/score.py`,** at the current low level. The music ducks 12 dB under dialogue and sits about 15 dB below speech in pauses.
- **Lower the score further if the user asks.** Never raise it without being asked.
- **The final mix is normalized to −14 LUFS** and the audio is frame-exact, so there is no drift.

## Pipeline
- **Getting tools into the sandbox:** commit and push, then curl them from raw.githubusercontent.com at that commit. Base64 blobs are refused, and this container can't reach the Higgsfield upload host.
- **Large uploads time out in the foreground.** Run the PUT in the background; a 412 on a retry means the first PUT already succeeded.
- **The sandbox resets about 10 seconds after a call ends.** Start a background `sleep 1700` lease first, then send `mb.py`, `score.py`, the edit list, the cues and the upload script.
- **Keep everything in the repo:** `tools/` (scripts, edit lists, cue sheets) and `partN-shotlist-and-jobs.md` (all IDs).

## Lessons from Part 4 viewer notes
- Props named after household objects (e.g. "broom-handle bars") get drawn as the whole object. Describe the shape only ("plain smooth round wooden rails").
- In any close-up that shows a person's hand, check that their other arm is visible or clearly out of frame, never an empty sleeve.
- Run a full contact sheet of the FINAL cut (1 frame / 2 s) and look at every tile before delivering, not just the clips that were changed.
- Voice change can garble lines spoken through gritted teeth: always transcribe the voice-changed take, not just the raw one.

## Character lock: Bradley
- Bradley is the BLOND man from Parts 2–3 (short tousled blond hair, light stubble, gold watch). Reference frames: `e59ccf4f-99ae-4084-b9cc-9bd6a543d608` (Part 3, navy blazer) and `9bf308d3-8577-40d1-a9d9-88a305a544f3` (Part 3, white shirt).
- Do NOT use the old `BRADLEY` library image (`8f021d31…`, dark slick hair + beard): it looks like Ethan and viewers confuse the two.
- Over-the-shoulder listeners must be checked as carefully as speakers (hair colour, length, neckline).

## Lessons from Part 6
- Voice change sometimes drops a soft first word ("And", "Ignore"). Always compare the voice-changed transcript's FIRST word with the script; fix with an `l` splice (first word from raw, rest locked voice).
- Kling can invent a stray word before a shouted line: trim with the `ss` key rather than re-rolling.
- Fog/mist prompts can sprout smoke puffs: say "fog hangs still, no smoke, no steam, nothing appears".
- Asking for "platinum" hair can overshoot to silver/grey (reads as an older woman): say "light buttery blonde, NOT white/grey/silver/orange" and reference the character's own close-up.
- The 2 s contact sheet can skip clips shorter than 2 s; check those by timeline position.

## No real-person likenesses (hard rule)
- Every character must be an ORIGINAL face. Harold v1 looked like Samuel L. Jackson and was replaced everywhere (Part 4 shots 16-21, Part 6 shots 1-3, 8-11, 32-33).
- Generic "distinguished older man, white beard, round glasses, three-piece suit" prompts drift toward famous actors. Give specific, ordinary, unusual features and add "must not resemble any real actor or celebrity".
- Before a new character reference is used, look at it specifically for celebrity resemblance and for names of real people / TV characters in any text on the sheet.

## Speech accuracy (from Part 6 viewer notes)
- Never put dramatic pauses ("My name... is Ethan...") or CAPS emphasis ("HIS choosing") inside a Kling dialogue line: Kling repeats or garbles words around them ("Ethan is Caldwell", "Hess choosing"). Write the line plainly and describe the delivery outside the quotes.
- Before delivering, transcribe the FINAL cut with whisper medium.en and diff every line against the screenplay; re-check any mismatch on the isolated shot (full-mix transcripts can mishear "stop that" as "stopped that").
- Voice change can also alter words ("going" -> "doing"); if two voice-change attempts alter a shouted line, use Kling's raw take.

## Over-the-shoulder listeners must be identifiable
- A minor character seen only in a far wide shot must NOT appear alone in an OTS foreground: viewers read them as a random stranger. Show them in an identifying way (both attendants together, uniforms with patches, their prop such as the stretcher), or use a main character as the listener.

## Final cut: the full movie (2026-10-11)

**Current: https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/5a92cbdd-79a0-44fb-be3b-d3893922f80c.mp4** (media `5a92cbdd-79a0-44fb-be3b-d3893922f80c`). Runtime 36:23 (2183.4 s), 1080p24, 452 MB.

- **Order:** hook, then parts 1–9, each built from `tools/*_edit_list.json` and `*_cues.json` at commit 320dd8c. The pieces were joined end to end with no gaps.
- **Hook (0:00–0:34), all Seedance 2.5:** the toast, the slow-motion fall with the glass shattering, Grace on the ground calling the ambulance, the ER gurney rush with Dr. Patel, then the title card and "A FEW WEEKS EARLIER".
- **No "PART N" cards anywhere.** Time and place cards (e.g. "THREE WEEKS LATER") are kept.
- **Upload limit:** the plain copy-concat was 690 MB and was rejected with HTTP 413. A 499 MB test upload passed. The pieces were re-encoded in parallel (x264 veryfast, 1.5 Mbps video, 160 kbps AAC audio) and then concatenated.

| Piece | Starts at | Media (pre-recompress) |
|---|---|---|
| Hook | 0:00 | 2b0ba6e5-aa04-457f-b4e0-df475e2f7f2e |
| Part 1 | 0:34 | c8dc7d41-0e70-4f02-8328-d2ecd2761756 |
| Part 2 | 6:55 | f51eab93-8823-40ba-87a1-43d2d9626f6a |
| Part 3 | 10:54 | 284e831d-b08d-451a-a0d3-1195f57462b3 |
| Part 4 | 16:00 | 87f0bd22-c748-4cfa-a9b4-ae6137da6e2b |
| Part 5 | 20:36 | 4084a3e2-d2eb-484d-97c2-15fe8fec83a6 |
| Part 6 | 25:38 | dd396c03-1000-4d29-8f2f-3bf493ab9d5c |
| Part 7 | 29:14 | 251bf439-af65-4039-8897-2e56d3a8d8e0 |
| Part 8 | 30:51 | 42e91533-a5c7-4f3b-8d75-0344651440f0 |
| Part 9 | 33:27 | a4954065-8447-4e50-93d8-e1a06cdc0efa |

## Thumbnails (2026-10-11)

These were made with the locked character references (Grace in uniform, Ethan in the wheelchair or tux, Vanessa in the red gown, Bradley). Each prompt said only the named people appear and nobody looks at the camera.

| # | Concept | Job ID |
|---|---|---|
| **A (pick)** | Rainy mansion steps. Grace kneels and holds Ethan's hand in the wheelchair while Vanessa and Bradley leave with a suitcase. "EVERYONE LEFT HIM... / ONLY THE MAID STAYED" | `00e12ad5-1f2b-465a-82ba-c60968c862d5` |
| B | Split frame: the toast collapse with shattering glass, then Grace at the hospital bed, with a Vanessa ring inset. "HIS FIANCEE LEFT... / THE MAID STAYED" | `8caa009f-225b-4c15-9400-2d967fd3be44` |
| C | Close-up of Grace crying. Ethan in the wheelchair reaches toward Vanessa leaving through the doorway. "EVERYONE LEFT THE CEO... / SHE STAYED" | `0d889765-232f-46eb-8ca6-29afcc40bb75` |

**Photoreal, no-text version of A (pick):** `8b475c70-6a36-41c0-b5a7-683c242c7795`, 5504×3072, [open](https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_20261011_124954_8b475c70-6a36-41c0-b5a7-683c242c7795.png). Runner-up, closer to A's exact layout: `19063f99-fce3-4646-b875-2e741f80095f`.
- **Feeding the cartoon thumbnail back as a reference** carried its painted look over (`0c47cda8…`, `50ecb8b8…`). Describe the layout in words and pass only the real character references.
- **Warning:** the library's `BRADLEY` reference (`8f021d31…`) shows a dark-haired, stubbled man, but Bradley is blond. That reference can produce an Ethan lookalike, so prompt "BLOND, clean-shaven" explicitly. The `35dad300…` render put a different man beside Vanessa, and `8b475c70` fixes that.
