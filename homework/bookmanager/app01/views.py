from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def show_publist(request):
    all_publishers = models.Publisher.objects.all()  # 获取Publisher所有对象
    return render(request, 'publist.html', {'all_publishers': all_publishers})


def add_pub(request):
    '''
    增加出版社信息
    :param request:
    :return:
    '''
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'add_pub.html', {'error': '输入的名称不能为空'})
        ret = models.Publisher.objects.create(name=pub_name)
        print(ret, type(ret))
        return redirect('/show_publist')  # 重定向urls中的第一个元素
    return render(request, 'add_pub.html')


def del_pub(request):
    return render(request, 'publist.html')


def index(request):
    return render(request, 'index.html')
