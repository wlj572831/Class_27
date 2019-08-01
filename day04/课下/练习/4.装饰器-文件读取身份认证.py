#!/usr/bin/python
# coding:utf-8
# createtime: 2019-08-01

# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

def user():
    with open('file/user', mode='r', encoding='utf-8') as f:
        usr_dic = {}
        for line in f:
            if line:
                usr, pwd = line.strip().split('|')
                usr_dic[usr] = pwd
    return usr_dic


def wapper(funcname):
    # @wraps(funcname)
    def inner(*args, **kwargs):
        for i in range(3):
            inp_name = input('usr:').strip()
            inp_pwd = input('pwd:').strip()
            usr_dic = user()
            if inp_name in usr_dic and usr_dic[inp_name] == inp_pwd:
                ret = funcname(*args, **kwargs)
                return ret

    return inner


# 个人信息界面
@wapper
def information():
    print('个人信息界面')


# 成绩查询界面
@wapper
def sorce():
    print('成绩查询界面')


information()
sorce()
