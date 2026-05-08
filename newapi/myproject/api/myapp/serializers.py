from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  (
            'id',
            'name',
            'price',
            'stock',   
        )
    
    def validata_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "The price must be grated then 0."
            )
        return value 
             
    











