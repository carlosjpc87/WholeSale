# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disenador', '0020_auto_20170107_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_available_sizes',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99, max_digits=5),
            preserve_default=False,
        ),
    ]
