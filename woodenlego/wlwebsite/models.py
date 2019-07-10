from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.urls import reverse

PRODUCT_CATEGORIES = (('T', 'Toy'),('S', 'Souvenir'),)

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='static/image', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)


# Create your models here.
class Toy(models.Model):
    category = models.CharField(choices=PRODUCT_CATEGORIES,default='Toys',null=True,max_length=1)
    real_price  = models.IntegerField(default=1000, blank=True, null=True)
    price = models.IntegerField(default=1000, blank=True, null=True)
    model  = models.TextField(default='', blank=True, null=True)
    manufactor = models.TextField(default='WoodenLego', blank=True, null=True)
    stock        = models.BooleanField(default=True, blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    weight     = models.FloatField(default=0.5, blank=True, null=True)
    sizes     = models.TextField(default='', blank=True, null=True)
    header     = models.TextField(default='', blank=True, null=True)
    product_code = models.TextField(default='', blank=True, null=True)
    color = models.TextField(default='', blank=True, null=True)
    madein = models.TextField(default='Armenia', blank=True, null=True)
    quantity = models.IntegerField(default=10, blank=True, null=True)
    adddate   = models.DateTimeField(default=timezone.now,blank=True, null=True)
    mainimage = models.ImageField(upload_to='images/', max_length=100)
    image1 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image2 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image3 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image4 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image5 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image6 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image7 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image8 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    video =  models.FileField(upload_to='static/image', blank = True, null=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def image_tag_main(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.mainimage))
    image_tag_main.short_description = 'Main Image'
    def image_tag_1(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image1))
    image_tag_1.short_description = 'Image 1'
    def image_tag_2(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image2))
    image_tag_2.short_description = 'Image 2'
    def image_tag_3(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image3))
    image_tag_3.short_description = 'Image 3'
    def image_tag_4(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image4))
    image_tag_4.short_description = 'Image 4'
    def image_tag_5(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image5))
    image_tag_5.short_description = 'Image 5'
    def image_tag_6(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image6))
    image_tag_6.short_description = 'Image 6'
    def image_tag_7(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image7))
    image_tag_7.short_description = 'Image 7'
    def image_tag_8(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image8))
    image_tag_8.short_description = 'Image 8'
    def videotag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.video))
        videotag.short_description = 'VIDEO'


    def get_absolute_url(self):
        return reverse('wlwebsite:product', kwargs={'pk': self.id})

    class Meta:
        ordering = ('-adddate',)

    def __str__(self):
        return self.header

class ToyReview(models.Model):
    name = models.TextField(default='', blank=True, null=True)
    reviewtext = models.TextField(default='', blank=True, null=True)
    reviewrate = models.IntegerField(default=5, blank=True, null=True)
    reviewdate   = models.DateTimeField(default=timezone.now,blank=True, null=True)
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    def __str__(self):
        return "%s wrote %s review" % (self.name,self.reviewtext)

class DeliveryCost(models.Model):
    yerevan = models.IntegerField(default=400, blank=True, null=True)
    county = models.IntegerField(default=2000, blank=True, null=True)
    def __str__(self):
        return "%d dram %d dram" % (self.yerevan,self.county)
