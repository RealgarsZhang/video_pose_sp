# This program generates .npy for semantic parsing from sp_out, and the two example.txt files.

# For LIP dataset, the annotation rule is like the following:
"""
0.background
1.Hat
2.Hair
3.Glove
4.Sunglasses
5.UpperClothes
6.Dress
7.Coat
8.Socks
9.Pants
10.Jumpsuits
11.Scarf
12.Skirt
13.Face
14.Left-arm
15.Right-arm
16.Left-leg
17.Right-leg
18.Left-shoe
19.Right-shoe
"""
# Sijie et al uses the following order: background, face, hair, upper clothes, pants, skirt, left/right arm, left/right leg

LIP_WORDS = [
"background",
"hair",#"hat",
"hair",
"Glove",
"Sunglasses",
"UpperClothes",
"Dress",
"upperclothes",#"Coat",
"Socks",
"Pants",
"Jumpsuits",
"Scarf",
"Skirt",
"Face",
"Leftarm",
"Rightarm",
"Leftleg",
"Rightleg",
"Leftshoe",
"Rightshoe" 
]

SPT_WORDS = ["background", "face", "hair", "upperclothes", "pants", "skirt", "leftarm","rightarm", "leftleg","rightleg"]

from collections import defaultdict
SPT_DIC = defaultdict(int)
for i in range(len(SPT_WORDS)):
    SPT_DIC[SPT_WORDS[i].lower()] = i

for i in range(len(LIP_WORDS)):
    LIP_WORDS[i] = LIP_WORDS[i].lower()

print("LIP_WORDS:")
print(LIP_WORDS)
print("SPT_DIC:")
print(SPT_DIC)

SP_OUT_DIR = "sp_out"
PREPROCESS_OUT_DIR = "preprocess_out"
REFERENCE_IMG = "nikeman.jpg"
DST_DIR = "parsing"
A_EXAMPLE_TXT = "test_A_example.txt" # This file indicates the images which provide appearances
B_EXAMPLE_TXT = "test_B_example.txt" # Indicates the GT images for result. The GT is no use for us. But this is necessary for running the model

import os
import numpy as np


# put the semantic parsing to the format required by SPT
print("Remapping semantic parsing...Print the means:")
if not os.path.exists(DST_DIR):
    os.makedirs(DST_DIR)
    
for filename in os.listdir(SP_OUT_DIR):
    if filename.split(".")[-1]!="npy":
        continue
        
    src_sp = np.load(SP_OUT_DIR+"/"+filename)
    dst_sp = np.zeros(src_sp.shape, dtype = int)
    for i in range(src_sp.shape[0]):
        for j in range(src_sp.shape[1]):
            #print(src_sp[i,j])
            word = LIP_WORDS[src_sp[i,j]]
            dst_sp[i,j] = SPT_DIC[word]
            
    print(np.mean(dst_sp))
    np.save(DST_DIR+"/"+filename, dst_sp)
    
# generate the two example.txt files
print("Generate the example.txt files")
fa = open(A_EXAMPLE_TXT,"w")
fb = open(B_EXAMPLE_TXT,"w")
for filename in os.listdir(PREPROCESS_OUT_DIR):
    if filename.split(".")[-1]!="jpg":
        continue 
    fa.write("./imgs/"+REFERENCE_IMG+'\r\n')
    fb.write("./imgs/"+filename+'\r\n')
    
fa.close()
fb.close()
    
    

    

    
            


