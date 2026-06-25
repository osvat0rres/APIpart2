import django_filters
from myapp.models import Product
from rest_framework import filters


#This will return only items that are in stock
class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        #This will return only items that are in stock
        return queryset.filter(stock__gt=0)
        #This will return itmes that are not in stock
        # return queryset.exclude(stock__gt=0)
    


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        #The field product gives you control over how to look for the items
        fields = {
            'name' : ['exact', 'contains'],
            'price' : ['exact','lt', 'gt', 'range']
        }
