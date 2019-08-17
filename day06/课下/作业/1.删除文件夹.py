#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import os


# 递归删除非空文件夹
def remove_dir(path):
    if os.path.exists(path) and os.path.isdir(path):  # 判断是否给出合法的文件夹
        if os.listdir(path):  # 判断目录是否为空
            for i in os.listdir(path):  # 删除非空文件夹下的所有文件及文件夹
                i = os.path.join(path, i)
                if os.path.isdir(i):
                    remove_dir(i)
                else:
                    os.remove(i)  # 如果是文件，则直接删除
                    print('删除了文件:%s' % i)
            if os.path.exists(path) and len(os.listdir(path)) == 0:
                print('删除了空文件夹:%s' % path)
                os.rmdir(path)  # 如果目录为空，则直接删除空文件夹
    else:
        print('请给出有效的文件夹')

if __name__ == '__main__':
    path = r'E:\安全\temp111111111'
    remove_dir(path)
