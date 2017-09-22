# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Disenador', '0015_auto_20161220_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designer_Employee',
            fields=[
                ('role', models.CharField(choices=[('JR', 'Assistant')], default='JR', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='yo_d_employee', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Designer_Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='yo_designer', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='designer_employee',
            name='works_for',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='boss', to=settings.AUTH_USER_MODEL),
        ),
    ]
