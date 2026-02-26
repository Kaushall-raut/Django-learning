from django.shortcuts import render
from .models import Student



obj=Student.objects.all()
# Create your views here.
def home(request):
    return render(request,'index.html',{"data":obj})