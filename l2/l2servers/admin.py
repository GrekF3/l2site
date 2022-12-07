from django.contrib import admin
from .models import GameServer, Ads


@admin.register(GameServer)
class ServersAdmin(admin.ModelAdmin):
    """доступные сервера"""
    list_display = [f'name', 'online_game', 'moderate']
    prepopulated_fields = {'server_slug': ('name',), }
    ordering = ['moderate']

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    """реклама серверов"""
    list_display = ['server', 'vip', 'top_vip']
