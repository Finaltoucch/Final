#!/bin/bash
# THE MONEY — full assembly, v4 (all corrections applied).
#
# Runs in the Higgsfield sandbox via sandbox_exec, NOT locally: this session's
# egress policy returns 403 CONNECT for d8j0ntlcm91z4.cloudfront.net, so the
# clips can only be fetched from inside the sandbox.
#
# Launch detached, then poll with `tail -n 40 /home/user/v4.log`. The sandbox
# survives a poll but dies when a command is killed by timeout, so never run
# this in the foreground.
#
#   cat > v4.sh << 'EOS' ... EOS
#   chmod +x v4.sh && setsid nohup ./v4.sh >/dev/null 2>&1 </dev/null & disown
#
# Before launching, call media_upload for the output file and paste the
# presigned URL into UPLOAD_URL below — the file is ephemeral and must be
# pushed out inside this same script.

exec > /home/user/v4.log 2>&1
set -u

B=https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY
UPLOAD_URL="PASTE_PRESIGNED_URL_HERE"

# 41 shots in SCREEN order: scenes 1-17, then 26-41, then 18-25.
# Corrected shots are marked; see the-money-shot-manifest.md.
U=(
"$B/hf_20260802_194328_337dd699-14d6-4fb4-9312-cfa35489c8ff.mp4"
"$B/hf_20260802_194330_b2755783-a4fc-496e-90f9-4bb09e49dbe1.mp4"
"$B/hf_20260802_195359_fd9d4129-52fb-421c-ad56-b1521db6bfd6.mp4"
"$B/hf_20260802_195401_fe81c2e9-84db-42af-b63b-f595c470867f.mp4"
"$B/hf_20260802_194338_53708b65-ca54-4446-a6b0-5157e7fd5130.mp4"
"$B/hf_20260802_194340_30f2b40a-ca9b-475b-b75e-e72a3eb964a9.mp4"
"$B/hf_20260805_165043_338d8ab8-ddaa-4bb0-8193-c6edc2454eee.mp4"   # 7  CORRECTED
"$B/hf_20260802_194345_24fa8f84-15b7-4bdf-b10a-e45a794054b2.mp4"
"$B/hf_20260802_203813_c5d39f6d-ba05-40cd-8257-8ea355510c0a.mp4"
"$B/hf_20260802_203755_40d28cf6-b608-4758-8589-900bedc8010d.mp4"
"$B/hf_20260802_200358_a3639046-8324-4fe1-a257-1a4472677704.mp4"
"$B/hf_20260802_200359_1ed49781-71c2-423e-a585-c4dae0e5d52e.mp4"
"$B/hf_20260802_203817_b2b27516-9cde-43f9-bc8d-8f043db438ec.mp4"
"$B/hf_20260805_165049_697c2b8a-9622-4133-a968-dd0617e040e8.mp4"   # 14 CORRECTED
"$B/hf_20260805_071317_2efa12e2-e809-469a-b8a6-f12ce3853499.mp4"   # 15 corrected, reframe still pending
"$B/hf_20260805_072129_34b321dc-51cb-469b-84ea-934d75487d68.mp4"   # 16 corrected, reframe still pending
"$B/hf_20260802_202430_ff5d3768-1bb5-480d-b33e-1f60d3a1eee8.mp4"
"$B/hf_20260805_071306_0510764d-73e8-40ae-977c-8a98a7f80a27.mp4"   # 18 CORRECTED
"$B/hf_20260805_071308_a8276d0c-ab06-4ac7-a41e-f0a482b8928a.mp4"   # 19 CORRECTED
"$B/hf_20260803_131858_51041fa5-9228-44ab-a848-1bb2855f21aa.mp4"
"$B/hf_20260803_131900_f113c04c-2176-4ac7-954d-aea394fef95d.mp4"
"$B/hf_20260803_131918_d62534d3-9acc-426f-8541-25c718b05e69.mp4"
"$B/hf_20260805_071848_623fc96d-edeb-416e-9d1d-1c32ba7c39c4.mp4"   # 23 CORRECTED
"$B/hf_20260803_131920_762d42f2-2cc9-481e-8f0b-adde984ba5a0.mp4"
"$B/hf_20260803_131923_5df6e692-f109-42c4-bbb7-57383cd9ef86.mp4"
"$B/hf_20260803_173858_d2b25bb9-bff5-4434-9668-4308b8378518.mp4"
"$B/hf_20260803_173900_21d33ddf-4579-45eb-9b69-937d43fd0bc5.mp4"
"$B/hf_20260803_173903_9d90d2d6-74b9-4009-ade2-20f10d257e9d.mp4"
"$B/hf_20260803_173905_e8575014-a98f-4adc-82f2-8ce5442cbd6e.mp4"
"$B/hf_20260803_173925_4d0fabb1-1403-4768-84fa-2793fa0a9005.mp4"
"$B/hf_20260805_071310_ab6ad1f7-3ea4-4fb6-908a-6c7716829818.mp4"   # 31 CORRECTED
"$B/hf_20260805_071555_cb8868c2-96c1-4a87-8dc6-5285d5c08962.mp4"   # 32 CORRECTED
"$B/hf_20260803_173912_95428532-8694-4d1c-8e4d-0aff5fefb497.mp4"
"$B/hf_20260802_202401_682e7e0e-0980-46bf-add5-942e25ae4ba5.mp4"
"$B/hf_20260802_202404_9dbcb6fd-3deb-450a-ba5a-1a570bbce8fe.mp4"
"$B/hf_20260802_202406_48ad870c-5efe-4755-8e55-81fb648d45ab.mp4"
"$B/hf_20260805_071552_52aeb330-69df-4bd4-bd76-9afb19213a97.mp4"   # 37 CORRECTED
"$B/hf_20260805_071558_4f755ffb-24a2-4137-b89d-546ce2a4081e.mp4"   # 38 CORRECTED
"$B/hf_20260805_071303_ea59d9dd-e3ba-4720-926b-5d5c0df35f9f.mp4"   # 39 CORRECTED
"$B/hf_20260802_203806_e337c108-4710-4b3f-b891-8dde7e37668c.mp4"
"$B/hf_20260802_204039_ce539869-87d6-4450-aa75-045d8d466beb.mp4"
)

echo "START $(date)  shots=${#U[@]}"
for i in "${!U[@]}"; do n=$((i+1)); curl -sfL -o "v${n}.mp4" "${U[$i]}" & done

# Narration: Nora, breath-punctuated v3. This is the take the audio was
# approved on — do not substitute an earlier block set.
curl -sfL -o n1.wav "$B/hf_20260804_165441_bab0fe64-322f-4450-b5e3-d9d8646f10aa.wav" &
curl -sfL -o n2.wav "$B/hf_20260804_165446_9bf5d311-7ad4-4b09-b6f5-d3ce37c0287d.wav" &
curl -sfL -o n3.wav "$B/hf_20260804_165451_3fc64e0c-e4b7-4a5f-8eb6-ab53d33a1cb2.wav" &
curl -sfL -o n4.wav "$B/hf_20260804_165455_be132ab5-84d5-4adb-b7e3-c591b691f9f2.wav" &
curl -sfL -o n5.wav "$B/hf_20260804_165500_6b2e9b6d-dca4-4daf-aade-1939d344a87f.wav" &
wait
echo "downloaded video=$(ls v*.mp4 2>/dev/null | wc -l)/41 audio=$(ls n*.wav 2>/dev/null | wc -l)/5"

for i in $(seq 1 41); do
  [ -s "v${i}.mp4" ] || { echo "FATAL missing v${i}.mp4"; exit 1; }
done

rm -f vl.txt
for i in $(seq 1 41); do echo "file '/home/user/v${i}.mp4'" >> vl.txt; done
ffmpeg -y -loglevel error -f concat -safe 0 -i vl.txt -c copy silent.mp4
VD=$(ffprobe -v error -show_entries format=duration -of csv=p=0 silent.mp4)
echo "picture=${VD}s"

# 1.05 lifts the read off its natural drag without touching pitch.
for i in 1 2 3 4 5; do
  ffmpeg -y -loglevel error -i "n${i}.wav" -filter:a "atempo=1.05" -ar 44100 "t${i}.wav"
done
D1=$(ffprobe -v error -show_entries format=duration -of csv=p=0 t1.wav)
D2=$(ffprobe -v error -show_entries format=duration -of csv=p=0 t2.wav)
D3=$(ffprobe -v error -show_entries format=duration -of csv=p=0 t3.wav)
D4=$(ffprobe -v error -show_entries format=duration -of csv=p=0 t4.wav)
D5=$(ffprobe -v error -show_entries format=duration -of csv=p=0 t5.wav)
echo "blocks: $D1 $D2 $D3 $D4 $D5"

# Two seconds of air between blocks. Concatenating them back to back is what
# drifted Ben's backstory onto Gabby's drawer scene in the first cut.
S2=$(python3 -c "print(int(($D1+2)*1000))")
S3=$(python3 -c "print(int(($D1+2+$D2+2)*1000))")
S4=$(python3 -c "print(int(($D1+2+$D2+2+$D3+2)*1000))")
S5=$(python3 -c "print(int(($D1+2+$D2+2+$D3+2+$D4+2)*1000))")
echo "starts ms: 0 $S2 $S3 $S4 $S5"

ffmpeg -y -loglevel error -i t1.wav -i t2.wav -i t3.wav -i t4.wav -i t5.wav \
  -filter_complex "\
[0:a]adelay=0|0[x1];[1:a]adelay=${S2}|${S2}[x2];[2:a]adelay=${S3}|${S3}[x3];\
[3:a]adelay=${S4}|${S4}[x4];[4:a]adelay=${S5}|${S5}[x5];\
[x1][x2][x3][x4][x5]amix=inputs=5:duration=longest:normalize=0,volume=3.2,apad,atrim=0:${VD}[out]" \
  -map "[out]" narr.wav
echo "narration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 narr.wav)s"

ffmpeg -y -loglevel error -i silent.mp4 -i narr.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k final.mp4
echo "BUILT $(ffprobe -v error -show_entries format=duration -of csv=p=0 final.mp4)s $(stat -c%s final.mp4) bytes"

if [ "$UPLOAD_URL" != "PASTE_PRESIGNED_URL_HERE" ]; then
  curl -f -s -X PUT -H "Content-Type: video/mp4" --upload-file final.mp4 "$UPLOAD_URL"
  echo "UPLOADED rc=$?"
else
  echo "NO UPLOAD URL SET — final.mp4 will be lost when the sandbox is reclaimed"
fi
echo "DONE $(date)"
