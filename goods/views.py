# coding=utf-8
from django.shortcuts import render

from models import *
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


# 相信信息页数据的加载操作
# 参数Id：产品编号
def detail(request, id):
    good = GoodInfo.objects.get(pk=id)

    list1 = GoodInfo.objects.all()

    list2 = list1[0:2]

    dic = {
        'good': good,
        'list1': list2
    }

    return render(request, 'goods/detail.html', dic)


# 进行列表页数据的加载操作
# 参数typeId：类型编号
# 参数pIndex：当前页码编号
def goodslist(request, typeId, pIndex):
    goodlist = Dict.objects.get(pk=typeId).goodinfo_set.all()
    pag = Paginator(goodlist, 1)
    pagelist = pag.page_range

    list1 = goodlist[0:2]

    if pIndex == '':
        pIndex = '1'

    list2 = pag.page(int(pIndex))

    pdic = {'list1':list1, 'list2': list2, 'pagelist': pagelist, 'pIndex': int(pIndex), 'type':typeId}

    return render(request, 'goods/list.html', pdic)

