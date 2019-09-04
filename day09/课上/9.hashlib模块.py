#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import hashlib

# 密码不能明文存储
# 获取到整个用户登录信息文件了所有的密码都泄露了

# 1. MD5
# a.MD5加密只接受字节类型，生成固定32位
# b.一次接收所有的值生成的加密结果和分批接受后生成结果加密值相同
# a.
# user = 'alex'
# md5 = hashlib.md5(('只有我知道,别人不知道的秘密的字符串%s123456' % user).encode('utf-8'))
# # md5.update(b'123456')
# ret = md5.hexdigest()
# print(ret)
# # 3637d0d29844612b6d20ce99a6d7d289
#
# # 2. sha1加密 结果固定40位
# user = 'alex'
# md5 = hashlib.sha1(('只有我知道,别人不知道的秘密的字符串%s123456' % user).encode('utf-8'))
# # md5.update(b'123456')
# ret = md5.hexdigest()
# print(ret)

# 3. 文件MD5值校验
# file1 = 'E:\Re061361454.zip'
# file2 = 'E:\Re061361454 - 副本.zip'
#
#
# def get_md5(file):
#     md5 = hashlib.md5()
#     with open(file, 'rb') as f:
#         content = f.read()
#         md5.update(content)
#     ret = md5.hexdigest()
#     return ret
#
#
# ret = get_md5(file1)
# ret2 = get_md5(file2)
# print(ret, ret2)
# 274773cc326dc96c0c502e04e39c0e14
# 274773cc326dc96c0c502e04e39c0e14
