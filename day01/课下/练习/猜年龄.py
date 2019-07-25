'''
练习1：猜年龄游戏 (10分钟)
要求：
允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
'''
#
# #定义真实年龄
# age = 22
#
# #循环次数初始值
# count = 0
#
# while count < 3 :
#     #用户输入年龄并转为int类型
#     input_age = int(input('猜年龄:'))
#     if input_age == age:
#         exit('恭喜您猜对了')
#     #循环次数+1
#     count += 1


'''
练习2：猜年龄游戏升级版 
要求：
1. 定义循环初始值，while 循环内要求用户输入年龄：
    如猜对，则退出程序
    如猜错，则每次循环将循环次数count +1 
2. 把第一步的while 循环嵌套进条件为choice的while循环中，
  当第一层循环超过三次(即count等于3)时，要求用户输入是否继续游戏(y/n)
    如果输入y: 将count初始化为0, 重新进行第一步循环
    如果输入n: 将choice变为False，结束循环  
'''
#
# #定义真实年龄
# age = 22
#
# #choice 根据用户输入来选择是否继续游戏，默认True
# choice = True
#
# #循环次数初始值为0
# count = 0
#
# while choice:
#     while count < 3 :
#         #用户输入年龄并转为int类型
#         input_age = int(input('猜年龄:'))
#         #如果猜对直接退出程序
#         if input_age == age:
#             exit('恭喜您猜对了')
#         count += 1
#
#     #用户选择是否继续
#     choice_input = input('是否继续(y/n):')
#     #输入的内容全部转为大写，方便比较
#     choice_input = choice_input.upper()
#     #用户输入'y'时，则初始化循环次数
#     if choice_input == 'Y':
#         count = 0
#     #用户输入'n'时,choice为False,中止循环
#     elif choice_input == 'N':
#         choice = False
#     else:
#         print('输入指令错误')