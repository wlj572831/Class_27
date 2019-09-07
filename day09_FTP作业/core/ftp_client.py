#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import struct
import json
from core.public import Public as  pu
from core import authentication as  au
from conf import setting as se


def main():
    ip_port = ('127.0.0.1', 9091)
    sk = socket.socket()
    sk.connect(ip_port)

    while True:
        msg_wel = pu.rev_msg(sk)
        print(msg_wel)
        for i in range(3):
            inp_user = input('请输入用户名:').strip()
            inp_pwd = input('请输入密码:').strip()
            user_dic = {'username': inp_user, 'password': inp_pwd}  # 把输入的帐号密码当转换成json发送
            user_js = json.dumps(user_dic)
            print(user_js)
            pu.send_msg(sk, user_js)
            print(pu.rev_msg(sk))
    sk.close()
