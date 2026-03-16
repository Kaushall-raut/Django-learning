from django.shortcuts import render,get_object_or_404,redirect
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

def contact_update(request, id):
    contact = get_object_or_404(ContactForm, id=id)

    if request.method == 'POST':
        forms = Contact(request.POST, instance=contact)
        if forms.is_valid():
            forms.save()
            return redirect('/list')   # better than render
    else:
        form = Contact(instance=contact)

    return render(request, 'index.html', {'form': form})