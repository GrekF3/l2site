from django.forms import ModelForm, TextInput, FileInput, EmailInput, HiddenInput
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.core.files.images import get_image_dimensions


class ProfileForm(ModelForm):

    class Meta:
        
        model = Profile
        fields = ['bio','is_gold', 'link', 'avatar']
        
        widgets = {
            'bio': TextInput(attrs={
                'class': 'form-control',
            }),
            'avatar': FileInput(attrs={
                'class': 'form-control',
            }),
        }

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name",'last_name', 'email', 'username']
        required_fields = ['email', 'username']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control'
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
            }),
        }
