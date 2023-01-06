from django.forms import ModelForm, TextInput, FileInput, URLInput, Textarea
from .models import GameServer
from django import forms

GAMES = [
        ('lineage-2','Lineage 2'),
        ('Rust', 'Rust'),
        ('Minecraft', 'Minecraft'),
        ('Word_of_Warcraft', 'World of Warcraft'),
        ('csgo', 'Counter-Strike: Global Offensive'),
        ('arma3', 'ARMA-3'),
        ('DayZ', 'Day-Z'),
        ('Others', 'Другие')
    ]

class GameServerForm(ModelForm):

    online_game = forms.ChoiceField(choices=GAMES, widget=forms.Select(attrs={
        'class':'form-select'
    }))
    
    class Meta:
        model = GameServer
        fields = ['name', 'online_game', 'server_banner', 'description', 'server_site']
        widgets = {
            'name':TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лучший сервер'
            }),
            'server_banner': FileInput(attrs={
                'class': 'form-control'
            }),
            'server_site': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.google.com/'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Лучший сервер по *игра-нейм*, высокий онлайн, лучшие миниигры, карта десять тыщь километров, заходи!',
            }),
        }
