from django.contrib import admin
from .models import student

# Register your models here.
@admin.register(student)
class AdminStudent(admin.ModelAdmin):
    list_display=['name','email']

    