from django.urls import path
from . import views

urlpatterns = [
    path("set-session",views.setsession,name='set-session'),
    path("get-session",views.getsession,name='get-session'),
    path("remove-session",views.removesession,name='remove-session')
]