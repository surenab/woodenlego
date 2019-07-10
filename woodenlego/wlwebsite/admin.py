from django.contrib import admin
from .models import Toy, ToyReview, DeliveryCost, Video
# Register your models here.
class ToyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Toy._meta.get_fields()][1:]
    #list_display = ['category']
    list_display+=['image_tag_main','image_tag_1','image_tag_2','image_tag_3','image_tag_4','image_tag_5','image_tag_6','image_tag_7','image_tag_8']
    list_display.remove('image1')
    list_display.remove('image2')
    list_display.remove('image3')
    list_display.remove('image4')
    list_display.remove('image5')
    list_display.remove('image6')
    list_display.remove('image7')
    list_display.remove('image8')
    list_display.remove('mainimage')
    list_display = list_display[2:]
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

