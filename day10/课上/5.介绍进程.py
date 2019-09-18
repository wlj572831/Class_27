#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun


# 进程是计算机中资源分配的最小单位
# 所有的计算机中的内存资源 文件资源 程序代码

# 进程可以被操作系统调度\CPU执行
# 一个进程在创建的时候 必须创建大量内存资源 文件资源 程序代码
# 一个进程在结束的时候 必须被销毁
# 谁来销毁这个进程？
    # 一个进程总是被他的父进程摧毁掉
# 进程与进程之间有一个父子关系
    # 父进程要负责销毁子进程
# 你在你写的python代码中开启的所有进程都是子进程
# 而你写的这个程序本身是这些子进程的父进程
from multiprocessing import  Process    # 1.导入 模块

def func(a, b): # 2.把需要子进程执行的写入到函数里
    print('一个子进程', a, b)

if __name__ == '__main__':
    p = Process(target=func, args=(1, 2))   # 3.创建一个进程对象
    p.start()   # 4. 执行子进程中代码
    p.join()    # 阻塞 等待子进程执行完毕