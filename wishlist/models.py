from django.db import models
from wlwebsite.models import Toy
from django.conf import settings
from decimal import Decimal
# Create your models here.



class WishItem(models.Model):
    product = models.ForeignKey(Toy,related_name='wish_items', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="wish_user", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.id)

