from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'searchapp'

urlpatterns = [
    path('',views.searchresult,name='searchresult'),
    ]