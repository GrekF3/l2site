from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import BlogPost
from Users.models import UserIP



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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.model.objects.get(slug=self.kwargs['slug'])
        ip = get_client_ip(self.request)
        print(ip)
        if UserIP.objects.filter(ip=ip).exists():
            post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        else:
            UserIP.objects.create(ip=ip)
            post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        return context


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = self.model.objects.all().order_by("-date_published")
        return qs

