#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

import os
import sys
base_name = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_name)

from core import ftp_server as fs
fs.main()

