#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import pickle
from conf import settings as cof
from core import course as co

class Course():  # 课程类
    def __init__(self, name, price, cycle, teacher):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.teacher = teacher


class Public(object):  # 公共类
    def show_courses(self):  # 查看所有课程
        with open(cof.course_file, mode='rb') as  f:
            print('序号:\t课程名\t课程价格\t课程周期\t老师')
            n = 1
            while True:
                try:
                    course = pickle.load(f)
                    tplt = '{0:<3}{1:<15}{2:<10}{3:<10}{4:<10}'
                    print(tplt.format(n, course.name, course.price, course.cycle, course.teacher))
                    n += 1
                except EOFError:
                    break

    def exit(self):  # 退出
        exit('bye')

