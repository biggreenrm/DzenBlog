from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


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