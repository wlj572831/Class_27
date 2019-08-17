#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wang_liu_jun

import os
import sys


# 文件拷贝
def copy(sour_folder, des_folder):
    if os.path.exists(sour_folder):  # 判断文件目录是否存在
        if os.path.isdir(sour_folder):  # 如果是文件夹
            for f in os.listdir(sour_folder):
                sour = os.path.join(sour_folder, f)
                des = os.path.join(des_folder, f)
                if os.path.isfile(sour):
                    if not os.path.exists(des_folder):  # 目标文件夹不存在就创建
                        os.makedirs(des_folder)

                    # 如果文件不存在，或者不相同，则覆盖
                    if not os.path.exists(des) or (
                            os.path.exists(des) and (os.path.getsize(des) != os.path.getsize(sour))):
                        with open(sour, mode='rb') as f1, open(des, mode='wb') as f2:
                            f2.write(f1.read())
                        print('已复制文件:%s' % sour)
                if os.path.isdir(sour_folder):
                    copy(sour, des)
        else:  # 如果是文件
            with open(sour_folder, mode='rb') as f1, open(des_folder, mode='wb') as f2:
                f2.write(f1.read())
    else:
        print('请输入合法的文件或文件夹')


# 获取文件大小
def dir_size(path):
    if os.path.isdir(path):
        sumsize = 0  #
        name_lst = os.listdir(path)  # ['demo']
        for name in name_lst:
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path):
                sumsize += os.path.getsize(full_path)  # sum_size = 0+1200 = 1200
            else:
                sumsize += dir_size(full_path)
        return sumsize
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:
        print('找不到文件')


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
    if sys.argv[1] == 'copy':  # 复制
        copy(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'size':  # 计算大小
        sum_size = dir_size(sys.argv[2])
        print('文件或文件夹大小大小为:%s' % sum_size)
    elif sys.argv[1] == 'move':  # 移动文件，先拷贝，再移除
        copy(sys.argv[2], sys.argv[3])
        remove_dir(sys.argv[2])
    elif sys.argv[1] == 'rename':  # 重命名
        os.rename(sys.argv[2], sys.argv[3])
    else:
        print('指令不正确')
