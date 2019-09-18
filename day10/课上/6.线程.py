#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 创建一个进程是非常浪费时间和资源
# 线程 -- 轻型进程
# 同一进程内多个线程内存是共享的
# 线程的开启速度比进程快
# 线程也可以利用多核

# 正常的进程和线程之间的区别:
    # 进程是内存隔离
    # 线程之间 内存共享的

# python的线程
    # cpython解释器下的多现场
    # 同一个进程下的多个线程不能被CPU同时执行
    # 多个线程之间的IO操作仍然会被规避

# 大部分,只要涉及到文件\网络操作，多线程会比多进程快些
# 真正能够参与计算的不过就是那几个CPU
    # 规避IO操作，让IO操作的时间尽量的缩短
    # 或者尽量的复用这部分时间

import time
import requests
from threading import Thread

url_lst = [
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.qq.com',
    'http://www.163.com',
    'http://www.taobao.com',
    'http://www.jd.com',
    'http://www.tmall.com',
    'http://www.cnblogs.com',
    'http://www.mi.com',
    'http://www.luffycity.com',
]

def get_url(url):
    ret = requests.get(url)

start_t = time.time()
t_lst = []
for url in url_lst: # 开启10个线程，每个线程各自去请求一个网页
    t = Thread(target=get_url, args=(url,))
    t.start()
    t_lst.append(t)

print(time.time() - start_t)

# 普通访问
# start_t = time.time()
# for url in url_lst:
#     requests.get(url)
# print(time.time() - start_t)

# jypython Python语言 最终是被JAVA解释器的 而java解释器
# cpython 有一个全局解释器锁，GIL是由于GC机制和解释器型语言双重导致了必须要在解释器中加锁
    #导致了在一个进程中不能有多个进程同时访问CPU
    # 虽然不能同时做计算会影响一些效率，但是绝大部分情况下线程仍然能够非常好的 提高程序的效率
