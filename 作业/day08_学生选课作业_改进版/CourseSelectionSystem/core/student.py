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
        self.flag = False

    def __str__(self):
        return self.name

    def __repr__(self):
        course_name_lst = [course.name for course in self.course_list]
        return '%s: %s' % (self.name, '|'.join(course_name_lst))

    @classmethod
    def init(cls, username):  # 取出之前的的学生对象
        for stu_obj in cls.pickle_load_generator(cof.select_course):
            if stu_obj.name == username:
                obj = stu_obj
                obj.flag = False
                return obj

    def opt_course(self):  # 查看可选课程pickle_load
        self.show_courses()

    def select_course(self):  # 选择课程
        self.show_courses()
        choice = int(input('请输入要选择的序号:').strip())
        count = 1
        courses_name = [course.name for course in self.course_list]
        for couse in self.pickle_load_generator(cof.course_file):
            if choice == count and couse.name not in courses_name:
                self.course_list.append(couse)  # 添加课程
                print('%s 已成功选择 %s 科目' % (self.name, couse.name))
                self.flag = True
                break
            elif count == choice:
                print('已经选过这个课程')
                break
            count += 1
        else:
            print('您输入了错误的序号,没有找到对应的课程')

    def show_selected_course(self):  # 查看已选课程
        for index, course in enumerate(self.course_list, 1):
            print(index, course.name)

    def exit(self):
        if self.flag == True:  # 如果学生进行了选课活动，对文件进行更改
            with open(cof.tmp, 'wb') as f2:
                for stu in self.pickle_load_generator(cof.select_course):
                    if stu.name == self.name:  # 判断这个学生对象是不是当前登陆学生
                        pickle.dump(self, f2)  # 如果是,把现在选课之后的信息写入文件
                    else:  # 不是
                        pickle.dump(stu, f2)  # 将原本学生的信息原封不动的写入新的文件
            os.remove(cof.select_course)
            os.rename(cof.tmp, cof.select_course)
        exit('bye')
