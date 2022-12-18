from django.urls import path
from .views import profile, ChangePasswordView, subscribe, Login, register_request, logout_request

urlpatterns = [
    path('auth/', Login.as_view(), name='auth' ),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('user/<username>', profile, name='profile'),
    path('user/<username>/subscribe', subscribe, name='sub'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'), 
]

