# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20161014_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Citas',
            new_name='Cita',
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
    ]