# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 17:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Disenador', '0019_size_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='designer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('base', 'color_or_print', 'material', 'attribute', 'size_group'), ('designer', 'clave')]),
        ),
    ]
