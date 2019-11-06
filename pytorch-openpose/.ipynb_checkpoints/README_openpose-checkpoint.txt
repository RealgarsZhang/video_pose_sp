WHAT WE DID:
We wrote the ./python/run_input.py to generate the keypoints.csv file.

HOW TO RUN:
1. Go to https://github.com/Hzzone/pytorch-openpose, download the pretrained model. Put the body_pose_model.pth file in ./python
2. Go to ./python. Put the input images to ./python/input_images. Then:
$ python run_input.py

A keypoints.csv file will be generated. 