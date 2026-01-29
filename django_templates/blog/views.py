from django.shortcuts import render

# Create your views here.
def home(request):
    data={
        "name":"kaushal",
        "age":22,
        "city":"<b>vapi</b>",
        "contact":None

    }
    return render(request,'home.html' ,data)