# Starting a new chat (continuing the studio)

## Step 1: open the new chat on this repo
Start a new Claude Code session on **finaltoucch/final**. Either continue on branch `claude/brave-allen-oc95k1` or let the new session make its own branch; everything below is already pushed. Connect the Higgsfield connector as before.

## Step 2: paste this as your first message
(Fill in the story idea at the end.)

```
Continue my AI drama movie studio from the previous chat. Everything is saved in this repo (finaltoucch/final, branch claude/brave-allen-oc95k1).

Before doing anything, read these files in this order:
1. SESSION-MEMORY.md (where we left off, who I am, and what's next)
2. STORY-BLUEPRINT.md (the proven formula: The Maid Who Stayed got 38K views in 2 weeks)
3. NEXT-STORY-PITCHES.md (9 pitches for the next 50-minute story, with your ranking)
4. STUDIO-PLAYBOOK.md (rules, camera angles and shot recipes, models, voices, music, QA, pipeline, YouTube packaging)
5. lessons-learned.md (every past mistake and its rule)
6. voices-and-sound.md and tools/score.py, the-maid-who-stayed-movie-screenplay.md, tools/part9_shots.py and youtube-upload-kit.md

Follow every standing rule in STUDIO-PLAYBOOK.md section 1 without exception, and check your work before showing me anything.

Next step: the new story is 50 minutes long and aims for 1M views. My pick is: <WRITE THE PITCH NAME HERE, or "help me choose">.
Write the full screenplay (a hook plus about 11 parts) and the cast sheet, and show them to me for approval before generating anything.
```

## What carries over automatically
- **Rules and craft:** `STUDIO-PLAYBOOK.md` and `lessons-learned.md`.
- **Pipeline:** `tools/mb.py` (edit list to video), `tools/score.py` (original score and SFX), the QA scripts, and the script checker.
- **Voices:** the preset voice IDs in `voices-and-sound.md`. Reuse them or pick new ones.
- **YouTube template:** `youtube-upload-kit.md`.

## What does NOT carry over
- Characters, faces and locations from The Maid Who Stayed. The new story needs its own cast and original faces.
- The sandbox (it's temporary). Everything is rebuilt from the repo at a commit SHA.
