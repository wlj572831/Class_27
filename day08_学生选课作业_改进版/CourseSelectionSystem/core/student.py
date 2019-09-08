#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun
import pickle
import os
from conf import settings as cof
from core import course as co
from core.course import Public as pu


class Student(co.Public):  # 学生类
    # 存储学生菜单
    menu_list = [
        ('查看可选课程', 'opt_course'),
        ('选择课程', 'select_course'),
        ('查看所选课程', 'show_selected_course'),
        ('退出', 'exit')
    ]

    def __init__(self, name):
        self.name = name
        self.course_list = []

    @classmethod
    def init(cls, username):
        with open(cof.select_course, mode='rb') as  f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == username:
                        return stu_obj
                except EOFError:
                    break

    def opt_course(self):  # 查看可选课程
        co.Public.show_courses(self)

    def select_course(self):  # 选择课程
        pu.show_courses(self)
        choice = int(input('请输入要选择的序号:').strip())
        obj_iter = pu.read_file(cof.course_file)
        for index, obj in enumerate(obj_iter, 1):  # 根据输入的序号添加课程对象
            if choice == index:
                self.course_list.append(obj)
                print('用户%s，添加%s课程成功' % (self.name, obj.name))
        tmp = os.path.dirname(cof.select_course) + '/tmp'
        with open(cof.select_course, mode='rb') as f1, open(tmp, mode='wb') as f2:
            while True:
                try:
                    obj = pickle.load(f1)
                    if obj.name == self.name:
                        obj = self
                    pickle.dump(obj, f2)
                except EOFError:
                    break
        os.remove(cof.select_course)
        os.rename(tmp, cof.select_course)

    def show_selected_course(self):  # 查看已选课程
        obj_iter = pu.read_file(cof.select_course)
        for obj in obj_iter:
            if self.name == obj.name:
                for index, i in enumerate(obj.course_list, 1): print(index, i.name)
