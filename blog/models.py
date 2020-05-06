# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField


class Post(models.Model):
    theory = "th"
    practice = "pr"
    poetry = "po"
    mindflow = "mf"
    THEME_CHOICES = (
        (theory, "Theory"),
        (practice, "Practice"),
        (poetry, "Poetry"),
        (mindflow, "Mindflow"),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    theme = models.CharField(max_length=255, choices=THEME_CHOICES, default=theory)
    slug = AutoSlugField(populate_from="title")

    class Meta:
        ordering = ("-published_date",)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
