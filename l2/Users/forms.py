from django import forms
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(forms.ModelForm):
    
    bio = forms.CharField(max_length=125, required=False)
    avatar = forms.ImageField(required=False)
    is_gold = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'avatar', 'is_gold', 'link')

class UserForm(forms.ModelForm):

    first_name = forms.CharField(required=None)
    last_name = forms.CharField(required=None)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=60, required=True)

    
    class Meta:
        model = User
        fields = ("first_name",'last_name', 'email', 'username')
    
