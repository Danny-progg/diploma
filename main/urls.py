from django.urls import path

from main.apps import MainConfig
from main.views import (category, DoctorsDeleteView, DoctorsUpdateView, DoctorsDetailView, DoctorsCreateView,
                        DoctorsListView, SpecificListView)

app_name = MainConfig.name


urlpatterns = [
    path('', category, name='category_list'),

    path('list/', DoctorsListView.as_view(), name='doctors_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_doctors_list'),

    path('create/', (DoctorsCreateView.as_view()), name='doctors_form'),
    path('view/<int:pk>/', DoctorsDetailView.as_view(), name='doctors_detail'),
    path('edit/<int:pk>/', DoctorsUpdateView.as_view(), name='doctors_update_form'),
    path('delete/<int:pk>/', DoctorsDeleteView.as_view(), name='doctors_confirm_delete'),
]