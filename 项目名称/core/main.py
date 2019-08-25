# 整个程序的逻辑
from core import auth


def entry_point():
    print('in main')
    auth.login()

# 成功
# 'F:\\python自动化27期\\项目名称\\core',
# 报错
# ['F:\\python自动化27期\\项目名称\\bin','F:/python自动化27期/项目名称'}
