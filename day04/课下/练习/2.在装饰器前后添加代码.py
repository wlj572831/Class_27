#!/usr/bin/python
# coding:utf-8
# createtime: 2019-8-1

# 2.
# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
# 编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’

# def wapper(funcname):
#     def inner():
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         funcname()
#         print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
#
#     return inner
#
# @wapper
# def func():
#     print('this is a func')
#
# func()

#4.