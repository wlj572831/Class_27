#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket


# sk = socket.socket()

# 登录/注册
# 具体的操作:上传／下载
def login():
    pass


def register():
    pass


opt_lst = [('登录', login), ('注册', register)]

for index, opt in enumerate(opt_lst, 1):
    print(index, opt[0])

num = int(input('请输入要选择的操作序号:'))
func = opt[num - 1][1]
func()