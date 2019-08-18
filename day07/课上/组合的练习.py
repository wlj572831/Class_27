#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time

class Student:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        # self.course = course


class Course:
    def __init__(self, cname, period, price):
        self.cname = cname
        self.period = period
        self.price = price


alex = Student('alex', '男', 25)
print(alex.__dict__)
alex.course = Course('python', '5 month', 20000)
print(alex.__dict__)
print(alex.course.__dict__)
