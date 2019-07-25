#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

# 思考题
# 求1000内的数
# a + b +c == 1000
# a + b == c

start_time = time.time()
# play A   41s
# for c in range(1,501):
#      for b in  range(1,501):
#           for a in range(1, 501):
#                sum1 = a + b
#                sum2 = a + b +c
#                if sum1 == c and sum2 ==1000:
#                     print(a, b, c)

# play B
c = 500
for a in range(1, 501):
    b = c - a
    sum = a + b
    if sum == 500:
        print(a, b, c)
end_time = time.time()
print('共用时:', (end_time - start_time))
