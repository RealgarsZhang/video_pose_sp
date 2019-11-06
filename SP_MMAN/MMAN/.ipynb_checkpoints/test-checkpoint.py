PARSING_DIR = "sp_out"

import time
import os
from options.test_options import TestOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
from util.visualizer import Visualizer
from util import html
import numpy as np

if not os.path.exists(PARSING_DIR):
    os.makedirs(PARSING_DIR)

opt = TestOptions().parse()
opt.nThreads = 1   # test code only supports nThreads = 1
opt.batchSize = 1  # test code only supports batchSize = 1
opt.serial_batches = True  # no shuffle
opt.no_flip = True  # no flip

data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
model = create_model(opt)
visualizer = Visualizer(opt)
# create website
web_dir = os.path.join(opt.results_dir, opt.name, '%s_%s' % (opt.phase, opt.which_epoch))
webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.which_epoch))
# test
for i, data in enumerate(dataset):
    if i >= opt.how_many:
        break
    model.set_input(data)
    model.test()
    
    
    visuals = model.get_current_visuals()
    img_path = model.get_image_paths()
    visualizer.save_images(webpage, visuals, img_path)
    
    print('process image... %s' % img_path)
    
    img_path = model.get_image_paths()
    img_id = img_path[0].split("/")[-1].split('.')[0]
    raw_parsing = model.fake_B_GAN.data[0].cpu().float().numpy()
    parsing = np.zeros((raw_parsing.shape[1],raw_parsing.shape[2]),dtype = int)
    for i in range(raw_parsing.shape[1]):
        for j in range(raw_parsing.shape[2]):
            parsing[i][j] = np.argmax(raw_parsing[:,i,j])
    np.save(PARSING_DIR+"/"+img_id+".npy",parsing)
    
