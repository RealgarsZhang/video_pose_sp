#!/usr/bin/env bash

# Example Usage:
# ./slowmo_monkey.sh -d driving-video.gif -x8 -f32 -s source-img.jpeg -o out-file.gif


scale=8
fps=32

while getopts "d:s:o:x:f:" OPT
do case $OPT in
    d) driving_video=$OPTARG ;;
    s) source_image=$OPTARG ;;
    o) out_file=$OPTARG ;;
    x) scale=$OPTARG ;;
    f) fps=$OPTARG ;;
esac done

d_in_name=$(echo $driving_video | cut -f1 -d.)
d_out_name=$d_in_name-${scale}x-${fps}fps

../Super-SloMo/video_to_slomo.py \
    --checkpoint '../Super-SloMo/SuperSloMo.ckpt' \
    --ffmpeg $(dirname $(realpath $(which ffmpeg))) \
    --video $driving_video \
    --output $d_out_name.mp4 \
    --sf ${scale} --fps ${fps}
    
ffmpeg -i $d_out_name.mp4 $d_out_name.gif && rm $d_out_name.mp4

smooth_driving_video=$d_out_name.gif

conda activate monkey-net

python ../monkey-net/demo.py \
    --config '../monkey-net/config/taichi.yaml' \
    --driving_video $smooth_driving_video \
    --source_image $source_image \
    --checkpoint '../monkey-net/taichi-cpk.pth.tar' \
    --out_file $out_file