from django.contrib import admin
from main.models import Doctors, Category


@admin.register(Doctors)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')
    search_fields = ('name', 'description')


@admin.register(Category)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name', 'description')