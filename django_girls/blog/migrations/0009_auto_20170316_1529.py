# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170316_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='contact_email',
            field=models.EmailField(blank=True, default=b'', max_length=75, null=True),
        ),
    ]