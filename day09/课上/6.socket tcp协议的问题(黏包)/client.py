#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

# 同时执行多条命令之后，得到的结果很可能只有一部分，
# 在执行其他命令的时候又接收到之前执行的另外一部分结果，这种显现就是黏包。
sk = socket.socket()
sk.connect(('127.0.0.1', 8777))
for i in range(1, 10000): i * i
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.close()
