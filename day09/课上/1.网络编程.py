#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

# 1. 架构的分类及应用
# C/S 架构: 网盘、FTP、微信、QQ
    # c: client
    # s: server

# B/S 架构: 百度、知乎等
    # 对客户端依赖小
    # 需要有浏览器
    # b:browser
    # s:server


# 2. B/S和C/S的特点和优势
# B/S 是特殊的 C/S 架构
# C/S： 安全性高，历史数据的保存
# B/S： 轻量级
# PC端趋势: B/S 统一了入口
# 移动端: 微信小程序\支付宝支付平台垄断

# 3.IP地址范围和作用

# ipv4协议 0.0.0.0-255.255.255.255
# 192.168.11.22
# 172.16.00.00
# 10.0.1.1

# ip地址能够帮助我们找到网络上唯一一台机器
# port能够帮助我们确认一台机器上的唯一一个服务

# 127.0.0.1 特殊的ip地址 本地回环地址
    # 本机中排除网络因素 进行代码的功能性测试
# socket 套接字

