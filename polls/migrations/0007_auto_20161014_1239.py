# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20161013_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='citas',
            name='Observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='Hist',
            field=models.TextField(),
        ),
    ]
