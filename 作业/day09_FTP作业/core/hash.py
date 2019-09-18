#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import hashlib


def to_md5(obj):
    '''给出值，返回MD5加密后的结果'''
    return hashlib.md5(obj.encode('utf-8')).hexdigest()
