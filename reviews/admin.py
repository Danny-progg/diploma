from django.contrib import admin

from reviews.models import Review


# Register your models here.


@admin.register(Review)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'review')
    list_filter = ('id', 'name', 'title', 'review')
    search_fields = ('name', 'title', 'review')