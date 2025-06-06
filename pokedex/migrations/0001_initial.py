# Generated by Django 4.2 on 2025-05-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('nivel', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_pokemon/')),
            ],
        ),
    ]
