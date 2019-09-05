#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

import socket

ip_port = ('127.0.0.1', 9091)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024).decode('utf-8')
    print('receive:', data)
    inp = input('please input:')
    sk.sendall(bytes(inp, encoding='utf-8'))
    if inp == 'exit':
        break

sk.close()
