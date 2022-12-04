from django.urls import path
from .views import profile


urlpatterns = [
    path('user/<username>', profile, name='profile') 
]