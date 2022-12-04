from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib.auth import get_user_model

@login_required
@transaction.atomic
def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Ваш профиль был обновлен.')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        Profileform = ProfileForm(instance=user.profile)
        Userform = UserForm(instance=user)
        context = {
            'profile_form' : Profileform,
            'User_from' : Userform,
        }
        
        return render(request, 'profile.html', context=context)

    return redirect("home")
