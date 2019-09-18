#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

from gevent import monkey

monkey.patch_all()
import gevent
import socket


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
        gevent.spawn(func, conn)
    conn.close()
    sk.cloese()
