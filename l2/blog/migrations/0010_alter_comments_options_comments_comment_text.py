# Generated by Django 4.1.2 on 2022-12-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(default=None, max_length=455),
        ),
    ]
