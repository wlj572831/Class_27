#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# a. 使用while循环实现输出2-3+4-5+6...+100 的和
#
# num = 2
# sum_num = 0
#
# while num < 101:
#     # 偶数加，奇数减
#     if num % 2 == 0:
#         sum_num += num
#     else:
#         sum_num -= num
#     num += 1
# print(sum_num)

# b. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
#
# num = 0
# while num < 12:
#     num += 1
#     # 遇10跳过
#     if num == 10:
#         continue
#     print(num)

# c. 使用 while 循环实现输出 1-100 内的所有奇数
#
# num = 0
# while num < 100:
#     num += 1
#     # 遇偶数就跳过本次循环
#     if num % 2 == 0:
#         continue
#     else:
#         print(num)


# d. 使用 while 循环实现输出 1-100 内的所有偶数
#
# num = 0
# while num < 100:
#     num += 1
#     # 遇奇数就跳过本次循环
#     if num % 2 == 1:
#         continue
#     else:
#         print(num)

# e.使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束

#num_down记录从100-50的值
num_down = 100
#num_up记录从0-50的值
num_up = 0

while num_down > 0 or num_up < 51:
    '''num_down 大于等于50时,输出num_down
    其他情况输出num_up，并依次+1'''
    if num_down >= 50:
        print(num_down)
    else:
        print(num_up)
        num_up += 1
    num_down -= 1