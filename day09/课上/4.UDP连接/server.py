#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # 1.创建socket对象，SOCK_DGRAM为UDP协议
sk.bind(('127.0.0.1', 8001))  # 2.开启服务端及端口号
while True:
    msg, addr = sk.recvfrom(1024)  # 3.接收消息和IP
    print(msg.decode('utf-8'))
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)  # 4.根据IP发送信息
sk.close()  # 5.关闭链接
