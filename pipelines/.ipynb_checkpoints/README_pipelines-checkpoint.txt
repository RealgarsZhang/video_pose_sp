WHAT WE DID:
We wrote this directory from scratch. 

HOW TO RUN: 
Read the README in each directory to learn how to run the model. How to run the pipeline:
1. Run preprocess.py to generate the frame images and the reference image cropped and sampled.

2. Put the images in pipelines/preprocess_out to SP_MMAN/Human/test_LIP_A, and run gen_fake_seg.py to generate fake segmenations, which is required by the model but has no influence on anything. Then run the MMAN model to get predicted semantic parsing. Perhaps you need to clean up the .ipynb checkpointers in the test_LIP_A and test_LIP_B dirs.

3. Put the images in pipelines/preprocess_out to pytorch-openpose/python/input_images. Run run_input.py to generate keypoints.csv.

4. Copy the semantic parsing generated from 2 to pipelines/sp_out. Run process_sp_out.py to process the sp_out folder, and generate the two example.txt files required by Sijie's model. The processed semantic parsing is in the pipelines/parsing directory.

5. Put the semantic parsing in pipelines/parsing, the jpg images in pipelines/process_out, the keypoints.csv in pytorch-openpose , and the two example.txt files to appropriate directory in Sijie's repo. Then run the model.The output image are put in gan_out


OTHER INFO:
1. All filenames, directory names are hardcoded at the beginning of .py files. Check the .py files for more info.
2. visualize_sp.py is to visualize a semantic parsing. Mainly for debugging. 
3. To put frame images into a .gif, use the code in ../make_video.