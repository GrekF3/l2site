# Generated by Django 4.1.2 on 2022-12-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l2servers', '0006_alter_gameserver_moderate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameserver',
            name='online_game',
            field=models.CharField(choices=[('lineage-2', 'Lineage 2'), ('Rust', 'Rust'), ('Minecraft', 'Minecraft'), ('Word_of_Warcraft', 'World_of_Warcraft'), ('csgo', 'Cs_Go'), ('arma3', 'Arma3'), ('DayZ', 'DayZ'), ('Others', 'Others')], max_length=17, verbose_name='Игра'),
        ),
    ]