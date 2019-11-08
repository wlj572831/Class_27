from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def show_publist(request):
    all_publishers = models.Publisher.objects.all()  # 获取Publisher所有对象
    # for all_publisher in all_publishers:
    #     print(all_publisher.id, all_publisher.name)
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
        return redirect('/show_publist')  # 重定向urls中的第一个元素
    return render(request, 'add_pub.html')


def del_pub(request):
    pk = request.GET.get('pk')
    obj = models.Publisher.objects.filter(pk=pk).delete()  # 删除查询到的数据
    return redirect('/show_publist/')


def index(request):
    return render(request, 'index.html')


def alt_pub(request):
    pub_pk = request.GET.get('pk')
    obj = models.Publisher.objects.get(pk=pub_pk)
    # obj = models.Publisher.objects.filter(pk=pub_pk)[0]
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        obj.name = pub_name
        obj.save()
        return redirect('/show_publist/')
    return render(request, 'alt_pub.html', {'obj': obj})
