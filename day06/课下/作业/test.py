#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun
import os

#
# def dir_size(path):
#     if os.path.isdir(path):
#         sumsize = 0  #
#         name_lst = os.listdir(path)  # ['demo']
#         for name in name_lst:
#             full_path = os.path.join(path, name)
#             if os.path.isfile(full_path):
#                 sumsize += os.path.getsize(full_path)  # sum_size = 0+1200 = 1200
#             else:
#                 sumsize += dir_size(full_path)
#         return sumsize
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:
#         print('找不到文件')
#
# print(dir_size(r'E:\安全\Python22天'))

# def get_size(path):
#     if os.path.isdir(path):
#         sum_size = 0
#         li_dir = os.listdir(path)
#         li_dir = map(lambda n: os.path.join(path, n), li_dir)
#         for i in li_dir:
#             if os.path.isdir(i):
#                 sum_size += get_size(i)
#             if os.path.isfile(i):
#                 sum_size += os.path.getsize(i)
#         return sum_size
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:
#         print('找不到文件')
#
# path = r'E:\安全\Python22天'
# print(get_size(path))
