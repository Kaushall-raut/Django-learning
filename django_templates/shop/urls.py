from django.urls import path
from . import views

urlpatterns = [

    path("shop",views.product_page,name="products_page"),
]