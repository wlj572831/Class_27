#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06


li = [1, 2, 3, 5, 4, 55, 67, 50, 70, 66, 99, 80, 90, 100, 500, 45, 30]
li.sort()
print(li)
find_num = 6
max_index = len(li)
min_index = 0
mid_index = (max_index + min_index) // 2
# 第一次查找
count = 0
while True:
    count += 1
    if find_num > li[mid_index]:
        min_index = mid_index + 1
        mid_index = (max_index + min_index) // 2
    elif find_num < li[mid_index]:
        max_index = mid_index
        mid_index = (max_index + min_index) // 2
    else:
        if li[mid_index] == find_num:
            print('该数位置为:%s,共查找%s次' % (mid_index, count))
            break
        else:
            print('不存在')
            break


