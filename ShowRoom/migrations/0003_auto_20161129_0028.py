# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoom', '0002_auto_20161128_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inc',
            name='showrooms',
        ),
        migrations.AddField(
            model_name='inc',
            name='showroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShowRoom.Inc'),
        ),
    ]
