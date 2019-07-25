#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# Creation time : 2019-7-19

user_dic = {
    'alex': 'a347258',
    'Gen': 'abcd',
}


# 注册
def register():
    while True:
        reg_user = input('请输入用户名（q退出）:')
        if reg_user.upper() == 'Q':
            break
        reg_pwd = input('请输入密码:')
        again_pwd = input('再次确认密码:')
        '''1.校验输入的帐号密码是否为空
           2.校验所输入的用户名是否已经存在
           3.校验两次输入的密码是否一致
        '''
        if reg_user and reg_pwd:
            if reg_user in user_dic:
                print('用户名已存在')
            elif reg_pwd != again_pwd:
                print('两次输入的密码不同')
            else:
                user_dic[reg_user] = reg_pwd
                print('已添加用户:%s' % reg_user)
                break
        else:
            print('用户名或密码为空，请重新输入')


# 登录
def login():
    count = 0
    while count < 3:
        input_user = input('请输入用户名(q退出):')
        if input_user.upper() == 'Q':
            break
        input_pwd = input('password:')
        # 去除用户名密码两边空格
        input_user = input_user.strip()
        input_pwd = input_pwd.strip()
        '''
        1.判断输入帐号密码是否为空,如果为空，则退出重试(不计入次数)
        2.校验输入的帐号密码,判断用户名是否存在，如果存在是否与密码匹配
        3.如果全部正确无误，则结束循环
        '''
        if input_user and input_pwd:
            if input_user in user_dic and user_dic[input_user] == input_pwd:
                print('welcome! %s' % input_user)
                break
            else:
                print('用户名或密码不正确')
                count += 1
            # 输错三次，结束循环
            # if count > 3:
            #     print('输入错误超过三次,即将退出')
            #     cycle = False
        else:
            print('帐号或密码输入为空，请重试')
    else:
        print('输入错误超过三次,即将退出')  # 三次未能成功登录则退出


while True:
    print('菜单'.center(30, '-'))
    print('a.注册\tb.登录\tq.退出')
    menu = input('请选择:')
    if menu.upper() == 'A':
        print('注册界面'.center(30, '-'))
        register()
    elif menu.upper() == 'B':
        print('登录界面'.center(30, '-'))
        login()
    elif menu.upper() == 'Q':
        break
    else:
        print('输入指令不正确')
