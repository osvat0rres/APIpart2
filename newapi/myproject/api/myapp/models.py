from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    #When an image is uploaded, it will be stored in the 'products/' directory within the media folder.
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    
    #This function checks if the product is in stock by verifying if the stock quantity is greater than zero. 
    @property
    def in_stock(self):
        return self.stock > 0
    #This will return the name of the product when the object is printed or displayed in the admin interface.
    def __str__(self):
        return self.name
    
class Order(models.Model):
    class StatusChoises(models.TextChoices):
        PENDING = 'Pending',
        CONFIRMED = 'Confirmed',
        CANCELED = 'Canceled',
        
        
        #this gives a ID to the order
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #This creates the time when the order is created
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, 
                              choices=StatusChoises.choices, 
                              default=StatusChoises.PENDING )
    
    products = models.ManyToManyField(Product, through="Orderitem", related_name="orders")
    
    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"

class OrderItem(models.Model):
    #This will delete all object acosiated with the object order
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    @property
    def  item_subtotal(self): 
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order{self.order.order_id}"
