#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import struct


# 黏包发生:
# 实际上，当一次发送多条数据 因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据
# 造成前后两次发送的内容有可能混合在一块
# 解决方案: 先发送字节长度，再根据接受到的字节长度来接受下面字符串
def send_msg(conn, msg):
    msg_b = msg.encode('utf-8')
    len_msg = len(msg_b)
    pack_len = struct.pack('i', len_msg)
    conn.send(pack_len)
    conn.send(msg_b)


sk = socket.socket()  # 1.创建socket对象
sk.bind(('127.0.0.1', 8989))  # 2. 创建服务端
sk.listen()  # 3.开启服务端连接
conn, addr = sk.accept()  # 等待被连接

while True:
    send_msg(conn, 'nihao')
conn.close()
sk.close()
