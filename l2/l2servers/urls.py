from django.urls import path
from .views import index, ServersListView

urlpatterns = [
    path('', index, name='home'),
    path('servers/<slug:game_slug>/', ServersListView.as_view(), name='servers'),
]