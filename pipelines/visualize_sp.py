import numpy as np
from PIL import Image

sp_path = "sp_out/walking_0.npy"
palette_idx = np.array([[0, 0, 0], [0, 255, 255], [255, 0, 255], [255, 255, 0], [255, 170, 255], [255, 255, 170], [170, 255, 255], [85, 255, 255], [85, 170, 255], [105, 45, 190],
              [170, 105, 255], [170, 255, 85], [255, 170, 85], [255, 85, 170],  [85, 255, 85], [0, 255, 85], [255, 0, 85], [255, 85, 85], [0, 85, 255], [85, 85, 255]])



sp = np.load(sp_path)
result = np.zeros(shape = (sp.shape[0], sp.shape[1], 3))

for i in range(sp.shape[0]):
    for j in range(sp.shape[1]):
        result[i][j] = palette_idx[sp[i][j]]
        
result = result.astype(np.uint8)
image_pil = Image.fromarray(result)
image_pil.save("visual.png")
        