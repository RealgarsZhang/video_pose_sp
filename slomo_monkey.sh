#!/usr/bin/env bash

# Example Usage:
# ./slowmo_monkey.sh -d driving-video.gif -x8 -f32 -s source-img.jpeg -o out-file.gif

slomo_ckpt_url='http://drive.google.com/uc?id=1IvobLDbRiBgZr3ryCRrWL8xDbMZ-KnpF'
monkey_ckpt_url='https://yadi.sk/d/6vqE41BTZKIAKQ'

slomo_ckpt='./checkpoints/SuperSloMo.ckpt'
monkey_ckpt='./checkpoints/taichi-cpk.pth.tar'

while getopts "d:s:o:x:f:" OPT
do case $OPT in
    d) driving_video=$OPTARG ;;
    s) source_image=$OPTARG ;;
    o) out_file=$OPTARG ;;
    x) scale=$OPTARG ;;
    f) fps=$OPTARG ;;
esac done

if [[ ! -z "$scale" ]] && [[ ! -z "$fps" ]]
then
    if [[ ! -f "$slomo_ckpt" ]]
    then
        mkdir -p checkpoints
        gdown -O $slomo_ckpt $slomo_ckpt_url
    fi
    d_in_name=$(echo $driving_video | rev | cut -f2- -d. | rev)
    d_out_name=$d_in_name-${scale}x-${fps}fps
    ./Super-SloMo/video_to_slomo.py \
        --checkpoint $slomo_ckpt \
        --ffmpeg $(dirname $(realpath $(which ffmpeg))) \
        --video $driving_video \
        --output $d_out_name.mp4 \
        --sf ${scale} --fps ${fps}
    ffmpeg -i $d_out_name.mp4 $d_out_name.gif && rm $d_out_name.mp4
    driving_video=$d_out_name.gif
fi

if [[ ! -z "$source_image" ]] && [[ ! -z "$out_file" ]]
then
    if [[ -f "$monkey_ckpt" ]]
    then
        python ./monkey-net/demo.py \
            --config './monkey-net/config/taichi.yaml' \
            --driving_video $driving_video \
            --source_image $source_image \
            --checkpoint $monkey_ckpt \
            --out_file $out_file
    else
        echo "Error: $monkey_ckpt not found!"
        echo "Please manually download MonkeyNet checkpoint at $monkey_ckpt_url"
    fi
fi