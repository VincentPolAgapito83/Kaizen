import django_filters

from .models import *

class AuthorsFilter(django_filters.FilterSet):
    class Meta:
        models = Authors
        fields = '__all__'

