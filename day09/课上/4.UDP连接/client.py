#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # 1.创建socket 对象
addr = ('127.0.0.1', 8001)
while True:
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)  # 2.sendto('内容',addr)发送消息
    msg, addr = sk.recvfrom(1024)  # 3.接收消息
    print(msg.decode('utf-8'))
sk.close()  # 4.关闭链接
