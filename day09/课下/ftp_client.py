#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import struct
import json

ip_port = ('127.0.0.1', 9091)
sk = socket.socket()
sk.connect(ip_port)


def rev_msg(sk):  # 收消息函数
    len_b = sk.recv(4)
    msg_len = struct.unpack('i', len_b)[0]
    msg_b = sk.recv(msg_len)
    return msg_b.decode('utf-8')


def send_msg(conn, msg):  # 发消息函数
    msg_b = msg.encode('utf-8')
    len_msg = len(msg_b)
    pack_len = struct.pack('i', len_msg)
    conn.send(pack_len)
    conn.send(msg_b)


while True:
    msg_wel = rev_msg(sk)
    print(msg_wel)
    for i in range(3):
        inp_user = input('请输入用户名:').strip()
        inp_pwd = input('请输入密码:').strip()
        user_dic = {'username': inp_user, 'password': inp_pwd}  # 把输入的帐号密码当转换成json发送
        user_js = json.dumps(user_dic)
        print(user_js)
        send_msg(sk, user_js)
        print(rev_msg(sk))
sk.close()
