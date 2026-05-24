from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def setcookies(request):
    response=HttpResponse(' cookies set successfully')
    response.set_cookie("name","kaushal",max_age=60*60*24)
    return response

def getcookies(request):
    username=request.COOKIES.get('name','guest')
    return HttpResponse(f"Hello, {username}")
def delcookies(request):
    response =HttpResponse("cookies deleted successfully")
    response.delete_cookie("name")
    return response