#!/bin/bash
# Assemble the three native ratios from the cleaned master.
set -e
FF=/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2
S=/tmp/claude-0/-home-user-Final/cd63c724-a39b-5037-8d91-6395028ce328/scratchpad
SRC=$S/build/clean_master.mp4
PRESET=${PRESET:-veryfast}
CRF=${CRF:-19}

# timings (seconds)
LOCK_IN=0.30;  LOCK_OUT=28.90
HEAD_IN=0.35;  HEAD_OUT=2.85
PORT_IN=16.30; PORT_OUT=19.80
END_IN=29.37

render () {
  TAG=$1; W=$2; H=$3; REFRAME=$4
  A=$S/assets/$TAG
  OUT=$S/out/cherry_solana_${TAG}.mp4
  echo ">>> $TAG  ${W}x${H}"
  $FF -hide_banner -loglevel error \
    -i "$SRC" \
    -loop 1 -i "$A/lockup.png" \
    -loop 1 -i "$A/headline.png" \
    -loop 1 -i "$A/portal_slug.png" \
    -loop 1 -i "$A/endcard.png" \
    -filter_complex "\
[0:v]${REFRAME},setsar=1[v0];\
[1:v]format=rgba,fade=t=in:st=${LOCK_IN}:d=0.35:alpha=1,fade=t=out:st=${LOCK_OUT}:d=0.35:alpha=1[lk];\
[2:v]format=rgba,fade=t=in:st=${HEAD_IN}:d=0.35:alpha=1,fade=t=out:st=${HEAD_OUT}:d=0.35:alpha=1[hd];\
[3:v]format=rgba,fade=t=in:st=${PORT_IN}:d=0.18:alpha=1,fade=t=out:st=$(echo "$PORT_OUT-0.18"|bc):d=0.18:alpha=1[ps];\
[4:v]format=rgba,fade=t=in:st=${END_IN}:d=0.25:alpha=1[ec];\
[v0][lk]overlay=0:0:enable='between(t,${LOCK_IN},29.30)'[a1];\
[a1][hd]overlay=0:0:enable='between(t,${HEAD_IN},3.25)'[a2];\
[a2][ps]overlay=0:0:enable='between(t,${PORT_IN},${PORT_OUT})'[a3];\
[a3][ec]overlay=0:0:enable='gte(t,${END_IN})'[a4];\
[a4]subtitles='$A/captions.ass':fontsdir=/root/.fonts[vout]" \
    -map "[vout]" -map 0:a \
    -c:v libx264 -preset $PRESET -crf $CRF -pix_fmt yuv420p \
    -c:a aac -b:a 192k -movflags +faststart \
    "$OUT" -y
  ls -lh "$OUT"
}

render 16x9 1920 1080 "scale=1920:1080"
render 9x16 1080 1920 "crop=608:1080:656:0,scale=1080:1920:flags=lanczos"
render 1x1  1080 1080 "crop=1080:1080:420:0,scale=1080:1080:flags=lanczos"
echo "ALL DONE"
