This repo currently aims to run the semantic parsing model of Sijie Song et al. 
The source repo used:
person_generation_spt: https://github.com/SijieSong/person_generation_spt
SP_MMAN: https://github.com/RoyalVane/MMAN
pytorch-openpose: https://github.com/Hzzone/pytorch-openpose

This repo contains four directories. There is a README(README_pipelines.txt, README_MMAN.txt, etc) for each of them. Please read it to learn what code we wrote and how to run the model. For convenience, we included all pretrained model files and output files. Before running each model, please set the environment accordingly. For person_generation_spt and pytorch-openpose, just follow the instructions from the original repos. For SP_MMAN, please use CPU.  

To get started, read the README in ./pipelines

We have run a result and you can find them in ./person_generatin_spt/gan_out. All intermediate data are kept. 



