from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from day01.models import Humen


def get_humen(req):
    data = Humen.objects.all()
    print(data)

    return render(req,'humen.html',{'humens':data})


def hehe(req):
    params = req.GET
    print(params)
    print(params.get('msg'))
    return HttpResponse('hehe')

def make_frinds(req):
    parms = req.GET
    name = parms.get('name')
    age = int(parms.get('age'))
    yz = int(parms.get('yz'))
    money = int(parms.get('money'))

    if money >= 1000 and yz > 80 and age > 18 and age < 22:
        return HttpResponse('喜欢')
    elif yz > 80 and age > 18 and age < 22 and money < 1000:
        return HttpResponse('好人卡')
    else:
        return HttpResponse('呵呵')














