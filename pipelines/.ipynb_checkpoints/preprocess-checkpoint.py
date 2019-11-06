# This program preprocess the video. 
# Generate the frame image, to the sampling rate, and cropping required
# The frames images and the reference image will be padded to 256x256 and put together into a dir.

VIDEO_FILENAME = "dancing.mp4"
REFERENCE_IMG = "nikeman.jpg"
OUTPUT_DIR = "preprocess_out"
SIZE = 256
Y_MIN = 0
Y_MAX = 1
X_MIN = 0.2
X_MAX = 0.8
SAMPLING_RATE = 4 # sample the frames to 1:SAMPLING_RATE



import cv2
import os

def pad_square(img, size = 256):
    """
    desired = max(img.shape)
    delta_w = max(desired - img.shape[1],0)
    delta_h = max(desired - img.shape[0],0)
    top, bottom = int(delta_h/2), delta_h-int(delta_h/2)
    left, right = int(delta_w/2), delta_w-int(delta_w/2)
    color = [0, 0, 0]
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT)
    """
    img = cv2.resize(img, (size, size))
    
    
    return img

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

vidcap = cv2.VideoCapture(VIDEO_FILENAME)
success,image = vidcap.read()
count = 0
# read the frame images iteratively
while success: 
    
    if count%SAMPLING_RATE == 0:
        y_min = int(image.shape[0]*Y_MIN)
        y_max = int(image.shape[0]*Y_MAX)
        x_min = int(image.shape[1]*X_MIN)
        x_max = int(image.shape[1]*X_MAX)
        
        image = image[y_min:y_max,x_min:x_max]
        image = pad_square(image, size=SIZE)
        
        cv2.imwrite(OUTPUT_DIR+"/"+VIDEO_FILENAME.split(".")[0]+"_%d.jpg" % count, image)  
        
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
    
# process the reference image
image = cv2.imread(REFERENCE_IMG)
image = pad_square(image, size=SIZE)

cv2.imwrite(OUTPUT_DIR+"/"+REFERENCE_IMG, image)  


