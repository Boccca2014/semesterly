# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-05-10 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_student_sis_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaltimetable',
            name='is_official',
            field=models.BooleanField(default=False),
        ),
    ]