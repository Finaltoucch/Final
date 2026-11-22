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
