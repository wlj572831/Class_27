#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# CreateTime： 2019-08-13

# 1. locals /globals 查看当前作用域的局部变量和全局变量

# name = 'alex'
#
#
# def func():
#     a = 1
#     b = 2
#     print(locals())
#     print(globals())
#
#
# def func1():
#     c = 3
#     d = 4
#     print(locals())
#     print(globals())
#
#
# func()
# func1()

# 2. eval/exec 把字符串用按照python代码解释
#   exec 执行但没有返回值
#   eval 执行，接受输出结果
def func():
    print('1234')

# eval会输出，会返回
ret = eval('func()')
# print(ret)

print(exec('func()'))
# print(ret)