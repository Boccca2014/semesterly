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
# Generated by Django 1.9.5 on 2016-05-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(db_index=True, max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(default=b'', max_length=1500)),
                ('unstopped_description', models.TextField(default=b'', max_length=1500)),
                ('campus', models.TextField(default=b'', max_length=300)),
                ('prerequisites', models.TextField(default=b'', max_length=1000)),
                ('exclusions', models.TextField(default=b'', max_length=1000)),
                ('num_credits', models.FloatField(default=-1)),
                ('areas', models.CharField(default=b'', max_length=300, null=True)),
                ('department', models.CharField(default=b'', max_length=250, null=True)),
                ('level', models.CharField(default=b'', max_length=30, null=True)),
                ('cores', models.CharField(blank=True, max_length=50, null=True)),
                ('geneds', models.CharField(blank=True, max_length=50, null=True)),
                ('related_courses', models.ManyToManyField(blank=True, related_name='_course_related_courses_+', to='timetable.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=5.0)),
                ('summary', models.TextField(max_length=1500)),
                ('professor', models.CharField(max_length=250)),
                ('course_code', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=1)),
                ('time_start', models.CharField(max_length=15)),
                ('time_end', models.CharField(max_length=15)),
                ('location', models.CharField(default=b'TBA', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField(default=-1)),
                ('enrolment', models.IntegerField(default=-1)),
                ('waitlist', models.IntegerField(default=0)),
                ('section_type', models.CharField(default=b'L', max_length=50)),
                ('instructors', models.CharField(default=b'TBA', max_length=500)),
                ('semester', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('detail_url', models.URLField(max_length=1000)),
                ('image_url', models.URLField(max_length=1000)),
                ('author', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='TextbookLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Section')),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Textbook')),
            ],
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('update_field', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(default=b'Scheduled Update', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='offering',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Section'),
        ),
    ]
