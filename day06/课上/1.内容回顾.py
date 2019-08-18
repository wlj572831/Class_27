#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time
import re

# 1. findall(正则表达式，待匹配的字符串)

# 分组优先
# ret = re.findall(r'\d(\d)', 'a1,b22,c345')
# print(ret)

# 取消分组优先
# ret = re.findall(r'\d(?:\d)', 'a1,b22,c345')
# print(ret)

# 2. search(正则表达式,待匹配的字符串)
