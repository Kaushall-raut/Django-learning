from django.shortcuts import render,get_object_or_404
from .form import Contact
from.models import ContactForm
# Create your views here.

def contact(request):
    data=Contact(request.POST)
    if request.method== 'POST':
        if data.is_valid():
            data.save()
            return render(request,"thanks.html")

    return render(request,"index.html",{"form":data})

def contact_list(request):
    contacts=ContactForm.objects.all()
    # contacts=get_object_or_404(Contact,)
    return render(request,'contact_list.html',{"contacts":contacts})

def contact_details(request,id):
    contacts=get_object_or_404(ContactForm,id=id)
    return render(request,'contact_details.html',{'contacts':contacts})