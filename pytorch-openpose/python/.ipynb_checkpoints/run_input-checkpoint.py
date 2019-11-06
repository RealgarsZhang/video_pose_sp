INPUT_DIR = "input_images"
OUTPUT_FILENAME = "keypoints.csv"
#REFERENCE_IMG = "putin.jpg"


import os
import sys
sys.path.insert(0, 'python')
import cv2
import model
import util
from hand import Hand
from body import Body
import matplotlib.pyplot as plt
import copy
import numpy as np
import pandas as pd

body_estimation = Body('body_pose_model.pth')

annotation_file = pd.DataFrame(columns=['name', 'keypoints_y', 'keypoints_x'])
for filename in os.listdir(INPUT_DIR):
    if filename.split(".")[-1] not in ("jpg","png"):
        continue
        
    print("processing:"+filename)
    test_image = INPUT_DIR+"/"+filename
    oriImg = cv2.imread(test_image)  # B,G,R order
    candidate, subset = body_estimation(oriImg)
    
    x_kps = []
    y_kps = []
    for i in range(18):
        index = int(subset[0][i])
        if index == -1:
            x_kps.append(-1)
            y_kps.append(-1)
        else:
            x_kp, y_kp = candidate[index][0:2]
            x_kps.append(int(x_kp))
            y_kps.append(int(y_kp))
            
    annotation_file = annotation_file.append({"name":filename,"keypoints_y":y_kps,"keypoints_x":x_kps}, ignore_index = True)
    print({"name":filename,"keypoints_y":y_kps,"keypoints_x":x_kps})

    
"""
filename = REFERENCE_IMG
print("processing:"+REFERENCE_IMG)
test_image = REFERENCE_IMG
oriImg = cv2.imread(test_image)  # B,G,R order
candidate, subset = body_estimation(oriImg)
    
x_kps = []
y_kps = []
for i in range(18):
    index = int(subset[0][i])
    if index == -1:
        x_kps.append(-1)
        y_kps.append(-1)
    else:
        x_kp, y_kp = candidate[index][0:2]
        x_kps.append(int(x_kp))
        y_kps.append(int(y_kp))
            
annotation_file = annotation_file.append({"name":filename,"keypoints_y":y_kps,"keypoints_x":x_kps}, ignore_index = True)
print({"name":filename,"keypoints_y":y_kps,"keypoints_x":x_kps})
"""
    
print(annotation_file.shape)    
annotation_file.to_csv(path_or_buf = OUTPUT_FILENAME, sep = ":", index = False)
