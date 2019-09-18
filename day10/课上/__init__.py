#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

path = r'D:\develop\mysql5.5\my.ini'
with open(path,mode='r',encoding='utf-8') as f:
    content = f.read()

print(content)