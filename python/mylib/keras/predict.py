# -*- coding: utf-8 -*-
from __future__ import print_function
from operator import itemgetter
import sys
import cv2
import numpy as np
from networks import lenet
from mylib.tools import *

def mat_to_np(mat):
    img = mat.flatten().astype(np.float32)/255.0
    img = np.asarray(img)
    img = img.reshape((200, 200))
    img = img[np.newaxis, np.newaxis, :, :]
    return img

def predict_likelihoods(img, model):
    img_np = mat_to_np(mat=img)
    pred = model.predict(img_np, batch_size=128, verbose=0)
    likelihoods = pred[0]
    return likelihoods

def output(is_sorted_value=False, show_num=26):
    args = sys.argv
    hdf_path = '/home/abe/ga_font/cnn_model/multifont_20160813/train_weights.hdf5'
    model = lenet.LeNet.build(width=200, height=200, depth=1, classes=26, weight_path=hdf_path)
    alphs = make_alphabets()
    for (i, img_path) in enumerate(args):
        if i == 0:
            continue
        img = cv2.imread(img_path, -1)
        likelihoods = predict_likelihoods(img, model)
        print (img_path)
        zipped_alphs_likelihoods = zip(alphs, likelihoods)
        if is_sorted_value:
            zipped_alphs_likelihoods.sort(key=itemgetter(1), reverse=True)
        for (i, (alph, likelihood)) in enumerate(zipped_alphs_likelihoods):
            if i >= show_num:
                break
            print("{0}: {1:013.10f}%".format(alph, likelihood * 100))
        print ()

if __name__ == '__main__':
    output(True, 3)
