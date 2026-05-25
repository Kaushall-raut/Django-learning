from django.contrib import admin
from .models import ytChannel
# Register your models here.

@admin.register(ytChannel)

class ytAdmin(admin.ModelAdmin):
    list_display=('name','email','subscribers')
    