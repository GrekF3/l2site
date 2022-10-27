from django.contrib import admin

from .models import Game, GameServer, Ads


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'game_slug': ('name',), }
    pass


@admin.register(GameServer)
class ServersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'server_slug': ('name',), }
    pass

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['server', 'vip', 'top_vip']
    pass