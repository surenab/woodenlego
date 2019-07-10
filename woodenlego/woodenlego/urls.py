"""woodenlego URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
import wlwebsite.views as views
from .views import register, OrdersView
from django.conf import settings
from django.conf.urls.static import static
from django_registration.views import RegistrationView
from django.contrib.sitemaps.views import sitemap
from .sitemaps_custom import ToySitemap
from wishlist.views import WishesView, delete_wish,add_wish
sitemaps = {
    'toys': ToySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.Feature.as_view(), name='profile'),
    path('accounts/register/', register, name='register'),
    path('accounts/orders/', OrdersView.as_view(), name='orders'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/wishlist', WishesView.as_view(), name='wishes'),
    path('accounts/wishlist/delete/<int:pk>/', delete_wish, name='delete_wish'),
    path('accounts/wishlist/add/<int:pk>/', add_wish, name='add_wish'),
    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap_custom'),
    path('', include('wlwebsite.urls', namespace='wlwebsite')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
