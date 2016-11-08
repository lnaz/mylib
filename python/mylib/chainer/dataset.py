# -*- coding: utf-8 -*-
import cv2
import numpy as np

def filelist_to_list_for_dcgan(filename):
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
        img = img.astype(np.float32)
        image_list.append(img)
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
    return image_list
