from django.forms import ModelForm, TextInput, FileInput, EmailInput, PasswordInput, CharField
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class ProfileForm(ModelForm):

    class Meta:
        
        model = Profile
        fields = ['bio','is_gold', 'avatar']
        
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
        fields = ["first_name",'last_name', 'email']
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


class RegisterForm(UserCreationForm):

    password1 = CharField(
        label=_("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = CharField(
        label=_("Password confirmation"),
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    
    class Meta:
        model = User
        fields = ['username',]
        widgets = {
            'username': TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={"autofocus": True, "class":'form-control'}))
    password = CharField(
        label=_("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )
