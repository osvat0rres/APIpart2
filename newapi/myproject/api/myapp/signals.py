from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from django.core.cache import cache


#This function will work when teh signal save or delete works on the Product model
@receiver([post_save, post_delete], sender=Product)
def invalidate_prduct_list_cache(sender,**kwargs):
    print("Clearing the product cache")
    
    cache.delete_pattern("product_list")
    