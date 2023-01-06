from django.shortcuts import redirect, render, get_object_or_404
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
            qs = self.model.objects.filter(online_game__iexact=self.kwargs['game_slug']).order_by('-server_owner__profile__is_gold')
        return qs

def add_server(request):

    if request.method == "POST":
        if request.user.is_authenticated:
            game_server_form = GameServerForm(request.POST, request.FILES)
            if game_server_form.is_valid():
                server = game_server_form.save(commit=False)
                server.server_owner = request.user
                # Проверка изображений
                banner = Image.open(server.server_banner)
                if banner.height > 90 or banner.width > 728:
                    messages.error(request, message='Неверный размер изображения')
                    return redirect('new_Server')
                # Проверка изображений
                if GameServer.objects.all().filter(name=server.name).exists():
                    messages.error(request, message='Такой сервер уже существует')
                    return redirect('new_Server')
                    
                if server.server_owner.profile.is_gold:
                    server.moderate = True
                    server.save()
                    messages.success(request, message='Вы успешно добавили сервер!')
                    return redirect('profile', request.user.profile.link )   

                server.save()
                messages.success(request, 'Ваш сервер успешно отправлен на модерацию')
                return redirect('new_Server')
            else:
                messages.error(request, message=game_server_form.errors)
        else:
            return redirect('auth')

    game_server_form = GameServerForm()
    return render(request, 'new_server.html', {'game_server_form': game_server_form})


@login_required
def vote(request,name):
    user = request.user
    server = GameServer.objects.get(name=name)

    if user in server.liked_by.all():
        print(server.liked_by)
        server.liked_by.remove(user)
        messages.warning(request,'Вы убрали свой голос за сервер')
        return redirect('servers', server.online_game)
    else:
        server.liked_by.add(user)
        messages.success(request,'Вы проголосовали за сервер')
        return redirect('servers', server.online_game)


def gold(request):
    return render(request, 'gold_status.html')