# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-10 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jhed', models.CharField(default=b'', max_length=255, null=True)),
                ('email_address', models.CharField(default=b'', max_length=255, null=True)),
            ],
        ),
    ]
