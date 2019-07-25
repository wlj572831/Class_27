#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# Creation time : 2019-7-18

# 4.写代码，有如下列表，请按照功能要求实现每一个功能
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
#
# # 请根据索引输出“Kelly”
# ke = li[2][1][1]
# print(ke)
#
# # 请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
# li[2][2] = li[2][2].upper()
# print(li)

# 5、有如下变量，请实现要求的功能
#
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
#
# # a.讲述元组的特性
# # (1). 可存放多个值，可嵌套元组、列表等其他数据类型
# # (2). 不可变，一旦创建，无法修改
# # (3). 有序，根据下标从0开始到
#
# # b. 请问tu变量中的第一个元素“alex”是否可被修改？
# # 不可以被修改,
#
# # c. 请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# # 'k2'是字典的键，对应的值是列表， 列表中元素可以被修改
# tu[1][2]['k2'].append('Seven')
# print(tu)
#
# # 请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# # 'k3'是字典的键，对应的值是元组，元组本身无法被修改，
# # 但是如果要改变'k3'对的值，可以重新创建一个元组与k3组成键值对
#
# value = list(tu[1][2]['k3'])
# value.append('Seven')
# tu[1][2]['k3'] = tuple(value)
# print(tu)

# 6.转换
# a. 将字符串s = “alex”转换成列表
# s = 'alex'
# li = list(s)
# print(li)

# b. 将字符串s = “alex”转换成元祖
# s = 'alex'
# tu = tuple('alex')
# print(tu)

# c. 将列表li = [“alex”, “seven”]转换成元组
# li = ['alex', 'seven']
# tu = tuple(li)
# print(tu)

# d. 将元组tu = (‘Alex’, “seven”)转换成列表
# tu = ('Alex', 'seven')
# li = list(tu)
# print(li)

# e. 将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
# li = ['alex', 'seven']
# dic = {}
# for i in range(len(li)):
#     dic[li[i]] = i+10
# print(dic)

# 7. 元素分类
# 有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，
# 将小于66的值保存至第二个key的值中。
# 即：{‘k1’:大于66的所有值, ‘k2’:小于66的所有值}。（编程题）

# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1': [], 'k2': []}
#
# for i in li:
#     if i > 66:
#         dic['k1'].append(i)
#     elif i < 66:
#         dic['k2'].append(i)
#
# print(dic)

# 8.在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]。（编程题）
#
# li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
# max_num = max(li) #方法1:
# 方法2:
# max_num = 0
# for i in li:
#     if max_num < i:
#         max_num = i
#
# print('最大值为：', max_num)

# 9. 在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值的数
# li = [-100,1,3,2,7,6,120,121,140,23,411,99,243,33,85,56]。（编程题）

# li = [-100, 1, 3, 2, 7, 6, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
# avg = (max(li) + min(li)) / 2  # 计算平均值
# differ = max(li) - min(li)
# result = 0
#
# for i in li:
#     if abs(avg - i) < differ:  # 将每个元素与平均值的差的绝对值和已经获取的差值比对
#         differ = abs(avg - i)
#         result = i
# print(result)

# 10. 利用for循环和range输出9 * 9乘法表 。（编程题）

for x in range(1, 10):
    for y in range(1, x + 1):
        print('%s×%s=%s' % (x, y, x * y), end='|')
    print()

# 11. 求100以内的素数和。（编程题）

# prime = [2, 3] #存储素数的集合
# for i in range(4,101):
#     for j in  range(2,i):
#         if i%j == 0:
#             break
#     else:
#         prime.append(i)
# print('100以内素数集合是:', prime)

# 12、请说明python2 与python3中的默认编码是什么？
# python2 是 ASCII码
# python3 是 UTF-8

# 13、为什么会出现中文乱码？你能列举出现乱码的情况有哪几种？
# 1. 写入和读取时字符编码不同

# 14、分别写出在windows和mac上用py2输出中文怎么做？

# 15、任一个英文的纯文本文件，统计其中的每个单词出现的个数，注意是每个单词。。
