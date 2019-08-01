#!/usr/bin/python
# coding:utf-8
# createtime: 2019-8-1

import time
from functools import wraps


# 1、整理装饰器的形成过程，背诵装饰器的固定格式

def wapper(funcname):
    # @wraps(funcname)
    def inner(*args, **kwargs):
        start = time.time()
        ret = funcname(*args, **kwargs)
        print(time.time() - start)
        return ret

    return inner


@wapper
def func(*args, **kwargs):
    '''装饰器'''
    print('this is a func')
    a, b = args[0], args[1]
    return a + b


print(func.__name__, id(func), func.__doc__)
# 函数名、函数名地址、函数注释
# 添加装饰器前 ：func 35385968 123
# 添加装饰器后 inner 11334328 None
# 装饰器内添加 wraps后

#
# 1.对扩展是开放的
#     为什么要对扩展开放呢？
#     我们说，任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改。
#     所以我们必须允许代码扩展、添加新功能。
#
# 2.对修改是封闭的
# 　　为什么要对修改封闭呢？
# 　　就像我们刚刚提到的，因为我们写的一个函数，很有可能已经交付给其他人使用了，
#     如果这个时候我们对其进行了修改，很有可能影响其他已经在使用该函数的用户。


# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
