from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import HttpResponse
# Create your views here.

def bulk(request):
    message1= ("hello user " , "Welcome to our website","kaushalraut.code@gmail.com",["kaushalraut755@gmail.com"])

    send_mass_mail((message1,))
    return HttpResponse("Mail sent successfully")