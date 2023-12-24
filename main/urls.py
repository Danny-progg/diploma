from django.urls import path

from main.apps import MainConfig
from main.views import services

app_name = MainConfig.name


urlpatterns = [
    path('', services, name='service_list'),
]