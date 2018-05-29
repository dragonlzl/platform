# -*- coding:utf-8 -*-

from django.http import HttpResponse
from cmdb.models import UserInfo
from cmdb.models import Test

def data_add(request):
    #test1 = Test(name='runoob')
    test1 = UserInfo(user = "test123",pwd = "test321")
    test1.save()
    #UserInfo.objects.all().delete()
    return HttpResponse("<p>数据增加成功！！</p>")

def data_all_del(request):
    #test1 = Test(name='runoob')
    # test1 = UserInfo(user = "test123",pwd = "test321")
    # test1.save()
    UserInfo.objects.all().delete()
    return HttpResponse("<p>全部数据删除成功！！</p>")

def data_del(request):
    #test1 = Test(name='runoob')
    # test1 = UserInfo(user = "test123",pwd = "test321")
    # test1.save()
    UserInfo.objects.filter(user ="123").delete()
    return HttpResponse("<p>全部数据删除成功！！</p>")

def data_get(request):
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = UserInfo.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    #response2 = UserInfo.objects.filter(user = "321")

    # 获取单个对象
    #response3 = UserInfo.objects.get(user = "321")

    # 数据排序
    #UserInfo.objects.order_by("user")

    # 上面的方法可以连锁使用
    #UserInfo.objects.filter(user="13").order_by("user")

    # 输出所有数据
    for var in list:
        response1 += var.user + " " + var.pwd + ","
    response = response1
    return HttpResponse("<p>" + response + "</p>")

def data_update(request):
    # 修改其中一个user=test的pwd字段，再save，相当于SQL中的UPDATE
    test1 = UserInfo.objects.get(user="test")
    test1.pwd = 'test123'
    test1.save()

    # 另外一种方式
    # UserInfo.objects.filter(user="test").update(pwd = 'test123')

    # 修改所有的列
    # UserInfo.objects.all().update(pwd = 'test123')

    return HttpResponse("<p>修改成功</p>")