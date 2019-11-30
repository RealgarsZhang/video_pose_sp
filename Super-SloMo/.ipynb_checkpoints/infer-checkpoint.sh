#!/usr/bin/env bash

scale=8
fps=32

input=$1
in_name=$(echo $input | cut -f1 -d.)
out_name=$in_name-${2:-$scale}x-${3:-$fps}fps

./video_to_slomo.py \
    --checkpoint SuperSloMo.ckpt \
    --ffmpeg $(dirname $(realpath $(which ffmpeg))) \
    --video $input \
    --output $out_name.mp4 \
    --sf ${2:-$scale} --fps ${3:-$fps}
    
ffmpeg -i $out_name.mp4 $out_name.gif && rm $out_name.mp4