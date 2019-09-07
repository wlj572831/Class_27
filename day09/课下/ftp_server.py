#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import json
import struct
import socketserver
import hash

user_db = r'D:\Class_27\Class_27\day09\课下\db\user'


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


def login():  # 登录方法
    with open(user_db, mode='r', encoding='utf-8') as  f:
        for line in f:
            user, pwd = line.strip().split('|')
            yield user, pwd


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        send_msg(conn, '欢迎使用FTP,请登录:')
        # 三次登录
        for i in range(3):
            usr_dic = json.loads(rev_msg(conn))
            user_info = login()
            if usr_dic['username'] == user_info[0] and usr_dic['password'] == user_info[1]:
                send_msg(conn, '登录成功')
                break
            else:
                msg = '帐号密码有误，还有%s次机会' % (2 - i)
                send_msg(conn, msg)
        else:
            send_msg(conn, '输错帐号密码超过三次')


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9091), MyServer)
    server.serve_forever()