# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileHandler', '0003_filehandler_unique_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filehandler',
            name='unique_url',
        ),
    ]
