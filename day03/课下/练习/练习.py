#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊
# Creation time : 2019-7-26

# 练习1 任一个英文的纯文本文件，统计其中的每个单词出现的个数，注意是每个单词。。
# with open('file/count_word.txt',encoding='utf-8') as f:
#     content = f.read()
#
# ch = ''
# dic = {}
# for i in content:
#     if i.isalpha():
#         ch += i
#     else:
#         if ch in dic:
#             dic[ch] += 1
#         else:
#             dic[ch] = 1
#         ch = ''
# print(dic)


# 练习2 写函数，计算传入数字参数的和。（动态传参）
# def count(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# sum = count(1, 2, 3, 4, 5)
# print(sum)

# 练习3 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
# import os
# path = 'file/'
# def change_file(file, source, target):
#     file = path + file
#     print(file)
#     with open(file, encoding='utf-8') as  f1, open(file+'.bak', mode='w',encoding='utf-8') as f2:
#         content = f1.read()
#         content = content.replace(source, target)
#         f2.write(content)
#     os.remove(file)
#     os.rename(file+'.bak', file)
#
# change_file('change_file.txt', 'cheese', 'CHEESE')


# 练习4 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
#
# def check_space(a):
#     for i in a:
#         if type(i) is int or type(i) is float: continue
#         if ' ' in i:
#             return True
#     return False
#
#
# list = [1, 2, 3, 4, ' ']
# str = 'check this str'
# tu = ('a', 'b', 'c', 'd d')
# a = check_space(list)
# b = check_space(str)
# c = check_space(tu)
# print(a, b, c)

# 练习5 写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容（对value的值进行截断），并将新内容返回给调用者，注意传入的数据可以是字符、list、dict

# def trun(obj):
#     for i in obj:
#         if len(obj[i]) > 2:
#             obj[i] = obj[i][0:2]
#     return obj
# dic = {'a':'abcd', 'b':'bcda', 'c': 'dddd'}
# result = trun(dic)
# print(result)

# 练习6 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
# type_ = ('红心', '花草', '黑桃', '方块')
# num = range(1, 14)
#
#
# def poker(type_, num):
#     li = []
#     for i in num:
#         for j in type_:
#             tu = (i, j)
#             li.append(tu)
#     return li
#
#
# li = poker(type_, num)
# print(li)

# 练习7 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 　例如:minmax(2,5,7,8,4)
# 　返回:{‘max’:8,’min’:2}

# def sort(*args):
#     dic = {}
#     dic['max'] = max(args)
#     dic['min'] = min(args)
#     return dic
#
# result = sort(1,2,3,4,5,6,7)
# print(result)

# 练习8 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积
# 计算圆形面积
# def cir_area(param):
#     area = 3.14 * param * param
#     return area
#
#
# # 计算长方形/正方形面积
# def squ_area(*param):
#     area = param[0] * param[1]
#     return area
#
#
# def area(form, *param):
#     if form == '圆形':
#         return cir_area(*param)
#     elif form == '正方形' or form == '长方形':
#         return squ_area(*param)
#     return
#
# area = area('圆形', 5)
# print(area)

# 练习9 写函数，传入一个参数n，返回n的阶乘
#
# def cal(num):
#     if num == 1:
#         return 1
#     return num * cal(num - 1)
#
#
# result = cal(7)
# print(result)

# 练习10 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# a.通过哪个内置函数可以计算购买每支股票的总价

# 用自定义函数实现
# def traversal(portfolio):
#     li = []
#     for i in portfolio:
#         dic ={}
#         key = i['name']
#         value = i['shares'] * i['price']
#         dic[key] = value
#         li.append(dic)
#     return li
# result = traversal(portfolio)
# print(result)

# 用map 实现
# result = map(lambda dic:{dic['name']:(dic['shares']*dic['price'])}, portfolio)

# b.用filter过滤出，单价大于100的股票有哪些
# res = filter(lambda dic:dic['price']>100,portfolio)
# print(list(res))

# 练习11 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请将以字母“a”开头的元素的首字母改为大写字母；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# def upp(str):
#     if str.startswith('a'):
#         return str.capitalize()
#     return str
#
# result = list(map(upp, li))
# print(result)

# 练习12 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请以列表中每个元素的第二个字母倒序排序；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# print(list(sorted(li,key=lambda x :x[1],reverse=True)))

# 练习13 有名为poetry.txt的文件，其内容如下，请删除第三行；
# import os
# path = 'file/poetry.txt'
# with open(path,encoding='utf-8') as f1,open(path + '.bak',mode='w',encoding='utf-8') as f2:
#     line = f1.readlines()
#     del line[2]
#     line = ''.join(line)
#     f2.write(line)
# os.remove(path)
# os.rename(path + '.bak',path)

# 练习14 有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”alex”,
# 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在；

# import os
# path = 'file/username.txt'
# with open(path, mode='r', encoding='utf-8') as  f1, open(path + '.bak', mode='w', encoding='utf-8') as f2:
#     content = f1.read()
#     li = content.split('\n')
#     if 'alex' in li:
#         print('该用户已存在')
#     else:
#         li.append('alex')
#     content = '\n'.join(li)
#     f2.write(content)
# os.remove(path)
# os.rename(path+'.bak', path)

# 练习15 有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；

# import os
# path = 'file/user_info.txt'
# with open(path, mode='r', encoding='utf-8') as  f1, open(path + '.bak', mode='w', encoding='utf-8') as f2:
#     cotent = f1.readlines()
#     print(cotent)
#     for i in cotent:
#         if '100003' in i:
#             pass
#         else:
#             f2.write(i)
# os.replace(path + '.bak', path)

# 练习16 有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；
#
# import os
# path = 'file/user_info.txt'
# update_id = '100002'
# update_name = 'alex li'
# with open(path, mode='r', encoding='utf-8') as  f1, open(path + '.bak', mode='w', encoding='utf-8') as f2:
#     for line in f1:
#         if update_id in line:
#             line = ','.join([update_name, update_id])
#             f2.write(line + '\n')
#         else:
#             f2.write(line)
# os.replace(path + '.bak', path)
