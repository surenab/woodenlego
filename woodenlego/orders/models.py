from django.db import models
from wlwebsite.models import Toy
from django.conf import settings
from decimal import Decimal
# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    phone = models.CharField(max_length=50,default='')
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return  sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Toy,related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20,decimal_places=1)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    delivery_date = models.DateField(null=True)
    def get_total_price(self):
        return self.quantity*self.price
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return  Decimal(self.price) * Decimal(self.quantity)
