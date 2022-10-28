import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_fsm import FSMField, transition

STATES = ['New', 'Open']
STATES = list(zip(STATES, STATES))


class Game(models.Model):
    Lineage_2 = 'Lineage 2'
    Rust = 'Rust'
    Word_Of_Warcraft = 'Word Of Warcraft'
    Minecraft = 'Minecraft'
    Cs_Go = 'CS-GO'
    ARMA_3 = 'ARMA 3'
    DayZ = 'DayZ'
    Others = 'Others'

    A_GAMES = [
        (Lineage_2, 'Lineage 2'),
        (Rust, 'Rust'),
        (Minecraft, 'Minecraft'),
        (Word_Of_Warcraft, 'World_of_Warcraft'),
        (Cs_Go, 'Cs_Go'),
        (ARMA_3, 'Arma3'),
        (DayZ, 'DayZ'),
        (Others, 'Others')
    ]

    name = models.CharField(choices=A_GAMES, max_length=20, default=Lineage_2)
    game_slug = models.SlugField(unique=True, db_index=True, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.game_slug})

    def __str__(self):
        return self.name


class GameServer(models.Model):
    name = models.CharField(max_length=1000)
    date_published = models.DateField()
    server_open = models.DateField()
    max_online = models.IntegerField(default=0)
    current_online = models.IntegerField(default=0)
    online_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='Game')
    server_ico = models.ImageField(upload_to='servers_logo')

    server_slug = models.SlugField(unique=True, db_index=True, null=True, blank=True, default=None)
    state = FSMField(default='Open', choices=STATES)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GameServer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.online_game} {self.name}'

    @transition(field=state, source='New', target='Open')
    def opened(self):
        date = datetime.date.today()
        print(date)
        if date == self.server_open:
            open = GameServer.opened
            open.save()


class Ads(models.Model):
    server = models.ForeignKey(GameServer, on_delete=models.CASCADE)
    default = models.BooleanField(default=True)
    vip = models.BooleanField(default=None)
    top_vip = models.BooleanField(default=None)

    def __str__(self):
        return f'{self.server} {self.server.name}'

    class Meta:
        verbose_name = 'Рекламный пост'
        verbose_name_plural = 'Рекламные посты'
