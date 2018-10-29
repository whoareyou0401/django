from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect


# Create your views here.


def json_test(req):
    data = {
        'code':1,
        'msg':'ok哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈返回结果快乐与天赋和环境健康机遇和',
        'data':[1,2,3,4,5]
    }

    return JsonResponse(data)
    # return HttpResponse(json.dumps(data))

def test_res(req):

    response = HttpResponse()
    response.content = '遮天'
    response.status_code = 404

    return response

def mylogin(req):

    if req.method == 'GET':
        return render(req,'login.html')
    elif req.method == 'POST':
    #     解析参数：名字，密码

        params = req.POST
        name = params.get('username')
        password = params.get('password')
    #     假设校验通过
        response = redirect('/day05/index')
        response.set_cookie('user',name,max_age=30)
        req.session['password'] = password
        return response
    else:
        return HttpResponseNotAllowed('请求方式无法解析')


# 首页
def index001(req):

    u_name = req.COOKIES.get('user')
    u_name = u_name if u_name else '游客'
    req = req.sesseion.get('password')
    print(req)
    return render(req,'index001.html',{'user_name':u_name})






