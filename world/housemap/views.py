from django.shortcuts import render
from django.views import generic
from .models import HomeSpot
# Create your views here.
class MapView(generic.ListView):
    template_name = 'mapview.html'
    context_object_name = 'qs_results'


    def get_queryset(self):
            return HomeSpot.objects.all()
