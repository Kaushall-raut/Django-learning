from django.shortcuts import render
from .models import Students
# Create your views here.


def home(request):
    data=Students.objects.all()
    return render(request,'list.html',{'data':data})