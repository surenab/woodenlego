from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
