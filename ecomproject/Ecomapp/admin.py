from django.contrib import admin

from . models import Category, Products

 # Register your models here.

class Catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,Catadmin)


class Prodadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','avail','created','updated']
    list_editable = ['price','stock','avail']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(Products,Prodadmin)
