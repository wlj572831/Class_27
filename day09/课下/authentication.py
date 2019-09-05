#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

# 注册登录类
import setting as se

class Authentication:   #注册登录类
    class Login:
        def __init__(self, name):
            self.name = name

        @staticmethod
        def login():    #登录方法
            for i in range(3):
                with open(se.user_info, mode='r', encoding='utf-8') as  f:
                    input_usr = input('请输入用户名:').strip()
                    input_pwd = input('请输入密码:').strip()
                    for line in f:
                        user, pwd = line.strip().split('|')
                        if input_usr == user and hash.to_md5(input_pwd) == pwd:
                            return True
                    else:
                        print('已输错%s，还有%s次机会' % (i + 1, 2 - i))
            else:
                print('登录失败')
                return

        def regedit(self):

