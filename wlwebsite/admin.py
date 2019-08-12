from django.contrib import admin
from .models import Toy, ToyReview, DeliveryCost, Video, Customer, OfflineOrder, OfflineOrderItem
# Register your models here.
class ToyAdmin(admin.ModelAdmin):
    list_display = ['category','real_price','price','model','manufactor','stock','description','weight','sizes','header','product_code','color','madein','quantity','adddate','pub_date']
    list_display+=['image_tag_main','image_tag_1','image_tag_2','image_tag_3','image_tag_4','image_tag_5','image_tag_6','image_tag_7','image_tag_8','videotag']
admin.site.register(Toy,ToyAdmin)


class ToyReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ToyReview._meta.get_fields()]
admin.site.register(ToyReview,ToyReviewAdmin)

class DeliveryCostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeliveryCost._meta.get_fields()]
admin.site.register(DeliveryCost,DeliveryCostAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields()]
admin.site.register(Video,VideoAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['contact_name1','phone_number1','contact_name2','phone_number2','address','shop_name','shop_type','comments']
admin.site.register(Customer,CustomerAdmin)

class OfflineOrderItemInline(admin.TabularInline):
    model=OfflineOrderItem
    raw_id_fields = ['toy']


class OfflineOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OfflineOrder._meta.get_fields()]
    list_display.remove('id')
    inlines = [OfflineOrderItemInline]
admin.site.register(OfflineOrder,OfflineOrderAdmin)


class OfflineOrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OfflineOrderItem._meta.get_fields()]
admin.site.register(OfflineOrderItem,OfflineOrderItemAdmin)
