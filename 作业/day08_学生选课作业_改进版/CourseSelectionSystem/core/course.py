#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import pickle
from conf import settings as cof


class Course:  # 课程类
    def __init__(self, name, price, cycle, teacher):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.teacher = teacher

    def __str__(self):  # 直接调用对象时，返回各个属性
        return '%10s %10s %10s %10s' % (self.name, self.price, self.cycle, self.teacher)


class Public(object):  # 公共类
    def show_courses(self):  # 查看所有课程
        self.pickle_load(cof.course_file)

    @staticmethod
    def pickle_load_generator(filename):  # pickle对象生成器
        with open(filename, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    def pickle_load(self, filename):  # 用于显示课程
        for index, obj in enumerate(self.pickle_load_generator(filename), 1):
            print(index, obj)

    def exit(self):  # 退出
        exit('bye')
