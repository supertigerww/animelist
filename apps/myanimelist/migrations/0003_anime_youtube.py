# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanimelist', '0002_auto_20180228_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='youtube',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]