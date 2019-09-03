#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8777))
for i in range(1, 10000): i * i
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.close()
