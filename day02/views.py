from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from day02.models import Item, Category

# 字符串格式化方式
def str_format():
    name = '托尼'
    age = 22
    brother = '王大锤'

    my_str = '我叫{},今年{}岁,我哥{}'.format(name,age,brother)
    print(my_str)




def get_html(req):

    str_format()
    return render(req,'item.html')

def create_item(req):

    params = req.POST
    name = params.get('i_name')
    barcode = params.get("i_barcode")
    cate_id = int(params.get("cate_id"))


    item = Item.objects.create(
        name=name,
        barcode=barcode,
        category_id=cate_id
    )

    return HttpResponse('创建成功了{}'.format(item.name))


def get_category(req):
    cates = Category.objects.all()

    return render(req,'cates.html',{'data':cates})


def select_data(req):

    # data = Item.objects.filter(name='雪碧')
    # 查询以某字结尾
    # data = Item.objects.filter(name__endswith='可乐')
    #
    # print(data)
    # # print(dir(data))
    # data = data.filter(name='可乐')

    # data = Item.objects.all().order_by('-id')
    data = Item.objects.filter(id__lt=6).values()
    print(data)

    return render(req,'items.html',{'items':data})


def get_item_by_cate_id(req):

    c_id = int(req.GET.get('c_id'))

    item = Item.objects.filter(category_id=c_id)

    return render(req,'items.html',{'items':item})






