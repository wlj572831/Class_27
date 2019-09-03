#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 8777))
sk.listen()
conn, addr = sk.accept()
conn.send(b'0026')
conn.send(b'world')
conn.close()
sk.close()
