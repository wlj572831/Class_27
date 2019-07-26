#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# Creation time : 2019-7-26

import re

# 1. 读取文件内容
with open('stock_data.txt', encoding='utf-8') as  f:
    content = f.read()

# 2.把数据转化成列表, 去除不需要的内容(相关链接那栏)
cont_list = content.split('\n')
for i in range(len(cont_list)):
    cont_list[i] = cont_list[i].split('\t')
    del cont_list[i][3]
# 3.定义表头
title_list = ['序号', '代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '最高', '最低', '今开', '昨收', '量比', '换手率', '市盈率',
              '市净率']


# 4.定义函数，用来判断是否可以把字符串转化成小数
def is_float(obj):
    try:
        float(obj)
    except:
        return False
    else:
        return True


# 5.负责统一将亿、万，%转换成数字
def to_num(obj):
    if '万' in obj:
        obj = obj.replace('万', '')
        obj = float(obj)
        obj *= 10000
        return obj
    if '亿' in obj:
        obj = obj.replace('亿', '')
        obj = float(obj)
        obj *= 100000000
        return obj
    if '%' in obj:
        obj = obj.replace('%', '')
        obj = float(obj)
        return obj
    result = obj
    return result
# 6.列表内容格式化
'''
1. 把万、亿统一转换成数字或者浮点型类型
2. 把数字、float类型的进行转换,第一列序号和第二列编号不转换
3. 换手率中有 '-'标识符，方便比较，统一转换成0
'''
for i in range(len(cont_list)):
    for j in range(3, len(cont_list[i])):
        # if ('亿' in cont_list[i][j]) or ('万' in cont_list[i][j]): #1
        #     cont_list[i][j] = to_num(cont_list[i][j])
        if is_float(cont_list[i][j]):   #2
            cont_list[i][j] = float(cont_list[i][j])
        if cont_list[i][j] == '-':  #3
            cont_list[i][j] = 0

# 7.模糊查询
def fuzzy_(name):
    find_result = []
    for i in cont_list:
        if name in i[2]:
            find_result.append(i)
    return find_result, len(find_result)

# 8.比较查询
'''
1.将输入的结果根据<>分割成“查询项”和数量对比，根据查询项在表头内搜索，获取到下标，根据下标去列表中取相应的数值
2.两者进行比较，将符合条件的加入新列表返回
'''
def compare(obj):
    if obj.count('<') == 1:
        tu = obj.split('<')
        for i in tu:i=i.strip()
        if tu[0] in title_list:
            find_index = title_list.index(tu[0])
            if '%' in tu[1]:
                tu[1] = tu[1].strip('%')
            if ('亿' in tu[1]) or ('万' in tu[1]) or ('%' in tu[1]):  # 1
                tu[1] = to_num(tu[1])
            if is_float(tu[1]):
                tu[1] = float(tu[1])
            find_result = []
            for i in cont_list:
                if to_num(i[find_index]) < tu[1]:
                    find_result.append(i)
            return find_result, len(find_result)
        else:
            return
    elif obj.count('>') == 1:
        tu = obj.split('>')
        if tu[0] in title_list:
            find_index = title_list.index(tu[0])
            # if ('亿' in tu[1]) or ('万' in tu[1])or ('%' in tu[1]):  # 1
            #     tu[1] = to_num(tu[1])
            if is_float(tu[1]):
                tu[1] = float(tu[1])
            find_result = []
            for i in cont_list:
                print(type(i[find_index]), type(tu[1]))
                if to_num(i[find_index]) > to_num(tu[1]):
                    find_result.append(i)
            return find_result, len(find_result)
        else:
            return
    else:
        return
while True:
    choice = input('股票查询接口(b退出)>>:').strip()
    '''
    1.退出
    2.如果与'>' '<'号，就判断为比较查询
    3.其他默认为名称的模糊查询
    '''
    if choice.upper() == 'B':
        break
    elif '>' in choice or '<' in choice:
        if compare(choice):
            find_result, count = compare(choice)
            for i in find_result: print(i)
            print('共找到%s条'%count)
        else:
            print('所查询的项不存在')
    else:
        find_result, count = fuzzy_(choice)
        for i in find_result: print(i)
        print('共找到%s条'%count)
