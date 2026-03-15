from django.urls import path
from . import views
app_name="contact"
urlpatterns = [
  
    path('',views.contact),
    path('list/',views.contact_list),
    path('list/details/<int:id>',views.contact_details),
]
