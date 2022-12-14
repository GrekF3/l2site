# Generated by Django 4.1.2 on 2022-12-12 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comments_options_comments_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='moderate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(default=None, max_length=455, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='raiting',
            field=models.IntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (4, '5 звезд')], verbose_name='Оценка поста'),
        ),
    ]
