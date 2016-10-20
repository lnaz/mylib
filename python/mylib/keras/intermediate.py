# -*- coding: utf-8 -*-
from __future__ import print_function
from keras import backend as K
# from networks import lenet
from mylib.keras import predict
import numpy as np
import cv2
from mylib.tools import *
from mylib.cv2_tools import *

def convert_intermediate_to_img(layer_np, range_num):
    img = layer_np / range_num * 128
    img += 127
    return img

def get_intermediate_layer(img, model, layer_num):
    img_np = predict.mat_to_np(mat=img)
    print (img_np.shape)
    get_layer_output = K.function([model.layers[0].input], [model.layers[layer_num].output])
    layer_output = get_layer_output([img_np])[0]
    return layer_output[0]

def save_intermediate_layers(img, model, layer_nums, dst_dir_path):
    for layer_num in layer_nums:
        dst_l_dir_path = dst_dir_path + str(layer_num) + '/'
        make_dir(dst_l_dir_path)
        layer_output = get_intermediate_layer(img, model, layer_num)
        range_num = max(np.max(layer_output), abs(np.min(layer_output)))
        for i, layer_np in enumerate(layer_output):
            layer_img = convert_intermediate_to_img(layer_np, range_num)
            dst_l_img_path = dst_l_dir_path + str(i) + '.png'
            cv2.imwrite(dst_l_img_path, layer_img)

def debug():
    img = cv2.imread('/home/abe/font_dataset/png_6628_200x200/E/69.png', -1)
    hdf_path = '/home/abe/ga_font/cnn_model/multifont_20160813/train_weights.hdf5'
    model = lenet.LeNet.build(width=200, height=200, depth=1, classes=26, weight_path=hdf_path)
    save_intermediate_layers(img, model, [2, 5], make_dir('output_debug/E_69/'))

if __name__ == '__main__':
    # user_input()
    debug()
