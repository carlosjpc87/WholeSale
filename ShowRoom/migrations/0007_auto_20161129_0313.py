# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 03:13
from __future__ import unicode_literals

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('ShowRoom', '0006_auto_20161129_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_Name', models.CharField(max_length=40)),
                ('url', models.URLField()),
                ('Business_address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
            ],
        ),
        migrations.RemoveField(
            model_name='inc',
            name='Business_address',
        ),
        migrations.RemoveField(
            model_name='inc',
            name='user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='company',
        ),
        migrations.DeleteModel(
            name='Inc',
        ),
        migrations.AddField(
            model_name='contact',
            name='store',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ShowRoom.Store'),
            preserve_default=False,
        ),
    ]
