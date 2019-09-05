#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import hashlib


def to_md5(obj):
    return  hashlib.md5(obj.encode('utf-8')).hexdigest()