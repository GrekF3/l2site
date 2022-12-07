from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import GameServerForm
from django.contrib import messages

from .models import GameServer, Ads


def index(request):
    lineage2_servers = GameServer.objects.all().filter(online_game='lineage-2')
    rust_servers = GameServer.objects.all().filter(online_game='Rust')
    wow_servers = GameServer.objects.all().filter(online_game='Minecraft')
    csgo_servers = GameServer.objects.all().filter(online_game='Word_of_Warcraft')
    arma3_servers = GameServer.objects.all().filter(online_game='csgo')
    dayz_servers = GameServer.objects.all().filter(online_game='arma3')
    others_servers = GameServer.objects.all().filter(online_game='DayZ')
    minecraft_servers = GameServer.objects.all().filter(online_game='Others')

    context = {
        'l2servers_count': len(lineage2_servers),
        'Rust_Count': len(rust_servers),
        'Wow_Count': len(wow_servers),
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
            qs = self.model.objects.filter(online_game=self.kwargs['game_slug']).filter(ads=None)
            print(self.kwargs['game_slug'])
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['ads'] = Ads.objects.all().filter(server__online_game=self.kwargs['game_slug'])
        return context

@login_required
def add_server(request):

    if request.method == 'POST':
        game_server_form = GameServerForm(request.POST, request.FILES)

        if game_server_form.is_valid():
            game_server_form.save()
            messages.success(request, 'Ваш сервер успешно отправлен на модерацию')
            return redirect('new_Server')
    else:
        game_server_form = GameServerForm(request.POST, request.FILES)
        print(game_server_form.errors)
        return render(request, 'new_server.html', 
        {'game_server_form': game_server_form})



def gold(request):
    return render(request, 'gold_status.html')