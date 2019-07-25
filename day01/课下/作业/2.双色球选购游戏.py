#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

'''
基础需求：
先让用户依次选择6个红球（红球的选择范围是1-32），
再选择2个蓝球（篮球的选择范围是1-16），最后统一打印用户选择的球号。
确保用户不能选择重复的，选择的数不能超出范围
'''

#定义红蓝球选择范围
blue = list(range(1, 11))
red = list(range(1,33))
#存储选择的红篮球
choice_all = []

#6次选择红球
red_count = 0
print('请依次选择6个红球(1-32)')
while red_count < 6:
    choice = int(input('>>>'))
    '''
    1.选择不在范围内，跳出本次循环,用户重新输入
    2.如果选择内容已存在，跳出本次循环,用户重新输入
    3.选择数据无异常,添加到choice_all列表中，记录循环次数+1
    '''
    if choice not in red:
        print('不在范围内')
        continue
    elif choice in choice_all:
        print('选择内容有重复,try again')
        continue
    else:
        choice_all.append(choice)
        red_count += 1

#2次选择蓝球(1-10)
blue_count = 0
print('请依次选择2个蓝球(1-10)')
while blue_count < 2:
    choice = int(input('>>>'))
    '''
    1.选择不在范围内，跳出本次循环,用户重新输入
    2.如果选择内容已存在，跳出本次循环,用户重新输入
    3.选择数据无异常,添加到choice_all列表中，记录循环次数+1
    '''
    if choice not in blue:
        print('不在范围内')
        continue
    elif choice in choice_all:
        print('选择内容有重复,try again')
        continue
    else:
        choice_all.append(choice)
        blue_count += 1

print('选择了红球:%s 蓝球:%s' %(choice_all[:6], choice_all[6:]))