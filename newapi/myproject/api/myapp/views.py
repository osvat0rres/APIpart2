from myapp.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from myapp.models import Product, Order, OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics
from rest_framework.permissions import  (
    IsAuthenticated, 
    IsAdminUser,
    AllowAny,
)
from rest_framework.views import APIView
from myapp.filters import ProductFilter, InStockFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination 

# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    #Only products that are in stock
    #queryset = Product.objects.filter(stock__gt=0)
    #Producst that are out of stock
    #queryset = Product.objects.exclude(stock__gt=0)
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    
    #For the fields that you want to filter (search)
    filterset_class = ProductFilter
    #This allows you to search from fields specify in the search_fileds (or accross many fileds from the models)
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter,
        filters.OrderingFilter,
        InStockFilterBackend,
        ]
    #If you want an exact match just add a '=' to the item ('=name')
    search_fields = ['name','description']
    ordering_filds = ['name','price','stock']
    
    #This will overwrite the default setting for pagination 
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2
    #This will give you the page number on the url
    pagination_class.page_query_param = 'pagenum'
    #The user will be abalable to select the number of pages it wants
    pagination_class.page_size_query_param = 'size'
    #set the max number of pages it wants
    pagination_class.max_page_size = 3
    

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

#Create a products
class ProductCreateAPIView(generics.CreateAPIView):
    Model = Product
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data) 
        return super().create(request, *args, **kwargs)

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #This is used when the url parameter is different from the default 'pk'
    #lookup_url_kwarg = 'product_id'   
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT','PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    

#List order information
class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    #Only authenticated users can access their orders
    permission_classes = [IsAuthenticated]

        #dynamically filter orders
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)

# Information about the products
class ProductInfoAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products' : products,
            'count' : len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']  
        })
        return  Response(serializer.data)
        




