#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# CreateTime：


from math import pi


# 圆形类
class Circle:
    def __init__(self, r):
        self.r = r

<<<<<<< HEAD

s = Son()
s.func()
# 请说出上面一段代码的输出并解释原因？
=======
    def peri(self):  # 周长
        peri = 2 * pi * self.r
        return peri
>>>>>>> b76ef598e2a14dd66ceee6fb5202f9fb9bd59f0a

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
