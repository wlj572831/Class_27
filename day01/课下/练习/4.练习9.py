#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author ：wangliujun

# 现有如下两个变量,请简述 n1 和 n2 是什么关系?
n1 = 1
n2 = n1

# 1.当定义 n1 = 1时，pyhon就开辟了一个内存空间存储数字1,
#   变量n1指向这个内存空间。根据 id()方法可以看出n1 和 1指向的都是1的内存地址
print(id(1))
print(id(n1))
# 2.当n2 = n1 把n1的值赋给n2时, 按道理说 n2应该指向n1。
#   但通过改变n1的值发现，n2并不会随着n1的变化而变化，再观察下id(n2)跟id(1)相等
#   由此可见，n2在被赋值的时，实际是直接指向存储数字1的内存空间的
n1 = 123
print(id(n2),n2)
print(id(n1))
# 总结: 当执行 n2 = n1 时, 是定义n2变量，n2指向 n1指向的内存的地址，而不是n1