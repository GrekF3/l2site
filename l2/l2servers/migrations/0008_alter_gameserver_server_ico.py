# Generated by Django 4.1.2 on 2022-10-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l2servers', '0007_alter_ads_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameserver',
            name='server_ico',
            field=models.ImageField(default=None, upload_to='servers_logo'),
        ),
    ]