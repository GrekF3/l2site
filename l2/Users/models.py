from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(max_length=125,blank=True, verbose_name='Статус')
    avatar = models.ImageField(upload_to='profile_avatars', verbose_name='Аватар', blank=True, null=True , default='profile_avatars/def_ava.jpeg')
    is_gold = models.BooleanField(verbose_name='GOLD подписчик', default=False, null=True)
    link = models.SlugField(verbose_name='Ссылка на пользователя', unique=True, null=True, blank=True, default=None)

    def save_link(self, *args, **kwargs):
        self.link = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return f'{self.user} профиль'


class UserIP(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip
    