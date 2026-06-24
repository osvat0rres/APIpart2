import django_filters
from myapp.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        #The field product gives you control over how to look fgor the items
        fields = {
            'name' : ['exact', 'contains'],
            'price' : ['exact','lt', 'gt', 'range']
        }