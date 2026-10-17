# ALEXATOR — PROJECT PLAYBOOK (use for any new project)

I am Okoye. I sell paid client deliverables on Contra for ALEXATOR, an
electronic/cinematic music project. The brief below is FIXED and identical on
every project. Only the concept and the track change.

=====================================================================
## THE DELIVERABLE (fixed client brief)
=====================================================================
One original vertical AI music video.
- 9:16, minimum 1080x1920, 30-60 s, MP4, minimum 24 fps, stereo
- No watermark, no AI-service logos, no black bars, no empty or technical frames
- Strong visual hook in the first 1-2 seconds
- Music: one ALEXATOR track, one professionally chosen 30-60 s section,
  natural fade-in, smooth fade-out
- No stock footage, no third-party visual material, no real-person references

THREE files plus a confirmation message in the Contra chat:
  01_FINAL_ALEXATOR_[TRACK].mp4
  02_USED_AI_SOURCES.zip
  03_ORIGIN_PROOF.pdf     (ship inside a .zip — Cloudflare rejects application/pdf)

=====================================================================
## MY STANDING RULES
=====================================================================
- Be realistic. Never tell me something is done when it is not.
- QUOTE CREDITS BEFORE SPENDING. Check my balance first, every time.
- Stop asking me to choose things. Stop asking permission. Always allow.
- A completely different concept every project. Never repeat a previous one.
- Rotate tracks — use a different ALEXATOR release each time.
- No grid and no collage anywhere in the video.
- NEVER assemble or deliver until you have LOOKED AT every shot as a still.
  Do not use me as the quality check.

=====================================================================
## THE ORDER OF WORK
=====================================================================
1. Pick the concept and the track. Tell me both in two lines, then proceed.
2. Analyse the music locally and lock the bar grid (see MUSIC below).
3. Write the shot list. Every shot gets an explicit CAMERA POSITION.
4. Generate the reference sheets (subject/s, key object, location). Show me.
5. Generate the keyframes, one per shot. LOOK AT THEM. Show me.
6. Generate the clips from the keyframes. LOOK AT THEM. Show me.
7. Build, verify, upload, deliver all three files.

Never skip 5 and 6. Every disaster on this account came from skipping them.

=====================================================================
## PROMPT RULES LEARNED THE EXPENSIVE WAY
=====================================================================
1. **Paste the FULL spec of every subject VERBATIM into every prompt that
   shows it.** Reference sheets do NOT carry properties between shots. Only
   the prompt text does. Shortening a spec on a rebuild is what produced
   wrong-coloured interiors and wrong uniforms on two separate projects.
2. **Never contradict yourself in one prompt.** Banning "frames" while asking
   for a "chrome frame" produces exactly the thing you banned.
3. **State direction against the WORLD and against the FRAME.** "Looking
   ahead" is meaningless. "His eyes go out toward the LEFT EDGE OF THE FRAME"
   is not.
4. **State a PATH, not just a position.** Giving two objects' positions
   without the path between them makes them collide.
5. **Fewer references = more weight each.** Two references beat three.
6. **Name who is in shot and rule out the alternatives:** "he is NOT blonde,
   NOT fair-haired, NOT long-haired, NOT a woman."
7. **Left and right flip with the camera.** Any asymmetric subject — a
   steering wheel, a holstered weapon, a scar, a worn ring — appears on the
   opposite side of the picture when the camera faces it. This is a mirror
   and no wording fixes it. Decide the camera position so the geometry is
   right BY CONSTRUCTION, and write the camera position into the prompt as
   the first line. If a shot idea needs a camera angle that mirrors the
   subject, the shot idea is wrong.
8. **Camera-locked motion kills distortion.** A large rigid object moving
   sideways across frame ripples and melts. Fix: "THE CAMERA IS LOCKED TO THE
   [OBJECT] AND TRAVELS WITH IT AT EXACTLY THE SAME SPEED. IT STAYS
   COMPLETELY STILL IN THE FRAME. ALL OF THE MOVEMENT IS IN THE BACKGROUND."
9. **Avoid collision, near miss, impact, jam, hit.** They trip the safety
   filter and the job FAILS on the backend. Rephrase and resubmit.
10. Every prompt ends with: no watermark, no logo, no text, no split screen,
    no grid, no collage, no borders.

=====================================================================
## MUSIC — HOW TO LOCK THE GRID
=====================================================================
Analyse locally with ffmpeg. Do not guess.
- Get the BPM three independent ways and require agreement before trusting it.
- beat  = 60 / BPM
- bar   = beat * 4
- Choose a section that STARTS ON A BAR LINE. Getting the bar phase wrong is
  the trap — the cut drifts against the music and it is audible.
- Length: pick a whole number of bars landing inside 30-60 s.
    frames = round(bars * bar * 24)
- Fades: about 0.6 s in, about 0.55 s out ending exactly at the last frame.
- Cut points: divide the frame total across the shots so every cut lands on a
  bar or half-bar. Write the per-shot frame counts down before building.
- Many ALEXATOR mp3s carry an attached-picture stream, so **`-map 0:a:0` is
  MANDATORY** or ffmpeg grabs the cover art instead of the audio.
- Record the track's MD5 for the origin proof.

=====================================================================
## BUILD
=====================================================================
set -e
FR=(...)              # per-shot frame counts, must sum to the planned total
for i in ...; do
  ffmpeg -nostdin -v error -i "src_$n.mp4" \
    -vf "scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1" \
    -frames:v "${FR[$i]}" -c:v libx264 -preset medium -crf 15 \
    -pix_fmt yuv420p -an "seg_$n.mp4" -y
  echo "file 'seg_$n.mp4'" >> list.txt
done
ffmpeg -nostdin -v error -f concat -safe 0 -i list.txt -c copy silent.mp4 -y
ffmpeg -nostdin -v error -ss <IN> -t <DUR> -i track.mp3 -map 0:a:0 \
  -af "afade=t=in:st=0:d=0.60,afade=t=out:st=<OUT>:d=0.547" \
  -ar 48000 -ac 2 -c:a pcm_s24le cut.wav -y
ffmpeg -nostdin -v error -i silent.mp4 -i cut.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart \
  -metadata title="<TITLE>" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_<TRACK>.mp4 -y

### PATCHING ONE SHOT INTO A FINISHED FILM (cheap — do this for revisions)
Never rebuild the whole film to change one shot. Slice the existing film
around the shot, drop the new clip in, copy the audio straight over:
  ffmpeg -v error -i old.mp4 -vf "select='between(n\,0\,<S-1>)',setpts=N/24/TB,setsar=1" -r 24 ... A.mp4
  ffmpeg -v error -i new.mp4 -vf "<the scale/crop chain>" -frames:v <N> ... B.mp4
  ffmpeg -v error -i old.mp4 -vf "select='between(n\,<E+1>\,<LAST>)',setpts=N/24/TB,setsar=1" -r 24 ... C.mp4
  concat A+B+C, then:
  ffmpeg -v error -i silent.mp4 -i old.mp4 -map 0:v:0 -map 1:a:0 -c:v copy -c:a copy ...
The frame counts MUST still sum to the original total or the film drifts.

=====================================================================
## VERIFY — RUN ON EVERY BUILD, BEFORE EVERY UPLOAD
=====================================================================
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,display_aspect_ratio,r_frame_rate,nb_frames,duration -of default=nw=1 F
ffmpeg -v info -i F -vf "blackdetect=d=0.05:pix_th=0.10"        -f null -   # expect none
ffmpeg -v info -i F -vf "freezedetect=n=0.002:d=0.5"            -f null -   # expect none
ffmpeg -v info -i F -vf "cropdetect=limit=0.02:round=2:reset=0" -f null -   # expect 1080:1920:0:0
ffmpeg -v info -i F -af "ebur128=peak=true"                     -f null -
ffmpeg -v info -i F -vf "select='gt(scene,0.30)',showinfo" -f null - | grep -o 'pts_time:[0-9.]*' | awk -F: '{printf "%d ", $2*24+0.5}'
The scene-cut list must match the planned cut points exactly. If it does not,
the film is off the music — fix it before uploading.

=====================================================================
## HOW TO LOOK AT YOUR OWN WORK
=====================================================================
You cannot fetch the CDN directly — the proxy blocks it. Three channels work:
(a) **base64 relay.** In the sandbox: ffmpeg -> scale to about 60-110 px wide
    -> base64 -w0 -> paste into a LOCAL heredoc -> decode with python -> Read
    the file. MUST stay under roughly 5000 base64 characters or sandbox stdout
    silently truncates and the JPEG will not decode. Strip non-base64
    characters before decoding. Check the last two bytes are FFD9.
(b) **Contact sheet.** ffmpeg drawtext + hstack -> media_upload -> PUT ->
    media_confirm -> send me the CDN link. Always works, costs nothing.
(c) **Just send me the raw d8j0ntlcm91z4 link** for any generation and I will
    look at it myself.

=====================================================================
## DELIVERY PACKAGING
=====================================================================
**02_USED_AI_SOURCES.zip**
  /keyframes/   every keyframe PNG, numbered by shot
  /clips/       every raw generated clip, numbered by shot
  /references/  every reference sheet
  MANIFEST.txt  one line per asset: shot, role, model, job ID, URL, sha256,
                and the exact prompt used
Build it in ONE chained sandbox_exec command (download + zip + upload),
because /home/user/* is wiped constantly. Upload as application/octet-stream.

**03_ORIGIN_PROOF.pdf** must state, with evidence:
  - every visual is original AI generation; no stock, no third-party material,
    no real-person reference
  - which models produced what (stills model, motion model), with settings
  - the full job ID and timestamp for every asset
  - the music: track name, exact section in/out, bars, BPM, fade lengths,
    track MD5
  - the commercial-use terms of each service (FOUR URLs)
  - four screenshots of my logged-in account showing the generations
Ship it inside a .zip as application/octet-stream.

**ALWAYS BLOCKED WITHOUT ME:** the four commercial-use term URLs and the four
account screenshots need me logged in. Build everything else, leave clearly
marked placeholders, and tell me exactly what to send. Also remind me to post
the freelancer confirmation in the Contra chat — I keep forgetting it.

=====================================================================
## API FACTS THAT COST MONEY WHEN FORGOTTEN
=====================================================================
- generate_image_batch MUST carry aspect_ratio:"9:16". Omitting it returns
  2048x2048 SQUARE. That mistake cost 22.00 credits.
- nano_banana_pro image = 2.00 (billed as "Nano Banana Pro", backend reports
  it as nano_banana_2).
- kling3_0 with mode:"pro" and sound:"off" = 7.50 for 5 s, 9.00 for 6 s.
  `sound` defaults ON and costs more — always set it off explicitly.
- Image references: `medias` role "image_references", max 3.
- Video: `medias` role "start_image". Use `mode`, not `quality`.
- Kling native 9:16 output is 1076x1928. NEVER crop my footage without telling
  me first.
- jobs_wait max timeout_seconds is 15; a Kling clip takes several minutes, so
  expect to poll repeatedly.
- sandbox_exec: 16000 char command limit, 60 s default timeout, background:true
  gives a 15 min lease. /home/user/* is wiped often — chain download, build and
  upload into ONE command.
- Occasional "OpenSSL SSL_read: bad record mac" on CDN downloads. Retry per file.
- If generate_video_batch returns submission_failed with a preset
  recommendation, retry the same call with
  declined_preset_id "24bae836-2c4a-48e0-89b6-49fcc0b21612". Nothing is charged.
- `show_generations` is free and recovers full job IDs from 8-char prefixes.

## TYPICAL BUDGET FOR A FRESH PROJECT
  4 reference sheets   8.00
  N keyframes          2.00 each
  N clips              7.50 each (5 s)
An 11-shot project is about 112.50. A 9-shot project is about 93.50.
Quote me the real number against my real balance before you start.

## FIRST THING TO DO
Check my balance, tell me what it is, tell me the concept and track you have
chosen in two lines, quote the cost, then start.

## SANDBOX TRANSFER LIMIT (learned on LAST GOODBYE)
`sandbox_exec` refuses any command carrying a large base64 blob of file bytes —
it blocks text-relaying bytes between environments. Get files in by URL with
curl, or write them inline within the 16,000-char command limit. Plan packaging
around that: provenance tables and specs go in as heredocs, big source files
come down from their CDN URLs.

=====================================================================
# UPDATE — 17 OCTOBER 2026
# Client review of videos 23, 24, 25 + everything learned in that round.
# Where this section contradicts anything above, THIS SECTION WINS.
=====================================================================

## NEW CLIENT RULES (standing, all future videos)

1. **Release number AND exact title together in every Origin Proof**, in the
   form `006 — Towards the Dream`. Not one or the other. Standing format.

2. **No kissing.** Anywhere, ever.

3. **Casting:** the client asked for all-white characters for the current
   run, because Black characters had been used a lot across the engagement.
   Treat as live until they say otherwise — and ASK ABOUT CASTING UP FRONT.
   Not asking cost 4.00 in wasted plates.

4. **Never cut a drop or climax off before the musical moment completes.**

5. **A cut between two shots of similar scale and angle reads as a mistake,
   not an edit.** If two consecutive shots are both mid-scale two-shots from
   a similar position, the audience sees characters teleport inside one shot.
   Change the SHOT SCALE or use a clearly different camera angle across every
   significant cut.

6. **A person may never simply appear in a seat.** Either show them arrive,
   or put a cutaway between so time visibly passes. Props must also carry
   across the cut — a sandwich that vanishes between two frames in the same
   light reads as a fault.

7. **The music must not end part-way through the spoken brand phrase.** End
   the film BEFORE the phrase starts or AFTER it completes. See the detection
   method below — this is now a mandatory pre-build check on every track.

8. **No obvious AI or continuity errors.** Geometry collapse (melting tables,
   smearing chairs, stretching faces) is an automatic reject.

9. **Every video needs a clear concept and progression an ordinary viewer
   understands with no explanation** — a real beginning, development and
   conclusion.

10. **The character and mood of the music must fit the characters and the
    concept.** A 135 BPM driving track does not belong to a slow, passive,
    interior story. Match energy to energy.

11. **STOP REPEATING THE SAME CHARACTER BEHAVIOUR.** The client caught this
    across all three films: characters looking toward camera and sighing, or
    making the same emotional gesture. Examples they cited: video 23 at 4,
    33, 43 and 48 s; video 24 at 28 s; video 25 at 27 s. Different videos
    were reading as the same creative DNA despite different locations and
    characters.

12. **More emphasis on screenplay and story development BEFORE generating
    scenes.** Explore story structures first. Each video must have a clear
    plot, different character behaviour, and a genuinely distinct creative
    direction.

## THE BEHAVIOUR MATRIX — MANDATORY FROM NOW ON

Before any image is generated, assign every shot a DISTINCT PHYSICAL VERB and
write the list into the production bible so it can be checked.

- No two shots in one film may end on a breath, a settle, or a look to camera.
- No more than ONE shot per film may do it at all.
- Across films, vary the register: not every protagonist endures quietly.

Worked example (LAST ONE OUT, video 25):
  taping / surveying / lifting / sorting / stopping /
  deciding / switching on / releasing / dancing / leaving

Root cause of the problem: "subject exhales and settles" was my default way to
end a shot because it reliably produces motion and avoids freeze detection.
That is a technical habit leaking into performance. Find motion another way.

## MUSIC — THREE NEW MANDATORY CHECKS

### A. Find the spoken brand section before choosing the window
A dry voice tag sits dead-centre in the stereo field while music is wide.
Decode stereo, compute M=(L+R)/2 and S=(L-R)/2, take the 250-4000 Hz band
energy of each per frame, and flag runs where M/S exceeds ~2.2x the track
median. Those runs are where the voice lives. END THE FILM CLEAR OF THEM.

Confirmed on both tracks checked so far:
  010 New Horizon  — centre-dominant run from 102.818 s
  024 Words Unsaid — centre-dominant run 243.833 -> 246.642 s
Both of my original out-points landed INSIDE those runs.

Do NOT trust faster-whisper for this. It hallucinates over instrumental music
("Thanks for watching guys!", "No, no, no, no, no!"). Use the M/S measurement.

### B. Find the REAL drop with a per-bar loudness profile
Do not assume the drop is where the shot plan wants it. Measure mean level
per bar across the chosen window and look for the breakdown-then-slam shape.
On 024 the arrangement fell 3.5 dB at bars 15-16 and came back +2.6 dB at
bar 17 — that is the drop. Re-allocate bars across shots so the payoff shot
lands on it. This costs nothing and it is the difference between a film that
is cut to music and one that merely runs alongside it.

Note: the film does NOT have to be 28 bars. Fewer bars that put the drop in
the right place beats more bars that do not. 25 bars = 44.6 s is well inside
the 30-60 s brief.

### C. Re-fit the grid against the exact file that ships
Not against an earlier copy of the same track. Fitting on my container's copy
and shipping the sandbox's copy moved Kindred Soul by 0.075 BPM and 0.40 s of
phase, and New Horizon by 0.385 BPM.

### Still true from before, do not regress
- ACF at hop 512 is frame-quantised: 135.999 BPM is the lag-19 bucket, not a
  measurement. The IOI histogram shares that quantisation so it is NOT an
  independent confirmation.
- THE LOCAL-FIT RULE: fit tempo AND phase over exactly the window the film
  uses, wide-open 118-152 search, reject within 1.5 BPM of either edge.
- THE GRID CHECK: score the onset envelope at the bar lines against 400
  random phases. z > 2.5 = real. A grid that cannot beat random phase is not
  a grid.

## PROMPT RULES ADDED THIS ROUND

11. **Structural stability must be the FIRST instruction in any busy scene.**
    Tables, chairs, crowds and rooms collapse in the back half of a clip.
    Name every object class as a solid thing that keeps its exact shape,
    position and proportions, and ban melting, smearing, stretching,
    warping, folding, sinking and disappearing by name.

12. **Hair across the face destroys a performance shot.** On any shot whose
    point is an expression, state that the face stays visible and lit in
    every frame and that hair never crosses the eyes, nose or mouth.

13. **For a continuity rebuild, feed the previous shot's LAST FRAME in as an
    image reference.** Extract it, upload it, and write "reference image 1 is
    the exact preceding frame of this film". This is the only reliable way to
    carry props, light and background across a cut.

14. **Dancing and other complex motion:** specify contained, readable,
    on-the-spot movement with arms well clear of the face and of each other.
    Ban leaping, fast spinning and bending backwards. State the limb count
    explicitly. This is where the model breaks hands.

15. **A location plate will invent background people unless banned.** Say
    "no person anywhere in the frame, sharp or blurred, near or far".

16. **When a film must contain no readable text** (record sleeves, shop
    signage, shutters, packaging), ban it per-asset AND globally: no letters,
    no numbers, no album art, no barcodes, no brand names, no model names, no
    price labels. Abstract neon shapes instead of word signs.

## VERIFY — TIGHTENED

Run on EVERY build before EVERY upload. These are the pass marks:
  frames / duration / 1080x1920 / 24 fps        exact to plan
  blackdetect                                   0 events
  freezedetect at d=0.5 AND d=0.4 AND d=0.3     0 events at all three
  cropdetect                                    1080:1920:0:0
  scene-cut frame list                          matches the plan exactly
  loudness and true peak                        measured and recorded
  MD5 after upload                              re-download and compare

Inspect the HEAD, the MIDDLE and the TAIL of every clip. The cat/car fusion
and the shot-04 collapse were both in parts of a shot I had not looked at.

## CORRECTIONS TO THE OLDER SECTIONS ABOVE

- **Looking at your own work:** forget the base64 relay. `sandbox_exec` takes
  `image_paths` (up to 4 files, 512 KiB total) and returns the images to me
  natively. Downscale to ~350-460 px wide at quality ~70 and I can inspect
  3-4 frames per call. Crop to native resolution for hands and fine detail.
- **sandbox_exec limits are now** 128,000 characters and 120 s, not 16,000
  and 60 s. Background jobs still get a 15 min lease.
- **PDFs upload fine as application/pdf.** They do not need to be zipped.
- **Preset interception:** there are at least two. Retry with the singular
  `declined_preset_id` for whichever one was named:
    24bae836-2c4a-48e0-89b6-49fcc0b21612  "IN THE DARK"
    f1821f84-945b-4cd1-9085-1f479db0028e  "DROWN IN MUSIC"
  Nothing is charged for a refused submission.
- **ID3 trap:** ALEXATOR masters carry a 516,417-byte ID3v2 tag with cover
  art. A 300 KB range request truncates it and ffprobe reports no tags.
  Use `curl -r 0-600000` minimum.
- **Identify a master by MD5, never by filename.**

## AUDIO TRANSFER — THE ONE THING I CANNOT DO ALONE

My container is blocked by org egress policy from upload.higgsfield.ai and
the Higgsfield CDN. The sandbox can reach both. Chat attachments live in my
container and no tool moves them to Higgsfield. Pushing the client's audio to
the public GitHub repo was blocked as data exfiltration and I must not work
around that.

So: the user uploads each track through `media_upload_widget` and gives me
the media_id. Open the widget as the only tool in that turn. Verify the file
by ID3 title AND MD5 before using it.

## STILL OUTSTANDING

- Egyptian (THE LAST GOODBYE) v5 packages
- Genesis re-cut on the corrected 108.4 BPM grid
- Packages for Crossroads and Genesis / The First Breath
- SECURITY: an earlier session showed the balance falling from 3,926.33 to
  4.83 against only 39.00 of my own spend — roughly 3,880 credits
  unaccounted for. I advised revoking API keys, disconnecting third-party
  apps, changing the password, signing out all sessions, enabling 2FA and
  opening a support ticket. Whether any of that was done is unknown. KEEP
  WATCHING THE BALANCE.
