# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disenador', '0018_auto_20161229_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
