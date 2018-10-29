from django.db.models import Avg, Q, F

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from day03.models import *


def get_data(request):
    humens= Humen.objects.filter(money__gt=1050)
    avg_age = humens.aggregate(Avg('age'))
    print(avg_age)

    return HttpResponse('平均年龄为{}'.format(avg_age))

def get_data_by_q(req):
    data = Humen.objects.filter(Q(age__lt=10)|Q(money__gt=1050))
    # data = Humen.objects.filter(id__lt=10,age__gt=10)
    # data = Humen.objects.filter(~Q(age__lt=10) & Q(money__gt=1050))
    # data = Humen.objects.filter(age__gt=F('id'))
    # data = Humen.objects.filter(age__gt=F('money'))


    return render(req,'humens.html',{'humens':data})



def delete_hume(req):
    param = req.GET
    h_id = param.get('h_id')
    h_id = int(h_id)

    obj = Humen.objects.filter(id__lt=h_id)

    obj.delete()
    return HttpResponse('删除成功')


def update_humen(req):
    new_name = req.GET.get('name')
    obj = Humen.objects.all().first()
    obj.name = new_name

    obj.save()

    return HttpResponse('OK')


def get_id_by_per(req):
    person = Person.objects.get(pk=1)
    idcard = person.idcard.num

    return HttpResponse(idcard)

def get_per_by_idcard(req):
    # idcard = '111'
    # obj = IdCard.objects.get(num=idcard)
    # pername = obj.person.name

    person = Person.objects.filter(idcard__addre='北京').first()
    print(person)
    return HttpResponse(person)

def get_classes_by_stu(req):
    stu = Student.objects.get(id=2)
    print(stu)

    return HttpResponse(stu)

def get_stu_by_cla(req):
    # 找到指定班级ID
    classes = Classes.objects.filter(id=1)
    # 得到指定班级里指定ID代表的人
    stus = classes.filter(id=1)
    print(stus)
    return HttpResponse(stus)


def get_aut_by_book(req):

    book = Book.objects.filter(pk=1)
    res = book.all()
    print(res)

    return HttpResponse(res)


def get_book_by_aut(req):
    author = Author.objects.filter(pk=1)
    res = author.all()
    print(res)

    return HttpResponse(res)






















