# from django.urls import path,include
# from . import views
# urlpatterns = [
#     path("login/",views.login_user,name='login'),
#     path("register",views.register,name='register'),
#     path("dashboard",views.dashboard,name='dashboard'),
#     path("logout",views.logOut,name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name='login'),
    path("register/", views.register, name='register'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("logout/", views.logOut, name='logout'),
]