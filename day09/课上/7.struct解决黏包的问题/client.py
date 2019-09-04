#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import struct


def rev_msg(sk):
    len_b = sk.recv(4)
    msg_len = struct.unpack('i', len_b)[0]
    msg_b = sk.recv(msg_len)
    return msg_b.decode('utf-8')


sk = socket.socket()

sk.connect(('127.0.0.1', 8989))
while True:
    ret = rev_msg(sk)
    print(ret)
sk.close()
