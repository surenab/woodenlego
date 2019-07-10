from django.db import models
import datetime
# Create your models here.
from djgeojson.fields import PointField
from django.db import models

class HomeSpot(models.Model):

    geom = PointField(null=True)
    description = models.TextField(default='')
    created = models.DateTimeField(default=datetime.datetime.now())
    saledate = models.DateTimeField(default=datetime.datetime.now())
    price = models.IntegerField(default=0.0,null=True)

    picture = models.TextField(default='',null=True)
    address = models.TextField(default='')
    @property
    def popupContent(self):
        return '<img width="100" height="100" src="{}" /><p>{}</p><p>Price: EUR {}</p><p>Sale Date: {}</p>'.format(
            self.picture,
            self.description,
            self.price,
            self.saledate)
    class Meta:
        ordering = ('-created',)

'''
address = HomeSpot()
address.geom = {'type': 'Point', 'coordinates': [0, 0]}
address.picture = 'https://b.dmlimg.com/MGEyZWUyYjVhZjMyNDc2MDMzMTJjM2RjZDNhOWQ5Yjex7FWekMkTXtAYqswYOl-VaHR0cDovL3MzLWV1LXdlc3QtMS5hbWF6b25hd3MuY29tL21lZGlhbWFzdGVyLXMzZXUvMS9jLzFjZjVmMTA4MWEzZmU1MmIzYjBkMWRjMjJhNTNkMTA1LmpwZ3x8fHx8fDEwNDV4NjAwfHx8fA==.jpg'
address.description = 'Home 1'
address.save()

address = HomeSpot()
address.geom = {'type': 'Point', 'coordinates': [110, 0]}
address.picture = 'https://b.dmlimg.com/MGEyZWUyYjVhZjMyNDc2MDMzMTJjM2RjZDNhOWQ5Yjex7FWekMkTXtAYqswYOl-VaHR0cDovL3MzLWV1LXdlc3QtMS5hbWF6b25hd3MuY29tL21lZGlhbWFzdGVyLXMzZXUvMS9jLzFjZjVmMTA4MWEzZmU1MmIzYjBkMWRjMjJhNTNkMTA1LmpwZ3x8fHx8fDEwNDV4NjAwfHx8fA==.jpg'
address.description = 'Home 1'
address.save()
'''