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
