WHAT WE DID:
1.Due to environment setting(have to use Pytorch 0.3.6), we modified some codes so that the model can be run on CPU. Please run it on CPU. 
2. We modified the test.py to generate a semantic parsing for each frame. 

HOW TO RUN:
1. Go to https://github.com/RoyalVane/MMAN, find the link to the pretrained model, and put the pretrained model into ./checkpoints/Exp_0
2. Put the input images to ../Human/test_LIP_A. Then run gen_fake_seg.py to generate fake segmentations in test_LIP_B. Then run:
$ python test.py --dataroot ../Human --dataset LIP --name Exp_0 --gpu_ids -1 --which_epoch 30 --how_many <num_images> --output_nc 20 --loadSize 256
The output semantic parsings will be in sp_out. <num_images> is the number of images to be processed. 

