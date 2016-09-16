# -*- coding: utf-8 -*-
import os

# ディレクトリが存在しない場合のみ作成
def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# ディレクトリ名を正しく直す
# 'hoge/hoge' to 'hoge/hoge/'
def correct_dir_path(path):
    path_sp = path.split('/')
    if path_sp[-1] == '':
        return path
    return path + '/'

# アルファベット大文字を数字に
# Aから0,1...
# 'A' to 0
def a2n(alph):
    return ord(alph) - 65

# 文字列リストを連結して返す
def list2str(ls):
    st = ''
    for l in ls:
        st += str(l) + '/'
    print st
    return st

# 連番ディレクトリ作成
# 作成したディレクトリのパスを返す
def make_num_dir(path):
    cor_path = correct_dir_path(path)
    cor_path_sp = cor_path.split('/')
    dir_name = cor_path_sp[-2]
    del cor_path_sp[-2:]
    i = -1
    while(True):
        i += 1
        num_path_list = []
        num_path_list = cor_path_sp[:]
        num_path_list.append(dir_name + str(i))
        num_path = list2str(num_path_list)
        if not os.path.exists(num_path):
            os.makedirs(num_path)
            break
    return num_path

# アルファベット軍の配列を作成
def make_alphabets():
    alphs = [chr(i + 65) for i in xrange(26)]
    return alphs
