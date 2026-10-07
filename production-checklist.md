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
