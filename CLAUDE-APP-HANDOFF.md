# Kharune Studios: full memory for a new Claude chat

This one file contains everything from my previous chat about how we make AI drama movies. Read all of it before answering. Then continue from the section "What's next" in SESSION MEMORY below.


==================================================================
# FILE: SESSION-MEMORY.md
==================================================================

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


==================================================================
# FILE: STORY-BLUEPRINT.md
==================================================================

# Story Blueprint: the proven formula

**Proof:** *The Maid Who Stayed* reached **38,000 views in its first 2 weeks** on a channel where 99.5 % of watch time comes from non-subscribers. The structure, the emotional hook and the storyline all worked, so **reuse this skeleton for the next story** with a new setting, new characters and a new twist.

Source: `the-maid-who-stayed-movie-screenplay.md`, plus the final cut timings in `production-checklist.md`.

---

## 1. The core promise (one sentence)
> **Everyone abandoned the powerful one at their lowest. Only the humble one, whom everyone looked down on, stayed, and in the end she was the one who was rewarded.**

Every new story needs its own version of this sentence before anything else is written. The title and thumbnail are this sentence: *"Everyone Left the Paralyzed CEO… Only the Maid Stayed."*

## 2. The cast archetypes (keep all six roles)
| Role | In The Maid Who Stayed | Why it works |
|---|---|---|
| **Humble hero** | Grace, the new maid. She studies at night, supports her mother and her little brother with asthma, and has faith (gold cross). | Instantly relatable. Viewers root for her from the first scene. |
| **Kind powerful lead** | Ethan, the young CEO. He is kind to the staff and falls hard. | Gives the hero someone worth staying for, and turns his fall from power into the story. |
| **Glamorous cruel rival** | Vanessa, the fiancée, always in red. She bullies the maid and leaves when he's weak. | A villain the viewers love to hate. Her humiliation pays off at the end. |
| **Hidden villain inside the family** | Bradley, the charming brother with gambling debts, who is the poisoner. | Gives the story a twist and a reason to rewatch. |
| **Wise ally** | Mrs. Hayes, strict at first, then loyal. Also Harold, the honest lawyer. | Moves from enemy to friend, and supplies help and evidence. |
| **Heart at home** | Mama Ruth ("be careful with your heart") and Sam, who needs the $340 inhaler. | Raises the stakes: the hero can't afford to lose this job. |

## 3. The beat sheet (minute marks from the final 36-minute cut)
| Time | Beat | Emotion it delivers |
|---|---|---|
| 0:00 | **Hook:** the biggest real moment. The toast, the collapse in slow motion, the hero calling the ambulance, the ER rush. Then the title card and "A FEW WEEKS EARLIER". | Shock. "What happened? I have to know." |
| 0:34 | **Arrival:** the hero prays at the gate, gets humiliated by the rival, gets a warm welcome from the lead, and learns the house rules. | Sympathy for the underdog. |
| ~3:00 | **Small kindnesses:** she notices what nobody else does (he burns his tongue on his coffee every morning) and he notices her ("It's refreshing"). | The spark between them. |
| ~4:00 | **Rival bullying:** "Clean it again. Harder." Her answer: "I need this job more than I need my pride." | Anger at the rival, respect for the hero. |
| ~5:15 | **The hero's wound and dream:** her dad's stroke, and studying physical therapy. *This sets up the payoff, because she already has the skill he will need.* | Hope, and quiet foreshadowing. |
| ~6:30 | **The threat:** the rival overhears her family's money trouble and threatens her ("One word to Ethan…"). | Dread. |
| 6:54 | **The big event:** the toast, the hidden villain's "don't forget your meds", the collapse, the rival saying "Don't call 911, there's press here", and **the hero calls anyway** and saves his life. | Terror, then pride: "The maid just saved his life." |
| ~9:00 | **The diagnosis:** "Will I walk again?" | Grief. |
| 10:53 | **Everyone leaves:** the fiancée ("I didn't sign up to push a wheelchair"), the storage room, the board hands control to the brother, her pay is cut in half. **The hero stays.** | Injustice. This is the title moment. |
| ~13:00 | **The "You fight!" speech.** | The emotional peak of the first half. People clip and share this one. |
| 15:59 | **Falling:** her mother warns her, she discovers the pills are poison, the confession "I think I'm falling in love with you", and she overhears the villains' plan. | Love and danger at the same time. |
| 20:35 | **Framed:** a planted bracelet, the police, she's fired and walks out in the rain, and her brother's asthma emergency. | Rock bottom. Viewers are furious. |
| 25:38 | **The rescue:** she comes back, uses the recording and the lawyer, and the lead fights to stand up ("I'm not going anywhere"). | Comeback energy. |
| 29:14 | **"I heard you":** rehab, the first steps, intimacy. | Tenderness. |
| 30:50 | **The boardroom:** the lead **walks** in, plays the recording, the villains are arrested, and the room votes him back. | Justice. The biggest payoff. |
| 33:27 | **Six weeks later:** she passes her licence, the porch proposal with his late mother's ring, the wedding. | Happy tears. |
| 36:09 | **Closing quote cards:** "Some people love the life you have. The right one loves you when you have nothing. Who stayed for you?" | A reflective question that drives comments. |

## 4. The rules that made it land
1. **Open with the real climax, not a trailer.** It only works when it's a true scene the viewer will see again in context.
2. **Plant every payoff early.** Her physical-therapy study (5 min) pays off as his rehab, and the "meds" line (7 min) pays off as the poison reveal.
3. **Keep the hero's money stakes concrete** (a $340 inhaler, half pay). Specific numbers make the struggle feel real.
4. **The rival's cruelty must be public and petty** (a clean table, "people like you"), so her downfall feels earned.
5. **Give the hero one speech** that is quotable on its own ("You're allowed to be angry… You fight!").
6. **Hit rock bottom about 55–60 % of the way in** (framed and fired in the rain), then climb.
7. **The villain falls in public** (the boardroom, the recording, the arrest), never offscreen.
8. **The romance is earned slowly:** coffee, then respect, then caring for him, then confession, then the proposal. No early kiss.
9. **Keep scenes short** (10–40 s each), with time cards between jumps and no narrator.
10. **End on a question to the viewer**, which drives comments (and the pinned comment repeats it).

## 5. How to make the next story fresh while keeping the formula
Swap the **world** and the **twist**, and keep the **six roles and the beat sheet**. Some combinations:
- A nurse or caregiver, a famous musician after an accident, his manager or girlfriend, and a hidden villain who is his business partner.
- A school janitor, a wealthy widow or widower, their greedy children, and a hidden villain who is the family doctor.
- A driver or chauffeur, a CEO heiress who goes blind or is framed for fraud, her fiancé, and a hidden villain who is her stepmother.
- A village girl on a Lagos estate, a young chief, a socialite fiancée, and a hidden villain who is a cousin.

For each one, write the one-sentence promise, the title (contrast plus payoff) and the hook moment **first**.


==================================================================
# FILE: NEXT-STORY-PITCHES.md
==================================================================

# Next story: three 50-minute pitches

Goal: a stronger emotional structure than *The Maid Who Stayed* (38K views in 2 weeks), aiming for 1M.

**What makes these stronger than last time:**
1. **Dramatic irony.** The viewer learns the secret in the first 2 minutes and the characters don't. Every scene after that hurts, because the viewer knows who is being mistreated.
2. **Blood ties.** A mother or a child beats a romance for tears and shares.
3. **A sacrifice the hero hides.** She gives up something real and never asks for credit.
4. **A mirror ending.** The humiliation in the hook is reversed in the same place, in front of the same people.

All three keep the six roles and the beat logic from `STORY-BLUEPRINT.md`.

---

## ⭐ Pitch 1 (recommended): **"The Cleaner Was His Mother"**
**Title:** *He Threw the Old Cleaner Out in the Rain… He Didn't Know She Was His Mother | Full Movie*

**Promise:** A mother gave up her baby to save his life. Thirty-four years later she cleans his skyscraper just to see him every day, and he's the one who throws her out.

**The six roles:**
| Role | Character |
|---|---|
| Humble hero | **Mama Esther** (58), night cleaner. She has a tin box with a baby hospital bracelet in it, a savings jar labelled "for Danny", and her faith. |
| Powerful lead (his arc is from cold to broken to redeemed) | **Daniel Cole** (34), a self-made CEO raised by a wealthy adoptive family. He is proud and rude to the staff, but a loving father. |
| Glamorous cruel rival | **Victoria**, his wife. She is elegant and cruel, and humiliates Esther ("People like you should be invisible"). |
| Hidden villain | **Victoria and Grant**, the CFO, are having an affair and stealing the company. The adoptive mother **Margaret** buried the truth about Daniel's birth. |
| Wise ally | **Mr. Okafor**, the old night guard, who knows Esther's secret. |
| The child (heart) | **Lily** (7), Daniel's daughter. She bonds with "Grandma Cleaner". Later she falls ill, and only a blood relative can be her donor. |

**Beat sheet (about 50 min, a hook plus 11 parts):**
| Time | Beat |
|---|---|
| 0:00 | **Hook (real scene):** In a glass lobby in front of all the staff, Daniel shouts, "Get this woman out of my building!" Security drags Esther into the rain. A tiny baby hospital bracelet falls from her coat into a puddle, and nobody sees it. Title card, then "34 YEARS EARLIER". |
| 0:45 | **Prologue (2 min):** Young Esther holds a baby who needs heart surgery she can't pay for. A rich woman, Margaret, offers to pay on one condition: "You disappear. Forever." Esther signs the paper, kisses the baby and ties the bracelet to her own wrist. "PRESENT DAY". |
| 3:00 | Esther takes the night-cleaner job at Cole Tower just to be near him. She polishes his office and touches his childhood photo. |
| 6:00 | Daniel is cold to her ("Don't touch my things"), but she sees how gentle he is with Lily. Esther knows his habits ("You still don't eat when you're stressed"), and it unsettles him. |
| 9:00 | Lily gets lost in the tower at night and Esther finds her. They form a bond: songs, braids, and the lullaby Esther sang to baby Danny. Lily hums it at home, and Daniel freezes, because he knows that song from somewhere. |
| 13:00 | Victoria humiliates Esther: she pours coffee on the floor and says "Clean it, on your knees." Esther obeys. |
| 16:00 | Because cleaners are invisible, Esther overhears Victoria and Grant planning to drain the company and frame Daniel. She records them on her old phone. |
| 20:00 | **Framed:** Victoria plants a missing diamond in Esther's cleaning cart. This leads to the hook scene in the lobby, rain and all. **Rock bottom.** |
| 24:00 | Okafor finds the bracelet in the puddle and reads the name and date on it. |
| 27:00 | **The child in danger:** Lily collapses with leukaemia. No match in the family. Daniel breaks down in the hospital chapel. |
| 31:00 | Esther hears about it, gets tested secretly and **matches**. She donates anonymously, through the hospital, and asks for no credit. |
| 36:00 | Lily recovers. The doctor says, "Only a blood relative could have matched this closely. A grandmother, most likely." Daniel confronts Margaret, who confesses and shows him the signed paper. |
| 40:00 | **Daniel searches for Esther** and finds her tiny room: the savings jar "for Danny" and 34 years of birthday cards she never sent. **This is the emotional peak.** |
| 44:00 | **The boardroom:** Esther arrives with the recording just as Grant moves to seize the company. Victoria and Grant are exposed and arrested. |
| 47:00 | **The mirror ending:** in the same lobby, in front of the same staff, Daniel kneels in front of Esther, ties the bracelet back on her wrist and says, "Mama." Lily runs into her arms. |
| 49:00 | Closing cards: *"A mother's love doesn't leave. It waits." / "Call your mother today."* Then THE END. |

**Why it should travel further:** the viewer knows from minute 1 who is being thrown into the rain, so every insult lands twice. Mother-and-child stories get shared to family WhatsApp groups and Facebook, not just watched. The closing line ("Call your mother today") also drives comments.

---

## Pitch 2: **"The Waiter at Her Wedding"**
**Title:** *They Mocked the Old Waiter at the Billionaire's Wedding… Then the Bride Saw His Face*

A father went to prison for a crime his rich business partner committed, and lost his baby daughter to that partner's family. Twenty-five years later she is marrying into wealth, and he works as a waiter at her wedding just to see her once. The groom's family humiliates him. He uncovers the groom's fraud during the reception and sacrifices his last chance to stay hidden to save her. The reveal is the father-daughter dance.

## Pitch 3: **"The Girl Who Carried Her Brother"**
**Title:** *Orphan Girl Raised Her Baby Brother Alone… 20 Years Later He Became a Surgeon*

A 12-year-old girl raises her baby brother on the streets, selling water and skipping meals so he can go to school. He becomes a rich surgeon, marries a snobbish woman, and is ashamed of his "uneducated" sister. Then she is wheeled into his emergency room. The story is built on sacrifice, ingratitude and redemption, with an apology on his knees in the market where she once sold water.

---

**Next step:** pick one. Pitch 1 is recommended. Then comes the full screenplay (a hook plus 11 parts, about 50 min) and the cast sheet, before anything is generated.

---

# Round 2: six more pitches with very strong emotional hooks

Each pitch gives you:
- **The first 60 seconds**, which decide whether a viewer stays.
- **The secret**, which the viewer knows and the characters don't.
- **The gut punch**, the midpoint scene that makes people cry or comment.
- **The mirror ending**, where the hook's humiliation is reversed in the same place.

## ⭐ Pitch 4: "Just Our Old Gardener"
**Title:** *She Called Her Father "Just the Gardener" at Her Engagement Dinner… He Smiled and Kept Serving*
- **First 60 s:** At a glittering engagement dinner, her rich future in-laws ask about the old man pouring the wine. The bride, now a successful lawyer, says, "Oh, he's just our old gardener." He smiles, bows and keeps serving. In the kitchen he takes off his apron, and there is a long surgical scar across his side. Title card, then "15 YEARS EARLIER".
- **The secret:** He sold a kidney to pay for her law school, and told her the money was a scholarship.
- **The gut punch:** His last kidney fails, and she is the only match. In the hospital she sees the scar, and the doctor says, "He's had a kidney removed before… years ago." She opens his old tin box and finds the clinic receipt dated the week her "scholarship" arrived.
- **Mirror ending:** At her wedding, in front of the same in-laws, she walks him to the head table: "This is not our gardener. This is my father, and everything I am is his."
- **Why it hits:** shame and sacrifice between a parent and child, which is the most-shared emotion there is. Everybody has felt ashamed of a parent once.

## Pitch 5: "Grandma at the Bus Stop"
**Title:** *Her Son Left Her at a Bus Stop in the Rain… He Didn't Know She Owned the Company*
- **First 60 s:** A luxury car stops at a rainy bus stop. The son's wife says, "Wait here, Mama, the car to the home is coming." They drive away. The old woman, holding one small suitcase, keeps waving until the car is gone. Nobody comes.
- **The secret:** She quietly holds 51 % of the company her son "built". She was testing whether anyone would stay.
- **The gut punch:** A homeless teenage girl shares her only bread with her and walks her to a shelter. The grandmother teaches her to read the newspaper's business page.
- **Mirror ending:** At the shareholders' meeting, the son walks in to be named chairman, and the grandmother is in the chair, with the girl beside her: "The company goes to the one who stayed with me in the rain."

## Pitch 6: "The Boy Who Sold Water"
**Title:** *Boy Sold Water in Traffic for His Mother's Surgery… The Billionaire in the Car Was His Father*
- **First 60 s:** A 10-year-old runs between cars in the heat selling water, with a hospital bill folded in his pocket. A black SUV splashes him with mud, and the driver laughs. In the back seat, a CEO sees the boy's face and **freezes**: the boy has his eyes.
- **The secret:** Ten years ago the CEO's mother paid the boy's mother to disappear while she was pregnant, and told her son that she had left him.
- **The gut punch:** The boy counts his coins in the hospital corridor, still short, and whispers to his sleeping mother, "I'll sell more tomorrow, Mama. Don't go."
- **Mirror ending:** In the same traffic jam, the CEO steps out of the SUV, kneels in the road and buys every bottle, then the surgery, then signs the adoption papers. He tells his mother, "You took ten years from me."

## Pitch 7: "The Blind Wife's Anniversary"
**Title:** *He Announced the Divorce at Their Anniversary… His Blind Wife Didn't See Who Was Standing Next to Him*
- **First 60 s:** At their anniversary party, the husband taps his glass and announces the divorce. His new woman stands beside him: **her best friend**. The blind wife smiles politely at the wrong side of the room. Only her driver steps forward to hold her hand.
- **The secret:** The driver has been reading to her every night for two years, and he sold his late mother's house to pay for her eye surgery, anonymously.
- **The gut punch:** When the bandages come off, the first face she sees is his, and she doesn't know who he is until he speaks. "You're the voice."
- **Mirror ending:** At a gala, the ex-husband, now broke because she inherited the company he was hiding, sees her arrive on the driver's arm, and she recognises the best friend's face at last.

## Pitch 8: "The Soldier in the Garden"
**Title:** *Everyone Thought He Died in the War… He Came Back as the Gardener to Watch His Son Grow Up*
- **First 60 s:** A scarred man in a worn coat stands at the gate of a mansion holding a photo of a baby. Through the window he sees his wife, remarried to a rich man, and a 7-year-old boy who has his eyes. He takes the gardener job that's on offer.
- **The secret:** His face was burned, so nobody recognises him, and he chooses never to tell anyone, to protect their new life.
- **The gut punch:** The boy, bullied at school for "having no real dad", builds a treehouse with the gardener. "I wish you were my dad." The man has to turn away.
- **Mirror ending:** The rich stepfather's fraud is exposed. The wife hears the gardener humming their wedding song and drops her cup. He finally says the boy's name the way only his father would.
- **Production note:** no war scenes are needed. Use one old photo and the scars only.

## Pitch 9: "The Twin Who Was Given Away"
**Title:** *The Poor Girl Worked as a Maid in Her Own Twin Sister's Mansion… Neither of Them Knew*
- **First 60 s:** A hospital nursery, 25 years ago: a nurse hands one of two newborn twins to a crying poor woman whose baby died. Present day: a maid kneels to clean the shoes of a rich bride who looks exactly like her.
- **The secret:** They are twins, separated at birth.
- **The gut punch:** The rich twin needs a bone-marrow donor, and the maid matches perfectly.
- **Mirror ending:** Their real mother sees them side by side for the first time.
- **⚠ Production note:** this breaks our **no lookalikes** rule on purpose, and it's hard for AI to keep two identical faces consistent. Only choose this one if you accept the extra checking work.

---

## My ranking for the 1M target
1. **"Just Our Old Gardener"** (Pitch 4). It has the strongest shame-to-sacrifice punch, a small cast and simple locations.
2. **"The Cleaner Was His Mother"** (Pitch 1).
3. **"The Boy Who Sold Water"** (Pitch 6).
4. **"Grandma at the Bus Stop"** (Pitch 5).
5. **"The Blind Wife's Anniversary"** (Pitch 7).
6. **"The Soldier in the Garden"** (Pitch 8).
7. **"The Twin Who Was Given Away"** (Pitch 9), because of the production risk.


==================================================================
# FILE: STUDIO-PLAYBOOK.md
==================================================================

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


==================================================================
# FILE: lessons-learned.md
==================================================================

# The Maid Who Stayed — Lessons Learned (Parts 1–6)

Every mistake made so far, why it happened, and the rule that prevents it.
**Read this before starting any new part.** Detailed working notes stay in `production-checklist.md`.

---

## 1. The user's standing rules (never break these)

| Rule | Source |
|---|---|
| **No licensed sound or music of any kind.** Score is our own procedural score (`tools/score.py`). | User: "noo i dont want any licenced sound" |
| **No ambience beds.** Dialogue + low score only. Never raise the score unless asked. | User rejected ambience |
| **Every character is an ORIGINAL face** — never resembling a real actor or celebrity. | User: "this is a real actors face" (Harold looked like Samuel L. Jackson) |
| **Two-person dialogue is over-the-shoulder:** speaker sharp and facing camera, listener's back of head/shoulder soft in the foreground. | User: "the person being talked to is slightly showed in the frame, maybe slightly blurred or back view" |
| **Natural human voices, not storyteller/narrator presets** for main characters. | User: "not a random story telling voice" (Harold) |
| **Strict realism and continuity.** Check every image before animating. | Standing instruction |
| **Bradley is the BLOND man** from Parts 2–3, never the dark-haired one. | User flagged twice in Part 5 |
| **Every spoken line must match the screenplay.** | User: "There are a lot of speech errors here" (Part 6) |

---

## 2. Mistake log (what went wrong → fix → rule)

### Faces and identity
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 4, 6 — Harold | Harold's face resembled **Samuel L. Jackson** (prompt "distinguished older Black man, white beard, round glasses, three-piece suit" drifted to a famous actor) | New original Harold v2 (heavy-set, grey mustache, tortoiseshell glasses, navy pinstripe, burgundy bow tie); all 17 shots re-made | Describe specific, ordinary features; add "must not resemble any real actor or celebrity"; inspect every new face for celebrity resemblance |
| Library — Detective | Reference sheet labelled "Detective Sarah Linden" (a TV character) and resembled that actress | Replaced with original detective v2 before use | Check text on reference sheets for real/TV names |
| 1, 5 — Bradley | Old dark-haired Bradley ref looked like Ethan; viewers confused them (Part 5 shots 21, 55, 56) | Locked to blond Bradley refs (`e59ccf4f…`, `9bf308d3…`) | Never use library image `8f021d31…`. **Part 1 S11b and S46 still show the old Bradley (pending fix)** |
| 3 — shots 32, 46 | A dark-skinned man appeared where Ethan should be | Re-made | Check identity of EVERY person, including partly visible ones |
| 5 — shot 20 | Blurred wheelchair listener drawn as a Black man instead of Ethan | Re-made | Blurred listeners get the same identity check as speakers |
| 5 — shots 17, 19 | Blurred Vanessa had a short bob instead of long hair | Re-made | Check hair length/colour of listeners |
| 6 — shot 19 | Blurred Vanessa's hair went orange; first retry went silver (looked old) | "light buttery blonde, NOT white/grey/silver/orange" + her own close-up as reference | Name the exact shade and the shades to avoid |
| 5 — shots 40, 42 | Hospital clerk from behind looked like Mrs Hayes | Clerk changed to a young man in navy scrubs | Minor characters must not resemble main characters from behind |
| 6 — shots 21, 24 | A lone man in a blue shirt filled the foreground — viewer asked "who is this?" (he was a transport attendant only seen tiny in a wide shot) | Both attendants shown together, uniforms with patches, stretcher between them | A minor character never appears alone in an OTS foreground without identifying details |
| 3 — shot 1 | Two orderlies were identical twins | Re-made | Describe each extra differently (age, build, ethnicity, hair) |
| 2 | Grace came out with blue eyes once | Re-made | Check eye colour against reference |

### Bodies, props and continuity
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 4 — shots 22, 24, 28 | "Broom-handle bars" were drawn as whole brooms | "plain smooth round wooden rails" | Describe a prop's shape, never the household object it's made from |
| 4 — shot 42 | Ethan had one arm / empty sleeve | Re-made with both arms | In hand close-ups check the other arm |
| 3, 5 — several | Empty bed / empty wheelchair where a character should be (Part 3 shots 47, 48, 50; Part 5 ER shots 43, 45, 48) | Reframed | If someone is in a bed/chair, no other shot of that room may show it empty; no spare wheelchairs |
| 5 — shot 44 | Grace's braids hung loose instead of tied under the wrap | Re-made | Check hairstyle per scene |
| 3 | Bradley's shirt changed colour within a scene | Feed previous shot's frame as reference | Wardrobe identical inside a scene |
| 6 — shot 41 | Coffee cup in hand AFTER it had shattered in shot 29 | Removed | Track props across the scene |
| 6 — shot 1 | Harold held a book instead of the laptop he brings | Regenerated with the silver laptop | Track props across the scene |
| 6 — shot 32 | Court papers vanished from Harold's hand mid-shot | Re-rolled with "holds the papers the ENTIRE time" | Check middle frames, not just start/end |
| 6 — shot 29 | Feet with the wrong skin tone in a close-up | Regenerated with no people | Avoid ambiguous body parts |
| 6 — shot 32 | Officer's neck too dark | Regenerated | Check skin tones on partial views |
| 6 — shot 3 | Apple logo on the laptop | Unbranded laptop | No brand logos (user's Titans jersey is the only exception, per screenplay) |
| 6 — shot 12 | Fog prompt sprouted smoke puffs | "fog hangs still, no smoke, no steam, nothing appears" | Spell out what must NOT appear |

### Speech and voices
| Part / shot | Mistake | Fix | Rule |
|---|---|---|---|
| 6 — shot 28 | "My name is Ethan **is** Caldwell" — caused by dramatic pauses "My name... is Ethan..." in the prompt | Line written plainly | **Never put "..." pauses inside a dialogue line** |
| 6 — shot 32 | "facility of **Hess** choosing" — caused by CAPS "HIS" | Plain wording | **Never use CAPS emphasis inside a line** |
| 6 — shot 33 | "An officer… hear recording" (lost "And," and "a") | "hear this recording" | Avoid tiny unstressed words where a firmer word works |
| 6 — shot 10 | "stopped" instead of "stop" | Re-roll + "in the present tense" | Transcribe every clip and every voice-changed take |
| 6 — shot 9 | "I filed" instead of "I've filed" | "I have filed" | Spell out contractions that tend to get dropped |
| 6 — shots 6, 20 | Voice change dropped the first word ("And", "Ignore") | Word splice: first word raw, rest locked voice | Compare the FIRST word of every voice-changed take |
| 6 — shot 28 | Voice change turned "going" into "doing" twice | Kept Kling's raw take (shout) | Shouts keep the raw take |
| 6 — shots 10, 22 | Kling ad-libbed "Huh?" / "Hey…" before the line | `ss` start-trim | Trim stray words rather than re-roll |
| 4 — Harold | Voice sounded like a generic narrator preset (Barrett → Sterling still wrong) | Cloned a natural voice from Harold's own raw Kling audio ("Harold natural", element `277d8e8e…`) | Main characters get natural voices; clone from raw takes |
| 4 — shot 24 | Voice change garbled a line said through gritted teeth | Re-shot with clearer diction | Transcribe voice-changed takes |
| 5 — shots 17, 42 | Voice change garbled | Raw audio | If two voice-change tries fail, use raw |
| Any | Kling ad-libs words when the line is shorter than the clip | Describe silent action to fill the time | Match clip length to the line |

### Story and editing
| Mistake | Rule |
|---|---|
| Cut straight from normal moment to crisis (Parts 1–2) | Build up with warning signs; use time cards |
| Key action shown only by an object | Show the action itself (the body falls) |
| Emergencies felt slow | "RUNNING at full speed", patient visible on the gurney |

### Pipeline
| Problem | Rule |
|---|---|
| Sandbox resets ~10 s after a call | Start `(sleep 1700 &)` first; re-curl helpers; run builds in background and poll |
| sandbox_exec hard limit ~60 s | Long jobs (whisper medium, builds) in `nohup … &`, poll in later calls |
| Voice change 429 rate limits | ≤6 jobs at a time, after Kling queue drains |
| Big uploads time out | PUT in background; 412 on retry = already uploaded |
| Files into the sandbox | Commit + push, curl from raw.githubusercontent.com at the commit SHA |

---

## 3. Pre-flight checklist for every new part

**Writing prompts**
1. Every person described unambiguously (race, age, hair colour/length/style, wardrobe); use the character-lock references (Bradley blond, Harold v2, Detective v2).
2. Over-the-shoulder for all two-person dialogue; listener identifiable (main character or clearly marked minor character with props).
3. Dialogue lines written plainly: no "...", no CAPS, contractions spelled out when risky; delivery described outside the quotes.
4. Physical state stated (Ethan standing/wheelchair/bed as per the story point); props tracked shot-to-shot.
5. Negative instructions for known failures (no smoke, no duplicates, no logos, no empty wheelchair, "must not resemble any real actor").

**Checking frames (before animating)**
6. Every face, including blurred/back views: identity, skin tone, hair, eye colour, wardrobe, props, no celebrity likeness.

**Checking clips**
7. Frames at 12 / 50 / 92 % of every clip (props mid-shot, extra people, morphing).
8. Transcribe raw take AND voice-changed take with whisper; compare word-for-word with the screenplay, especially the first word.

**Checking the final cut**
9. Contact sheet at 1 frame / 2 s; check short clips (<2 s) by timeline position.
10. Full transcript of the final mix with whisper `medium.en`; any mismatch re-checked on the isolated shot.
11. Only then deliver the link.

---

## 4. Locked references

| Character | Reference | Voice |
|---|---|---|
| Grace | library GRACE_* | Naomi `caeba733…` |
| Ethan | library ETHAN_* | Benji `e6f9b893…` (raw for shouts) |
| Vanessa | library VANESSA_* (light buttery blonde) | Celine `57ccb351…` |
| Bradley (blond) | `e59ccf4f…`, `9bf308d3…` | Reid `66469f5a…` |
| Mrs Hayes | `a06cf4f3…` | Helena `3c2b83c0…` |
| Harold v2 | `7d7b513f-a9ea-4ddc-8cf8-4c7ae77cc5bf` | "Harold natural" clone `277d8e8e…` (element) |
| Detective v2 | `9d7a04cc-bbfd-49a6-ad6e-59077f966591` | raw Kling |
| Denise, Reyes, clerk, attendants, Sam | library | raw Kling |

**Retired — never use:** Harold v1 `9d1044f9…`, Detective v1 `9d45d4c2…`, old Bradley `8f021d31…`.

---

## 5. Added during Part 7
| Mistake | Fix | Rule |
|---|---|---|
| Story beat contradicted: they kissed when the screenplay says she stops a breath away | Start frame with a visible gap + "their lips never touch" | Check every action against the screenplay's stage directions, not just dialogue |
| Start frame too close → Kling closes the gap | Regenerate the start frame | Kling continues motion from the start frame; set up the frame so the wrong outcome is unlikely |
| A character's face drifted (older, receding hair) when only the library sheet was used | Use the most recent approved close-up as the face reference | Always feed the latest approved close-up of each main character |
| Reverse-angle OTS put the speaker alone mid-bench | Generate the reverse from the matching OTS frame ("reverse angle of reference") | Keep seating geometry consistent across OTS pairs |
| Voice change dropped "'d" in "I'd better" | Raw take | Contractions like 'd and 've are fragile; check them in the voice-changed take |
| Sandbox reset killed a build while I was busy elsewhere | Restart and poll continuously | Never leave a running build unpolled for more than ~10 s |

## 6. Added during Part 8 (group scenes)
| Mistake | Fix | Rule |
|---|---|---|
| Room empty / people missing / people in the wrong seats between shots of the same scene | Keep a seating chart; generate every group frame from the latest approved group frame | In group scenes, write the seating chart into the prompt and check every person in every frame |
| A character changes position (Bradley at the head after giving up the chair) | Explicitly state the new position in every later prompt | When the blocking changes, update every later frame's prompt and references |
| Villains raising their hands in a vote against themselves | Name who does NOT act | For group actions, list who acts AND who does not |
| A prop (cane) vanished three takes in a row because the start frame had a hand in a pocket | New start frame with the prop clearly gripped; cut away before it vanishes | Start frames must show props clearly held; if Kling still drops it, cut to a reaction shot and carry the dialogue as voice-over |
| A character standing at the door also appeared seated in the background | Remove duplicates in the background | Check backgrounds for duplicates of main characters |
| Kling adds speech to non-dialogue shots ("Thank you" over applause) | Mute that clip | Transcribe silent/ambient clips too |

## 7. Added during Part 9 (the proposal & wedding)
| Mistake | Fix | Rule |
|---|---|---|
| Kling dropped a key line from a long read ("Marry her." vanished; heard as "Love her, Mom") | Cut the shot after the last correct word and generate a short continuation from that exact frame saying only the missing words | For 12 s monologues, check the LAST sentence especially; patch with a continuation from the cut frame instead of re-rolling the whole take |
| Kling inserted a hard camera cut (wide → close-up) inside a 3 s shot, and the prop vanished | `maxdur` before the cut (found with ffmpeg scene detection) | Run scene-change detection on every clip, not just eyeball 3 frames |
| Voice change turned "Ethan." into "equal" | Raw take | One-word lines are the most fragile in voice change; always transcribe them |
| Kling ad-libbed "You know," before a line | `ss` trim to just before the first scripted word | Whisper medium hears ad-libs that base misses; use medium for the check, base for timestamps |
| Licensed songs in the screenplay (Johnny Cash, "I Walk the Line") | Replaced with the original procedural score | Never use a song named in the screenplay; the score carries the moment |
| Voice change rate-limited (429) while Kling was still rendering | Submit voice changes only after the Kling batch drains, 3 at a time | Queue voice changes behind Kling, don't spam retries |

## 8. Added during the Parts 1–2 over-the-shoulder remake
| Mistake | Fix | Rule |
|---|---|---|
| Parts 1 and 2 shot conversations as separate singles, never as speaker-sharp / listener-blurred OTS | Every conversation line re-shot from a two-person OTS frame (`part1r_shots.py`, `part2r_shots.py`), cut one clip per line | Every two-person exchange is OTS, both directions, from the first part on |
| The model kept painting Grace's cross pendant on her BACK in OTS foregrounds (D1, I1, J1, L1) | Image edit: "remove the necklace from her back" | Add "no jewelry visible from behind" to every OTS prompt, and check the blurred shoulder in every frame |
| Voice change swapped small words: "Then" → "And", "dirty" → "Dodie", "a clean table" → "the clean table", "nim" for "ma'am" | Raw take for those lines | Compare the voice-changed transcript word by word, articles included |
| Voice change caps jobs in flight (429 after ~9) | Submit in batches of 9, collect, then submit the next | Batch of 9, never more |
| Kling turned a panic shout into an excited grin (Part 2 "my legs") | Re-rolled with "terrified, never smiling, frightened to the very last frame" | Check the LAST second of every emotional shot, not just the middle |
| Kling added a spoken line ("I'll take over.") to a silent beat | `ss` past it | Transcribe silent shots too |
| A kept old cutaway (uniform sleeve, daylight) no longer matched the remade scene (evening, sundress) | Two new shots from the remade frames | When a scene is remade, re-check every old shot left inside it for wardrobe and light |
| Raw Kling lines run 1–2 s of dead air before the first word | `mkremake.py` trims each line to speech −0.3 s / +0.55 s and loudness-matches it to −25 LUFS | Measure (`meas.py`) and trim every dialogue clip; never cut on the clip's full length |

## 9. Added after the viewer notes on the OTS remake
| Mistake | Fix | Rule |
|---|---|---|
| Remade lines were copied from the old shot list, which had shortened the screenplay ("can wait" for "should be able to wait", missing "Don't be sorry.", "He works too hard.", the guard's "Is it that obvious?" exchange) | 18 lines re-shot word for word | Diff every line against the SCREENPLAY (`tools/script_check.py`, `tools/script_check_all.py`), never against an older shot list |
| Pantry: Grace stood face-to-face with Bradley during his secret phone call | New first shot from behind Grace in the hallway, Bradley's back to her; he turns and sees her only after the call | Overheard moments are shot from the eavesdropper's hiding place, from behind them |
| A peeking face pasted onto the door frame read as "inside the door" | Show the eavesdropper's back and shoulder at the door edge, clearly outside | Hiding = back of the head at the frame edge, never a face flattened against the wood |
| Coffee carafe refilled itself after pouring; mug changed between shots | New burn shot starting with the carafe already set down; ice cube into the same tall white mug | Start a shot after the risky action, and reference the exact prop from the neighbouring frame |
| Vanessa knew about the inhaler with no way of hearing it (plot hole in the screenplay itself) | New mansion-hallway shot: Grace on the phone about the inhaler, Vanessa listening in a doorway; screenplay scene 15b added | Every threat or reveal must be set up on screen where the character could learn it |
| Part 4 lawyer delivered his lines straight into the lens | OTS: Harold talks to Grace (blurred from behind), plus her silent nod | No character addresses the camera; every line has a listener in frame |
| Regenerating Harold from text drifted into a celebrity-like face | Edit from a still of the approved Harold (uploaded frame) instead of describing him | Recurring minor characters: always edit from an approved still, never re-describe |
| Kling ad-libbed before scripted lines ("Train is manned", "Hey, it's me") | `ss` trim to the first scripted word | Read word timestamps of every take, not just the transcript text |
| Voice change dropped "Ah!" from "Ah! Every single morning." | Raw take | Exclamations are dropped as often as short words |

## 10. Added during the Parts 3–4 over-the-shoulder pass

| Problem | Fix | Rule |
|---|---|---|
| The listener was wrong for a line said to a third person (Ethan answering Vanessa with Grace's back in frame) | Re-edit with the person actually being addressed in the foreground | Map the listener from the screenplay line being answered, not from who stands nearest |
| A back-of-head edit showed Mrs. Hayes's pearl necklace | Edit the frame again to remove it | Check every foreground back for jewelry before animating |
| Mama's back views had gray hair and a cardigan she does not wear in her own close-ups | Edit the backs (and one close-up) to match her front shot | Use the speaker's own approved frame as the reference for their back |
| The small whisper model "heard" a "What?" over silent score | Re-check the section with medium before cutting anything | Confirm any unexpected word with the medium model on that exact time range |
| Vanessa (3057) looked almost into the lens with a toothy grin | New frame: head turned three-quarters to the listener, closed-mouth thin smile; prompt "subtle, restrained, never looks toward the camera" | Check the speaker's eyeline in the start frame; a near-frontal face drifts into the lens when animated |
| Kling ran "nice, sir" together ("nicer") | Re-roll with "nice... sir" and a stated pause | Short words after commas need an explicit pause in the prompt |
| Voice change turned "He needs help" into "She needs help" | Second voice-change pass was correct | Re-run a garbled voice change once before falling back to the raw take |
| Kling filled a crowd shot with guests who had Ethan's and Bradley's faces | Re-shot in Seedance 2.5 with "he is the only man with dark hair and a beard; every guest looks clearly different" | Zoom into every crowd frame for lead lookalikes before animating; generic "guests" inherit the lead's face |
| Seedance draft finalize costs the full price | Draft at 480p to judge, then finalize once | Budget a draft plus a full-price final |


==================================================================
# FILE: voices-and-sound.md
==================================================================

# Voices & Sound Plan — The Maid Who Stayed

## Locked character voices (Higgsfield preset voices)

These were picked from Higgsfield's voice library by description. Preview each one in Higgsfield.
To change a voice later, rerun Voice Change on that character's clips (about 1 credit per 10s).

| Character | Voice | voice_id |
|---|---|---|
| **Grace** | Naomi | `caeba733-3c17-43db-863e-69c7025512cd` |
| **Ethan** | Benji (your choice; replaces Holden, which was too deep) | `e6f9b893-51b1-51d3-afe9-9e0482cb7ac1` |
| **Vanessa** | Celine | `57ccb351-84d7-54ba-afd4-26b566ca6023` |
| **Bradley** | Reid (~168 Hz, younger and slicker) | `66469f5a-10db-586a-bab1-72f6ee66ba69` |
| **Mrs. Hayes** | Helena | `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd` |
| **Mama Ruth** | Opal | `66f35c82-2088-55eb-a0aa-7bf715dc03b7` |
| **Security Guard** | Desmond | `563f728c-e249-5a85-97ab-8461e8c09da6` |
| **Dr. Patel** | Elena (female, matches the doctor on screen) | `ca83ca7f-c186-493d-bd69-0d765fa861b2` |
| Nurse (Part 2) | Kling's own voice (one line) | — |
| Harold (Part 4+) | "Harold natural": cloned from his own on-camera Kling delivery (natural, not a narrator preset) | `277d8e8e-25ba-49e3-ab3e-3a758731bb94` (voice_type element) |
| Sam (Part 5+) | ElevenLabs line + lip-sync, or keep Kling's child voice | — |

## How the voice lock works
- **Tool:** Higgsfield **Voice Change** (`voice_change`). It keeps the words, timing and lip movement, and swaps the voice. About **1 credit per 10s**.
- **One-speaker clips:** one pass with that character's voice.
- **Two-speaker clips:** one pass per speaker. In the editor, cut each line from the pass in that speaker's voice. The timing is identical, so the lips stay in sync.

## Part 1 voice passes

| Clip | Speakers → passes |
|---|---|
| 2 | Grace |
| 3 | Vanessa, Grace |
| 4, 5, 6 | Guard, Grace |
| 7, 9 | Mrs. Hayes, Grace |
| 8 | Mrs. Hayes |
| 10 | Bradley, Grace |
| 12 | Ethan, Mrs. Hayes |
| 13 | Ethan, Grace, Mrs. Hayes |
| 18, 36 | Ethan |
| 20, 21, 30, 34 | Ethan, Grace |
| 23, 24, 27, 39 | Vanessa, Grace |
| 25, 28, 40 | Vanessa |
| 29 | Ethan, Vanessa |
| 31, 35 | Grace |
| 32, 33 | Mama Ruth, Grace |
| 1, 11, 14–17, 19, 22, 26, 37, 38 | Silent: no pass, add ambience in the editor |

## Ambience (built into the edit, Oct 6). NO licensed sounds
Every ambience sound is synthesized on the editing machine (room tone, traffic, fridge hum, dryer, crickets, water, tension drone),
except birdsong, which is the **public-domain** recording "Gentle breeze and birds singing" (Wikimedia Commons, PD: no copyright, no credit needed).

## Ambience & music (original plan)

Higgsfield's audio tools only make speech, so add music and sound effects from **CapCut's sound library**,
the **YouTube Audio Library** or **Pixabay**.

| Clips | Ambience / SFX | Music |
|---|---|---|
| 1–3 Gate | birds, light wind, then a car horn and tire screech, gate clang | hopeful soft piano → hard stop at the horn |
| 4–6 Driveway / living room | footsteps on brick, then a big echoey room | light curious strings |
| 7–9 Mrs. Hayes | quiet room tone, a clock ticking | none |
| 10–11 Pills | phone murmur, pills rattling, cabinet slam | low suspense drone |
| 12–14 Ethan | footsteps on stairs | warm gentle piano |
| 15–17 Montage | sheet whoosh, polishing squeak, towels | upbeat light montage track |
| 18–21 Coffee | coffee pour, mug clink, ice cube plop, birds outside | soft romantic piano |
| 22–28 Vanessa | car door, heels on marble, bag rustle | tense strings, low |
| 29–31 Ethan walks in / "pride" | dishes, running water | sad piano at "pride" |
| 32–33 Apartment | TV murmur through a wall, Sam coughing, traffic outside | gentle, emotional |
| 34–36 1 a.m. | fridge hum, crickets outside | intimate soft piano |
| 37–38 Pool house | water lapping, crickets, towel drop | heartbeat + rising drone |
| 39–40 Threat | dryer hum | dark drone → cut to black |

**Mixing tip:** voices at 0 dB, ambience around −20 dB, and music around −18 dB under dialogue
(−10 dB when nobody is talking).


## Sound design (current, Oct 6)
All synthesized ambience has been removed at the user's request. Every part now uses an **original procedural film score** from `tools/score.py`. It uses no samples or licensed audio, so there is no Content ID risk.

| Cue | Used for |
|---|---|
| hope | Soft piano arpeggios, for Grace's arrival |
| elegant | Piano waltz, for the mansion and the party |
| tender | Piano and strings, for Grace and Ethan moments |
| suspense | Plucked ostinato with low drone, for the pill swap and the bullying |
| tension | Heartbeat, low drone and high dissonance, for discoveries |
| dark | Braams, heartbeat and cluster, for threats and betrayal |
| panic | Fast strings and drums, for the collapse and the ER |
| sad | Slow strings, for the hospital and Mama Ruth |

Sound effects are risers, impacts, stingers, braams and a whoosh on every title card. The music ducks by 8 dB under dialogue, and the final mix is normalized to −14 LUFS.
