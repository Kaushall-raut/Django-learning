
from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.upload,name='upload'),
    path('view_profile/',views.view_profile,name='view_profile'),
]