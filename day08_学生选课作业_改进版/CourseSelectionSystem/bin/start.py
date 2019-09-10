#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun
import os
import sys

base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件所在目录
sys.path.append(base_dir)

from core import main as m
from core.course import *
from core.student import *

# print(sys.modules[stu])

if __name__ == '__main__':
    m.main()
