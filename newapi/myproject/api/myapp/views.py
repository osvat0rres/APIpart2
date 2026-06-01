from django.shortcuts import render, get_object_or_404
from myapp.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from myapp.models import Product, Order, OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics

# Create your views here.

class ProductListAPIView(generics.ListAPIView):
    #Only products that are in stock
    #queryset = Product.objects.filter(stock__gt=0)
    #Producst that are out of stock
    #queryset = Product.objects.exclude(stock__gt=0)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #This is used when the url parameter is different from the default 'pk'
    #lookup_url_kwarg = 'product_id'    


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    #only authenticated users can access their orders
    permission_classes =[IsAuthenticated]
    
    
        #dynamically filter orders
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products' : products,
        'count' : len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']  
    })
    return  Response(serializer.data)
