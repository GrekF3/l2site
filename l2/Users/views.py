from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ProfileForm

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import BlogPost
from .models import Profile

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Вы успешно изменили пароль"
    success_url = reverse_lazy('home')


@login_required
# Вместо Username можем ставить link,slug,id, в общем любое обозначение ссылки на пользователя
def profile(request, username):

    # Получение нужного пользователя по никнейму
    get_current_user = get_object_or_404(Profile,link__iexact=username)


    # Получем его посты
    user_context = BlogPost.objects.all().filter(author=get_current_user.id)
    posts_count = user_context.count()

    # Тест

    

    # ------------------ Редактирование профиля ----------------------
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect('profile', request.user.username)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    # ------------------ Редактирование профиля ----------------------

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, 'posts':user_context, 'posts_count': posts_count, 'profile':get_current_user,})


def subscribe(request, username):
    get_current_user = get_object_or_404(Profile,link__iexact=username)
    user_req = request.user
    print (get_current_user.user, user_req)

    if user_req != get_current_user.followers:
        get_current_user.followers.add(user_req)
    else:
        pass

    return redirect('profile', get_current_user.user )