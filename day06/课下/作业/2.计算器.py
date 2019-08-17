#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wang_liu_jun
import re


def mul_div(atom_exp):
    '''计算乘除'''
    if '*' in atom_exp:
        a, b = atom_exp.split('*')
        return float(a) * float(b)
    elif '/' in atom_exp:
        a, b = atom_exp.split('/')
        return float(a) / float(b)


def add_sub(no_bracket_exp):
    '''计算加减'''
    ret_li = re.findall('[-+]?\d+(?:\.\d+)?', no_bracket_exp)
    sum_count = 0
    for num in ret_li:
        sum_count += float(num)
    return sum_count


def exp_format(exp):
    '''格式化表达式'''
    exp = exp.replace('--', '+')
    exp = exp.replace('+-', '-')
    exp = exp.replace('-+', '-')
    exp = exp.replace('++', '+')
    return exp


# 计算最内侧括号中的结果
def cal_oper(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
        if ret:
            ret_exp = ret.group()
            result = str(mul_div(ret_exp))
            exp = exp.replace(ret_exp, result)
        else:
            break
    exp = exp_format(exp)
    sum_count = add_sub(exp)
    return sum_count


str_cal = '1 - 2 * ( (60-30 +(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )*(-40/5)) - (-4*3)/ (16-3*2) )'
if __name__ == '__main__':
    str_cal = str_cal.replace(' ', '')
    while True:
        ret = re.search('\([^()]+\)', str_cal)
        if ret:
            res = ret.group()
            ret = str(cal_oper(res))
            str_cal = str_cal.replace(res, ret)
        else:
            break
    fina_res = cal_oper(str_cal)
    print('最终结果为:%s' % fina_res)
