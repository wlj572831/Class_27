#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊


import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
# with open(r'D:\Class_27\Class_27\day09\课上\1.网络编程.py', mode='rb') as  f:
#     a = f.read()
sk.sendto(b'1:111:eva:eva:32:wahaha', ('192.168.0.49', 2425))

# 格式: '1:111:用户名:密码:32:发送内容' 2425为飞秋端口
