# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanimelist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='original',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='website',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
