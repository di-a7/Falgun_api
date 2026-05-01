from django_filters.rest_framework import FilterSet
from .models import Menu

class MenuFilter(FilterSet):
   class Meta:
      model = Menu
      fields = {
         'price' : ['gt', 'lt']
      }