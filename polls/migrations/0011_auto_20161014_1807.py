# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20161014_1724'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogCategoria',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Post',
        ),
    ]