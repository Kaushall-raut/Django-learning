from django.shortcuts import render
from django.core.cache import cache
from .models import ytChannel
# Create your views here.

def home(request):
    users=cache.get('user-data')
    if not users:
        print("Cache data not available .Fetching directly from database")
        users=ytChannel.objects.all()
        cache.set('user-data',users,timeout=120)
    else:
        print("cache found , fetching from cache")
    return render(request,'list.html',{'users':users})