# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-04-18 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(default=datetime.date(2018, 4, 19)),
        ),
    ]