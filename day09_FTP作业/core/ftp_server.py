#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import json
import socketserver
from core.public import Public as  pu
from core import authentication as  au
from conf import setting as se


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        pu.send_msg(conn, '欢迎使用FTP,请登录:')
        # 三次登录
        for i in range(3):
            usr_dic = json.loads(pu.rev_msg(conn))
            user_info = au.read_user(se.user_info)
            if usr_dic['username'] == user_info[0] and usr_dic['password'] == user_info[1]:
                pu.send_msg(conn, '登录成功')
                break
            else:
                msg = '帐号密码有误，还有%s次机会' % (2 - i)
                pu.send_msg(conn, msg)
        else:
            pu.send_msg(conn, '输错帐号密码超过三次')


def main():
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9091), MyServer)
    server.serve_forever()
