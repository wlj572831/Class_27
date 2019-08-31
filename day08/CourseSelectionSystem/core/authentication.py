#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import os
import sys
from conf import settings as cof


def login():
    input_usr = input('请输入用户名:').strip()
    input_pwd = input('请输入密码:').strip()
    with open(cof.user_file, mode='r', encoding='utf-8') as f:
        for line in f:
            if line:
                usr, pwd, role = line.strip().split('|')
                if usr == input_usr and pwd == input_pwd:
                    print('%s登录成功,欢迎您%s' % (role, usr))
                    return usr, pwd, role
        else:
            print('账号密码错误')
            return None

