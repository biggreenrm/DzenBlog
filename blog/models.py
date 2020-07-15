# django
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

# first-party
from likedislike.models import LikeDislike

# third-party
from autoslug import AutoSlugField
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__lte=timezone.now())


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
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    theme = models.CharField(max_length=255, choices=THEME_CHOICES, default=theory)
    slug = AutoSlugField(populate_from="title")
    votes = GenericRelation(LikeDislike, related_query_name="posts")
    # this manager allow to add, get list of tags and delete it from Post objects
    tags = TaggableManager()
    # default manager
    objects = models.Manager()
    # custom manager only for published posts
    published = PublishedManager()

    class Meta:
        ordering = ("published_date",)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # Good method to avoid hardcore urls in templates like "href=/xxx/yyy/<id>"
    def get_absolute_url(self):
        # import pdb; pdb.set_trace()
        return reverse(
            "post_detail",
            args=[
                self.created_date.year,
                self.created_date.month,
                self.created_date.day,
                self.id,
            ],
        )


class Comment(models.Model):
    post = models.ForeignKey(
        "blog.Post", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    votes = GenericRelation(LikeDislike, related_query_name="comments")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
