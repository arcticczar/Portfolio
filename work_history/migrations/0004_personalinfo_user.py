# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-28 01:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_history', '0003_education_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='User',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
