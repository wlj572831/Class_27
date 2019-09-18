#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
while True:
    message = sk.recv(1024)
    print(message)
    sk.send(message)
conn.close()
