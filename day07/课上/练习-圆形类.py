#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def peri(self):
        peri = 2 * pi * self.r
        return peri

    def area(self):
        area = pi * (self.r ** 2)
        return area


class Ring:
    def __init__(self, big_r, li_r):
        self.big_r = big_r
        self.li_r = li_r
        self.r1 = Circle(self.big_r)
        self.r2 = Circle(self.li_r)

    def peri(self):
        sum_ = self.r1.peri() + self.r2.peri()
        return sum_

    def area(self):
        sum_ = self.r1.area() - self.r2.area()
        return sum_


yuan1 = Ring(20, 10)
print(yuan1.peri(), yuan1.area())
