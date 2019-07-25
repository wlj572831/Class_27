#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 1.实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
#
# user = 'seven'
# pwd = 123
#
# input_user = input('用户名:')
# input_pwd = int(input('密码:'))
#
# if input_user == user and input_pwd == pwd:
#     print('登录成功')
# else:
#     print('登录失败')

# 2.实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次

# user = 'seven'
# pwd = 123
#
# #定义循环初始值
# count = 0
#
# while count < 3:
#     input_user = input('用户名:')
#     input_pwd = int(input('密码:'))
#     #输入和结果对比
#     if input_user == user and input_pwd == pwd:
#         exit('登录成功')
#     else:
#         print('登录失败')
#     #每次循环次数+1
#     count += 1

# 3.实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,
# 否则登陆失败,失败时允许重复输入三次
#
# #定义循环初始值
# count = 0
#
# while count < 3:
#     input_user = input('用户名:')
#     input_pwd = int(input('密码:'))
#     #输入和结果对比
#     if input_user == 'seven' or input_user =='alex' and input_pwd == 123 :
#         exit('登录成功')
#     else:
#         print('登录失败')
#     #每次循环次数+1
#     count += 1