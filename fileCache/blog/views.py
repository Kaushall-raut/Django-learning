from django.shortcuts import render
from .models import Students
from django.core.cache import cache
# Create your views here.


def student_list(request):
    student_data=cache.get('student_data')

    if student_data is None:
        student_data=Students.objects.all()
        cache.set('student_data',student_data)
        print("data fetched from database")
    else:
        print('data is fetched from file cache')

    return render(request,'student.html',{"data":student_data})