#!/usr/bin/python
# coding:utf-8
# createtime: 2019-08-01

# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

flag = False


def read_user():
    global flag
    with open('file/user', mode='r', encoding='utf-8') as f:
        for line in f:
            if line:
                usr, pwd = line.strip().split('|')
                inp_name = input('usr:').strip()
                inp_pwd = input('pwd:').strip()
                if inp_name == usr and inp_pwd == pwd:
                    flag = True
                    break


def wapper(funcname):
    # @wraps(funcname)
    def inner(*args, **kwargs):
        i = 0
        if flag is False and i < 3:
            read_user()
            i += 1
        if flag:
            ret = funcname(*args, **kwargs)
            return ret

    return inner


@wapper
def information():
    '''个人信息'''
    print('个人信息界面')


@wapper
def sorce():
    '''成绩查询'''
    print('成绩查询界面')


information()
sorce()
