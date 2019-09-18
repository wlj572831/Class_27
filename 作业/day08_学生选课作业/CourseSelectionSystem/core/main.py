#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import sys
from core import authentication as au
from core import manager as ma
from core import student as stu


def main():
    ret = au.login()
    if ret:
        while True:
            usr, role = ret[0], ret[2]
            if role == 'Student':
                cls = getattr(stu, role)
            elif role == 'Manager':
                cls = getattr(ma, role)
            obj = cls.init(usr)
            print('-' * 40)
            for index, i in enumerate(cls.menu_list, 1):  # 遍历列表中菜单
                print(index, i[0])
            print('-' * 40)
            choice = int(input('请选择序号:').strip())
            func = obj.menu_list[choice - 1][1]  # 取出选择序号对应的方法名，字符串类型
            getattr(obj, func)()  # 执行对象中的方法
            # cls = getattr(sys.modules[__name__], role)
            # obj = cls.init(usr)
            # print('-' * 40)
            # for index, i in enumerate(cls.menu_list, 1):  # 遍历列表中菜单
            #     print(index, i[0])
            # print('-' * 40)
            # choice = int(input('请选择序号:').strip())
            # func = obj.menu_list[choice - 1][1]  # 取出选择序号对应的方法名，字符串类型
            # getattr(obj, func)()  # 执行对象中的方法
