# Generated by Django 4.2 on 2025-05-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='nivel',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='imagen',
            field=models.ImageField(upload_to='imagenes_pokemon/'),
        ),
    ]
