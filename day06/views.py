import random
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Book


def mylogin(req):
    if req.method == 'GET':
        return render(req,'login1.html')
    else:
        params = req.POST
        name = params.get('username')
        pwd = params.get('pwd')

        user = authenticate(username=name,password=pwd)

        if user:
            login(req,user)
            return HttpResponse('登录成功')
        else:
            return HttpResponse('有错误')


def get_prize(req):
    print('被执行')
    num = random.randint(1,100)
    if num > 90:
        return HttpResponse('奖金100万')
    else:
        return HttpResponse('酱油一瓶')


def create_book_v1(req):

    if req.method == 'GET':
        book = Book.objects.all().first()
        icon_url = 'http://{}/static/uploads/{}'.format(
            req.get_host(),
            book.icon.url
        )
        return render(req,'mybook.html',{'book_name':book.name,'icon':icon_url})

    name = req.POST.get('name')
    myfile = req.FILES.get('icon')
    book = Book.objects.create(
        name=name,
        icon=myfile
    )


    return HttpResponse('OK')








