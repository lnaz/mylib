# -*- coding: utf-8 -*-
import os
import glob
from datetime import datetime

# ディレクトリの存在の確認し，
# 存在しなければディレクトリ作成
# -pオプションでまとめてディレクトリ作成
def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# ディレクトリ名を正しく直す
# 'hoge/hoge' => 'hoge/hoge/'
def correct_dir_path(path):
    path_sp = path.split('/')
    if path_sp[-1] == '':
        return path
    return path + '/'

# アルファベット大文字を数字に
# A => 0, B => 1, ..., Z => 26
def a2n(alph):
    return ord(alph) - 65

# リストの要素をパスの形式にして返す
# ['foo', 'bar'] => 'foo/bar/'
def list2path(ls):
    st = ''
    for l in ls:
        st += str(l) + '/'
    return st

# 連番ディレクトリ作成
# 作成したディレクトリのパスを返す
# if 'foo/bar0/'が存在しない
#   'foo/bar/' => 'foo/bar0/'を作成，パスを返す
# if 'foo/bar0/'が存在
#   'foo/bar' => 'foo/bar1'を作成，パスを返す
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
        num_path = list2path(num_path_list)
        if not os.path.exists(num_path):
            os.makedirs(num_path)
            break
    return num_path

def make_date_dir(path):
    cor_path = correct_dir_path(path)
    cor_path_sp = cor_path.split('/')
    dir_name = cor_path_sp[-2]
    del cor_path_sp[-2:]
    date_path_list = cor_path_sp[:]
    now_str = datetime.now().strftime('%Y%m%d%H%M%S')
    date_path_list.append(dir_name + '_' + now_str)
    date_path = list2path(date_path_list)
    os.makedirs(date_path)
    return date_path

    

# アルファベット大文字の配列を作成
# => [A, B, ..., Z]
def make_alphabets():
    alphs = [chr(i + 65) for i in range(26)]
    return alphs

# パスのディレクトリ内のファイルのパスを取得
# findnameでワイルドカード検索可能
# 'foo/bar/', '*.png' => 'foo/bar/'内のpng画像のパスのリストを返す
def get_filepaths(dirpath, findname):
    cor_dirpath = correct_dir_path(dirpath)
    filepaths = glob.glob(cor_dirpath + findname)
    return filepaths

# ファイル名リストにadditionを追加して返す
# 'foo.png', '_bar' => 'foo_bar.png'
def set_filepaths(filepaths, addition):
    added_filepaths = []
    for path in filepaths:
        path_sp = path.split('.')
        ext = '.' + path_sp[-1]
        added_path = path.rstrip(ext)
        added_path += addition
        added_path += ext
        added_filepaths.append(added_path)
    return added_filepaths

# ファイル名にadditionsリストの順番通り追加して返す
# ['foo.png', 'bar.png'], ['_A', '_B']
#   => ['foo_A.png', 'bar_B.png']
def set_special_filepaths(filepaths, additions):
    added_filepaths = []
    for (path, addition) in zip(filepaths, additions):
        path_sp = path.split('.')
        ext = '.' + path_sp[-1]
        added_path = path.rstrip(ext)
        added_path += addition
        added_path += ext
        added_filepaths.append(added_path)
    return added_filepaths
    
