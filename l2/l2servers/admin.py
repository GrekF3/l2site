from django.contrib import admin
from .models import Game, GameServer, Ads


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """доступные игры"""
    prepopulated_fields = {'game_slug': ('name',), }


@admin.register(GameServer)
class ServersAdmin(admin.ModelAdmin):
    """доступные сервера"""
    prepopulated_fields = {'server_slug': ('name',), }


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    """реклама серверов"""
    list_display = ['server', 'vip', 'top_vip']
