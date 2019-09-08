#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import pickle
from conf import settings as cof
from core import course as co


class Course:  # 课程类
    def __init__(self, name, price, cycle, teacher):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.teacher = teacher


class Public(object):  # 公共类
    def show_courses(self):  # 查看所有课程
        obj_iter = Public.read_file(cof.course_file)
        for index, obj in enumerate(obj_iter, 1):  # for 循环取迭代器中的对象，enumerate获取下标
            print(index, obj.name, obj.price, obj.cycle, obj.teacher)

    @staticmethod
    def read_file(filename):
        with open(filename, mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except EOFError:
                    break

    def exit(self):  # 退出
        exit('bye')
