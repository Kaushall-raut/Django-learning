from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def show_message(request):
    messages.debug(request,"message for debug")
    messages.info(request,"message for info")
    messages.warning(request,"message for warning ")
    messages.error(request,"message to show error")
    messages.success(request,'message to display success')
    return render(request,"index.html")