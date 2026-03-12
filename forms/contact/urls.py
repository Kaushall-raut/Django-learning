from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.contact_form,name='contact'),
    path('submit',views.submit,name='submit')

]
