from django.urls import path
from . import views

urlpatterns = [
    path('local-cache',views.home,name='local-cache')
]