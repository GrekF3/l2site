from django.contrib import admin
from .models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',), }

    list_display = ['blog_title', 'date_published']