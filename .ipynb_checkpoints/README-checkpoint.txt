NTRODUCTION:
This repo currently aims to run the semantic parsing model of Sijie Song et al. 
The source repo used:
person_generation_spt: https://github.com/SijieSong/person_generation_spt
SP_MMAN: https://github.com/RoyalVane/MMAN
pytorch-openpose: https://github.com/Hzzone/pytorch-openpose
Super SloMo: https://github.com/avinashpaliwal/Super-SloMo
Monkey Net: https://github.com/AliaksandrSiarohin/monkey-net

We write a README(README_pipelines.txt, README_MMAN.txt, etc) for each directory except Super-SloMo and monkey-net. Please read them to learn what code we wrote and how to run the model. Before running each model, please set the environment and download pretrained models accordingly. For person_generation_spt and pytorch-openpose, just follow the instructions from the original repos. For SP_MMAN, please use CPU. For Super-SloMo and monkey-net, please follow the instructions in VIDEO IMPROVEMENT. 


KEY FRAME GENERATION:
To get started, read the README in ./pipelines. You will know how to run the model step by step.

After establishing appropriate environments(spenv_light for MMAN and sijieenv for openpose and SPT, we have provided requirements for the two environments), also making sure you can use "conda activate" in your shell script, you can use the following script to run key frame generation. You can configure parameters at the beginning.
$ bash gen_keyframe_gif.sh

After running key frame generation, to remove intermediate files:
$ bash make_clean.sh

You might see some errors and exceptions when running the above scripts. They are normal.


VIDEO IMPROVEMENT
Following the keyframe generation, you can run video improvement as follows:
1. install requirements_slowmo_monkey.txt in a new python environment
2. download pretrained model from
    * http://drive.google.com/uc?id=1IvobLDbRiBgZr3ryCRrWL8xDbMZ-KnpF
    * https://yadi.sk/d/6vqE41BTZKIAKQ 
   and save them to ./checkpoints/
$ bash slowmo_monkey.sh -d <driving-video> -x <smoothing-scale> -f <output_fps> -s <source-image> -o <out-file>


INPUT AND OUTPUT:
The input data we use are under the pipelines folder. 
The output results are under the make_video folder. Check make_video/REAMDE_video.txt






