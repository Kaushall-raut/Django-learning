from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def page(request):
    posts=Post.objects.all().order_by('-id')

    paginator = Paginator(posts,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'blog/page.html',{'pages':page_obj})