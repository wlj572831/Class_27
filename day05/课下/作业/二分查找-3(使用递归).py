#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06


li = [1, 2, 3, 4, 55, 67, 50, 70, 66, 99, 80, 90, 100, 500, 45]
li.sort()


#
# # PS： 自己写的二分查找，最后发现如果对返回值进行了运算，查找不存在的数字的时候就没办法做处理了，还是有很多需要改进的地方。
def find(li, find_num):
    max_index = len(li) - 1
    min_index = 0
    mid_index = (max_index + min_index) // 2
    if find_num > li[mid_index]:
        li = li[mid_index + 1:]  # 如果要找的数在右半边，将右半边的数传进find()函数，然后返回的下标加上左边的长度
        ret = find(li, find_num) + mid_index + 1
    elif find_num < li[mid_index]:
        li = li[:mid_index]  # 如果要找的数在左半边，就无需考虑右边下标
        ret = find(li, find_num)
    elif find_num == li[mid_index]:
        ret = mid_index
    return ret


index = find(li, 45)
print(index)

# 女神版本的二分查找
# def search(num, l, start=None, end=None):
#     start = start if start else 0
#     end = end if end is not None else len(l) - 1
#     mid = (end - start) // 2 + start
#     if start > end:
#         return None
#     elif l[mid] > num:
#         return search(num, l, start, mid - 1)
#     elif l[mid] < num:
#         return search(num, l, mid + 1, end)
#     elif l[mid] == num:
#         return mid
# #
# #
# print(search(55, li))
