from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_model

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Название')
    date_published = models.DateField(verbose_name='Дата публикации')
    blog_text = tinymce_model.HTMLField(verbose_name='Текст поста')
    blog_image = models.ImageField(upload_to="posts_images", verbose_name='Главная картинка поста', help_text='Не более 400х400')
    blog_slug = models.SlugField(unique=True, db_index=True, null=True, blank=True, default=None, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.blog_title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"blog_slug": self.blog_slug})
    
    def __str__(self):
        return str(f'{self.blog_title}')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"