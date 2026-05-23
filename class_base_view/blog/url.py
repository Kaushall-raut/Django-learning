from django.urls import path
from .views import PostListView,PostDetailView,PostEditView,PostCreateView,PostDeleteView
urlpatterns = [
    path("",PostListView.as_view(),name='PostListView'),
    path("post/<int:pk>/",PostDetailView.as_view(),name='PostDetailView'),
    path("post/<int:pk>/edit",PostEditView.as_view(),name='PostEditView'),
    path("post/new/",PostCreateView.as_view(),name='PostCreateView'),
    path("post/<int:pk>/delete",PostDeleteView.as_view(),name='PostDeleteView'),
]