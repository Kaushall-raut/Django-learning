from django.urls import path
from . import views

urlpatterns = [
    path("set-cookies",views.setcookies,name='set-cookies'),
    path("get-cookies",views.getcookies,name='get-cookies'),
    path("del-cookies",views.delcookies,name='del-cookies')
]