#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import sys
import pickle
from core import student as stu
from core import course as co
from conf import settings as cof


class Manager(co.Public):  # 管理员
    menu_list = [
        ('创建课程', 'create_course'),
        ('查看所有课程', 'show_courses'),
        ('创建学生账号', 'create_stu'),
        ('查看所有学生', 'show_students'),
        ('查看所有选课情况', 'show_sit'),
        ('退出程序', 'exit')]  # 管理员菜单

    def __init__(self, name):
        self.name = name

    @classmethod
    def init(cls, username):
        return cls(username)  # 返回实例化对象

    def pickle_dump(self, obj, filename):  # dump函数
        with open(filename, mode='ab') as f:
            pickle.dump(obj, f)

    def create_course(self):
        name = input('课程名:')
        price = input('课程价格:')
        cycle = input('课程周期：')
        teacher = input('老师：')
        course = co.Course(name, price, cycle, teacher)  # 创建新的课程对象
        self.pickle_dump(course, cof.course_file)  # 把课程对象存入课程文件中

    def create_stu(self):  # 创建学生账号
        user = input('请输入学生用户名:').strip()
        pwd = input('请输入密码:').strip()
        cof_pwd = input('确认密码:').strip()
        if pwd == cof_pwd and user and pwd:
            with open(cof.user_file, 'a', encoding='utf-8') as f:
                f.write('\n%s|%s|%s' % (user, pwd, 'Student'))
                print('用户%s创建成功' % user)
            stu_obj = stu.Student(user)
            self.pickle_dump(stu_obj, cof.select_course)
        else:
            print('帐号密码格式不符合')

    def show_students(self):  # 查看所有学生
        self.pickle_load(cof.select_course)

    def show_sit(self):  # 查看所有选课情况
        for index, stu_obj in enumerate(self.pickle_load_generator(cof.select_course)):
            print(index, repr(stu_obj))
