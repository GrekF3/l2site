from django.urls import path
from .views import index, ServersListView, add_server, gold, vote

urlpatterns = [
    path('', index, name='home'),
    path('servers/<slug:game_slug>/', ServersListView.as_view(), name='servers'),
    path('new_server/', add_server, name='new_Server'),
    path('gold/', gold, name='gold'),
    path('vote/<name>', vote, name='vote')
]
