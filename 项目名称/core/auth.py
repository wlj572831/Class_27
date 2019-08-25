from conf import settings


def login():
    print('登陆了')
    with open(settings.userinfo, 'r') as f:
        print(f.read())
