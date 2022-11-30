from django.urls import path
from .views import index, ServersListView, details, profile, gold

urlpatterns = [
    path('', index, name='home'),
    path('servers/<slug:game_slug>/', ServersListView.as_view(), name='servers'),
    path('new_server/', details, name='new_Server'),
    path('profile/', profile, name='profile'),
    path('gold/', gold, name='gold'),

]
