# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import numpy as np
from keras.utils import np_utils
# cPickleのほうが高速らしい
# 参考:http://ja.pymotw.com/2/pickle/
try:
    import cPickle as pkl
except:
    import pickle as pkl

# train.txtのようなファイルから
# 画像データ、正解ラベルをimage_list,label_listに
# 参考:http://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
def filelist_to_list(filename):
    image_list, label_list = [], []
    # 行数をゲット
    with open(filename, 'r') as file:
        max_count = sum(1 for line in file)
    file = open(filename, 'r')
    for count, readline in enumerate(file):
        if count % 1000 == 0:
            print ('making list... ({0}/{1})'.format(count, max_count))
        readline = readline.rstrip()
        readline_sp = readline.split(' ')
        img = cv2.imread(readline_sp[0], -1)
        image_list.append(img.flatten().astype(np.float32)/255.0)
        label_list.append(int(readline_sp[1]))
    file.close()
    pic_size = img.shape
    print('converting into numpy format...')
    image_list = np.asarray(image_list)
    label_list = np.asarray(label_list)
    print('reshaping...')
    image_list = image_list.reshape((image_list.shape[0], pic_size[0], pic_size[1]))
    print('adding new shape...')
    image_list = image_list[:, np.newaxis, :, :]
    print('converting 1-of-k format...')
    label_list = np_utils.to_categorical(label_list, 26)
    return image_list, label_list

def twolist_to_pkl(list1, list2, filename):
    with open(filename, 'w') as file:
        pkl.s_dump((list1, list2), file)

def pkl_to_twolist(filename):
    with open(filename, 'r') as file:
        list1, list2 = pkl.s_load(file)
    return list1, list2

# train.txtを与えたらtrain.pklが作成される
def filelist_to_pkl(filename):
    filename_sp1 = filename.split('/')
    filename_sp2 = filename_sp1[-1].split('.')
    filename_pkl = filename_sp2[0] + '.pkl'
    print (filename_pkl)
    image_list, label_list = filelist_to_list(filename)
    print('dumping...')
    twolist_to_pkl(image_list, label_list, filename_pkl)

