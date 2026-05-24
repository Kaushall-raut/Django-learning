import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class SimpleLogMiddleware(MiddlewareMixin):

    def process_request(self,request):
        print(f"[{datetime.datetime.now()}] Request Url : {request.path}")
    
    def process_response(self,request,response):
        print(f"[{datetime.datetime.now()}] response status code : {HttpResponse.status_code}")

        return response

class BlockIpMiddleware(MiddlewareMixin):
    block_Ip=['127.0.0.1']

    def process_request(self,request):
        ip=request.META.get('REMOTE_ADDR')

        if ip in self.block_Ip:
            return HttpResponse('your ip is blocked')