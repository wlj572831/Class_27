#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06
# Author ：王刘俊

import re


# 实现计算器

# 计算
def to_cal(cal, sep):
    '''计算加减乘除'''
    if '/' == sep:
        cal_li = div.search(cal).group().split(sep)  # 利用符号分割字符串
        result = float(cal_li[0]) / float(cal_li[1])
    elif '*' == sep:
        cal_li = mult.search(cal).group().split(sep)  # 利用符号分割字符串
        result = float(cal_li[0]) * float(cal_li[1])
    elif '+' == sep:
        cal_li = add.search(cal).group().split(sep)  # 利用符号分割字符串
        result = float(cal_li[0]) + float(cal_li[1])
    elif '-' == sep:
        cal_li = sub.search(cal).group().split(sep)  # 利用符号分割字符串
        result = float(cal_li[0]) - float(cal_li[1])

    return cal.replace(div.search(cal).group(), str(result))  # 把计算完成的替换掉


str_cal = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
str_cal = str_cal.replace(' ', '')  # 去除表达式内的空格

inner_most = re.compile(r'\([^()]+\)')  # 匹配最内部的小括号 左边是'('，中间是非'(' ')'的字符，结尾只有一个')'
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')  # 匹配小数、整数和除法
mult = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')  # 匹配小数、整数和乘法
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻匹配小数、整数和乘法
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')  # 匹配小数、整数和加法

while inner_most.search(str_cal):  # 当表达式有括号时执行
    current_level = inner_most.search(str_cal).group()  # 最内层括号赋值给current_level
    if div.search(current_level):
        str_cal = str_cal.replace(current_level, to_cal(current_level, '/'))
    elif mult.search((current_level)):
        str_cal = str_cal.replace(current_level, to_cal(current_level, '*'))
    elif add.search((current_level)):
        str_cal = str_cal.replace(current_level, to_cal(current_level, '+'))
    elif sub.search((current_level)):
        str_cal = str_cal.replace(current_level, to_cal(current_level, '-'))
    # elif   # 检查表达式里是否还有运算，没有就脱括号，进行下一级运算,这里不会写--
    print(str_cal)
