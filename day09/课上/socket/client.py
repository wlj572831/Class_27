#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
#
# sk = socket.socket()
#
# sk.connect(('192.168.36.137', 7777))
# while True:
#     try:
#         msg = sk.recv(1024)
#         print(msg.decode())
#         send_msg = input('>>>')
#         if send_msg == 'q':
#             break
#         send_msg = sk.send(send_msg.encode('utf-8'))
#     except ConnectionAbortedError:
#         print('对方已关闭链接')
#         break
# sk.close()

import socket

sk = socket.socket()
sk.connect(('192.168.36.137', 7777))
while True:
    try:
        msg = sk.recv(1024)
        if msg == b'':
            break
        msg = msg.decode('utf-8')
        print(msg)
        mess = input('>>>>')
        if mess.upper() == 'Q':
            break
        send_msa = sk.send(mess.encode('utf-8'))
    except ConnectionAbortedError:
        print('对方已断开连接')
        break
sk.close()
