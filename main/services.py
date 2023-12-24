from django.conf import settings
from django.core.cache import cache

from main.models import Service


def get_services_cache():
    if settings.CACHE_ENABLED:
        key = 'service_list'
        service_list = cache.get(key)
        if service_list is None:
            service_list = Service.objects.all()
            cache.set(key, service_list)
    else:
        service_list = Service.objects.all()

    return service_list
