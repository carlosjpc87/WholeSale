# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoom', '0007_auto_20161129_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=12)),
                ('Sate', models.CharField(max_length=12)),
                ('Locality', models.CharField(max_length=22)),
                ('Zip_Code', models.IntegerField()),
                ('Street', models.CharField(max_length=120)),
                ('Dept', models.CharField(max_length=30)),
                ('Street2', models.CharField(blank=True, max_length=120, null=True)),
                ('Shipping_address', models.BooleanField()),
                ('Sample_shipping_address', models.BooleanField()),
                ('Reciever_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='store',
            name='Business_address',
        ),
        migrations.AddField(
            model_name='store',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShowRoom.Store'),
        ),
    ]
