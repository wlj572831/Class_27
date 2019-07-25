#!/usr/bin/python
#coding:utf-8

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
#根据'*的最大数量'计算出输出的总行数,也就是循环次数
max_count = 2*5 -1
#循环初始值
count = 1
#每行'*'的数量
num = 1

'''
1.记录循环次数，不得超过总共的行数
2.循环次数小于单行最大数量时，每次循环打印的'*'多一位
3.循环次数超过单行最大数量'*'时，每次循环减少一位 '*'
'''
while count <= max_count:
    if count < max_num:
        print('*'*num)
        num += 1
    else:
        print('*'*num)
        num -= 1
    count += 1