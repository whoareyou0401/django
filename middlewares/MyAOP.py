from django.http import HttpResponse, HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class YjMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # name = request.GET.get('name')
        # if name == 'tom':
        #     return HttpResponse('恭喜老板获得美女一枚')
        # elif name == 'haha':
        #     return HttpResponse('毛片一部')
        # elif name == '班长':
        #     return HttpResponse('咖妃')

        black_ip = []
        ip = request.META.get('REMOTE_ADDR')
        if ip in black_ip:
            return HttpResponseForbidden('黑名单成员，无法访问')
        else:
            return HttpResponse('欢迎来到1024社区')

