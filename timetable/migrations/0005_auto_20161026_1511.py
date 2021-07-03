"""
Copyright © 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-26 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20160520_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='corequisites',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='info',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='notes',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='geneds',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(default=b'', null=True),
        ),
    ]
