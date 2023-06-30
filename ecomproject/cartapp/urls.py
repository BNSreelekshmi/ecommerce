from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_details,name='cart_details'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
    path('all_remove/<int:product_id>/',views.all_remove,name='all_remove'),


]