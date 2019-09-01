#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import struct


def my_send(conn, msg):
    msg_b = msg.encode('utf-8')
    len_msg = len(msg_b)
    pick_len = struct.pack('i', len_msg)
    conn.send(pick_len)
    conn.send(msg_b)


sk = socket.socket()
sk.bind(('127.0.0.1', 7777))
sk.listen()

conn, addr = sk.accept()
msg1 = '你好'
msg2 = '吃了吗'
my_send(conn, msg1)
my_send(conn, msg2)
conn.close()
sk.close()
