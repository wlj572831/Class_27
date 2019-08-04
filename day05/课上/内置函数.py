#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time


tu1 = (('a'), ('b'))
tu2 = (('c'), ('d'))

ret = zip(tu1, tu2)

result = list(map(lambda tu: {tu[0]: tu[1]}, ret))
print(result)
