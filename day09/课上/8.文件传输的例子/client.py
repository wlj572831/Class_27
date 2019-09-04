#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import os
import json

file_name = r'E:\Re061361454.zip'
sk = socket.socket()

sk.connect(('127.0.0．1', 9787))
base_name = os.path.basename(file_name)  # 获取文件名
file_size = os.path.getsize(file_name)  # 获取文件大小
file_dic = {'filename': base_name, 'filesize': file_size}
json_dic = json.dumps(file_dic)
dic_b = json_dic.encode('utf-8')
sk.send(dic_b)
with open(file_name, mode='rb') as f:
    content = f.read()
    sk.send(content)
sk.close()
