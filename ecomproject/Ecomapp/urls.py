from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Ecomapp'

urlpatterns = [
    path('',views.productcat,name='productcat'),
    path('<slug:c_slug>/',views.productcat,name='productcategory'),
    path('<slug:c_slug>/<slug:p_slug>/', views.productdetails, name='productdetail'),

]