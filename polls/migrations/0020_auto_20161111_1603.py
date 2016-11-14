# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20161109_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='DNI',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Hist',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Antecedentes_Familiares',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Antecedentes_Personales',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Apellido1',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Apellido2',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Domicilio',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Email',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Fecha_Nacimiento',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Historia_Clinica',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefono',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
