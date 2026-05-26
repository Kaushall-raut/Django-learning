from django.shortcuts import render
from .models import student
# Create your views here.
from django.views.decorators.cache import cache_page
@cache_page(30)
def home(request):
    print("fetching from database")
    student_Data=student.objects.all()

    return render(request,'list.html' , {'data':student_Data})