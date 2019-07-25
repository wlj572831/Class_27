#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

'''
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
'''


user = 'alex'
pwd = 'helloword'

#记录循环次数
count = 1

while count <= 3:
    input_user = input('username:')
    input_pwd = input('password:')
    #匹配成功，退出程序
    if input_user == 'alex' and input_pwd == 'helloword':
        print('welcome', user)
        exit()
    print('已输错%s次' %count)
    if count == 3:
        print('超过三次，退出程序')
    #每次循环+1
    count += 1


