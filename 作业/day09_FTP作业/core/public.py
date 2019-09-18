#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import struct


class Public:

    @staticmethod
    def rev_msg(sk):
        '''接收消息函数'''
        len_b = sk.recv(4)
        msg_len = struct.unpack('i', len_b)[0]
        msg_b = sk.recv(msg_len)
        return msg_b.decode('utf-8')

    @staticmethod
    def send_msg(conn, msg):  # 发消息函数
        '''发送消息函数'''
        msg_b = msg.encode('utf-8')
        len_msg = len(msg_b)
        pack_len = struct.pack('i', len_msg)
        conn.send(pack_len)
        conn.send(msg_b)
