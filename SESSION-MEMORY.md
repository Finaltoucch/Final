# Session memory: hand-off to a new chat

The state of the project at the end of the first chat. A new chat should read this **first**, then the files it points to.

## Who you're working with
- The owner runs the YouTube channel **Kharune Studios** and makes full-length AI drama movies on Higgsfield.
- They write short, fast messages, often with typos, and expect you to work out the intent and act. They get frustrated when mistakes reach them, so **check your own work before showing anything.**
- They want results shown in the Higgsfield widgets (`show_result` for videos, `show_generation_by_ids` for images) plus a link. A path to a sandbox file is no use to them.
- A short question like "??" or "did you add it?" is a question, not an instruction to change something. Answer it plainly.

## What's finished
- **The Maid Who Stayed**, a 36:23 movie (hook plus 9 parts), is uploaded and doing well: **38K views in 2 weeks**. The owner says the structure, emotional hook and storyline worked.
  - Final cut (v2): https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/dc702e42-0351-419f-a0d9-84dfa9e93a08.mp4
  - YouTube kit (title, description with chapters, tags, hashtags, captions, pinned comment, thumbnails): `youtube-upload-kit.md`.
  - The thumbnail the owner chose is in the "Billionaire Maid" style, without text: https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/7e4f97d8-8d34-4fa2-a039-d7d43bfa77d6.jpg

## What's next (in progress)
- The owner wants a **new 50-minute story** with an **even stronger emotional structure**, aiming for **1 million views**.
- Nine pitches are in `NEXT-STORY-PITCHES.md`. The current ranking:
  1. "Just Our Old Gardener"
  2. "The Cleaner Was His Mother"
  3. "The Boy Who Sold Water"
  4. "Grandma at the Bus Stop"
  5. "The Blind Wife's Anniversary"
  6. "The Soldier in the Garden"
  7. "The Twin Who Was Given Away"
  8. "The Waiter at Her Wedding"
  9. "The Girl Who Carried Her Brother"
- **The owner hasn't picked one yet.** The next step is to get their pick, then write the full **50-minute screenplay** (a hook plus about 11 parts) and the **cast sheet** for approval **before generating anything.**

## Read these, in this order
1. `SESSION-MEMORY.md`: this file.
2. `STORY-BLUEPRINT.md`: the proven story formula (six roles, beat sheet with minute marks, 10 rules).
3. `NEXT-STORY-PITCHES.md`: the nine pitches and the ranking.
4. `STUDIO-PLAYBOOK.md`: standing rules, camera and shot language, models and costs, voices, music, QA, build pipeline, YouTube packaging and upload timing.
5. `lessons-learned.md`: every mistake made so far, with its fix and the rule it produced.
6. `voices-and-sound.md` and `tools/score.py`: the voice IDs and the original procedural score.
7. `the-maid-who-stayed-movie-screenplay.md` (screenplay format) and `tools/part9_shots.py` (shot-list format).
8. `youtube-upload-kit.md`: the upload template.

## The rules in one breath (full list in STUDIO-PLAYBOOK §1)
- No licensed music or ambience. Use only the original score from `tools/score.py`.
- Original faces only, and no lookalikes.
- Over-the-shoulder dialogue. Nobody looks into the camera.
- Natural voices. Shouts stay as the raw take.
- Every line word for word from the screenplay.
- Strict continuity, and no jewelry visible from behind.
- People enter through real doors in walls, never through glass onto the sky. No stray or disembodied hands.
- The hook is the real climax scene, reused in the movie.
- No PART cards and no black gaps in the final cut.
- Use frames from the movie as face references.
- No #AIMovie hashtag or tag, but the YouTube synthetic-content setting is still Yes.

## Channel facts
- The audience peaks **6–10 PM GMT+1**, strongest Friday to Sunday. **Schedule uploads for Friday about 3–4 PM GMT+1.**
- 99.5 % of watch time comes from non-subscribers, so the thumbnail and title do most of the work.
- Pinned comments are written as the creator, personal and story-specific. Don't quote a random line with a timestamp.

## Tools and credits
- Use Higgsfield for everything:
  - `nano_banana_pro` for frames and thumbnails.
  - `kling3_0` pro for dialogue.
  - `seedance_2_5` for action (draft, then finalize).
  - `voice_change` with preset voices.
  - `sandbox_exec` for ffmpeg and Whisper builds.
- The sandbox sometimes hits a concurrency limit. If it does, retry once.
- The local container can't reach CloudFront, so do all media work in the sandbox.
- The repo is `finaltoucch/final` and the working branch is `claude/brave-allen-oc95k1`. Commit and push after every meaningful step.
