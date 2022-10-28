from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from .models import Game, GameServer, Ads


def index(request):
    lineage2_servers = GameServer.objects.all().filter(online_game_id='1')
    Rust_servers = GameServer.objects.all().filter(online_game_id='2')
    WoW_servers = GameServer.objects.all().filter(online_game_id='3')
    csgo_servers = GameServer.objects.all().filter(online_game_id='4')
    arma3_servers = GameServer.objects.all().filter(online_game_id='5')
    dayz_servers = GameServer.objects.all().filter(online_game_id='6')
    others_servers = GameServer.objects.all().filter(online_game_id='7')
    minecraft_servers = GameServer.objects.all().filter(online_game_id='9')

    context = {
        'l2servers_count': len(lineage2_servers),
        'Rust_Count': len(Rust_servers),
        'Wow_Count': len(WoW_servers),
        'CsGo_count': len(csgo_servers),
        'Arma3_count': len(arma3_servers),
        'Dayz_Count': len(dayz_servers),
        'Others_Count': len(others_servers),
        'Minecraft_count': len(minecraft_servers),
    }

    return render(request, context=context, template_name='index.html')


class ServersListView(ListView):
    template_name = 'browse.html'
    model = GameServer
    context_object_name = 'server_list'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('game_slug'):
            qs = self.model.objects.filter(online_game__game_slug=self.kwargs['game_slug']).filter(ads=None)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['ads'] = Ads.objects.all().filter(server__online_game__game_slug=self.kwargs['game_slug'])

        return context


def details(request):
    return render(request, 'details.html')
