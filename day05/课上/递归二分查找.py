#!/usr/bin/python
# coding:utf-8
# Create Time 2019-08-06

li = [1, 2, 3, 4, 55, 67, 50, 70, 66, 99, 80, 90, 100, 500, 45]
li.sort()


def search(li, num, start=None, end=None):
    start = start if start else 0
    end = end if end else len(li) - 1
    mid = (end - start) // 2 + start
    if start > end:
        return None
    if li[mid] > num:
        return search(li, num, start, mid - 1)
    elif li[mid] < num:
        return search(li, num, mid + 1, end)
    elif li[mid] == num:
        return mid


a = search(li, 55)
print(a)
