from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import BlogPost

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog-detail.html'
    context_object_name = 'post'

class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = self.model.objects.all().order_by("-date_published")
        return qs

    
