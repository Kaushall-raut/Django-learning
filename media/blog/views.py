from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

# Create your views here.

def upload(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,'Photo uploaded')
            return redirect('view_profile')
        else :
            messages.error(request,"error occurred during media uploading")
    else :
        form=ProfileForm()
        return render(request,'upload.html',{'form':form})
    
def view_profile(request):
    profile=Profile.objects.all()
    return render(request,'view.html',{'profiles':profile})