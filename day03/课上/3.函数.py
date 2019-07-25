#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# dic = {'k1': 'v1', 'k2': 'v2'}
# li = [1, 2, 3, 4, 5]
#
#
# def mylen(seq):
#     i = 0
#     for j in seq:
#         i += 1
#     return i
#
#
# def compare(a, b):
#     if mylen(a) > mylen(b):
#         return a, mylen(a)
#     else:
#         return b, mylen(b)
#
#
# result = compare(dic, li)
# print('元素:%s 长度:%s' % result)

# def sum(a,b,c,*args,d='alex'):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#
# sum(1,2,3,4,d=5,6)

# 把list 拆分开作为位置参数依次传递给a b c
# def func(a,b,c):
#     print(a,b,c)
#
# list = [1,2,3]
# func(*list)

# 把dic 拆分开作为默认参数依次传递给函数，类似于
# func(k1='v1', 'k2'='v2', 'k3'='v3')
# def func(**kwargs):
#     print(kwargs)
#
# dic = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
# func(**dic)

# a = 1
# def fun1():
#     print(a)
#     def fun2():
#         print(a)
#         def fun3():
#             nonlocal a
#             a+=1
#             print(a)
#         fun3()
#     fun2()
# fun1()

# readme
# python 版本
#
