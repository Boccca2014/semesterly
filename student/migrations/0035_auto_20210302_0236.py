# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2021-03-02 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=21, null=True)),
                ('fav_book', models.CharField(default=b'Looking for Alaska', max_length=255, null=True)),
                ('fav_lang', models.CharField(default=b'Assembly', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='temp_mock',
            field=models.OneToOneField(blank=True, default=b'', on_delete=django.db.models.deletion.CASCADE, to='student.Temp'),
        ),
    ]