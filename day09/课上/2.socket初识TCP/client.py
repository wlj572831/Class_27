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

sk = socket.socket()  # 1.创建socket 对象
sk.connect(('127.0.0.1', 7777))  # 2.连接服务
while True:
    try:
        msg = sk.recv(1024).decode('utf-8')  # 3.接收信息
        if msg.upper() == 'Q':
            break
        print(msg)
        mess = input('>>>>')
        send_msa = sk.send(mess.encode('utf-8'))  # 4.发送信息
        if mess.upper() == 'Q': break
    except ConnectionAbortedError:
        print('对方已断开连接')
        break
sk.close()  # 5.关闭连接
