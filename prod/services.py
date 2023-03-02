from config import settings
from prod.models import Categories
from django.core.cache import cache


def get_categories_from_cache():
    queryset = Categories.objects.all()
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data
    return queryset
