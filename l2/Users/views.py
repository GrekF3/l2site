from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ProfileForm, RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth import login, logout
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import BlogPost
from .models import Profile
from PIL import Image

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Вы успешно изменили пароль"
    success_url = reverse_lazy('home')
    

class Login(LoginView):
    
    template_name = 'login.html'
    form_class = LoginForm
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        return redirect('profile', form.get_user())

def logout_request(request):
    logout(request)
    return redirect('home')

def register_request(request):

    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            link = user_form.cleaned_data['username']
            user = user_form.save()
            user.profile.link = link
            login(request, user)
            messages.success('Успешная регистрация')
            return redirect('home')
        else:
            messages.error('Что-то пошло не так!')
            return redirect('register')

    user_form = RegisterForm()
    return render(request, 'register.html',{'register_form':user_form})

# Вместо Username можем ставить link,slug,id, в общем любое обозначение ссылки на пользователя
def profile(request, username):

    # Получение нужного пользователя по никнейму
    get_current_user = get_object_or_404(Profile,link__iexact=username)


    # Получем его посты
    user_context = BlogPost.objects.all().filter(author=get_current_user.id)
    posts_count = user_context.count()

    if not request.user.is_authenticated:
        context = {
            'profile':get_current_user,
            'posts_count': posts_count,
            'posts': user_context,
        }
        return render(request, 'profile.html', context)

    # ------------------ Редактирование профиля ----------------------
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(commit=False)
            profile = profile_form.save(commit=False)

            image = Image.open(profile.avatar)

            # редактор аватарки
            if 'avatar' in profile_form.changed_data:
                    # НЕ ПУСТОЙ ФОН
                if image.format == 'PNG':
                    messages.error(request,'Неверный формат изображения')
                    profile_form.full_clean()
                    user_form.full_clean()
                    return redirect('profile', request.user.username)
                get_current_user.delete_avatar()
                profile_form.save()
                user_form.save()

                    # РАЗМЕРЫ ИЗОБРАЖЕНИЯ
                if image.height > 300 or image.width > 300:
                    new_img = (300, 300)
                    image.thumbnail(new_img)
                    image.save(profile.avatar.path)
                    messages.success(request, 'Ваш профиль успешно обновлен')
                    return redirect('profile', request.user.username)

            profile.save()
            user_form.save()
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

    if user_req != get_current_user.followers:
        get_current_user.followers.add(user_req)
    else:
        pass

    return redirect('profile', get_current_user.user )