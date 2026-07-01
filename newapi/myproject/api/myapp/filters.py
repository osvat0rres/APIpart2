import django_filters
from myapp.models import Product, Order
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
        
#This filter is uses to lookm for orders in status and when ut was created
class OrderFilter(django_filters.FilterSet):
    #This will allow you to filter by the date the order was created
    created_at = django_filters.DateFilter(field_name='created_at__date')
    class Meta:
        model = Order
        fields = {
            'status' : ['exact', 'contains'],
            'created_at' : ['exact', 'gt', 'range']
        }
