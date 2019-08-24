#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wang_liu_jun


class Foo:
    def func(self):
        print('in father')


class Son(Foo):
    def func(self):
        print('in son')

s = Son()
s.func()
# 请说出上面一段代码的输出并解释原因？

# in A
# in A
# in B
