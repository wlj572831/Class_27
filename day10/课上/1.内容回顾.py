#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 网络编程
# 1.概念
    # osi 七层协议：
        # 应用层(表示层、会话层): 你写好的具体的服务代码
        # 传输层： TCP/UDP协议 端口信息（确认两边的程序都能被os找到）
            # TCP 面向连接通信，并且数据之间无边界，可靠
                # 先建立连接: 三次握手
                # 基于连接通信：每一条信息都有回执
                    # struct 模块解决黏包问题
                # 断开连接: 四次挥手
            # UDP 不需要提前建立链接，数据之间有边界，不可靠
                # 不需要提前建立\断开连接
                # 只要知道对方的IP和端口直接发送信息就可以
        # 网络层：  IP地址，会变，标识两台机器之间的关系，由路由器负责处理
        # 数据链路层:    mac地址，终身不变，由交换机处理
        # 物理层:  转换成二进制
# 2.代码
    # socket

# tcp-server
import socket

sk =socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept() # 接收客户端请求连接- 三次握手
conn.send() #只接受字节类型
conn.recv() #可指定接收最大字节数
conn.close()    # 关闭了和某一个客户端的连接 -- 四次挥手

sk.close()  # 关闭了整个网络通信的服务端

# tcp-client
import socket
sk =socket.socket()
sk.connect(('127.0.0.1',9001))  #三次握手
msssage = sk.recv() #可指定接收最大字节数
sk.send()
sk.close()  #客户端断开连接

# udp-server
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001)) # 创建服务端
msg,addr = sk.recvfrom()    # 接收消息和IP地址
sk.sendto(msg,addr)     # 给指定IP发送消息

# udp-client
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto(msg, ('127.0.0.1',9001))
msg.server_addr = sk.recvfrom()
sk.close()

# socketserver
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request

server = socketserver.ThreadingTCPServer(Myserver, ('127.0.0.1',9001))
server.serve_forever()