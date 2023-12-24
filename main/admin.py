from django.contrib import admin
from main.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')
    search_fields = ('name', 'description')