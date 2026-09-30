# ALEXATOR — "THE PASS" — CONTINUE BRIEF (style edits, sources zip, origin proof)

I am Okoye. I sell paid client deliverables on Contra for ALEXATOR, an
electronic/cinematic music project. This project is LIVE and nearly finished.
Do not start over. Continue from the file below.

## THE CURRENT DELIVERED FILM
https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/247f0819-95c8-4eef-88e5-2ae8bbdb71f1.mp4

Verified: 1080x1920, DAR 9:16, 24 fps, 1035 frames, 43.126 s, 74,079,910 bytes.
blackdetect none. freezedetect none. cropdetect 1080:1920:0:0 (no bars).
ebur128 -13.0 LUFS, LRA 3.5 LU, true peak -4.3 dBFS.
Scene cuts land exactly on 86 172 259 345 431 517 647 776 905.

10 shots, 24 bars. Shot 06 was removed at my request and is not coming back.

## WHAT IS STILL OWED TO THE CLIENT
The brief requires THREE files plus a confirmation message in the Contra chat:
  01_FINAL_ALEXATOR_AWAKENING.mp4   <-- DONE, link above
  02_USED_AI_SOURCES.zip            <-- STALE, must be rebuilt for this cut
  03_ORIGIN_PROOF.pdf               <-- STALE, must be rebuilt for this cut
The live zips document the OLD 11-shot cut and old job IDs. They are wrong.

=====================================================================
## THE CAMERA LAW — BREAK THIS AND THE WHOLE JOB IS REJECTED
=====================================================================
The car is LEFT-HAND DRIVE. Whether the driver and the steering wheel appear
on the LEFT OF THE PICTURE depends ONLY on where the camera is. It is a
mirror. No prompt wording changes it.

| Camera position               | Driver + wheel appear         |
|-------------------------------|-------------------------------|
| Front, or front three-quarter | viewer's RIGHT  -- FORBIDDEN  |
| Directly behind, receding     | viewer's LEFT   -- SAFEST     |
| Car's LEFT flank, side-on     | near side       -- reads badly if the door fills the foreground |
| Car's RIGHT flank             | far side        -- FORBIDDEN  |

**NEVER POINT THE CAMERA AT THE FRONT OF THE CAR.**
The safest camera for any new car shot is BEHIND the car: from behind, the
car's left IS the picture's left and it cannot mirror. Shots 01 and 07 were
both rebuilt this way and that is what fixed them.

Also state in every moving-car prompt:
"THE CAMERA IS LOCKED TO THE CAR AND TRAVELS WITH IT AT EXACTLY THE SAME
SPEED. THE CAR STAYS COMPLETELY STILL IN THE FRAME. ALL OF THE MOVEMENT IS
IN THE BACKGROUND." Without this, the bodywork ripples and melts.

=====================================================================
## HOW TO DO A STYLE EDIT CHEAPLY (this is the important part)
=====================================================================
Do NOT rebuild the whole film. Patch one shot into the existing film. That is
how the last fix was done and it costs 9.50 per shot instead of 100+.

Shot boundaries in the current film (frame numbers):
  shot 01  0    - 85     (86 frames)
  shot 02  86   - 171    (86)
  shot 03  172  - 258    (87)
  shot 04  259  - 344    (86)
  shot 05  345  - 430    (86)
  shot 07  431  - 516    (86)
  shot 08  517  - 646    (130)
  shot 09  647  - 775    (129)
  shot 10  776  - 904    (129)
  shot 11  905  - 1034   (130)

To replace ONE shot (example: replacing shot 07, frames 431-516):
```bash
V="scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1"
E="-c:v libx264 -preset medium -crf 15 -pix_fmt yuv420p -an -y"
# everything before the shot
ffmpeg -v error -i old.mp4 -vf "select='between(n\,0\,430)',setpts=N/24/TB,setsar=1" -r 24 $E A.mp4
# the new shot, cut to the exact frame count
ffmpeg -v error -i new.mp4 -vf "$V" -frames:v 86 $E B.mp4
# everything after the shot
ffmpeg -v error -i old.mp4 -vf "select='between(n\,517\,1034)',setpts=N/24/TB,setsar=1" -r 24 $E C.mp4
printf "file 'A.mp4'\nfile 'B.mp4'\nfile 'C.mp4'\n" > list.txt
ffmpeg -v error -f concat -safe 0 -i list.txt -c copy silent.mp4 -y
# carry the audio straight over from the old film - it is already the exact
# 24-bar cut with both fades, so copy it, never re-cut it
ffmpeg -v error -i silent.mp4 -i old.mp4 -map 0:v:0 -map 1:a:0 -c:v copy -c:a copy \
  -movflags +faststart -metadata title="THE PASS" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_AWAKENING.mp4 -y
```
The frame counts MUST still add to 1035 or the film drifts off the music.

Verify EVERY build before uploading:
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,display_aspect_ratio,r_frame_rate,nb_frames,duration -of default=nw=1 F
ffmpeg -v info -i F -vf "blackdetect=d=0.05:pix_th=0.10"      -f null -   # expect none
ffmpeg -v info -i F -vf "freezedetect=n=0.002:d=0.5"          -f null -   # expect none
ffmpeg -v info -i F -vf "cropdetect=limit=0.02:round=2:reset=0" -f null - # expect 1080:1920:0:0
ffmpeg -v info -i F -af "ebur128=peak=true"                    -f null -
ffmpeg -v info -i F -vf "select='gt(scene,0.30)',showinfo" -f null - | grep -o 'pts_time:[0-9.]*' | awk -F: '{printf "%d ", $2*24+0.5}'
# cuts must read: 86 172 259 345 431 517 647 776 905
```

=====================================================================
## ASSETS
=====================================================================
Reference sheets (job IDs, reuse these, do not regenerate):
  man       92c5edfd-9cd7-45ab-bc34-25d86ab8a374
  woman     24895e4c-51b6-480c-9568-2cc8dbd7a851
  car LHD   5324843f-529b-45e3-8e87-bd8776fd7d83
  street    9d37fcec-3beb-4c0e-8a3a-6729b216b083

Shots 01 and 07 (the rebuilt ones, full IDs):
  01 keyframe c6af1bb8-6d03-4a87-abb0-cac79f54e811
     clip     05dd05d0-f92a-4422-8df3-634293e5fc8c
  07 keyframe c5863e01-8287-4131-92b2-6753cfc114b4
     clip     51912bee-02df-47a2-82cd-a4da51c95c29

Shots 02,03,04,05,08,09,10,11 — I only have the first 8 hex characters:
  02 kf 80819421 / clip e224259b
  03 kf 50939c05 / clip 16807b0b
  04 kf 251d0afb / clip b6fc4597
  05 kf 28aa6c52 / clip 0d5c866a
  08 kf 15da6d16 / clip f111f729
  09 kf d448420e / clip 54653b4c
  10 kf 1bcc9ca1 / clip 87ccf83a
  11 kf 2cbf7c41 / clip 3a5dc650
**To recover the full IDs and download URLs for these, call `show_generations`
(it is free) and match on the 8-character prefixes.** You need the full URLs
to build the sources zip.

=====================================================================
## LOCKED SPECS — paste VERBATIM into every prompt showing that subject
=====================================================================
Shortening these is what produced black car interiors. The reference sheet
does NOT carry these properties between shots. Only the prompt text does.

**CAR** — early-1960s European two-seat open-top roadster. Pale IVORY CREAM
bodywork, glossy, smooth, completely plain: no badges, no emblems, no marque
or model names, no bonnet ornament, no trim strips, no mouldings, no number
plates. Soft top FULLY DOWN and stowed out of sight under a smooth flush
panel. NOTHING STANDS UP ABOVE THE BODYWORK: no hood frame, no hood bows, no
roll bar, no roll hoop, no targa bar, no header rail, no window frames, no
bars, no struts, no rails. TAN PLEATED LEATHER SEATS, warm light golden-brown,
horizontal pleats. TAN DASHBOARD, same tone, small round chrome-rimmed dials.
Thin WOOD-RIMMED steering wheel, polished wooden rim, slender metal spokes.
Chrome bumpers, chrome wire-spoke wheels on whitewall tyres. Windscreen LOW
AND FRAMELESS: shallow glass with a slim polished edge, no higher than his
shoulder; no pillar, no A-pillar, no chrome surround, no quarter-light, no
side glass. Interior is TAN, never black, never dark brown, never grey, never
red, never blue. LEFT-HAND DRIVE: wheel and driving seat on the car's own
LEFT; the seat beside it completely empty, no wheel, no pedals.

**MAN** — White European, 25, tall, slim athletic. Short dark brown hair,
neatly cut, tapered at the sides, swept back with a clean side parting. Clean
shaven, defined jaw, straight nose, light warm tan, dark brown eyes. Open
NAVY BLUE linen blazer over a plain WHITE open-collar shirt, no tie. Tailored
STONE trousers. Plain flat silver wristwatch on the left wrist. He is NOT
blonde, NOT fair-haired, NOT long-haired, NOT a woman. NO sunglasses and NO
glasses of any kind.

**WOMAN** — White European, 24, slim. Long chestnut brown hair, soft wave,
centre parting, loose and swept forward over her LEFT shoulder. Fair skin,
green eyes, warm red lip. Floor-length DEEP EMERALD GREEN plain silk dress,
two thin straps, plain low back. Gold drop earrings, nude heels, small gold
clutch. Both arms down at her sides.

**STREET** — Tree-lined city street, pale stone townhouses, shuttered windows,
iron balconies, plane trees, wide pavement, low late-afternoon sun down the
far end. Empty of people. No signage.

=====================================================================
## 02_USED_AI_SOURCES.zip — HOW TO BUILD IT
=====================================================================
Contents, matching THIS cut exactly (10 shots, no shot 06):
  /keyframes/   the 10 keyframe PNGs, named 01..11 (no 06)
  /clips/       the 10 raw Kling mp4s, named 01..11 (no 06)
  /references/  the 4 reference sheet PNGs
  MANIFEST.txt  one line per asset: shot number, role, model, job ID, URL,
                sha256, and the exact prompt used
Build it in one sandbox_exec command (download + zip + upload chained), because
/home/user/* is wiped often. Upload with content type application/octet-stream.

=====================================================================
## 03_ORIGIN_PROOF.pdf — HOW TO BUILD IT
=====================================================================
Must state, with evidence:
  - that every visual is original AI generation, no stock, no third-party
    material, no real-person reference
  - the two models used and what each produced:
      nano_banana_pro  (billed as "Nano Banana Pro") — all stills
      kling3_0 mode pro, sound off — all motion
  - the full job ID and timestamp for every asset
  - the music: ALEXATOR track 002 "Awakening", section 108.400488 s to
    151.525488 s, 24 bars at 133.601 BPM, fade in 0.600 s, fade out 0.547 s
    from 42.578 s. Track MD5 6706a6ec2d17b0a836a3d63f8b269335
  - the commercial-use terms of each service (FOUR URLs)
  - four screenshots of my logged-in account showing the generations

**Cloudflare rejects an application/pdf PUT.** Put the PDF inside a .zip and
upload that as application/octet-stream.

**STILL BLOCKED AND NOT YOUR FAULT:** the four commercial-use term URLs and
the four account screenshots need me logged in. Build everything else, leave
clearly marked placeholders for those six items, and tell me exactly what to
send you. Also remind me to post the freelancer confirmation in the Contra
chat — that is still not done.

=====================================================================
## MY STANDING RULES
=====================================================================
- Be realistic. Never tell me something is done when it is not.
- QUOTE CREDITS BEFORE SPENDING and check my balance first.
- Stop asking me to choose things. Stop asking permission. Always allow.
- No grid and no collage anywhere in the video.
- NEVER assemble or deliver until you have LOOKED AT every changed shot as a
  still. Do not use me as the quality check. Two ways to look:
  (a) ffmpeg -> scale to about 60-110 px wide -> base64 -w0 -> paste into a
      LOCAL heredoc -> decode with python -> Read the file. It MUST stay under
      roughly 5000 base64 characters or sandbox stdout silently truncates and
      the JPEG will not decode. Strip non-base64 characters before decoding.
  (b) ffmpeg drawtext + hstack contact sheet -> media_upload -> PUT ->
      media_confirm -> send me the CDN link.
- You can also just give me the raw d8j0ntlcm91z4 CDN link for any generation
  and I will look at it myself.

=====================================================================
## API FACTS THAT COST MONEY WHEN FORGOTTEN
=====================================================================
- generate_image_batch MUST carry aspect_ratio:"9:16". Omitting it returns
  2048x2048 SQUARE. That mistake cost 22.00 credits.
- nano_banana_pro image = 2.00. kling3_0 mode:"pro" sound:"off" = 7.50 for 5 s,
  9.00 for 6 s. sound defaults ON and costs more — always set it off.
- Image references: `medias` role "image_references", max 3. TWO references
  (subject + car) beat three; fewer references means more weight each.
- Video: `medias` role "start_image". Use `mode`, not `quality`.
- Kling native 9:16 output is 1076x1928. NEVER crop my footage without telling
  me first.
- jobs_wait max timeout_seconds is 15; a Kling clip takes several minutes.
- sandbox_exec: 16000 char command limit, 60 s default timeout, background:true
  gives a 15 min lease. /home/user/* is wiped constantly — chain download,
  build and upload into ONE command.
- Occasional "OpenSSL SSL_read: bad record mac" on CDN downloads. Retry per file.
- If generate_video_batch returns submission_failed with a preset
  recommendation, retry the same call with
  declined_preset_id "24bae836-2c4a-48e0-89b6-49fcc0b21612". Nothing is charged.
- Avoid the words collision, near miss, impact, jam, hit in prompts. They trip
  the safety filter and the job FAILS on the backend.

## FIRST THING TO DO
Check my balance, tell me what it is, and tell me what any change I ask for
will cost BEFORE you spend anything.
