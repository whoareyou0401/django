from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from day04.models import *


def firstindex(req):

    return render(req,'firstindex.html')

def langs(req):


    data = Language.objects.all()
    html = loader.get_template('langs.html')
    print(dir(html))
    # return render(req,'langs.html',{'langs':data})
    # 渲染
    str_html = html.render({'langs':data})
    print(str_html)
    return HttpResponse(str_html)


def erindex(req):

    print('被执行')
    # return HttpResponseRedirect('langs')
    return redirect(reverse('day04:langs'))

def myindex_with_params(req,p1):
    print(p1)
    try:
        lua = Language.objects.get(pk=int(p1))
        res = '{}的描述是{}'.format(lua.name,lua.desc)
    except Language.DoesNotExist:
        res = '没有数据了'
    return HttpResponse(res)




def myindex_with_params_v1(req,p1):
    p2 = p1
    try:
        lua = Language.objects.get(pk=int(p2))
        res = '{}的描述是{}'.format(lua.name,lua.desc)
    except Language.DoesNotExist:
        res = '没有数据了'
    return HttpResponse(res)

def new_reverse(req):

    # return redirect(reverse('day04:myindex_with_params',args=(2,)))
    return redirect(reverse('day04:myindex_with_params_v1',kwargs={'p1':3}))


def extent(req):

    return render(req,'home.html')
