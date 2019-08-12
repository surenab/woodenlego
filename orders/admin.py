from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','address','postal_code','city','paid','created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline]
admin.site.register(Order,OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.get_fields()]
admin.site.register(OrderItem,OrderItemAdmin)

