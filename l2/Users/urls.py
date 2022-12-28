from django.urls import path
from .views import profile, ChangePasswordView, subscribe, Login, register_request, logout_request, password_reset
from django.contrib.auth import views as auth_views
from .payments import YandexPayments, notifications


urlpatterns = [
    path('auth/', Login.as_view(), name='auth' ),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('user/<username>', profile, name='profile'),
    path('user/<username>/subscribe', subscribe, name='sub'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-reset/', password_reset, name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
    path('gold/order', YandexPayments.as_view(), name='Order'),
    path('order_completed/', notifications)
]

