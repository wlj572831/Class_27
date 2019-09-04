#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

# 并发:
import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            conn.send(b'hello')


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8989), Myserver)
server.serve_forever()
#
# import socketserver
#
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         while True:
#             conn.send(b'hello')
#
#
# server = socketserver.ThreadingTCPServer(('127.0.0.1', 9001), Myserver)
# server.serve_forever()
