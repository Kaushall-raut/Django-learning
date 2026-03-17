from django.urls import path
from . import views
app_name="contact"
urlpatterns = [
  
    path('',views.contact),
    path('list/',views.contact_list,name='contact_list'),
    path('list/details/<int:id>',views.contact_details), 
    path('list/update/<int:id>',views.contact_update,name='contact_update'),
    path('list/delete/<int:id>',views.contact_delete,name='contact_delete'),
]
