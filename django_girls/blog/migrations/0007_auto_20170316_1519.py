# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170316_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='contact_email',
            field=models.EmailField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='contact_phone',
            field=models.BigIntegerField(default=0),
        ),
    ]
