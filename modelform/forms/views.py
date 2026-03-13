from django.shortcuts import render
from .form import Contact
# Create your views here.

def contact(request):
    data=Contact(request.POST)
    if request.method== 'POST':
        if data.is_valid():
            data.save()
            return render(request,"thanks.html")

    return render(request,"index.html",{"form":data})