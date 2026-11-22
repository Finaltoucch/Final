# Two Boys, One Heart: lessons learned (new mistakes and their fixes)

| Where | Mistake | Fix | Rule |
|---|---|---|---|
| Hook H4 | Trey's head too long at the back in side view (owner caught it) | New frame with "normal round head shape" in the prompt | Check every profile and back view of each lead for skull shape |
| Score | Old film's score reused | New engine `tools/score_tboh.py` with new cues and effects | Each film gets its own score |
| Part 1 lines | Spelled-out contractions ("I do not", "grandma is going to") made Kling say them literally, so the lines sounded robotic | Re-rolled with the screenplay's own contractions ("don't", "gonna", "I'm") | Write lines EXACTLY as in the screenplay, contractions included; add "contractions spoken naturally" |
| Silent shots | Kling ad-libs ("We'll be right back", "Thank you", murmurs) | Mute speech in silent shots | Transcribe every silent shot and mute stray speech |
| Rain frames | Wet straight hair turned into braid-like clumps from behind | Image edit: "sleek bone-straight, NOT braids/locs/twists" | Restate the hairstyle on every back view, especially when wet |
| Frames | Generic red car or the wrong driver appeared | Edit with the car sheet and Trey sheet as references | Always attach the car sheet `f295c3d4…` to car shots |
| Images | Safety filter falsely flags harmless prompts ("soaked", busy compositions) | Reword more simply, fewer references | Retry with plainer wording before changing the shot |

## Parts 2–4 lessons
- Voice swaps garble a short word roughly one time in eight ("any of" became "Emiya's", "Can I" became "You may", "Trey" became "Chui", "run" became "mind"). Re-running the same swap usually fails the same way. Fix it by splicing the word's time range from the raw Kling take (`~/splice.sh base raw a b out`), or, if the splice still reads wrong, use the raw take for that one line.
- Kling drops small words now and then ("nights at diner"). Re-roll the clip with "clearly saying every word including ..." in the prompt.
- Silent Kling clips keep inventing ad-libs ("Thank you for watching", "Hahaha", "You"). Mute every establishing or insert clip entirely and let the score carry it.
- The sandbox holds about 8 concurrent jobs across images, video and voice. Batch 6–8 at a time and fill slots as jobs finish.
- Whisper small/medium misreads some correct lines ("owing me" as "O.M.M.E."). Check the full-part dialogue track in context before re-rolling.
