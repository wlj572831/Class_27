#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import json

sk = socket.socket()
sk.bind(('127.0.0．1', 9787))
sk.listen()
conn, addr = sk.accept()

msg_dic = conn.recv(1024).decode('utf-8')
msg_dic = json.loads(msg_dic)

with open(msg_dic['filename'], mode='wb') as f:
    msg2 = conn.recv(msg_dic['filesize'])
    f.write(msg2)

conn.close()
sk.close()
