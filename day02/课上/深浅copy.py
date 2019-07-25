#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
import copy

a = [1, 2, 3, [4, 5, [15, 16]], 6]

# b指向a的指向的内存地址
b = a

# c 另外开辟一段内存空间,复制a的内存地址
c = copy.copy(a)

# d 另外开辟一块内存空间，递归复制a的全部内存地址
d = copy.deepcopy(a)

a.append(7)
a[3][1] = 11
d[3][2][1] = 20
print(a)
print(b)
print(c)
print(d)
