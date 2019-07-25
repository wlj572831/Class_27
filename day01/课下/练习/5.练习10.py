#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 10.使用while,完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

#单行'*'的最大数量
max_num = 5
#记录总行数，也就是循环的次数
count = 2*5 -1
#每行'*'的数量
num = 1
'''
1.记录循环次数，不得超过总共的行数
2.剩余循环次数大于单行最大数量时，每次循环打印的'*'多一位
3.剩余循环次小于单行最大数量'*'时，每次循环减少一位 '*'
'''
while count > 0:
    if count > max_num:
        print('*'*num)
        num += 1
    else:
        print('*'*num)
        num -= 1
    count -= 1