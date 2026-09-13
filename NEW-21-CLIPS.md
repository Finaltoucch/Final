# THE 21 NEW CLIPS — FIRED 2026-09-13

All `seedance_2_5`, 30s, 16:9, 195 credits each. **4,095 credits.**
Balance before: 6,013.45.

| # | Shot | Job ID |
|---|---|---|
| 1 | The morning run | 8c4f9660-a81d-46eb-a321-48a895dda784 |
| 2 | The call | 444a1cab-d76f-48bb-ad77-727521685a13 |
| 3 | The decision | ac300653-7e18-493f-9be6-8c8dd73a716f |
| 4 | The plan | f3f60ec0-ab07-4d29-948e-862b60c69f99 |
| 5 | Mateo goes to the water | e68f38eb-9c3f-4b01-adaf-af50f43bc224 |
| 6 | They lose him | 2eab3b2e-7d92-4bc7-8969-7fd292d2e108 |
| 7 | Liam | 899e0a7c-3289-4339-95e8-61435201f8e8 |
| 8 | Daniel runs | a7830ffd-cbb7-4037-b88a-a003315bb444 |
| 9 | Daniel stops | 1786d47d-5acb-4ed3-a8ee-0bd2ee18834d |
| 10 | The passages | 59e492a7-3222-402a-93aa-fb4922c9d4ce |
| 11 | The gate takes her | 605814e1-a69d-487e-a2e3-78ba3ea9d49e |
| 12 | After Marcus | 65c2ecf7-f86b-438f-a980-65453deb62b0 |
| 13 | The valuation | 2e59db9a-b399-4392-90f4-b5757ecefc83 |
| 14 | Mateo says goodbye | 4f481579-7bef-4cfb-80d6-d175300fff61 |
| 15 | Upriver | 3336ce1b-422d-42eb-aa08-587c6e5fff54 |
| 16 | Night one | 871919f0-f430-4661-9120-73604ec69f2c |
| 17 | The 1974 camp — bones | 97ef2d82-008a-4218-9d4c-1ac71c17b281 |
| 18 | The 1974 camp — the torn log | f9302ffd-9536-4903-88ed-6991e48e4bfd |
| 19 | The argument | 0240ab06-30c2-4b45-baa8-39d81f1c6576 |
| 20 | The drone sees her | 07f6af63-2f80-45ea-89fb-ea8d7499c8d9 |
| 21 | Armando shows him the diamond | e91e7093-67bc-4348-8c2b-16ebe69e369e |

## Two 429s, zero credits lost
Submission is rate-limited as well as concurrency-capped. Clip 21 and clip 10 each
bounced once on `rate_limit_reached`. No job is created on a 429 and nothing is charged —
resubmitted after a wait, both went through.

---

## THE ARMANDO SCENE — `ip_detected` ×3, ALL REFUNDED

The one shot that would not render. Three submissions, three `ip_detected` bounces:
`e91e7093`, `66974fcb`, `822f937d`. Zero credits charged on any of them —
confirmed against the balance, which moved by exactly 3,900 for exactly 20 clips.

**It is not the diamond.** Clips 3, 12 and 13 all carry `e0762233` and all rendered.
**It is not the wording.** Stripping "jewellery gem" changed nothing.
The only thing unique to this shot is the Armando element in that firelit village setting.

**Fallback shot, already rendered:** a 12-second no-faces insert (`dcde5779`) — an old
hand setting the rough uncut diamond on the crate, a younger hand picking it up and
turning it. It cuts into the existing Armando scene over the original audio and corrects
stone → diamond without regenerating the scene or touching a frame of its dialogue.

A fourth attempt (`b6646609`) reframes the scene on a lantern-lit deck with the old man
mending a net, no held-to-the-firelight beat. If it lands it replaces the scene outright.

## THE NEW REEL

21 clips in story order, **10:13**, concat-copy, no re-encode, every original audio
track untouched.
