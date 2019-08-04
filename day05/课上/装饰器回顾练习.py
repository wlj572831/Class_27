#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create Time

import time


def wapper(filename):
    def inner(*args, **kwargs):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if 'shop' in filename.__name__:
            with open('file/log.txt', encoding='utf-8', mode='a') as f:
                f.write('时间:%s 执行了 %s 函数\n' % (now_time, filename.__name__))
        else:
            print(filename.__name__)
        ret = filename(*args, **kwargs)
        return ret

    return inner


@wapper
def home():
    print('我是index')
    return True


@wapper
def shopp_car():
    print('我是shopp_car')


@wapper
def shop():
    print('我是shop')

shop()