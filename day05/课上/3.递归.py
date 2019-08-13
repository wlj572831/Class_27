#!/usr/bin/python
# -*- coding:utf-8 -*-
# Creat Time: 2019-08-04

# 1. 递归
# 自己调用自己
# 最大的递归深度 1000次 RecursionError
from sys import setrecursionlimit

# def wahaha():
#     print('haha')
#     wahaha()
#
# wahaha()

# lis = [1, 2, 3, 4, [5, 6, 7, 8, [6, 3, 2, 1]]]


# 2. 利用递归求所有元素的和
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

# 2.1. 非global版本
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

# def product(num):
#     if num == 1:
#         return 1
#     return num * product(num - 1)
#
# print(product(5))

# 4. 递归函数-二分查找
#
# li = [1, 5, 4, 7, 9, 10, 15, 20, 66, 77, 99, 88]
# li.sort()
#
#
# def find(li, num, start=0, end=0):
#     start = start if start else 0
#     end = end if end else len(li) - 1
#     mid = (end - start) // 2 + start
#     if start > end:
#         return None
#     if num > li[mid]:
#         find(li, num, mid + 1, end)
#     elif num < li[mid]:
#         find(li, num, start, mid - 1)
#     elif num == li[mid]:
#         return mid
#
#
# print(find(li, 5))

# 5.递归-三级菜单
# menu_dic = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {}, '网易': {}, 'Google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {}, '汽车之家': {}, 'youku': {}
#             },
#             '上地:': {
#                 '百度:': {}, '快手': {}, '小米': {}
#             }
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': '', '北航': {}},
#             '天通苑': {},
#             '回龙观': {}
#         },
#         '朝阳': {},
#         '东城': {}
#     },
#     '上海': {},
#     '河南': {},
# }
#
#
# def menu(dic):
#     while True:
#         for i in dic:
#             print(i)
#         choice = input('请选择:').strip()
#         if choice.upper() == 'B':
#             return  # 返回上一层
#         elif choice in dic:
#             if dic[choice]:
#                 menu(dic[choice])
#             else:
#                 print('已是最底层')
#         else:
#             print('指令不正确')
#
#
# menu(menu_dic)
