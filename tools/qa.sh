# Review sheet for clips (frames at 12/50/92%): qa.sh out.jpg id=stem ... (1-4 clips)
o=$1; shift; rows=""
for a in "$@"; do i=${a%%=*}; s=${a#*=}; [ -f $i.mp4 ] || curl -sf https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/$s.mp4 -o $i.mp4
 d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $i.mp4); fs=""
 for p in 0.12 0.5 0.92; do t=$(python3 -c "print($d*$p)"); ffmpeg -v error -y -ss $t -i $i.mp4 -frames:v 1 -vf "scale=400:225,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='$i':x=4:y=4:fontsize=20:fontcolor=yellow:box=1:boxcolor=black" $i-$p.jpg; fs="$fs $i-$p.jpg"; done
 convert $fs +append $i-row.jpg; rows="$rows $i-row.jpg"; done
convert $rows -append -quality 72 $o
