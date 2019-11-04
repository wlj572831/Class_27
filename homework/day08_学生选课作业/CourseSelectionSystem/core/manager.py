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

    def create_course(self):
        name = input('课程名:')
        price = input('课程价格:')
        cycle = input('课程周期：')
        teacher = input('老师：')
        course = co.Course(name, price, cycle, teacher)  # 创建新的课程对象
        with open(cof.course_file, 'ab') as f:
            pickle.dump(course, f)
            print('课程创建成功')  # 创建课程

    def create_stu(self):  # 创建学生账号
        user = input('请输入学生用户名:').strip()
        pwd = input('请输入密码:').strip()
        cof_pwd = input('确认密码:').strip()
        if pwd == cof_pwd and user and pwd:
            with open(cof.user_file, 'a', encoding='utf-8') as f:
                f.write('\n%s|%s|%s' % (user, pwd, 'Student'))
                print('用户%s创建成功' % user)
            stu_obj = stu.Student(user)
            with open(cof.select_course, mode='ab') as f:
                pickle.dump(stu_obj, f)
        else:
            print('帐号密码格式不符合')

    def show_students(self):  # 查看所有学生
        with open(cof.select_course, mode='rb') as f:
            n = 1
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s' % (n, obj.name))
                    n += 1
                except EOFError:
                    print('-' * 50)
                    break

    def show_sit(self):  # 查看所有选课情况
        with open(cof.select_course, 'rb') as  f:
            n = 1
            while True:
                try:
                    stu_obj = pickle.load(f)
                    print('%s 用户:%s\t' % (n, stu_obj.name), end='所选课程:')
                    for i in stu_obj.course_list: print(i.name, end='  ')
                    n += 1
                    print()
                except EOFError:
                    break
