# Generated by Django 4.1.2 on 2022-12-18 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('l2servers', '0009_delete_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameserver',
            name='server_ovner',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]