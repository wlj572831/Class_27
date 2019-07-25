#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# Creation time : 2019-7-18

# 1.请用代码实现：利用下划线将列表的每一个元素拼接成字符串
# li = ['alex', 'eric', 'rain']
# li = '_'.join(li)
# print(li)

# 2.查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
# 2.1 列表
# li = ["alec ", " Aric ", " Alex", "Tony", "rain"]
# new_list = []   #记录'a' 'A'开头'c'结尾的元素
#
# for i in range(len(li)):
#     li[i] = li[i].strip()
#     if li[i].upper().startswith('A') and li[i].endswith('c'):
#         new_list.append(li[i])
# print(li)
# print(new_list)
