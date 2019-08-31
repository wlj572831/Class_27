#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
import json
import pickle

# 序列化模块

# 一.json:
# json数据类型是一个特殊的字符串,在任何语言中它的type都必须是字符串
# # json是所有的编程语言都公认的一种数据类型
# 在python序列化的过程中 会把字典/其它数据类型转换成字符串
# 在转换的之前,字典还要满足一些要求 : key必须是字符串,且value只能是:字典 列表 字符串 数字 bool值
# json方法有:
# loads  dumps   和内存交互
# load   dump    和文件交互


# 二.pickle 只支持Python之间数据交互,支持大多数数据类型，自定义类型
# pickle方法有:
# loads  dumps   和内存交互
# # load   dump    和文件交互

# 1.json dumps 序列化
# dic = {'username': 'alex', 'pwd': '123嘎嘎嘎456', 'login': {'a': 1, 'b': 2}}
# print(dic)  # 数据类型是字典
# ret = json.dumps(dic)  # 1.序列化，结果是字符串类型，汉字则为utf-8编码表中位置 \u560e ： 嘎
# print(ret)
# ret = json.dumps(dic, ensure_ascii=False)   # 如果只想汉字显示汉字
# print(ret)
# byte_8 = ret.encode('utf-8')  # 以utf-8编码
# print(byte_8)
# # 序列化之后字符的存入文件
# with open('file/json.txt', mode='w', encoding='utf-8') as f1:
#     f1.write(ret)

# 2.json loads 反序列化
# str8 = byte_8.decode('utf-8')
# print(str8, type(str8))
# ret = json.loads(str8)
# print(ret, type(ret))

# 3.json dump 将序列化之后的字符串存入文件
# lst = ['alex', 1, 2, 3]
# with open('file/dump.txt', mode='w', encoding='utf-8') as f:
#     json.dump(lst, f)

# 4.json load 读取文件中json数据类型
# with open('file/dump.txt', encoding='utf-8') as f:
#     print(json.load(f))


dic = {'北京': {'朝阳', '昌平'}, ('天津', '河北'): [1, 2, 3]}
ret = pickle.dumps(dic)  # 直接转换成字节码
print(ret)
d = pickle.loads(ret)
print(d)
with open('file/pickle_file', 'wb') as f:
    pickle.dump(dic, f)
with open('file/pickle_file', 'rb') as f:
    ret = pickle.load(f)
    print(ret)


# pickle和json的区别
# pickle 支持python中的几乎所有数据类型,但是只能python一种语言中使用
# json   支持所有的语言,但只支持有限的数据类型