# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoom', '0011_auto_20161203_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='PO_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='item_chart',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item_chart',
            name='item_size',
        ),
        migrations.RemoveField(
            model_name='item_chart',
            name='po',
        ),
        migrations.RemoveField(
            model_name='po',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='po',
            name='items',
        ),
        migrations.DeleteModel(
            name='Item_chart',
        ),
        migrations.AddField(
            model_name='po_entry',
            name='po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShowRoom.PO'),
        ),
    ]
