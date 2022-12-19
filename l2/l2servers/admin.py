from django.contrib import admin
from .models import GameServer

@admin.register(GameServer)
class ServersAdmin(admin.ModelAdmin):
    """доступные сервера"""
    list_display = [f'name', 'online_game', 'moderate']
    prepopulated_fields = {'server_slug': ('name',), }
    ordering = ['moderate']
    filter_horizontal = ('liked_by',)
    

