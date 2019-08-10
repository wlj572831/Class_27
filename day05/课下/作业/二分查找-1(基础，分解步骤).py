#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06
# Author ：王刘俊


li = [1, 2, 3, 4, 55, 67, 50, 70, 66, 99, 80, 90, 100, 500, 45, 30]
li.sort()

find_num = 45
max_index = len(li)
min_index = 0
mid_index = (max_index + min_index) // 2

# 第一次查找
if find_num > li[mid_index]:
    min_index = mid_index
    mid_index = (max_index + min_index) // 2
elif find_num < li[mid_index]:
    max_index = mid_index
    mid_index = (max_index + min_index) // 2
else:
    print(mid_index)

# 第二次查找
if find_num > li[mid_index]:
    min_index = mid_index
    mid_index = (max_index + min_index) // 2
elif find_num < li[mid_index]:
    max_index = mid_index
    mid_index = (max_index + min_index) // 2
else:
    print(mid_index)

# 第三次查找
if find_num > li[mid_index]:
    min_index = mid_index
    mid_index = (max_index + min_index) // 2
elif find_num < li[mid_index]:
    max_index = mid_index
    mid_index = (max_index + min_index) // 2
else:
    print(mid_index)

# 第四次查找
if find_num > li[mid_index]:
    min_index = mid_index
    mid_index = (max_index + min_index) // 2
elif find_num < li[mid_index]:
    max_index = mid_index
    mid_index = (max_index + min_index) // 2
else:
    print(mid_index)
# ... 直到找到为止
