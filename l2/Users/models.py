from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(max_length=125,blank=True, verbose_name='Статус')
    avatar = models.ImageField(upload_to='profile_avatars', verbose_name='Аватар')
    is_gold = models.BooleanField(verbose_name='GOLD подписчик', default=None, null=True)
    link = models.SlugField(verbose_name='Ссылка на пользователя', unique=True, null=True, blank=True, default=None)

    def save_link(self, *args, **kwargs):
        self.link = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return f'{self.user} профиль'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    

