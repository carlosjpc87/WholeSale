# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disenador', '0016_auto_20161222_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer_profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designer_profile',
            name='created_in',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designer_profile',
            name='style',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
