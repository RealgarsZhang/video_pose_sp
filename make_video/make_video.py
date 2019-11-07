GAN_OUT_DIR = "gan_out"
GIF_NAME = "nikeman-walking.gif"
FPS = 2
#SIZE = 256

import cv2
import os
import numpy as np



img_fns = []
for fn in os.listdir(GAN_OUT_DIR):
    if fn.split(".")[-1] not in ("png","jpg","jpeg"):
        continue
    img_fns.append(fn)

img_fns.sort(key = lambda fn: int(fn.split(".")[0].split("_")[-1]))

from PIL import Image

# Create the frames
frames = []
for i in img_fns:
    new_frame = Image.open(GAN_OUT_DIR+"/"+i)
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



    