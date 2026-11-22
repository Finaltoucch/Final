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

## Full voice audit (15-minute cut)
Method: transcribe every part's dialogue track with Whisper large-v3 (medium/small miss errors) and compare to the screenplay; then check speaker identity with Resemblyzer embeddings against reference clips of each clone (Zara clearly separable; Malik and Trey sit close together, so a small margin needs the swap's voice_id checked).
Errors found and fixed:
- 1-07 "Question four got me too": the Malik clone always says "about". Fixed by splicing "four got" (2.82–3.14 s) from the raw take.
- 1-13 "You'd just be listening": "you'd just" slurs to "you just". Re-rolled with a beat after "You'd", then swapped cleanly.
- 3-03 "Get in": the Trey clone always says "Janine". Fixed by splicing "Get in," (2.38–2.98 s) from the raw take.
- 3-08 "You noticed that?": Kling kept dropping the -d. A re-roll with a stressed past tense came out right, then swapped.
- 8-02 "handlebars": the raw take said "handle-barbers". Re-rolled and swapped.
- 16-23 "Trey, I,": the clone can't say the name alone. Built from Zara-clone words used elsewhere ("Trey" from 3-10, "I" from 1-10), placed on the lip timing.
Rule: re-running the same voice swap repeats the same garble (it's deterministic); fix it with a raw-word splice or a re-roll.
Visual fixes in the same pass: car scale (Trey too big for the car in X04 and 1-02) and 3-06 (Zara was getting into a back seat that a two-seater doesn't have).
