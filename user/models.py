from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    man = "man"
    woman = "woman"
    secret = "secret"
    SEX_CHOICES = (
        (man, "Мужчина"),
        (woman, "Женщина"),
        (secret, "Скрыт")
    )
    sex = models.CharField(max_length = 2, choices=SEX_CHOICES, default="Скрыт", verbose_name="Пол")