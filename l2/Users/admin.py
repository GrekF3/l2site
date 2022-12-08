from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_gold')
    filter_horizontal = ('followers',)
