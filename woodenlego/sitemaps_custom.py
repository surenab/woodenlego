from django.contrib.sitemaps import Sitemap
from wlwebsite.models import Toy, ToyReview


class ToySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Toy.objects.all()

    def lastmod(self, obj):
        return obj.pub_date