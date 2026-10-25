# Starting a new story in a new chat

## Step 1: open the new chat on this repo
Start a new Claude Code session on **finaltoucch/final**. Either continue on branch `claude/brave-allen-oc95k1` or let the new session make its own branch; everything below is already pushed. Connect the Higgsfield connector as before.

## Step 2: paste this as your first message
(Fill in the story idea at the end.)

```
We're starting a NEW full-length AI drama movie, using the same studio process as "The Maid Who Stayed".

Before doing anything, read these files in the repo, in this order:
1. STUDIO-PLAYBOOK.md (rules, camera language, models, voices, music, QA, pipeline and YouTube packaging)
2. lessons-learned.md (every mistake made so far and the rule it produced)
3. voices-and-sound.md and tools/score.py (voice IDs and the original score)
4. the-maid-who-stayed-movie-screenplay.md (screenplay format) and tools/part9_shots.py (shot-list format)
5. youtube-upload-kit.md (upload template)

Follow every standing rule in STUDIO-PLAYBOOK.md section 1, without exception:
- no licensed music or ambience
- original faces only
- over-the-shoulder dialogue
- nobody looks into the camera
- natural voices
- every line word for word from the screenplay
- strict continuity, and no jewelry visible from behind
- no lookalikes
- the hook is the real story
- no PART cards or black gaps in the final cut
- entrances through real doors
- check your work before showing me

First deliverable: the screenplay (a hook plus 9 parts, about 36–40 min) and a cast sheet with a unique look for each lead. Show them to me for approval before generating anything.

Story idea: <WRITE YOUR NEW STORY IDEA HERE: who the hero is, the setting, the betrayal, the twist, the ending>
```

## What carries over automatically
- **Rules and craft:** `STUDIO-PLAYBOOK.md` and `lessons-learned.md`.
- **Pipeline:** `tools/mb.py` (edit list to video), `tools/score.py` (original score and SFX), the QA scripts, and the script checker.
- **Voices:** the preset voice IDs in `voices-and-sound.md`. Reuse them or pick new ones.
- **YouTube template:** `youtube-upload-kit.md`.

## What does NOT carry over
- Characters, faces and locations from The Maid Who Stayed. The new story needs its own cast and original faces.
- The sandbox (it's temporary). Everything is rebuilt from the repo at a commit SHA.
