#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun
import pickle
import os
from conf import settings as cof
from core import course as co

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
    def init(cls,username):
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
        co.Public.show_courses(self)
        choice = int(input('请输入要选择的序号:').strip())
        n = 1
        with open(cof.course_file, 'rb') as  f:
            while True:
                try:
                    obj = pickle.load(f)
                    if choice == n:
                        self.course_list.append(obj)
                        print('用户%s,添加课程%s成功' % (self.name, obj.name))
                        break
                    n += 1
                except EOFError:
                    print('没有要选的课程')
        tmp = os.path.dirname(cof.select_course) + '/tmp'
        with open(cof.select_course, mode='rb') as f1, open(tmp, mode='wb') as f2:
            # with open(select_course, mode='rb'):
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
        with open(cof.select_course, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if self.name == obj.name:
                        for i in obj.course_list:
                            print(i.name)
                except EOFError:
                    break
