#GAN_OUT_DIRS = ["gan_out_bdj_yang_new", "gan_out_bdj_yang", "gan_out_bdj_tachi1","yang"]
#GIF_NAMES = ["bdj_yang_new.gif", "bdj_yang.gif","bdj_taichi1.gif","yang.gif"]
GAN_OUT_DIRS = ["gan_out"]
GIF_NAMES = ["output.gif"]
FPS = 2
SIZE = 128
#SIZE = 256

import cv2
import os
import numpy as np


for i in range(len(GAN_OUT_DIRS)):
    GAN_OUT_DIR = GAN_OUT_DIRS[i]
    GIF_NAME = GIF_NAMES[i]
    img_fns = []
    for fn in os.listdir(GAN_OUT_DIR):
        if fn.split(".")[-1] not in ("png","jpg","jpeg") or len(fn.split('.')[0].split('_'))<2:
            continue
        img_fns.append(fn)

    img_fns.sort(key = lambda fn: int(fn.split(".")[0].split("_")[-1]))

    from PIL import Image

    # Create the frames
    frames = []
    for i in img_fns:
        new_frame = Image.open(GAN_OUT_DIR+"/"+i)
        new_frame = new_frame.resize((SIZE,SIZE))
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save(GIF_NAME, format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=300, loop=0)
"""

img = cv2.imread(GAN_OUT_DIR+"/"+img_fns[0])
height , width , layers =  img.shape
video = cv2.VideoWriter(VIDEO_NAME,-1,FPS,(width,height))

for fn in img_fns:
    img = cv2.imread(GAN_OUT_DIR+"/"+fn)
    video.write(img)

cv2.destroyAllWindows()
video.release() 
"""    



    