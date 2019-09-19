#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        self.request

sk = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
sk.serve_forever()