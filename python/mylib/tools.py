# -*- coding: utf-8 -*-
import os

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

