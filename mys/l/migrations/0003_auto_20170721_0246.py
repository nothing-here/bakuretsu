# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l', '0002_auto_20170721_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetails',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
