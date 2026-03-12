from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def contact_form(request) :
    return render(request,'contact.html')

def submit(request ):
    if request.method=='POST':
       name=request.POST.get('name')
       message=request.POST.get('message')

       if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse(f"Thank you for your message ,{name}")
       else:
            return HttpResponse("No fields can remain empty")
    return redirect(request,'contact.html')