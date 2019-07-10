from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import  HomeSpot

admin.site.register(HomeSpot, LeafletGeoAdmin)