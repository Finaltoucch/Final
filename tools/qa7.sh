# qa7.sh SHEET id=stem ... : frames sheet + loudness + background medium transcript into tr_SHEET.txt
o=$1; shift; bash qa.sh $o "$@"; fs=""
for a in "$@"; do i=${a%%=*}; fs="$fs $i.mp4"; echo $i $(ffmpeg -i $i.mp4 -af ebur128 -f null - 2>&1 | grep ' I:' | tail -1) >> lufs.txt; done
(nohup python3 trm.py $fs > tr_$o.txt 2>/dev/null &)
