from django.shortcuts import render
from main.models import Doctors, Category


def index(request):
    context = {
        'object_list': Doctors.objects.all(),
        'title': 'Врачи'
    }
    return render(request, 'main/service_list.html', context)


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'main/category_list.html', context)

