#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8989))

while True:
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
sk.close()
