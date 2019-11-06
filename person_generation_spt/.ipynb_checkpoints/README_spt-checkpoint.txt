WHAT WE DID:
We modified the test_demo.py to generate GAN output for each image.

HOW TO RUN:
1. Go to https://github.com/SijieSong/person_generation_spt to find the pretrained model. Put the pretrained model under ./checkpoints/demo_model
2.
Put the .jpg images to ./imgs.
Put the semantic parsings to ./parsing
Put the two example.txt files to ./data
Put the keypoints.csv file to ./imgs
Then run:
$ bash ./scripts/test_demo.sh
The output is in ./gan_out