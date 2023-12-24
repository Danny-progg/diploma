from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main.services import get_services_cache


@login_required
def services(request):
    context = {
        'object_list': get_services_cache(),
        'title': 'Услуги',
    }
    return render(request, 'main/service_list.html', context)
