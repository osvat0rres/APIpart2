from django.db import transaction
from rest_framework import serializers
from .models import Product, Order, OrderItem


#This serializer is used to serilaize the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'description',
            'name',
            'price',
            'stock',
        )
    #When created a new product, this will validate the price to make sure it is greater then 0
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price')

    class Meta:
        model = OrderItem
        fields = (
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        )
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = (
                'product',
                'quantity',
            )
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemCreateSerializer(many=True, required=True)
    
    def upadate(self, instance, validated_data):
        orderitem_data = validated_data.pop('items')
        
        #content manager
        #This line of code tell django to treate the following block of code as a single transaction. Ether 
        #some of it worlks or none of it works
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            
            if orderitem_data is not None:
                #clean existing data
                instance.items.all().delete()    
                
                #recreate items with the new updated data
                for item in orderitem_data:
                    OrderItem.objects.create(order=instance, **item)
        return instance
                


    def create(self, validated_data):
        orderitem_data = validated_data.pop('items')
        
        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            
            for item in orderitem_data:
                OrderItem.objects.create(order=order, **item)
            
        return order
                
    class Meta: 
        model = Order
        fields = ( 
            'order_id',
            'user',
            'status', 
            'items',
        )
        extra_kwargs = {
            'user': {'read_only': True}, 
        }


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'created_at',
            'user',
            'status', 
            'items',
            'total_price',
        )
        
    
 #This is a generic serializer. Notes, it does not take a model as a paramter        
class ProductInfoSerializer(serializers.Serializer):
    #get all products,count of products, max price 
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    


