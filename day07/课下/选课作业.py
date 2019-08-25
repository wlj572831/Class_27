#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：WangLiuJun
import pickle

course_file = r'file/course'  # 存储课程
user_file = r'file/user'  # 存储用户
select_course = r'file/select_course'  # 已选课程


class Public(object):
    def show_courses(self):  # 查看所有课程
        with open(course_file, mode='rb') as  f:
            print('课程名:\t课程价格\t课程周期\t老师')
            while True:
                try:
                    course = pickle.load(f)
                    print('%s\t%s\t%s\t%s' % (course.name, course.price, course.cycle, course.teacher))
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
    courses_list = []

    def __init__(self, name):
        self.name = name

    def opt_course(self):  # 查看可选课程
        Public.show_courses(self)

    def select_course(self):  # 选择课程
        Public.show_courses(self)
        with open(select_course, 'ab') as f1:
            course = input('请选择要学习课程名字:')
            if course in Student.courses_list:
                print('课程已存在')
            else:
                Student.courses_list.append(course)
                print(Student.courses_list, self.name)
                pickle.dump({self.name: Student.courses_list}, f1)
                print('用户%s,添加课程%s成功' % (self.name, course))

    def show_selected_course(self):  # 查看所选课程
        with open(select_course, mode='rb') as  f:
            courses_list = []
            while True:
                try:
                    course = pickle.load(f)
                    courses_list.append(course)
                    # print('%s\t%s\t%s\t%s' % (course.name, course.price, course.cycle, course.teacher))
                except EOFError:
                    break
        for i in courses_list:
            print(i[self.name])
            # print(i, self.name)
            # if self.name == i:
            #     print(i)


class Manager(Public):  # 管理员
    # 管理员菜单
    menu_list = [
        ('创建课程', 'create_course'),
        ('查看所有课程', 'show_courses'),
        ('创建学生账号', 'create_stu'),
        ('查看所有学生', 'show_students'),
        ('查看所有选课情况', 'show_sit'),
        ('退出程序', 'exit')]

    def __init__(self, name):
        self.name = name

    def create_course(self):  # 创建课程
        name = input('课程名:')
        price = input('课程价格:')
        cycle = input('课程周期：')
        teacher = input('老师：')
        course = Course(name, price, cycle, teacher)
        with open(course_file, 'ab') as f:
            pickle.dump(course, f)
            print('课程创建成功')

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
                print('创建成功:%s' % user)
        else:
            print('帐号密码格式不符合')

    def show_students(self):  # 查看所有学生
        print('学生列表>')
        for i in read_usr():
            if i[2].upper() == 'STUDENT':
                print(i[0])

    def show_sit(self):  # 查看所有选课情况
        pass


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
    for i in read_usr():
        if input_usr == i[0] and input_pwd == i[1]:
            print('%s登录成功，欢迎您：%s' % (i[2], input_usr))
            return i[0], i[1], i[2]

    else:
        print('账号密码错误')
        return None


if __name__ == '__main__':
    ret = login()
    if ret:
        while True:
            usr, role = ret[0], ret[2]
            obj = Student(usr)  # 实例化默认是学生
            if role.upper() == 'MANAGER':
                obj = Manager(usr)
            for index, i in enumerate(obj.menu_list, 1):  # 遍历列表中菜单
                print(index, i[0])
            choice = int(input('请选择序号:').strip())
            print('-' * 20)
            func = obj.menu_list[choice - 1][1]  # 取出选择序号对应的方法名，字符串类型
            getattr(obj, func)()  # 执行对象中的方法
            print('-' * 20)
