#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
import __init__

# 毕业练习题

class A:
    def __init__(self):
        self.__func()
        print(self.__func, '2')

    def __func(self):  # _A__func()
        print('in A')

    print(__func, '3')


class B(A):
    def __func(self):  # _B__func()
        print('in B')

    print(__func, '1')



print(abc.a)