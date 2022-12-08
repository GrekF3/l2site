from django.urls import path
from .views import profile, ChangePasswordView, subscribe

urlpatterns = [
    path('user/<username>', profile, name='profile'),
    path('user/<username>/subscribe', subscribe, name='sub'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'), 
]

