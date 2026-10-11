# ALEXATOR TRACK REGISTER
Which track belongs to which film. Rotation rule: **never reuse a track.**
Built by matching byte sizes of the audio on the Higgsfield account against
the local masters, then against every project bible in this repo.

| Track | Higgsfield media_id | Film |
|---|---|---|
| 001 Genesis | `f1c36ae6-f0b8-4e86-9858-9311686c1caf` (+4 duplicate uploads) | THE FIRST BREATH |
| 002 Awakening | `3e4f2fe4-f0c2-4b8f-849b-e0d86d05f5b6` | THE PASS — withdrawn at client request |
| 007 Full Throttle | `86cfe926-8f67-4cdd-a064-3746140c8742` | DESCENT |
| 008 Brighter Days | `50efb7c4-7d99-40de-a237-f51f9ceb3a13` | WHAT THE HANDS LET GO |
| 009 Crossroads | `41577603-fbf0-4376-81a4-561b12f4fe14` | THE POINTSMAN |
| 012 Last Goodbye | `0037a16b-b13d-4b1a-9638-db6d469c8c81` | THE LAST GOODBYE |
| 014 Ride the Storm | `c5282618-e2c9-434a-b69e-058c95df86d8` | RIDE THE STORM |
| 015 Break New Ground | `06810fb8-0829-4b6f-820f-118dddf94e4a` | THE CROSSING (the cat) |
| 016 By Your Side | `fe07005e-0b7f-4c47-85f9-c37bd7a4fa33` | BY YOUR SIDE |
| 017 All for You | `d19c43a2-50d2-480a-999a-fce08773e1a6` | THE KITE |
| 019 Never Let Go | `eb157740-dffd-485a-b93d-a2d987d3de31` | WHERE THE SOUND IS |
| 021 Adrenaline | `baccf609-2701-4098-af88-8029b29c8185` | THE SMOKEJUMPER |
| 025 Pain and Love | `438106cc-75e2-4403-afa2-f1857d5a1dd1` | THE AVALANCHE DOG |
| Rise Again | `05ea62db-e06d-4976-8e53-51a53b3ac6c6` | RISE AGAIN |
| *(title unknown)* | `af3c1bb9-3da2-48c9-87e8-5ee5e9f58fa3` | **THE LONGEST DINNER** |
| *(title unknown)* | `1f92398f-6444-47d9-ab0c-781361547229` | **WHAT SHE PUT IN HIS HAND** |
| *(one of these four)* | `41fddf73` `729f5631` `decb7898` | Through the Fire / Just Relax / Endless Sands |

The last two were found by elimination: every one of the seventeen
previously-used tracks accounts for exactly one distinct file size on the
account, and these two matched none of them. Both carry the ALEXATOR master
fingerprint — 48 kHz stereo mp3 at ~337 kbps with an attached MJPEG cover that
is the generic ALEXATOR.COM artwork — so they are genuine masters that had
never been cut. **Neither carries an ID3 title tag. The client must supply the
two release names before the deliverables can be given their final filenames.**

## HOW TO IDENTIFY AN UNKNOWN AUDIO MEDIA WITHOUT SPENDING ANYTHING
1. `show_medias type=audio` for the id list.
2. In the sandbox, `curl -sI` each URL and read `content-length`. Sizes are
   distinctive enough to identify a master outright.
3. `curl -s -r 0-300000` the head of the file and `ffprobe` it for
   `format_tags=title,artist`. ALEXATOR masters have none, but other audio on
   the account does, which separates music from generated speech at a glance.
4. Extract the attached picture with `-map 0:v:0 -frames:v 1` and look at it.
5. Fingerprint check: 48 kHz, stereo, ~337 kbps, an MJPEG stream, 190–250 s.
