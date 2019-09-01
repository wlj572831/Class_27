#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket

sk = socket.socket()  # 买手机
sk.bind(('192.168.36.137', 7777))  # 装上电话

while True:
    sk.listen()
    conn, addr = sk.accept()  # 等电话
    while True:
        try:
            send_msg = input('>>>')
            if send_msg == 'q':
                # q_msg = '对方已退出聊天'
                # conn.send(q_msg.encode('utf-8'))
                break
            conn.send(send_msg.encode('utf-8'))
            re_msg = conn.recv(1024)
            print(re_msg.decode('utf-8'))
        except ConnectionAbortedError:
            print('对方已关闭链接')
            break
    conn.close()  # 挂电话
sk.close()  # 关手机
