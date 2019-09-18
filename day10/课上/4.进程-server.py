#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import socket
from multiprocessing import Process


def func(conn):
    while True:
        conn.send(b'hello')
        message = conn.recv(1024)
        print(message)

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        Process(target=func, args=(conn,)).start()
    conn.close()
    sk.cloese()
