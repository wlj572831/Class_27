#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socketserver
import json
import hashlib
import os, sys
import struct

remote_file = os.path.join(os.path.dirname(__file__), 'remote')  # 存储服务端存放文件的绝对路径


class Auth:

    @classmethod
    def register(cls, usr_dic):  # 服务端注册校验结果
        pwd = cls.get_md5(usr_dic)
        with open('userinfo', 'a', encoding='utf-8') as f:
            f.write('%s|%s\n' % (usr_dic['username'], pwd))
        result_dic = {'operate': 'register', 'flag': True}
        return result_dic

    @classmethod
    def login(cls, usr_dic):  # 服务端登录校验结果
        pwd = cls.get_md5(usr_dic)
        with open('userinfo', encoding='utf-8') as f:
            for line in f:
                if line:
                    userinfo = line.strip().split('|')
                    if userinfo[0] == usr_dic['username'] and userinfo[1] == pwd:
                        result_dic = {'operate': 'login', 'flag': True}
                        break
            else:
                result_dic = {'operate': 'login', 'flag': False}
        return result_dic

    @staticmethod
    def get_md5(usr_dic):  # 根据用户名加盐对密码进行md5加密
        md5 = hashlib.md5(usr_dic['username'].encode('utf-8'))
        md5.update(usr_dic['password'].encode('utf-8'))
        pwd = md5.hexdigest()
        return pwd

    @staticmethod
    def myquit(opt_dic):  # 退出
        opt_dic['flag'] = False
        return opt_dic


class Myserver(socketserver.BaseRequestHandler):
    def mysend(self, dic, protocol=False):  # 发送信息
        str_d = json.dumps(dic).encode('utf-8')
        if protocol:
            len_b = len(str_d)  # 计算json格式的字典长度
            len_dic = struct.pack('i', len_b)  # 将长度利用struct转化为4个字节
            self.request.send(len_dic)  # 发送长度
        self.request.send(str_d)

    def myrecv(self, msg_len=1024, protocol=False):  # 自定义协议接收数据
        if protocol:
            bytes_len = self.request.recv(4)  # 接收4字节，即将接受字符串的长度
            msg_len = struct.unpack('i', bytes_len)[0]  # 解析字符串长度
        msg = self.request.recv(msg_len)  # 根据指定长度接收信息
        str_msg = msg.decode('utf-8')  # 解码
        opt_dic = json.loads(str_msg)
        return opt_dic

    @staticmethod
    def processBar(num, total):  # 实现进度条
        rate = num / total
        rate_num = int(rate * 100)
        if rate_num == 100:
            r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
        else:
            r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush

    def upload(self, opt_dic):  # 上传文件
        filename = opt_dic['filename']
        file_path = os.path.join(remote_file, filename)
        # 按指定大小依次接收文件内容，并写入新文件
        with open(file_path, 'wb') as f:
            filesize = opt_dic['filesize']
            while filesize > 0:
                content = self.request.recv(10240)
                f.write(content)
                filesize -= len(content)
                self.processBar(opt_dic['filesize'] - filesize, opt_dic['filesize'])
        print('已成功发送\033[34m%s\033[0m,共计\033[34m%s\033[0m字节' % (filename, opt_dic['filesize']))
        opt_dic['flag'] = True
        return opt_dic

    def download(self, opt_dic):  # 下载文件
        # 将remote 文件夹下的文件名和大小写入字典，准备发送到客户端
        file_dic = {}
        for file in os.listdir(remote_file):
            file_path = os.path.join(remote_file, file)
            file_dic[file] = os.path.getsize(file_path)
        self.mysend(file_dic, True)
        dic = self.myrecv(protocol=True)
        file_path = os.path.join(remote_file, dic['filename'])
        with open(file_path, 'rb') as  f:
            filesize = dic['filesize']
            while filesize > 0:
                content = f.read(10240)
                self.request.send(content)
                filesize -= len(content)
                self.processBar(dic['filesize'] - filesize, dic['filesize'])
        print('已发送文件\033[34m%s\033[0m 共计\033[34m%s\033[0m字节' % (dic['filename'], dic['filesize']))
        opt_dic['flag'] = True
        return opt_dic

    def myquit(self, opt_dic):  # 退出
        opt_dic['flag'] = False
        return opt_dic

    def handle(self):  # 重写handle方法
        while True:
            try:
                usr_dic = self.myrecv(protocol=True)  # 接收指令
                if hasattr(Auth, usr_dic['operate']):  # 反射注册、登录验证
                    result_dic = getattr(Auth, usr_dic['operate'])(usr_dic)
                if result_dic['flag'] and usr_dic['operate'] != 'myquit':
                    self.mysend(result_dic, protocol=True)
                while result_dic['flag']:
                    opt_dic = self.myrecv(protocol=True)
                    if hasattr(Myserver, opt_dic['operate']):  # 反射上传、下载
                        result_dic = getattr(Myserver, opt_dic['operate'])(self, opt_dic)
                        if not result_dic['flag']: break
                print('客户端%s已断开连接' % self.client_address[0])
                break
            except ConnectionResetError:
                print('客户端%s已断开连接:' % self.client_address[0])
                break


sk = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
sk.serve_forever()
