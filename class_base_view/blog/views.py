from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView):
    model=Post
    template_name='List.html'
    context_object_name='posts'

class PostDetailView(DetailView):
    model=Post
    template_name='detail.html'
    context_object_name='post'

class PostCreateView(CreateView):
    model=Post
    template_name='edit.html'
    fields=['title','content']

class PostEditView(UpdateView):
    model=Post
    template_name='edit.html'
    fields=['title','content']

class PostDeleteView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('PostListView')