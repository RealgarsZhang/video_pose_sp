 video_filename="bdj.mp4"
 reference_img="bdj.jpg"
 # you should try and find the best value for the following four parameters
 y_min=0.0
 y_max=1.0
 x_min=0.2
 x_max=0.8
 sampling_rate=128
 
 conda activate spenv_light # The environment for MMAN
 echo "Environment changed to spenv_light"
 
 echo "Preprocessing the video frames"
 
 # preprocess the images
 cd pipelines
 mkdir preprocess_out
 python preprocess.py --video_filename $video_filename --reference_img $reference_img --y_min $y_min --y_max $y_max --x_min $x_min --x_max $x_max --sampling_rate $sampling_rate
 
 # get the semantic parsing with MMAN
 
 cp -R preprocess_out ../SP_MMAN/Human/test_LIP_A
 cd ../SP_MMAN/Human
 mkdir test_LIP_B
 rm -rf test_LIP_A/.ipynb_checkpoints
 rm -rf test_LIP_B/.ipynb_checkpoints
 python gen_fake_seg.py
 echo "Fake segmentation generated"
 num_images=$(ls -1 test_LIP_A | wc -l)
 
 cd ../MMAN
 mkdir sp_out
 python test.py --dataroot ../Human --dataset LIP --name Exp_0 --gpu_ids -1 --which_epoch 30 --how_many $num_images --output_nc 20 --loadSize 256
 mv sp_out ../../pipelines/sp_out
 
 # process the SP, to fit to SPT model.
 cd ../../pipelines
 mkdir parsing
 python process_sp_out.py --reference_img $reference_img
 
 # run openpose
 conda activate sijieenv # the environment for openpose and SPT
 cp -R preprocess_out ../pytorch-openpose/python/input_images
 cd ../pytorch-openpose/python
 python run_input.py
 
 # copy stuff to SPT directory, and run SPT
 cd ../..
 mkdir person_generation_spt/gan_out
 mv pipelines/test_A_example.txt person_generation_spt/data/test_A_example.txt
 mv pipelines/test_B_example.txt person_generation_spt/data/test_B_example.txt
 mv pipelines/preprocess_out person_generation_spt/imgs
 mv pipelines/parsing person_generation_spt/parsing
 mv pytorch-openpose/python/keypoints.csv person_generation_spt/imgs/keypoints.csv
 
 cd person_generation_spt
 CUDA_VISIBLE_DEVICES=0 
 python2 test_demo.py --dataroot ./imgs --annotation_file './imgs/keypoints.csv'  --name demo_model --model PoseGuidedGenerationDemo --phase test --no_dropout --results_dir './results/demo_test' --dataset_mode 'pose_globallocal_face'  --how_many $num_images --which_epoch 'latest'
 
 mv gan_out ../make_video/gan_out
 cd ../make_video
 python make_video.py
 # the output.gif is the result
 
 
 
 
 
 
 
 
 
 
 
 