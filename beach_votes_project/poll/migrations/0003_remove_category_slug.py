# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-04-18 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20180418_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]