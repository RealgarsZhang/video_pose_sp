import os
import numpy as np
import cv2


for filename in os.listdir("test_LIP_A"):
    if filename.split(".")[-1] in ("png","jpg"):
        fake_seg = np.zeros((10,10),dtype=int)
        cv2.imwrite("test_LIP_B/"+filename.split(".")[0]+".png", fake_seg)
    

    