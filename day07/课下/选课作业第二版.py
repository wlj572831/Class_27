#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：WangLiuJun
import pickle
import sys
import os

course_file = r'file/course'  # 存储课程
user_file = r'file/user'  # 存储用户
select_course = r'file/select_course'  # 已选课程


class Public(object):
    def show_courses(self):  # 查看所有课程
        with open(course_file, mode='rb') as  f:
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


class Course():  # 课程类
    def __init__(self, name, price, cycle, teacher):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.teacher = teacher


class Student(Public):  # 学生类
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
    def init(username):
        with open(select_course, mode='rb') as  f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == username:
                        return stu_obj
                except EOFError:
                    break

    def opt_course(self):  # 查看可选课程
        Public.show_courses(self)

    def select_course(self):  # 选择课程
        Public.show_courses(self)
        choice = int(input('请输入要选择的序号:').strip())
        n = 1
        with open(course_file, 'rb') as  f:
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
        tmp = os.path.dirname(select_course) + '/tmp'
        with open(select_course, mode='rb') as f1, open(tmp, mode='wb') as f2:
            # with open(select_course, mode='rb'):
            while True:
                try:
                    obj = pickle.load(f1)
                    if obj.name == self.name:
                        obj = self
                    pickle.dump(obj, f2)
                except EOFError:
                    break
        os.remove(select_course)
        os.rename(tmp, select_course)

    def show_selected_course(self):  # 查看已选课程
        with open(select_course, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if usr == obj.name:
                        for i in obj.course_list:
                            print(i.name)
                except EOFError:
                    break


class Manager(Public):  # 管理员

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
        course = Course(name, price, cycle, teacher)  # 创建新的课程对象
        with open(course_file, 'ab') as f:
            pickle.dump(course, f)
            print('课程创建成功')  # 创建课程

    def create_stu(self):  # 创建学生账号
        user = input('请输入学生用户名:').strip()
        user_list = list(map(lambda n: n[0], list(read_usr())))  # 取出所有的用户
        if user in user_list:
            print('用户名已存在')
            return
        pwd = input('请输入密码:').strip()
        cof_pwd = input('确认密码:').strip()
        if pwd == cof_pwd and user and pwd:
            with open(user_file, 'a', encoding='utf-8') as f:
                f.write('\n%s|%s|%s' % (user, pwd, 'Student'))
                print('用户%s创建成功' % user)
            stu = Student(user)
            with open(select_course, mode='ab') as f:
                pickle.dump(stu, f)
        else:
            print('帐号密码格式不符合')

    def show_students(self):  # 查看所有学生
        with open(select_course, mode='rb') as f:
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
        with open(select_course, 'rb') as  f:
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


# 读取用户,
def read_usr():
    with open(user_file, mode='r', encoding='utf-8') as f:
        for line in f:
            if line:
                usr, pwd, role = line.strip().split('|')
                yield usr, pwd, role


# 登录函数
def login():
    input_usr = input('请输入用户名:').strip()
    input_pwd = input('请输入密码:').strip()
    with open(user_file, mode='r', encoding='utf-8') as f:
        for line in f:
            if line:
                usr, pwd, role = line.strip().split('|')
                if usr == input_usr and pwd == input_pwd:
                    print('%s登录成功,欢迎您%s' % (role, usr))
                    return usr, pwd, role
        else:
            print('账号密码错误')
            return None


if __name__ == '__main__':
    ret = login()
    if ret:
        while True:
            usr, role = ret[0], ret[2]
            cls = getattr(sys.modules[__name__], role)
            obj = cls.init(usr)
            print('-' * 40)
            for index, i in enumerate(cls.menu_list, 1):  # 遍历列表中菜单
                print(index, i[0])
            print('-' * 40)
            choice = int(input('请选择序号:').strip())
            func = obj.menu_list[choice - 1][1]  # 取出选择序号对应的方法名，字符串类型
            getattr(obj, func)()  # 执行对象中的方法
