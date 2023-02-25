from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )

    number = models.CharField(max_length=25, verbose_name='номер телефона')
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/')
    country = models.CharField(max_length=35, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []