# Awakening — asset IDs, build, verification

## Reference sheets

| Sheet | Job ID |
|---|---|
| Man, 4-view turnaround | `92c5edfd-9cd7-45ab-bc34-25d86ab8a374` |
| Woman, 4-view turnaround | `24895e4c-51b6-480c-9568-2cc8dbd7a851` |
| Car, 3-view, **LEFT-HAND DRIVE** | `5324843f-529b-45e3-8e87-bd8776fd7d83` |
| Street plate | `9d37fcec-3beb-4c0e-8a3a-6729b216b083` |
| ~~Car, first version — steering side unspecified~~ | ~~`70731bb7-124f-4566-806d-75c4e147ca70`~~ |

## Keyframes (delivered)

| Shot | Job ID |
|---|---|
| 01 | `329a3351-f457-4a1e-9a08-517ecc1749a1` (v3) |
| 02 | `10fa315d-e018-470a-bdd9-d56739cd6d23` (v2) |
| 03 | `88abe982-4781-4ed7-8ed3-35fbf65aea61` (v3) |
| 04 | `251d0afb-4603-4f9a-abe1-32d0a7611139` (v2, reveal) |
| 05 | `28aa6c52-229d-45f6-8c2e-b9fd15bd8840` (v2) |
| 06 | `c8627eea-a65b-4ec8-a465-ca5a7f2a4977` |
| 07 | `8eccc329-e9a0-4ebe-930f-ed84d5529dfa` (v2) |
| 08 | `2876426b-4f06-44cd-807b-5fcfd6d6ac7a` (v2) |
| 09 | `d448420e-ad0f-4d04-80d5-15de4ba6bba0` |
| 10 | `1bcc9ca1-436f-4db1-b81b-0047dfd62ecc` |
| 11 | `d5cfa0ad-d65c-47c1-a07c-f36658770071` (v2) |

## Clips (delivered)

| Shot | Job ID |
|---|---|
| 01 | `0b3c9679-9526-4976-acd6-7bbc65263b1f` |
| 02 | `3b948751-25d2-42cb-8b24-545ad95f56e2` |
| 03 | `a0ee8b21-e0bb-4993-b01e-7833f60374a9` |
| 04 | `b6fc4597-91ed-4b4f-a742-f64c07306ff0` |
| 05 | `0d5c866a-933d-451c-9ba7-184586a95c5b` |
| 06 | `1163cd0e-290b-4c45-a157-ced20591d5cd` |
| 07 | `af13bad2-7568-4640-9f51-0631c079e886` |
| 08 | `26d1bea9-2484-4e2d-86e7-9138a263c843` |
| 09 | `54653b4c-6615-4932-ba32-e5c408c9f799` |
| 10 | `87ccf83a-b2bb-4374-842c-cb3f399ccc4d` |
| 11 | `1654e4c7-80b5-47cf-93f3-fcd9b21b21c0` |

## Models and cost

| Model | Settings | Credits |
|---|---|---|
| `nano_banana_pro` | image, 2K | 2.00 each |
| `kling3_0` | `mode:"pro"`, `sound:"off"` | 1.50/s — 5 s = 7.50, 6 s = 9.00 |

API facts that cost money to learn:
- the Kling resolution parameter is **`mode`** (`std`/`pro`/`4k`), **not** `quality`
- the Kling audio parameter is **`sound`**; the default is `on` and costs more
- video media role is **`start_image`**; image reference role is
  **`image_references`**, maximum 3 per keyframe
- `mode:"pro"` returns native **1076×1928** → 1080×1920 via a 0.37 % Lanczos
  scale and a crop
- `jobs_wait` caps `timeout_seconds` at 15
- `sandbox_exec` has a **16000-character** command limit — long HTML must be
  written in chunks with `cat >>`
- `generate_image_batch` fails JSON parsing above roughly 20 KB — split into
  two batches of about six

Final round: 102.08 → 34.58 = **67.50** (6 keyframes 12.00 + 6 clips 48.00 +
shot 04 reveal clip 7.50). Matched the quote exactly.

---

## Build

```bash
#!/bin/bash
cd /home/user/drive
set -e
FR=(86 86 87 86 86 86 87 129 129 130 129)
rm -f list.txt seg_*.mp4 silent.mp4 cut.wav
for i in $(seq 0 10); do
  n=$(printf "%02d" $((i+1)))
  ffmpeg -nostdin -v error -i "src_$n.mp4" \
    -vf "scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1" \
    -frames:v "${FR[$i]}" -c:v libx264 -preset medium -crf 15 \
    -pix_fmt yuv420p -an "seg_$n.mp4" -y
  echo "file 'seg_$n.mp4'" >> list.txt
done
ffmpeg -nostdin -v error -f concat -safe 0 -i list.txt -c copy silent.mp4 -y
ffmpeg -nostdin -v error -ss 108.400488 -t 46.7083333 -i track.mp3 -map 0:a:0 \
  -af "afade=t=in:st=0:d=0.60,afade=t=out:st=46.1616663:d=0.546667" \
  -ar 48000 -ac 2 -c:a pcm_s24le cut.wav -y
ffmpeg -nostdin -v error -i silent.mp4 -i cut.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart \
  -metadata title="THE PASS" -metadata artist="ALEXATOR" \
  01_FINAL_ALEXATOR_AWAKENING.mp4 -y
```

Rules baked into that script:
- exact cumulative frame counts with `-frames:v N`, never `-t <duration>`
- `crop`, never `pad` — a pad is a black bar and the brief forbids them
- `-map 0:a:0` is mandatory: the mp3 carries an attached-picture stream
- segments `libx264 -crf 15`, concat via demuxer `-c copy`, mux `-c:v copy`

## Verification commands

```
ffprobe
blackdetect=d=0.05:pix_th=0.10
freezedetect=n=0.002:d=0.5
cropdetect=limit=0.02:round=2:reset=0
ebur128=peak=true
select='gt(scene,0.30)',showinfo      # needs -v info, NOT -v error
```

## Origin proof PDF

`proof.html` written in 3 chunks (`cat >` then `cat >>`, 16000-char limit), then:

```bash
/ms-playwright/chromium-1228/chrome-linux64/chrome --headless --disable-gpu \
  --no-sandbox --no-pdf-header-footer --print-to-pdf=03_ORIGIN_PROOF.pdf proof.html
```

6 pages, 158,321 bytes, text and tables only — **no contact sheets, no grids**,
per client instruction. Wrapped as `03_ORIGIN_PROOF.zip` (88,501 bytes) because
Cloudflare rejects a raw `application/pdf` PUT.
