# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170318_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(default=b'', max_length=42),
        ),
    ]
