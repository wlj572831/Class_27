#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun


#
menu_dic = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {}, '网易': {}, 'Google': {}
            },
            '中关村': {
                '爱奇艺': {}, '汽车之家': {}, 'youku': {}
            },
            '上地:': {
                '百度:': {}, '快手': {}, '小米': {}
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': '', '北航': {}},
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '上海': {},
    '河南': {},
}


def menu(current_level):
    while True:
        # 遍历当前菜单
        for i in current_level:
            print(i)
        choice = input('>>请选择(b返回q退出):').strip()
        if choice.upper() == 'B':return
        elif choice in current_level:
            if len(current_level[choice]):
                menu(current_level[choice])
            else:
                print('已是底层')
                continue


menu(menu_dic)
