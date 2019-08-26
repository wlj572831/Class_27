#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time


class Person:
    def __init__(self, name, hp, ad, sex, job):
        self.username = name
        self.hp = hp
        self.ad = ad
        self.sex = sex
        self.job = job

    def attack(self, dog):
        dog.hp -= self.ad
        print('%s打了%s,%s掉了%s血' % (self.username, dog.name, dog.name, self.ad))


alex = Person('alex', 100, 5, '不详', '乞丐')


class Dog:
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad

    def bite(self, person):
        person.hp -= self.ad
        print('%s咬了%s,%s掉了%s血' % (self.name, person.username, person.username, self.ad))


wang_cai = Dog('wangcai', 'teddy', 500, 200)
wang_cai.bite(alex)
alex.attack(wang_cai)
print(wang_cai.hp, alex.hp)
