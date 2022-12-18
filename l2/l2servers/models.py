from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class GameServer(models.Model):

    GAMES = [
        ('lineage-2','Lineage 2'),
        ('Rust', 'Rust'),
        ('Minecraft', 'Minecraft'),
        ('Word_of_Warcraft', 'World of Warcraft'),
        ('csgo', 'Counter-Strike: Global Offensive'),
        ('arma3', 'ARMA 3'),
        ('DayZ', 'Day Z'),
        ('Others', 'Другие')
    ]
    """сервера модель"""
    name = models.CharField(max_length=1000)
    online_game = models.CharField(max_length=40, choices=GAMES, verbose_name='Игра')
    server_banner = models.ImageField(upload_to='servers_logo')

    server_site = models.URLField(max_length=1000, default='l2.ru', verbose_name='Ссылка на сервер')

    description = models.CharField(max_length=500, default='Без описания', verbose_name='Описание сервера')
    server_slug = models.SlugField(unique=True, db_index=True, null=True, blank=True, default=None)

    moderate = models.BooleanField(default=False, verbose_name='Проверен')

    server_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(username='skyhelper').id)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.online_game} {self.name}'

    class Meta:
        verbose_name = 'Сервер'
        verbose_name_plural = 'Сервера'

