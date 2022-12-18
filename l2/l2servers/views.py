from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import GameServerForm
from django.contrib import messages
from django.contrib.auth.models import User
from PIL import Image

from .models import GameServer


def index(request):
    lineage2_servers = GameServer.objects.all().filter(online_game='lineage-2').filter(moderate=True)
    rust_servers = GameServer.objects.all().filter(online_game='Rust').filter(moderate=True)
    wow_servers = GameServer.objects.all().filter(online_game='Word_of_Warcraft').filter(moderate=True)
    csgo_servers = GameServer.objects.all().filter(online_game='csgo').filter(moderate=True)
    arma3_servers = GameServer.objects.all().filter(online_game='arma3').filter(moderate=True)
    dayz_servers = GameServer.objects.all().filter(online_game='DayZ').filter(moderate=True)
    others_servers = GameServer.objects.all().filter(online_game='others').filter(moderate=True)
    minecraft_servers = GameServer.objects.all().filter(online_game='Minecraft').filter(moderate=True)

    all_server = GameServer.objects.all().filter(moderate=True).count()
    moderate = GameServer.objects.all().filter(moderate=False).count()

    context = {
        'l2servers_count': len(lineage2_servers),
        'Rust_Count': len(rust_servers),
        'Wow_Count': len(wow_servers),
        'CsGo_count': len(csgo_servers),
        'Arma3_count': len(arma3_servers),
        'Dayz_Count': len(dayz_servers),
        'Others_Count': len(others_servers),
        'Minecraft_count': len(minecraft_servers),
        'allservers':all_server,
        'moderate':moderate,
    }

    return render(request, context=context, template_name='index.html')


class ServersListView(ListView):
    template_name = 'browse.html'
    model = GameServer
    context_object_name = 'server_list'


    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('game_slug'):
            qs = self.model.objects.filter(online_game__iexact=self.kwargs['game_slug'])
        return qs

def add_server(request):

    if request.method == 'POST':
        game_server_form = GameServerForm(request.POST, request.FILES)

        if game_server_form.is_valid():
            server = game_server_form.save(commit=False)
            server.server_owner = request.user
            banner = Image.open(server.server_banner)
            if banner.format != 'GIF' or 'gif':
                messages.error(request, message='Неверный формат изображения')
                return redirect('new_Server')
            
            if GameServer.objects.filter(name=server.name).exists():
                messages.error(request, message='Такой сервер уже существует')
                return redirect('new_Server')
                
            game_server_form.save()
            messages.success(request, 'Ваш сервер успешно отправлен на модерацию')
            return redirect('new_Server')
    else:
        game_server_form = GameServerForm(request.POST, request.FILES)
        return render(request, 'new_server.html', 
        {'game_server_form': game_server_form})



def gold(request):
    return render(request, 'gold_status.html')