This repo currently aims to run the semantic parsing model of Sijie Song et al. 
The source repo used:
person_generation_spt: https://github.com/SijieSong/person_generation_spt
SP_MMAN: https://github.com/RoyalVane/MMAN
pytorch-openpose: https://github.com/Hzzone/pytorch-openpose

This repo contains four directories. There is a README(README_pipelines.txt, README_MMAN.txt, etc) for each of them. Please read it to learn what code we wrote and how to run the model. For convenience, we included all pretrained model files and output files. Before running each model, please set the environment accordingly. For person_generation_spt and pytorch-openpose, just follow the instructions from the original repos. For SP_MMAN, please use CPU.  

To get started, read the README in ./pipelines. You will know how to run the model step by step.

After establishing appropriate environments(spenv_light for MMAN and sijieenv for openpose and SPT), also making sure you can use "conda activate" in your shell script, you can use the following script to run the model.

To run the model, you can run the following. You can configure parameters at the beginning.
$ bash gen_keyframe_gif.sh

After running, to remove intermediate files:
$ bash make_clean.sh

You might see some errors and exceptions when running the above scripts. They are normal.

Some result gif are under make_video folder.






