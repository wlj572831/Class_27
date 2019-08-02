#!/usr/bin/python
# coding:utf-8
# CreateTime: 2019-08-02

welcome = '''欢迎来到博客园首页
1:请登录
2:请注册
3:文章页面
4:日记页面
5:评论页面
6:收藏页面
7:注销
8:退出程序'''



login_status = False  # 登录状态


def wapper(funcname):
    # @wraps(funcname)
    global login_status

    def inner(*args, **kwargs):
        if login_status is False:
            print('您必须在登录之后才能访问此页面')
            login()
        if login_status:
            ret = funcname(*args, **kwargs)
            print('''3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面''')
            return ret

    return inner

def val():
    '''登录验证'''
    global login_status
    with open('register', mode='r', encoding='utf-8') as f:
        input_usr = input('用户名:').strip()
        input_pwd = input('密码:').strip()
        for line in f:
            if line:
                line = line.strip()
                usr, pwd = line.split('|')
                if input_usr == usr and input_pwd == pwd:
                    login_status = True
                    return

def login():
    print('欢迎进入登录界面')
    count = 0
    while login_status is False and count < 3:
        val()
        count += 1
        if count >= 3:
            exit('密码错误超过三次，结束程序')
    if login_status:
        menu_dic

menu = {1:['1:请登录',login, ]}
@wapper
def article():
    '''文章页面'''
    print('欢迎xx用户访问文章页面')

@wapper
def diary():
    '''日记页面'''
    print('欢迎xx用户访问日记页面')

@wapper
def comments():
    '''评论页面'''
    print('欢迎xx用户访问评论页面')


@wapper
def collection():
    '''收藏页面'''
    print('欢迎xx用户访问收藏页面')



menu_dic = {
    1: login,
    2: 'registered',
    3: article,
    4: diary,
    5: comments,
    6: collection,
    7: '注销',
    8: '退出'
}
while True:
    print('-' * 20)
    print(welcome)
    print('-' * 20)
    choice = int(input('请选择:').strip())
    menu_dic[choice]()
