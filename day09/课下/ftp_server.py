#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import json
import struct
import socketserver
import hash

user_db = r'D:\Class_27\Class_27\day09\课下\db\user'



#
# class MyServer(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf-8'))
#         Flag = True
#         while Flag:
#             data = conn.recv(1024).decode('utf-8')
#             if data == 'exit':
#                 Flag = False
#             elif data == '0':
#                 conn.sendall(bytes('通过可能会被录音.balabala一大推', encoding='utf-8'))
#             else:
#                 conn.sendall(bytes('请重新输入.', encoding='utf-8'))
#
#
# if __name__ == '__main__':
#     server = socketserver.ThreadingTCPServer(('127.0.0.1', 9091), MyServer)
#     server.serve_forever()
