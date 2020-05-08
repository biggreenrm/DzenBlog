from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
    
    def likes(self):
        # get queryset with entries > 0
        return self.get_queryset().filter(vote__gt=0)
    
    def dislikes(self):
        # get queryset with entries < 0
        return self.get_queryset().filter(vote__lt=0)
    
    def sum_rating(self):
        # summary rating
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
    
    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )
    
    vote = models.SmallIntegerField(verbose_name=_('Голос'), choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Пользователь'))
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    objects = LikeDislikeManager()