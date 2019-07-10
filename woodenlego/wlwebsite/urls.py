from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'wlwebsite'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.Products.as_view(), name='products'),
    #path('products/<str:sort>/', views.Products.as_view(), name='products'),
    path('products/<int:pk>/', views.ToyDetailView.as_view(), name='product'),
    path('contact-us/', views.Contactus.as_view(), name='contactus'),

    path('about/', views.About.as_view(), name='about'),
    path('delivery-information/', views.Delivery.as_view(), name='delivery'),
    path('privacy-policy/', views.Privacy.as_view(), name='privacy'),
    path('terms/', views.Terms.as_view(), name='terms'),

    path('aboutowners/', views.Owners.as_view(), name='aboutowners'),
    path('ideas/', views.Ideas.as_view(), name='ideas'),
    path('feature/', views.Feature.as_view(), name='feature'),

    path('blogs/', views.Blogs.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.Home.as_view(), name='blog'),

]
