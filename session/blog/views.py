from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setsession(request):
    request.session['username']='kaushal'
    request.session['pass']='5345'

    return HttpResponse("session created successfully ")

def getsession(request):
   username= request.session.get('username','guest')
   password= request.session.get('pass','none')
   return  HttpResponse(f"hi {username} your pass is {password}")

def removesession(request):
    request.session.flush()
    return HttpResponse("Session deleted successfully")


