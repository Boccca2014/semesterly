# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20160815_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='emails_enabled',
            field=models.NullBooleanField(default=True),
        ),
    ]