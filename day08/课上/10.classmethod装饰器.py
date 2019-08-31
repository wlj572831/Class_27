#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time

class A:
    @classmethod
    def func(cls):
        print(cls)

    print('')


class B(A):
    def func1(self): pass


b = B()
b.func()
print(B, A)
