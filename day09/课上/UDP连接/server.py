#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto(b'hello', ('127.0.0.1', 8001))

msg, addr = sk.recvfrom(1024)
print(msg)
sk.close()
