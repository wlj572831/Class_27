# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from app001 import models


def index(request):
    # ret = models.User.objects.all()  # 1.获取所有QuerySet 对象列表
    ret = models.User.objects.filter(password='alex3714')  # 2.获取所有符合条件的结果,查不到不报错
    for i in ret:
        print(i.username, i.password, type(i.username))

    # ret = models.User.objects.get(password='123456')  # 3.查询符合条件的结果，查到多个、查不到均会报错
    # print(ret.username,ret.password)
    return HttpResponse('ok')
    # return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user, pwd)
        if user == 'alex' and pwd == 'alex3714':
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error': '输入用户名或密码错误'})
    return render(request, 'login.html')
