from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings
from PIL import Image
from l2servers.models import GameServer
import os


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(max_length=125,blank=True, verbose_name='Статус')
    avatar = models.ImageField(upload_to='profile_avatars', verbose_name='Аватар', blank=True, null=True , default='profile_avatars/def_ava.jpeg')
    is_gold = models.BooleanField(verbose_name='GOLD подписчик', default=False, null=True)
    link = models.SlugField(verbose_name='Ссылка на пользователя', unique=True, null=True, blank=True, default=None)

    followers = models.ManyToManyField(User, verbose_name='Подписчики', related_name='Подписчики', blank=True, symmetrical=False)

    servers = models.ManyToManyField(GameServer, verbose_name='Сервера пользователя', blank=True, symmetrical=False)

    def save_link(self, *args, **kwargs):
        self.link = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def delete_avatar(self):
        try:
            self.avatar.delete()
        except ValueError:
            pass
        return self.avatar

    def all_folowers(self):
        return self.followers.count()
    
    def get_user_status(self):

        if self.is_gold:
            return str('GOLD подписчик')
        elif self.user.is_staff:
            return str('Администратор')
        else:
            return str('Обычный')
        
        

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = "Участники"
    
    def __str__(self):
        return f'{self.user} профиль'
    


class UserIP(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip