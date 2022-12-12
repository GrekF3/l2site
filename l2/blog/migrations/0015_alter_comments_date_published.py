# Generated by Django 4.1.2 on 2022-12-12 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comments_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
