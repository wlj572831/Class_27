#!/usr/bin/python
# -*- coding:utf-8 -*-
# Creat Time: 2019-08-04


lis = [1, 2, 3, 4, [5, 6, 7, 8, [6, 3, 2, 1]]]

# 求所有元素的和
# sum_num = 0
#
# def sum_(lis):
#     global sum_num
#     for i in lis:
#         if type(i) is list:
#             sum_(i)
#         else:
#             sum_num += i
#
# sum_(lis)
# print(sum_num)
#

# 2. 非global版本
# def sum_(lis):
#     sum_num = 0
#     for i in lis:
#         if type(i) is list:
#             summ = sum_(i)
#             sum_num += summ
#         else:
#             sum_num += i
#     return sum_num
#
#
# a = sum_(lis)
# print(a)


# 3. 阶乘
# 8! = 8*7*6*5*4*3*2*1


# 4. 递归函数-二分查找
