# sheet.sh out.jpg label=stem ...  : 3-column contact sheet of generated images (stem = 20261008_..._id)
o=$1; shift; i=0; rows=""; row=""
for a in "$@"; do l=${a%%=*}; s=${a#*=}; [ -f $l.png ] || curl -sf https://d8j0ntlcm91z4.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/hf_$s.png -o $l.png
 ffmpeg -v error -y -i $l.png -vf "scale=380:-1,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='$l':x=4:y=4:fontsize=22:fontcolor=yellow:box=1:boxcolor=black" t_$l.jpg
 row="$row t_$l.jpg"; i=$((i+1)); if [ $i -eq 3 ]; then convert $row +append r_$l.jpg; rows="$rows r_$l.jpg"; row=""; i=0; fi; done
[ -n "$row" ] && { convert $row +append r_last.jpg; rows="$rows r_last.jpg"; }
convert $rows -append -quality 72 $o
