#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊


class abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.__str__())

    def __str__(self):
        return self.name
    # def __repr__(self):
    #     return '%s,%s' % (self.name, self.age)


alex = abc('ale', 55)
print(alex)
