# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20161111_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Email',
            field=models.EmailField(max_length=200),
        ),
    ]