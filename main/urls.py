from django.urls import path

from main.apps import MainConfig
from main.views import (category, DoctorsDeleteView, DoctorsUpdateView, DoctorsDetailView, DoctorsCreateView,
                        DoctorsListView, SpecificListView)

app_name = MainConfig.name


urlpatterns = [
    # path('', index, name='service_list'),
    path('category/', category, name='category_list'),

    path('', (DoctorsListView.as_view()), name='doctors_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_doctors_list'),

    path('create/', (DoctorsCreateView.as_view()), name='doctor_form'),
    path('view/<int:pk>/', DoctorsDetailView.as_view(), name='doctor_detail'),
    path('edit/<int:pk>/', DoctorsUpdateView.as_view(), name='doctor_update_form'),
    path('delete/<int:pk>/', DoctorsDeleteView.as_view(), name='doctor_confirm_delete'),
]