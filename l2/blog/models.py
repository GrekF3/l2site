from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_model
from django.contrib.auth.models import User
from django.utils.timezone import now
from Users.models import UserIP

from PIL import Image

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Название')
    date_published = models.DateField(verbose_name='Дата публикации')
    blog_text = tinymce_model.HTMLField(verbose_name='Текст поста')
    blog_image = models.ImageField(upload_to="posts_images", verbose_name='Главная картинка поста', help_text='Не более 400х400')
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')

    views = models.ManyToManyField(UserIP, related_name="post_views", blank=True)

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.blog_title, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.blog_image.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.blog_image.path)

    
    def __str__(self):
        return str(f'{self.blog_title}')

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    def total_views(self):
        return self.views.count()
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"


class Comments(models.Model):

    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE, verbose_name='Пост')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    comment_text = models.TextField(max_length=455, default=None,verbose_name='Текст комментария')
    date_published = models.DateField(verbose_name='Дата публикации', default=now)

    moderate = models.BooleanField(default=False, verbose_name='Проверен')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"


