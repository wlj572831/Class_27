#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time

class Course:
    course_lst = []

    def __init__(self, name, cycle, price):
        self.name = name
        self.cycle = cycle
        self.price = price


class Role(object):
    def __init__(self, name):
        self.name = name

    def show_courses(self):
        for i in Course.course_lst:
            print(i.name, i.cycle, i.price)


class Student(Role):
    def __init__(self, name):
        super().__init__(name)


class Manager(Role):
    def __init__(self, name):
        super().__init__(name)
        self.course = []


python = Course('python', '6 months', 19800)
linux = Course('linux', '5 months', 17800)
Course.course_lst = [python, linux]
m = Manager('alex')
m.show_courses()
