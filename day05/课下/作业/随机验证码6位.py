#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06
# Author ：王刘俊

import random


def get_code():
    V_code = ''
    for i in range(6):
        num = random.randint(0, 9)
        cap = chr(random.randint(65, 90))  # ASCII码65-90位大写字母
        low = chr(random.randint(97, 122))  # ASCII码97-122位小写字母
        num_ = str(num)
        ran_str = random.choice([num_, cap, low])  # 随机从获取的三位随机字符中间选一个
        V_code += ran_str
    return V_code


code = get_code()
print(code)
