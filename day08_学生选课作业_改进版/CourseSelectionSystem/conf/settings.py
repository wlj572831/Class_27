#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun
import os

path = r'D:\Class_27\Class_27\day08_学生选课作业_改进版\CourseSelectionSystem'  # 项目目录

course_file = os.path.join(path, 'db\course')  # 存储课程
user_file = os.path.join(path, r'db\user')  # 存储用户
select_course = os.path.join(path, 'db\select_course')  # 已选课程
