from django.urls import path

from main.apps import MainConfig
from main.views import index, category

app_name = MainConfig.name


urlpatterns = [
    path('', index, name='service_list'),
    path('category/', category, name='category_list'),
]