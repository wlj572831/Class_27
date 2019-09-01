#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊


import socket
import struct


def my_recv(sk):
    pack_len = sk.recv(4)  # 3.1   接收前四位，即将接收字节类型的长度
    len_msg = struct.unpack('i', pack_len)[0]  # 3.2   长度接收长度转换成int类型
    msg = sk.recv(len_msg).decode('utf-8')  # 3.3   接收指定字节长度的字符串并解码
    return msg


sk = socket.socket()  # 1. 创建客户套接字
sk.connect(('127.0.0.1', 7777))  # 2.尝试连接服务器
msg = my_recv(sk)  # 3.发送/接收对话
print(msg)
msg = my_recv(sk)
print(msg)
sk.close()  # 4.关闭客户套接字
