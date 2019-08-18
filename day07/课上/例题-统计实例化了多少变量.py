#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time

class Person:
    count = 0

    def __init__(self):
        Person.count += 1


alex = Person()
wusir = Person()
wusir = Person()
print(alex.count)
print(wusir.count)
