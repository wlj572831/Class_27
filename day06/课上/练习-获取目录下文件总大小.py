#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
import os


# 1.目录下只有文件
# def get_size(path):
#     sum_size = 0
#     for i in os.listdir(path):
#         sum_size += os.path.getsize(os.path.join(path, i))
#     return sum_size


# path = r'E:\Class_27\Class_27\day06\课上'
# print(get_size(path))

# 2. 目录下文件和目录都有

def get_size(path):
    sum_size = 0
    li_dir = os.listdir(path)
    li_dir = map(lambda n: os.path.join(path, n), li_dir)
    for i in li_dir:
        if os.path.isdir(i):
            sum_size += get_size(i)
        if os.path.isfile(i):
            sum_size += os.path.getsize(i)
    return sum_size


path = r'E:\Class_27\Class_27'
print(get_size(path))
# 22978991447
# 22978991447
