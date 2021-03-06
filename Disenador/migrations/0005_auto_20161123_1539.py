# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 15:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Disenador', '0004_auto_20161123_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Available_Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='item_available_sizes',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disenador.Item'),
        ),
        migrations.AddField(
            model_name='item_available_sizes',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
