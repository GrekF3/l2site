from django.views.generic import ListView
from django.shortcuts import render
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

