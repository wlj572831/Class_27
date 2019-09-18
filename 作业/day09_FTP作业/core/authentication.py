#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

# 注册登录类
# from conf import settingg as se


class Authentication:  # 注册登录类

    @staticmethod
    def read_user(path):  # 读取用户方法
        with open(path, mode='r', encoding='utf-8') as  f:
            for line in f:
                user, pwd = line.strip().split('|')
                yield user, pwd
