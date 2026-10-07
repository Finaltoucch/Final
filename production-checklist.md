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
