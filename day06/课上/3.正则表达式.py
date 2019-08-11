#!/usr/bin/python
# -*- coding:utf-8 -*-
# create time

# import re
#
# ret = re.search('\d(?:\d)', 'a1,b22,c3456')
# print(ret.group())

from  urllib.request import urlopen

ret = urlopen('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=12&tn=98012088_5_dg&wd=%E7%99%BE%E5%BA%A6%E4%BA%91%E7%9B%98&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E4%25BA%2591%25E7%259B%2598&rsv_pq=b7d0347e000dd0a9&rsv_t=2329xDfvW4UwKGCcUGK%2BmReU46z3GRflmg%2B2XSOxoB1tBu4OCmm2nZ5ReablGZznPrdEaw&rqlang=cn&rsv_enter=0&rsv_dl=tb')
