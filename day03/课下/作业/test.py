#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun



title_list = ['序号', '代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '最高', '最低', '今开', '昨收', '量比', '换手率', '市盈率',
              '市净率']
obj = input('')
tu = obj.split('>')
print(tu)
find_index = title_list.index('振幅')
if ('亿' in tu[1]) or ('万' in tu[1]) or ('%' in tu[1]):  # 1
    print('1')
print(find_index)