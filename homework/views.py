import json

import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# 创建班级
from homework.models import *


def addClass(request):
    classes = Classes()
    list = ['python','UI','java']
    classes.name = random.choice(list)
    classes.save()
    return HttpResponse('创建班级成功')


def addStudent(req):

    student = Students()
    student.name = '张三'+ str(random.randint(20,80))
    student.age = random.randint(18,80)
    # list = ['python','UI','java']
    classes = Classes.objects.all()
    student.classes = random.choice(classes)

    student.save()

    return HttpResponse('创建学生成功')

# 从班级查询学生

def get_stu_by_cla(req):
    classes = Classes.objects.filter(pk=2)
    res = classes.all()

    print(res)
    return HttpResponse(res)

def get_cla_by_stu(req):

    student = Students.objects.filter(classes__name='java').all()
    print(student)

    return HttpResponse(student)

def play(req):


    return render(req,'2048/2048.html')





