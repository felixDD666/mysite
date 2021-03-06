# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161116_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Contenido', models.TextField()),
                ('Fecha_Creacion', models.DateTimeField(verbose_name='Fecha de creacion')),
                ('Publico_Privado', models.CharField(choices=[('pub', 'publico'), ('pri', 'privado')], default='pub', max_length=3)),
                ('Foto', models.ImageField(default='SOMETHING', upload_to='postPhotos')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Categoria')),
            ],
        ),
    ]
