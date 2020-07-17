# django
from django.contrib.sitemaps import Sitemap

# first-party
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return object.published_date
