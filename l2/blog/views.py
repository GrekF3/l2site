from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import BlogPost, Comments
from .forms import CommentsForm
from Users.models import UserIP
from django.contrib import messages



def get_client_ip(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

class BlogPostDetailView(DetailView):

    model = BlogPost
    template_name = 'blog-detail.html'
    context_object_name = 'post'
    form_class = CommentsForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_post = self.model.objects.get(slug=self.kwargs['slug'])


        context['comment_form'] = self.form_class



        comments = Comments.objects.all().filter(post=view_post)
        context['comments_list'] = comments
        ip = get_client_ip(self.request)
        if UserIP.objects.filter(ip=ip).exists():
            view_post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        else:
            UserIP.objects.create(ip=ip)
            view_post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        return context

    def NewComment(self,request):
        if request.method == 'POST':
            comment_form = self.form_class(request.POST)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request,'Комментарий успешно добавлен!')
                return redirect('post')
        else:
            comment_form = self.form_class(request.POST)
            return {'comment_form':comment_form}


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = self.model.objects.all().order_by("-date_published")
        return qs

    