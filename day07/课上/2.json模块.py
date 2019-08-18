#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
import json
import pickle
# 序列化模块

# json
# # json数据类型是一个特殊的字符串
# # 在任何语言中它的type都必须是字符串
# # 但是还要满足一些要求 : key必须是字符串,且value只能是:字典 列表 字符串 数字 bool值

# pickle 是只有Python,支持大多数数据类型

# 1.dumps
# dic = {'username': 'alex', 'pwd': '123嘎嘎嘎456', 'login': {'a': 1, 'b': 2}}
# print(dic)
# ret = json.dumps(dic)  # 结果是字符串类型
# print(ret)
# byte_8 = ret.encode('utf-8')  # 编码为字节了类型
# print(byte_8)
#
# with open('file/json.txt', mode='w', encoding='utf-8') as f1:
#     f1.write(ret)

# 2.loads
# str8 = byte_8.decode('utf-8')
# print(str8, type(str8))
# ret = json.loads(str8)
# print(ret, type(ret))

# 3.dump
# lst = ['alex', 1, 2, 3]
# with open('file/dump.txt', mode='w', encoding='utf-8') as f:
#     json.dump(lst, f)

# 4. load
# with open('file/dump.txt', encoding='utf-8') as f:
#     print(json.load(f))
