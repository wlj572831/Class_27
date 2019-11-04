#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：王刘俊

import socket
import json
import os, sys
import struct

local_file = os.path.join(os.path.dirname(__file__), 'local')  # 存储客户端存放文件的绝对路径


def send_dic(sk, dic, protocol=False):  # 自定义发送信息函数
    bytes_d = json.dumps(dic).encode('utf-8')  # 字典转为json格式并编码
    if protocol:
        len_b = len(bytes_d)  # 计算json格式的字典长度
        len_dic = struct.pack('i', len_b)  # 将长度利用struct转化为4个字节
        sk.send(len_dic)  # 发送长度
    sk.send(bytes_d)


def recv_dic(sk, msg_len=1024, protocol=False):
    if protocol:
        bytes_len = sk.recv(4)  # 接收4字节，即将接受字符串的长度
        msg_len = struct.unpack('i', bytes_len)[0]  # 解析字符串长度
    msg = sk.recv(msg_len)  # 根据指定长度接收信息
    str_msg = msg.decode('utf-8')  # 解码
    opt_dic = json.loads(str_msg)
    return opt_dic


def get_usr(opt='login'):  # 接收输入的用户名密码
    usr_dic = {}
    inp_usr = input('请输入用户名:').strip()
    inp_pwd = input('请输入密码:').strip()
    if inp_usr and inp_pwd and opt == 'register':
        cfm_pwd = input('再次确认密码:').strip()
        if inp_pwd == cfm_pwd:  # 发送明文密码
            usr_dic = {'username': inp_usr, 'password': inp_pwd, 'operate': opt}
    elif inp_usr and inp_pwd:
        usr_dic = {'username': inp_usr, 'password': inp_pwd, 'operate': opt}
    return usr_dic


def login(sk):  # 登录
    print('in login')
    ret = get_usr()
    if ret: send_dic(sk, ret, protocol=True)
    res_dic = recv_dic(sk, protocol=True)
    if res_dic['operate'] == 'login' and res_dic['flag']:
        print('登录成功')
    else:
        print('登录失败')
    return res_dic['flag']


def register(sk):  # 注册
    print('in register')
    ret = get_usr('register')
    if ret: send_dic(sk, ret, protocol=True)
    res_dic = recv_dic(sk, protocol=True)
    if res_dic['operate'] == 'register' and res_dic['flag']:
        print('注册成功')
    else:
        print('注册失败')
    return res_dic['flag']


def upload(sk):  # 文件上传
    path = input('请输入要上传的文件路径:').strip()
    if os.path.isfile(path):  # 确保文件是真实存在的
        # 拿到文件名字和大小
        filename = os.path.basename(path)
        filesize = os.path.getsize(path)
        dic = {'filename': filename, 'filesize': filesize, 'operate': 'upload'}
        send_dic(sk, dic, protocol=True)
        # 按指定字节大小发送文件
        with open(path, 'rb') as  f:
            al_size = filesize  # 记录下载进度
            while al_size > 0:
                content = f.read(10240)
                sk.send(content)
                al_size -= len(content)
                processBar(filesize - al_size, filesize)
            print('文件\033[34m%s\033[0m已成功上传' % filename)
    return True


def download(sk):  # 文件下载
    dic = {'operate': 'download'}
    send_dic(sk, dic, protocol=True)  # 发送download 指令
    file_dic = recv_dic(sk, protocol=True)  # 接收文件列表
    print('-' * 30)
    print('序号\t文件名\t文件大小')
    for index, file in enumerate(file_dic, 1):
        print('%s %s\t%s' % (index, file, file_dic[file]))
    print('-' * 30)
    choice = input('请输入要下载的文件名:').strip()
    if choice in file_dic and file_dic[choice]:  # 所选文件存在且大小不为0
        dic = {'filename': choice, 'filesize': file_dic[choice], 'operate': 'download'}
        send_dic(sk, dic, protocol=True)
        # 按指定字节大小接收文件到local目录
        file_path = os.path.join(local_file, choice)
        with open(file_path, 'wb') as f:
            filesize = dic['filesize']
            while filesize > 0:
                content = sk.recv(10240)
                f.write(content)
                filesize -= len(content)  # 发送大小
                processBar(dic['filesize'] - filesize, dic['filesize'])
            print('文件\033[34m%s\033[0m已下载至\033[34m%s\033[0m' % (dic['filename'], local_file))
    else:
        print('文件不存在')
    return True


def processBar(num, total):  # 实现进度条
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush


def myquit(sk):
    dic = {'operate': 'myquit'}
    send_dic(sk, dic, protocol=True)
    print('已断开连接')
    return False


def choose_opt(opt_lst):  # 选择菜单
    print('-' * 30)
    for index, opt in enumerate(opt_lst, 1):
        print(index, opt[0])
    print('-' * 30)
    while True:
        try:
            num = int(input('请输入要选择的操作序号:'))
            return opt_lst[num - 1][1]
        except (ValueError, IndexError):
            print('输入不合法')


sk = socket.socket()
sk.connect(('192.168.31.248', 9000))

opt_lst = [('登录', login), ('注册', register), ('退出', myquit)]
func = choose_opt(opt_lst)
res = func(sk)  # 登录注册
while res:
    opt_lst2 = [('上传', upload), ('下载', download), ('退出', myquit)]
    func = choose_opt(opt_lst2)
    res = func(sk)  # 登录注册
    if not res: break
sk.close()
