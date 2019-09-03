#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket()  # 1.买手机(创建一个socket对象)
# sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM) 默认参数
sk.bind(('127.0.0.1', 7777))  # 2.装上电话(绑定)
sk.listen()  # 开机

while True:
    conn, addr = sk.accept()  # 3.等电话(等待被连接)
    while True:
        try:
            send_msg = input('>>>')
            conn.send(send_msg.encode('utf-8'))  # 4.发送消息(只支持字节码)
            if send_msg.upper() == 'Q': break
            re_msg = conn.recv(1024).decode('utf-8')  # 5.接受消息(只支持字节码)
            if re_msg.upper() == 'Q':
                break
            print(re_msg)
        except ConnectionAbortedError:
            print('对方已关闭链接')
            break
    conn.close()  # 6.挂电话(关闭当前连接)
sk.close()  # 关手机   # 7.关闭服务
