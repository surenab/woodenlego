from django.contrib import admin
from .models import WishItem
# Register your models here.
class WishItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WishItem._meta.get_fields()]
admin.site.register(WishItem,WishItemAdmin)
