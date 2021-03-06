# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 04:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShowRoom', '0014_auto_20161220_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_conditions',
            name='down_payment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, null=True),
        ),
        migrations.RemoveField(
            model_name='show_room_employee',
            name='designers',
        ),
        migrations.AddField(
            model_name='show_room_employee',
            name='designers',
            field=models.ManyToManyField(blank=True, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
    ]
