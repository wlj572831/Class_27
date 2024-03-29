#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
from math import pi


# 圆形类
class Circle:
    def __init__(self, r):
        self.r = r

    def peri(self):  # 周长
        peri = 2 * pi * self.r
        return peri

    def area(self):  # 面积
        area = pi * (self.r ** 2)
        return area


# 圆环类
class Ring:
    def __init__(self, big_r, li_r):
        self.big_r = big_r
        self.li_r = li_r
        self.r1 = Circle(self.big_r)
        self.r2 = Circle(self.li_r)

    def peri(self):
        '''圆环周长'''
        sum_ = self.r1.peri() + self.r2.peri()
        return sum_

    def area(self):
        '''圆环面积'''
        sum_ = self.r1.area() - self.r2.area()
        return sum_


yuan1 = Ring(20, 10)
print(yuan1.peri(), yuan1.area())
