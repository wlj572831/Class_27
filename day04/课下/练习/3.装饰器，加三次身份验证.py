#!/usr/bin/python
# coding:utf-8
# createtime: 2019-8-1


# 3.编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.

# 方法1: 把身份验证放到函数里
# def login_(user, pwd):
#     for i in range(3):
#         input_user = input('user:').strip()
#         input_pwd = input('pwd:').strip()
#         if input_user == user and input_pwd == pwd:
#             return True
#     else:
#         return False
#
#
# user = 'alex'
# pwd = 'error'
#
# def wapper(funcname):
#     def inner():
#         if login_(user, pwd):
#             funcname()
#     return inner
#
#
# @wapper
# def func():
#     print('this is a func')

# 方法2
#
# def wapper(funcname):
#     # @wraps(funcname)
#     def inner(*args, **kwargs):
#         for i in range(3):
#             inp_name = input('usr:').strip()
#             inp_pwd = input('pwd:').strip()
#             if inp_name == args[0] and inp_pwd == args[1]:  # 如果登陆成功
#                 ret = funcname(*args, **kwargs)
#                 return ret
#
#     return inner
#
#
# @wapper
# def login_(usr, pwd):
#     print('恭喜您登陆成功')
#
#
# login_('alex', '123')
