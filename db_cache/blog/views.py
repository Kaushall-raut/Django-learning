from django.shortcuts import render
from .models import Student
from django.core.cache import cache

# Create your views here.

def home(request):
    users=cache.get("users_list")
    if not users:
        print("fetching from db")
        users=Student.objects.all()
        cache.set("users_list",users)
    else:
        print("cached found")

    return  render(request,'home.html',{'data':users})